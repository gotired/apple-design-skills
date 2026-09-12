# HIG on the web — translating native rules to HTML and CSS

Apple writes the HIG for native apps. This file says what each rule becomes in a browser,
and — just as important — which rules **don't** transfer.

Start from `../assets/apple-tokens.css`. Everything below assumes those tokens.

---

## 1. Type

```css
font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display",
             "Helvetica Neue", Helvetica, Arial, sans-serif;
```

`-apple-system` gets the real San Francisco on Apple devices and nothing anywhere else, so
the fallback chain has to hold up on its own. Do not self-host SF — Apple's license
restricts it to app UI mockups and to developer documentation, not to public web pages.

**Point to pixel.** 1 pt = 1 CSS px. The iOS type scale drops in unchanged: body is 17px,
not 16px. That single difference is most of why an "Apple-looking" web page usually looks
slightly wrong — everything is one step too small.

**Tracking is not optional.** SF is negatively tracked from 13 to 23 pt and positively
tracked above 24 pt. A page at `letter-spacing: normal` reads as generic Helvetica. Use the
`--ls-*` tokens next to each `--text-*` token.

**Dynamic Type has a web equivalent, and it isn't `rem`-only.** Use `rem` so the browser's
own font-size setting works, and pair it with `clamp()` for fluid headings. What you must
not do is fix everything in `px` and call it responsive.

```css
.title-1 { font: var(--text-title-1); letter-spacing: var(--ls-title-1); }
```

---

## 2. Color

Use the semantic tokens, not the raw hues. `--label-secondary` for supporting text,
`--separator` for rules, `--fill-tertiary` for a control's resting background. Reaching
past them to `--gray-3` is the web version of the HIG's "don't redefine semantic colors".

Both `--bg`/`--bg-secondary` and `--bg-grouped`/`--bg-grouped-secondary` exist because iOS
inverts them: on a plain screen the page is white and cards are gray; on a grouped
(Settings-style) screen the page is gray and cards are white. Pick one set per screen and
stay in it.

**Dark mode is three states**, not two. `prefers-color-scheme` covers the system default;
an explicit in-page toggle needs `[data-theme]` to win in both directions. The token file
already handles this. Never define a color only inside a media query.

**`prefers-contrast: more`** maps to the HIG's Increase Contrast variants — the accessible
color set is already in the token file.

**Don't assume the tokens are accessible just because they're Apple's.** `--label-secondary`
is 3.44:1 on white, and white on `--blue` is 3.52:1. Both fail AA for small body text. The
measured table is in `foundations.md` §5; check it before using a semantic color for
anything a reader has to read.

---

## 3. Liquid Glass

```css
background: rgb(255 255 255 / 0.72);
backdrop-filter: saturate(180%) blur(20px);
border: 0.5px solid rgb(255 255 255 / 0.55);
```

The rules that carry over intact:

- **Only on the functional layer** — the sticky header, the bottom bar, the sidebar. Never
  on a card, a section, or a content panel. Glass everywhere is the most common way an
  Apple-inspired page ends up looking cheap.
- **Regular over clear.** Clear (`blur(8px)`, very low opacity) is only for controls
  floating over a photo or video, and over bright media it needs the 35% dark scrim.
- **Content scrolls under it.** If your header has a solid background and the content stops
  at its edge, you have a 2013 header, not a glass one.

`backdrop-filter` costs real GPU time. One or two glass surfaces per page. Always give a
`@supports not (backdrop-filter: blur(1px))` fallback to an opaque background, and collapse
glass to opaque under `prefers-reduced-transparency`.

### Scroll edge effect

The current HIG replaces "bar with a background" with "bar with a scroll edge effect": a
short blurred, fading band where content passes under the control layer.

```css
.scroll-edge {
  backdrop-filter: blur(12px);
  mask-image: linear-gradient(to bottom, #000 40%, transparent);
}
```

---

## 4. Layout

| HIG says | On the web |
|---|---|
| Respect safe areas | `padding: env(safe-area-inset-top) env(safe-area-inset-right) …` |
| Extend content to the edges | full-bleed backgrounds; content padding via the gutter token |
| 16 pt side margins (iOS) | `--gutter: 16px`, `20px` on wide layouts |
| Reading order top→bottom, leading→trailing | logical properties: `margin-inline-start`, not `margin-left` |
| RTL mirroring | logical properties plus `dir="rtl"` — see the RTL flip list in `foundations.md` |
| iPad: defer the compact layout | container queries over viewport breakpoints |
| Don't put controls at the window bottom (macOS) | on the web the inverse is true for touch — bottom bars are correct on phones |

**Grouped lists** are the single most recognizable Apple layout shape: rounded container,
white rows on gray, hairline separators that inset past the leading icon, chevron at the
trailing edge, value text in `--label-secondary`. `.list-grouped` in the token file is that
shape.

---

## 5. Controls

- **44px minimum touch target**, and it's the *hit area*, not the visible box. A 20px icon
  button needs padding to reach 44px, or `::after { position: absolute; inset: -12px }`.
- **A press state is mandatory.** The HIG calls this out specifically for custom buttons.
  `:active { opacity: 0.6; transform: scale(0.97) }` reads as native.
- **One prominent button per view.** Two at the very most.
- **Never distinguish the preferred choice by size** — use style. Same-size buttons say
  "these are peers".
- **`:focus-visible`, always.** Keyboard access is the web's Full Keyboard Access.
- Destructive actions use red, and never carry the primary role even when they're the
  likely choice.

---

## 6. Motion

The system's feel is springs, not eases. `linear()` gets close:

```css
--ease-spring: linear(0, 0.35 12%, 0.72 24%, 0.95 34%, 1.04 43%, 1.05 55%, 1.0 76%, 1);
```

- 150ms for state changes, 250ms for transitions, 350ms for a sheet or a large move.
- Reverse the entry gesture on exit: a sheet that slid up slides down.
- Don't animate anything people do dozens of times a minute.
- `prefers-reduced-motion` is the web's Reduce Motion, and the HIG's advice applies exactly:
  fade instead of translate, drop the springs, don't animate blurs.

---

## 7. What does not transfer

- **SF Symbols.** The library is licensed for Apple platforms. On the web, use a symbol set
  with matching optical weight and stroke (Lucide and Phosphor are close) and keep icon
  weight matched to adjacent text weight, which is the actual HIG rule.
- **The San Francisco font files.** See above.
- **Real Liquid Glass.** `backdrop-filter` is a static blur; the system material has
  refraction and specular response that CSS has no equivalent for. Aim for the layering
  logic, not a pixel match.
- **Dynamic Type.** No browser API reports the OS text size. `rem` plus a generous layout
  is the substitute.
- **The elevated/base dark background swap.** iOS does it automatically for foreground
  surfaces; on the web you apply `--bg-elevated-*` by hand to modals and popovers.
- **Anything on the Technologies list** — Apple Pay, Sign in with Apple, Wallet, HealthKit,
  SharePlay. Their HIG pages are about native integration, not web UI. Use
  `references/technologies.md` to find the complete current list and then read the official
  page for the native integration.

---

## 8. A page that reads as Apple — the short version

1. 17px body, SF stack, correct negative tracking.
2. Semantic color tokens, both light and dark defined up front.
3. Generous vertical rhythm; content grouped into rounded containers with hairline
   separators.
4. Exactly one glass surface, on the navigation layer, with content scrolling beneath it.
5. One prominent action per screen, in the accent color, with a real press state.
6. 44px targets everywhere, visible focus rings.
7. Springs at 150–350ms, all of it disabled under Reduce Motion.
8. Nothing conveyed by color alone.
