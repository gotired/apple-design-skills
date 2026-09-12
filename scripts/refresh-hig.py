#!/usr/bin/env python3
"""Re-crawl the Apple Human Interface Guidelines and regenerate the derived references.

Apple renders the HIG as a single-page app; the real content sits behind a DocC JSON API
at /tutorials/data/<route>.json. System color values are published only as swatch images,
so they are sampled pixel-by-pixel.

    python3 scripts/refresh-hig.py [--cache DIR]

Writes:
    references/components.md      regenerated
    references/patterns.md        regenerated
    references/technologies.md    generated complete technology-page index
    references/coverage.md        generated current-topic inventory
    <cache>/swatches.json         sampled system colors
    <cache>/md/*.md               every HIG page as markdown, for hand-editing the rest

The hand-written files (foundations.md, platforms.md, web-mapping.md, checklist.md,
assets/apple-tokens.css) are never touched — diff them against <cache>/md/ by hand.
"""

import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.request

BASE = "https://developer.apple.com/tutorials/data"
IMG_BASE = "https://developer.apple.com/tutorials"
ROOT = "/design/human-interface-guidelines"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"}
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# --------------------------------------------------------------------------- fetch

def get(url, binary=False, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=timeout).read()
    return data if binary else json.loads(data)


def page_json(cache, path):
    fn = os.path.join(cache, "hig", path.strip("/").replace("/", "__") + ".json")
    if os.path.exists(fn):
        return json.load(open(fn))
    try:
        d = get(BASE + path + ".json")
    except Exception as e:
        print(f"  skip {path}: {e}", file=sys.stderr)
        return None
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    json.dump(d, open(fn, "w"))
    time.sleep(0.15)
    return d


def crawl(cache):
    seen, order = set(), []

    def walk(path, depth=0):
        if path in seen or depth > 4:
            return
        seen.add(path)
        d = page_json(cache, path)
        if not d:
            return
        order.append(path)
        refs = d.get("references", {})
        for s in d.get("topicSections", []):
            for i in s.get("identifiers", []):
                u = refs.get(i, {}).get("url", "")
                if u.startswith(ROOT + "/"):
                    walk(u, depth + 1)

    walk(ROOT)
    return order


# ----------------------------------------------------------------- json -> markdown

def inline(items, refs):
    out = []
    for it in items or []:
        t = it.get("type")
        if t == "text":
            out.append(it.get("text", ""))
        elif t in ("emphasis", "strong", "inlineHead"):
            out.append("**" + inline(it.get("inlineContent"), refs) + "**")
        elif t == "codeVoice":
            out.append("`" + it.get("code", "") + "`")
        elif t == "reference":
            out.append(inline(it.get("inlineContent"), refs)
                       or refs.get(it.get("identifier"), {}).get("title", ""))
        elif t == "link":
            out.append(it.get("title", ""))
        elif "inlineContent" in it:
            out.append(inline(it["inlineContent"], refs))
    return "".join(out)


