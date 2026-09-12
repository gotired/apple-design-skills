---
name: apple-design
description: "Apple Human Interface Guidelines as a working reference and review checklist. Use when designing, building, or reviewing any UI that should follow Apple's design language — SwiftUI/UIKit/AppKit apps for iOS, iPadOS, macOS, watchOS, tvOS, or visionOS, and web pages, artifacts, or components that want an Apple look. Covers typography and the Dynamic Type scale, exact system color values, Liquid Glass and standard materials, layout and safe areas, accessibility gates (contrast ratios, touch targets), motion, dark mode, every HIG component and pattern, and a HIG→CSS mapping for the web. Trigger on: 'Apple design', 'HIG', 'human interface guidelines', 'iOS design', 'make it look like an Apple app', 'SF Pro', 'Liquid Glass', 'Dynamic Type', 'SF Symbols', 'system colors', 'review this UI against Apple's guidelines'."
---

# Apple Human Interface Guidelines

A condensed, current copy of the HIG plus the parts Apple doesn't publish as text —
exact system color values, the full Dynamic Type ladder, and a translation layer for the web.
The generated coverage inventory and technology index keep newly added Apple topics visible.

## Which file to read

Don't read everything. Load what the task needs.

| Task | Read |
|---|---|
| Any UI work at all | the **non-negotiables** below |
| Type, color, materials, layout, accessibility, motion, dark mode | `references/foundations.md` |
| Branding, images, immersive experiences, spatial layout | `references/foundations-extended.md` |
| Building a specific control | `references/components.md` — find the component's section |
| Onboarding, feedback, loading, search, settings, modality, data entry | `references/patterns.md` |
| Targeting a specific OS | `references/platforms.md` |
| Apple platform or service integration (Apple Pay, Siri, HealthKit, Generative AI, etc.) | `references/technologies.md` — then open the official page |
| Designing or reviewing an app icon | `references/app-icons.md` |
| Gestures, keyboards, pointer, focus, Digital Crown, gaze, Pencil, controllers | `references/inputs.md` |
| Web, HTML, CSS, React, an Artifact | `references/web-mapping.md` + `assets/apple-tokens.css` |
| Want to see the tokens assembled into a screen | `examples/settings.html` |
| Reviewing or auditing an existing UI | `references/checklist.md` |
| Exact Dynamic Type numbers at a non-default size | `assets/type-scales.md` |
| Checking whether this skill covers a current HIG topic | `references/coverage.md` |

## Companion skills

Keep this skill as the design authority and reach for a companion only for its specific task:

| Branch | Reach for |
|---|---|
| Explore a flow or state model before implementation | `$prototype` |
| Build an interactive mockup or visual comparison | `$visualize` |
| Inspect rendered HTML/CSS or run browser QA | `$browser:control-in-app-browser` |
| Verify current Apple guidance against primary sources | `$research` |
| Review implementation changes against standards and spec | `$code-review` |

## The non-negotiables

These decide whether a UI reads as Apple's or as an imitation. Everything else is detail.

1. **Content first, chrome second.** Controls float above content on the Liquid Glass
   layer; content scrolls underneath and runs to the display edges. Never put glass in the
   content layer.
2. **The type scale is fixed.** iOS body is 17 pt with 22 pt leading. macOS body is 13/16.
   Weights are Regular through Bold, never Light or Thin. SF is negatively tracked from
   13–23 pt and positively above 24 pt; a page without that tracking doesn't read as Apple.
3. **Semantic color, never raw color.** `label` / `secondaryLabel` / `separator` / `fill`,
   each used only for its meaning. Every custom color needs a light variant, a dark
   variant, and an increased-contrast version of each.
4. **One prominent action per view.** Distinguish the preferred choice by *style*, not by
   size. Destructive actions are red and are never the default button.
5. **44 pt.** iOS/iPadOS/watchOS touch target, on the hit area, with ~12 pt of breathing
   room around it. macOS 28, tvOS 66, visionOS 60.
6. **4.5:1.** Text up to 17 pt, in both appearances. 3:1 for 18 pt+ or bold. Nothing is
   communicated by color alone.
7. **Motion has a job or it doesn't ship.** Reverse the entry gesture on exit, keep it
   under ~350 ms, let people cancel it, and honor Reduce Motion.
8. **The system settings are requirements, not suggestions.** Dark Mode, Dynamic Type,
   Increase Contrast, Reduce Transparency, Reduce Motion. Test them on and off, and in
   combination.

## Working method

**Building new UI**

1. Name the platform or device form factor. Read its section in `references/platforms.md`.
2. Set the foundation before the pixels: type scale, semantic color tokens, spacing,
   the light/dark pair. For the web, start from `assets/apple-tokens.css`.
3. Pick standard components. Read their section in `references/components.md` before
   building each one. Deviate only with a reason you can state.
4. Check the flow against `references/patterns.md` — loading, empty, error, and permission
   states are where most designs quietly fail.
5. Run `references/checklist.md` before calling it done.

**Reviewing existing UI**

Run `references/checklist.md` top to bottom. Section A is a gate: report every failure
there. For the rest, report what actually breaks a rule and skip what doesn't. Each finding
gets the rule, the location, and the fix.

## Boundaries

- The HIG is Apple's design guidance, not a component library. It says what should be true,
  not what to type. Pair it with SwiftUI's actual API, or with the CSS in `assets/`.
- Apple explicitly says **don't hard-code the system color values** in a native app — use
  `Color.red`, `UIColor.systemGray4`. The hex values in this skill exist for mockups, for
  web work, and for contrast checking. They change between OS releases.
- **San Francisco and SF Symbols are licensed for Apple platforms.** Don't self-host them
  on the web. `references/web-mapping.md` lists what to use instead.
- HIG technology pages are integration-specific and change quickly. `references/technologies.md`
  indexes every current technology page; open the official Apple page before making an API,
  privacy, availability, or platform-support decision.

## Source and freshness

Condensed from `https://developer.apple.com/design/human-interface-guidelines`, with the
current topic inventory generated by `scripts/refresh-hig.py`.

To refresh: `python3 scripts/refresh-hig.py`. It re-crawls Apple's documentation JSON,
regenerates component/pattern condensations, and updates `references/technologies.md` plus
`references/coverage.md`. Hand-written files (`foundations.md`, `foundations-extended.md`,
`platforms.md`, `inputs.md`, `app-icons.md`, `web-mapping.md`, `checklist.md`, the CSS) need
a human pass after a refresh.