def block(content, refs, depth=0):
    lines = []
    for b in content or []:
        t = b.get("type")
        if t == "heading":
            lines.append("\n" + "#" * min(b.get("level", 2) + 1, 6) + " " + b.get("text", "") + "\n")
        elif t == "paragraph":
            s = inline(b.get("inlineContent"), refs).strip()
            if s:
                lines.append(s + "\n")
        elif t in ("unorderedList", "orderedList"):
            for n, li in enumerate(b.get("items", []), 1):
                mark = "- " if t == "unorderedList" else f"{n}. "
                sub = block(li.get("content"), refs, depth + 1).strip().splitlines()
                if sub:
                    lines.append("  " * depth + mark + sub[0])
                    lines.extend("  " * (depth + 1) + x for x in sub[1:])
            lines.append("")
        elif t == "aside":
            s = block(b.get("content"), refs, depth).strip()
            lines.append(f"> **{b.get('name') or b.get('style', 'Note')}:** {s}\n")
        elif t == "codeListing":
            lines.append("```\n" + "\n".join(b.get("code", [])) + "\n```\n")
        elif t == "table":
            rows = b.get("rows", [])
            if rows:
                hdr = [block(c, refs).strip().replace("\n", " ") for c in rows[0]]
                lines.append("| " + " | ".join(hdr) + " |")
                lines.append("|" + "---|" * len(hdr))
                for r in rows[1:]:
                    lines.append("| " + " | ".join(
                        block(c, refs).strip().replace("\n", " ") for c in r) + " |")
                lines.append("")
        elif t == "termList":
            for it in b.get("items", []):
                term = inline(it.get("term", {}).get("inlineContent"), refs)
                d = block(it.get("definition", {}).get("content"), refs).strip().replace("\n", " ")
                lines.append(f"- **{term}**: {d}")
            lines.append("")
        elif "tabs" in b:
            # Dynamic Type tables and similar live inside tab navigators.
            for tab in b["tabs"]:
                lines.append("\n**[tab] " + str(tab.get("title") or "") + "**\n")
                lines.append(block(tab.get("content"), refs, depth))
        elif "content" in b:
            lines.append(block(b["content"], refs, depth))
    return "\n".join(lines)


def to_markdown(d):
    refs = d.get("references", {})
    parts = ["## " + d.get("metadata", {}).get("title", ""), "",
             inline(d.get("abstract"), refs), ""]
    for sec in d.get("primaryContentSections", []):
        if sec.get("kind") == "content":
            parts.append(block(sec.get("content"), refs))
    return "\n".join(parts)


# --------------------------------------------------------------------- condensing

BOLD = re.compile(r"^\*\*(.+?)\*\*\s*(.*)$")
LIST_BOLD = re.compile(r"^- \*\*(.+?)\*\*\s*(.*)$")


def condense(md):
    """Title, abstract, and the bold rule-headings from the cross-platform sections."""
    lines = md.splitlines()
    title = lines[0].replace("## ", "").strip() if lines else ""
    body = [l for l in lines[1:] if l.strip()]
    abstract = body[0] if body else ""

    core = md
    for stop in ("\n### Platform considerations", "\n### Specifications",
                 "\n### Resources", "\n### Change log"):
        i = core.find(stop)
        if i > 0:
            core = core[:i]

    rules = []
    for line in core.splitlines():
        line = line.strip()
        m = BOLD.match(line)
        m2 = LIST_BOLD.match(line)
        if m and len(m.group(1)) > 18:
            rules.append(m.group(1).rstrip(".").strip())
        elif m2:
            lead = m2.group(1).rstrip(".").strip()
            rules.append(lead if len(lead) > 18 else f"{lead}: {m2.group(2)[:160]}")
    return title, abstract, rules


# ------------------------------------------------------------------------ swatches

def sample_swatches(cache):
    """Read the exact system color values out of the HIG's swatch images."""
    try:
        from PIL import Image
    except ImportError:
        print("  Pillow not installed — skipping color sampling", file=sys.stderr)
        return {}
    d = page_json(cache, ROOT + "/color")
    if not d:
        return {}
    out = {}
    outdir = os.path.join(cache, "swatch")
    os.makedirs(outdir, exist_ok=True)
    for k, v in sorted(d.get("references", {}).items()):
        if v.get("type") != "image":
            continue
        if not (k.startswith("colors-unified") or k.startswith("ios-default-system")
                or k.startswith("ios-accessible-system")):
            continue
        urls = [x["url"] for x in v.get("variants", []) if "~dark" not in x["url"]]
        if not urls:
            continue
        fn = os.path.join(outdir, os.path.basename(urls[0]))
        if not os.path.exists(fn):
            try:
                open(fn, "wb").write(get(IMG_BASE + urls[0], binary=True, timeout=8))
            except Exception as e:
                print(f"  skip swatch {k}: {e}", file=sys.stderr)
                continue
        try:
            im = Image.open(fn).convert("RGB")
        except Exception as e:
            print(f"  skip unreadable swatch {k}: {e}", file=sys.stderr)
            continue
        w, h = im.size
        out[k.replace(".png", "")] = "#%02X%02X%02X" % im.getpixel((w // 2, h // 2))
    json.dump(out, open(os.path.join(cache, "swatches.json"), "w"), indent=1)
    return out


# -------------------------------------------------------------------------- output

COMPONENTS_HEADER = """# Components — HIG rules, condensed

Every rule below is a condensed "best practice" heading from the Apple Human Interface
Guidelines page for that component. Rules are cross-platform; platform-specific deltas
live in `platforms.md`. Full page: `https://developer.apple.com/design/human-interface-guidelines/<slug>`.

Use this file two ways:
- **Building** — read the section for the component you are about to build.
- **Reviewing** — read the section and check the UI against each line.
"""

PATTERNS_HEADER = """# Patterns — HIG rules, condensed

Patterns are whole-flow rules: onboarding, feedback, loading, modality, search, settings,
data entry, notifications. Condensed from the Apple Human Interface Guidelines.
Full page: `https://developer.apple.com/design/human-interface-guidelines/<slug>`.

"""


def slug_of(url):
    return url.rsplit("/", 1)[-1]


def write_components(cache, mdroot):
    d = page_json(cache, ROOT + "/components")
    refs = d["references"]
    out = [COMPONENTS_HEADER]
    for s in d["topicSections"]:
        for i in s["identifiers"]:
            cat = slug_of(refs[i]["url"])
            ct, _, _ = condense(open(f"{mdroot}/{cat}.md").read())
            out.append(f"\n## {ct}\n")
            sub = page_json(cache, refs[i]["url"])
            r2 = sub["references"]
            for t in sub.get("topicSections", []):
                for j in t["identifiers"]:
                    slug = slug_of(r2[j]["url"])
                    title, ab, rules = condense(open(f"{mdroot}/{slug}.md").read())
                    out.append(f"### {title}\n{ab}")
                    out.extend(f"- {r}" for r in rules)
                    out.append("")
    path = os.path.join(REPO, "references", "components.md")
    open(path, "w").write("\n".join(out))
    print(f"  wrote {path}")


def write_patterns(cache, mdroot):
    d = page_json(cache, ROOT + "/patterns")
    refs = d["references"]
    out = [PATTERNS_HEADER]
    for s in d["topicSections"]:
        for i in s["identifiers"]:
            slug = slug_of(refs[i]["url"])
            title, ab, rules = condense(open(f"{mdroot}/{slug}.md").read())
            out.append(f"## {title}\n{ab}")
            out.extend(f"- {r}" for r in rules)
            out.append("")
    path = os.path.join(REPO, "references", "patterns.md")
    open(path, "w").write("\n".join(out))
    print(f"  wrote {path}")


def write_technologies(cache):
    """Write a complete, low-maintenance index for HIG technology guidance."""
    d = page_json(cache, ROOT + "/technologies")
    if not d:
        return
    refs = d.get("references", {})
    out = [
        "# Technologies — complete HIG index",
        "",
        "Apple's technology guidance is integration-specific and changes faster than the",
        "general design rules. This index keeps every current technology page discoverable;",
        "open the official page before making a platform or API decision.",
        "",
        f"Generated from Apple's HIG data on {datetime.date.today().isoformat()}.",
        "",
        "| Topic | Official HIG page |",
        "|---|---|",
    ]
    for section in d.get("topicSections", []):
        for identifier in section.get("identifiers", []):
            ref = refs.get(identifier, {})
            title = ref.get("title", "")
            url = ref.get("url", "")
            if title and url:
                out.append(f"| {title} | [Read on Apple](https://developer.apple.com{url}) |")
    out.extend([
        "",
        "## How to use this file",
        "",
        "1. Identify the technology the product actually integrates.",
        "2. Read its official HIG page and the linked platform/component guidance.",
        "3. Apply the local checklist in `checklist.md` after the integration-specific review.",
        "",
        "This skill intentionally does not copy all technology pages into the repository:",
        "Apple is the source of truth for API availability, privacy requirements, platform",
        "support, and usage-specific restrictions.",
    ])
    path = os.path.join(REPO, "references", "technologies.md")
    open(path, "w").write("\n".join(out) + "\n")
    print(f"  wrote {path}")


def write_coverage(cache):
    """Write a generated inventory so missing or newly added HIG topics are visible."""
    root = page_json(cache, ROOT)
    if not root:
        return
    refs = root.get("references", {})
    labels = {
        "getting-started": ("`references/platforms.md`", "condensed; includes platform deltas"),
        "foundations": ("`references/foundations.md`, `references/foundations-extended.md`, `references/app-icons.md`", "condensed"),
        "patterns": ("`references/patterns.md`", "generated condensed rules"),
        "components": ("`references/components.md`", "generated condensed rules"),
        "inputs": ("`references/inputs.md`", "condensed"),
        "technologies": ("`references/technologies.md`", "complete official-page index"),
    }
    out = [
        "# HIG coverage inventory",
        "",
        "This file is generated by `scripts/refresh-hig.py`. It is an inventory, not a",
        "replacement for Apple's source pages. A topic marked condensed has local guidance;",
        "the official link remains authoritative for details and freshness.",
        "",
        f"Generated from Apple's HIG data on {datetime.date.today().isoformat()}.",
        "",
        "| HIG area | Current topics | Local entry point | Coverage model |",
        "|---|---:|---|---|",
    ]
    all_topics = []

    def descendants(page, area):
        count = 0
        for section in page.get("topicSections", []):
            for child in section.get("identifiers", []):
                child_ref = page.get("references", {}).get(child, {})
                if not child_ref.get("title") or not child_ref.get("url"):
                    continue
                count += 1
                all_topics.append((area, child_ref["title"], child_ref["url"]))
                child_page = page_json(cache, child_ref["url"])
                if child_page:
                    count += descendants(child_page, area)
        return count

    for identifier in root.get("topicSections", [{}])[0].get("identifiers", []):
        ref = refs.get(identifier, {})
        url = ref.get("url", "")
        slug = slug_of(url)
        page = page_json(cache, url) if url else None
        count = 0
        if page:
            count = descendants(page, ref.get("title", slug))
            if slug == "components":
                # The useful comparison is the 64 leaf components, not the 8 category pages.
                count -= sum(len(section.get("identifiers", [])) for section in page.get("topicSections", []))
        local, model = labels.get(slug, ("—", "official only"))
        out.append(f"| {ref.get('title', slug)} | {count} | {local} | {model} |")
    out.extend(["", "## Topic links", "", "| Area | Topic | Official HIG page |", "|---|---|---|"])
    for area, title, url in all_topics:
        out.append(f"| {area} | {title} | [Read on Apple](https://developer.apple.com{url}) |")
    path = os.path.join(REPO, "references", "coverage.md")
    open(path, "w").write("\n".join(out) + "\n")
    print(f"  wrote {path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=os.path.join(REPO, ".hig-cache"),
                    help="where to keep raw JSON, images, and per-page markdown")
    args = ap.parse_args()
    cache = args.cache
    mdroot = os.path.join(cache, "md")
    os.makedirs(mdroot, exist_ok=True)

    print("crawling…")
    pages = crawl(cache)
    print(f"  {len(pages)} pages")

    print("converting to markdown…")
    for p in pages:
        d = page_json(cache, p)
        if d:
            open(f"{mdroot}/{slug_of(p)}.md", "w").write(to_markdown(d))

    print("sampling system colors…")
    sw = sample_swatches(cache)
    print(f"  {len(sw)} swatches -> {cache}/swatches.json")

    print("regenerating references…")
    write_components(cache, mdroot)
    write_patterns(cache, mdroot)
    write_technologies(cache)
    write_coverage(cache)

    print(f"\nDone. Hand-written files were not touched — diff them against {mdroot}/:")
    for f in ("references/foundations.md", "references/foundations-extended.md",
              "references/platforms.md", "references/web-mapping.md",
              "references/checklist.md",
              "assets/apple-tokens.css", "assets/type-scales.md"):
        print(f"  {f}")


if __name__ == "__main__":
    main()
