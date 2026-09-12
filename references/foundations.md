# Foundations — the numbers and the rules

Everything here comes from the Apple Human Interface Guidelines. Values marked
**(sampled)** were read out of the HIG's own swatch images, because Apple publishes those
colors as pictures rather than text.

---

## 1. Typography

### System typefaces

| Family | Where | Notes |
|---|---|---|
| SF Pro | iOS, iPadOS, macOS, tvOS, visionOS | variable font, dynamic optical sizing |
| SF Compact | watchOS | SF Compact Rounded in complications |
| SF Mono | code, monospaced text | |
| New York (NY) | serif companion | available on all platforms except plain macOS AppKit default |
| SF Arabic / Armenian / Georgian / Hebrew | script variants | rounded variants also exist |

Rules:

- Minimize the number of typefaces, even in a heavily branded interface.
- Avoid Ultralight, Thin, and Light weights. Prefer Regular, Medium, Semibold, Bold.
- Use SF Symbols with SF text so symbol weight matches text weight automatically.
- Don't embed the system fonts — reference them.
- Keep the hierarchy intact when text scales; don't let everything grow uniformly.

### Default and minimum text sizes

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### iOS / iPadOS Dynamic Type — Large (the default size)

| Style | Weight | Size | Leading | Emphasized |
|---|---|---|---|---|
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

### macOS built-in text styles

| Style | Weight | Size | Line height | Emphasized |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

macOS does **not** support Dynamic Type.

### watchOS — Large (40/41/42mm default)

| Style | Weight | Size | Leading |
|---|---|---|---|
| Large Title | Regular | 36 | 38.5 |
| Title 1 | Regular | 34 | 36.5 |
| Title 2 | Regular | 28 | 30.5 |
| Title 3 | Regular | 19 | 21.5 |
| Headline | Semibold | 16 | 18.5 |
| Body | Regular | 16 | 18.5 |
| Caption 1 | Regular | 15 | 17.5 |
| Caption 2 | Regular | 14 | 16.5 |
| Footnote 1 | Regular | 13 | 15.5 |
| Footnote 2 | Regular | 12 | 14.5 |

### tvOS built-in text styles

| Style | Weight | Size | Leading |
|---|---|---|---|
| Title 1 | Medium | 76 | 96 |
| Title 2 | Medium | 57 | 66 |
| Title 3 | Medium | 48 | 56 |
| Headline | Medium | 38 | 46 |
| Subtitle 1 | Regular | 38 | 46 |
| Callout | Medium | 31 | 38 |
| Body | Medium | 29 | 36 |
| Caption 1 | Medium | 25 | 32 |
| Caption 2 | Medium | 23 | 30 |

The full Dynamic Type ladder (xSmall → AX5) is in `../assets/type-scales.md`.

### Tracking

In a real app the system adjusts tracking per point size. For static mockups and for web,
apply the SF Pro tracking table (same values on iOS, iPadOS, visionOS, macOS, tvOS):

| Size (pt) | Tracking (pt) | | Size (pt) | Tracking (pt) |
|---|---|---|---|---|
| 11 | +0.06 | | 20 | −0.45 |
| 12 | 0.00 | | 22 | −0.26 |
| 13 | −0.08 | | 24 | +0.07 |
| 15 | −0.23 | | 28 | +0.38 |
| 16 | −0.31 | | 34 | +0.40 |
| 17 | −0.43 | | 40 | +0.37 |

The pattern that matters: **13–23 pt is negatively tracked, 24 pt and up is positively
tracked, 12 pt is neutral.** Body text at 17 pt is the tightest point in the whole scale.

---

## 2. Color

### System colors — exact values **(sampled)**

Light / Dark are the default appearance. AX-Light / AX-Dark apply when Increase Contrast
is on.

| Name | Light | Dark | AX Light | AX Dark |
|---|---|---|---|---|
| Red | `#FF383C` | `#FF4245` | `#E9152D` | `#FF6165` |
| Orange | `#FF8D28` | `#FF9230` | `#C55300` | `#FFA056` |
| Yellow | `#FFCC00` | `#FFD600` | `#A16A00` | `#FEDF43` |
| Green | `#34C759` | `#30D158` | `#008932` | `#4AD968` |
| Mint | `#00C8B3` | `#00DAC3` | `#008575` | `#54DFCB` |
| Teal | `#00C3D0` | `#00D2E0` | `#008198` | `#3BDDEC` |
| Cyan | `#00C0E8` | `#3CD3FE` | `#007EAE` | `#6DD9FF` |
| Blue | `#0088FF` | `#0091FF` | `#1E6EF4` | `#5CB8FF` |
| Indigo | `#6155F5` | `#6D7CFF` | `#564ADE` | `#A7AAFF` |
| Purple | `#CB30E0` | `#DB34F2` | `#B02FC2` | `#EA8DFF` |
| Pink | `#FF2D55` | `#FF375F` | `#E7124D` | `#FF8AC4` |
| Brown | `#AC7F5E` | `#B78A66` | `#956D51` | `#DBA679` |

visionOS uses the **dark** values.

### iOS system grays **(sampled)**

| Name | Light | Dark | AX Light | AX Dark |
|---|---|---|---|---|
| systemGray | `#8E8E93` | `#8E8E93` | `#6C6C70` | `#AEAEB2` |
| systemGray2 | `#AEAEB2` | `#636366` | `#8E8E93` | `#7C7C80` |
| systemGray3 | `#C7C7CC` | `#48484A` | `#AEAEB2` | `#545456` |
| systemGray4 | `#D1D1D6` | `#3A3A3C` | `#BCBCC0` | `#444446` |
| systemGray5 | `#E5E5EA` | `#2C2C2E` | `#D8D8DC` | `#363638` |
| systemGray6 | `#F2F2F7` | `#1C1C1E` | `#EBEBF0` | `#242426` |

> The HIG says explicitly: **don't hard-code these in a native app.** Use `Color.red`,
> `UIColor.systemGray4`, etc. The values are for mockups, for web work, and for checking
> contrast. They change between OS releases.

### Semantic colors (iOS foreground)

`label` → `secondaryLabel` → `tertiaryLabel` → `quaternaryLabel` for text hierarchy,
`placeholderText` for placeholders, `separator` / `opaqueSeparator` for rules, `link` for links.

Backgrounds come in two sets, each with three levels:

- **system** — `systemBackground`, `secondarySystemBackground`, `tertiarySystemBackground`.
- **grouped** — `systemGroupedBackground`, `secondarySystemGroupedBackground`,
  `tertiarySystemGroupedBackground`. Use these when the screen is a grouped table.

Level meaning: primary = the overall view, secondary = a group inside it, tertiary = a
group inside the secondary group.

Rules:

- Don't reuse a semantic color outside its meaning. `separator` is not a text color.
- One color, one meaning, across the whole app.
- Never rely on color alone — pair it with a shape, an icon, or a label.
- Supply light **and** dark variants even if the app ships in one appearance, because
  Liquid Glass adapts in both.
- Test under bright sun, dim light, True Tone, and multiple displays.

---

## 3. Materials and Liquid Glass

Two material systems, and they are not interchangeable:

**Liquid Glass** — the functional layer. Tab bars, toolbars, sidebars, navigation.
It floats above the content layer and lets content scroll under it.

**Standard materials** — `ultraThin` / `thin` / `regular` / `thick`. These live *inside*
the content layer to separate one region of content from another.

Rules:

- **Never put Liquid Glass in the content layer.** The one exception: a slider or toggle
  may pick up a glass look while it is actively being dragged.
- Use it sparingly. Standard system components already adopt it. Custom glass should be
  limited to the most important functional elements.
- Two variants:
  - **regular** — blurs and adjusts the luminosity behind it. The default. Use it for
    anything text-heavy: alerts, sidebars, popovers.
  - **clear** — highly translucent. Only for controls floating over photos and video.
- With **clear** over bright content, add a **35% opacity dark dimming layer**. Over
  already-dark content, or with AVKit's own controls, skip it.
- Larger glass surfaces (sidebars) render more opaque than small ones (toolbars) so text
  stays legible.
- Color on glass: apply it to the *background* of the one primary action, not to symbols
  or labels, and not to several controls at once.
- Over colorful content, keep toolbars and tab bars monochromatic.
- Thicker material = more contrast for fine detail. Thinner = more context from behind.
- Always use system vibrancy colors on top of a material rather than picking your own.

---

## 4. Layout

- Extend backgrounds and full-screen artwork to the display edges; let scrollable content
  run all the way to the bottom and sides. Controls sit *on top of* content, not beside it.
- Where content doesn't span the window, use a background extension view so it appears to
  continue behind the sidebar or inspector.
- Reading order is top → bottom, leading → trailing. Most important item goes top-leading.
- Align components to each other. Alignment plus indentation is how hierarchy reads.
- Use progressive disclosure when a collection doesn't fit: show a partial item to hint
  that more exists.
- Respect safe areas — Dynamic Island, camera housing, home indicator.
- **iOS:** avoid full-width buttons; inset them to the system margins. Keep the status bar
  unless the experience is immersive.
- **iPadOS:** windows are freely resizable. Design the full layout first and defer the
  compact layout as long as possible. Hide tertiary columns (inspectors) before collapsing.
  Test at halves, thirds, and quadrants.
- **macOS:** don't put controls or critical info at the very bottom of a window — people
  drag windows past the bottom of the screen.
- **tvOS:** inset primary content **60 pt** top and bottom, **80 pt** left and right.
- **visionOS:** center important content; keep content inside window bounds because system
  controls live just outside them; keep interactive element centers **≥ 60 pt** apart.
- **watchOS:** run content edge to edge — the bezel is the padding. Max three glyph buttons
  or two text buttons in a row.

---

## 5. Accessibility

### Contrast (WCAG AA, what Accessibility Inspector checks)

| Text | Minimum ratio |
|---|---|
| Up to 17 pt, any weight | 4.5:1 |
| 18 pt and up | 3:1 |
| Bold, any size | 3:1 |

Dark Mode guidance goes further: **never below 4.5:1, aim for 7:1** on custom colors,
especially small text.

### Measured contrast of the semantic colors

Computed (WCAG 2.x) from the token values in `../assets/apple-tokens.css`. Worth knowing,
because **Apple's own semantic colors don't all clear AA**:

| Foreground | on white | on grouped `#F2F2F7` | on black | on elevated `#1C1C1E` |
|---|---|---|---|---|
| `label` | 21.0 | 18.8 | 21.0 | 17.0 |
| `secondaryLabel` | **3.44** | **3.29** | 6.36 | 5.94 |
| `tertiaryLabel` | 1.74 | 1.71 | 2.24 | 2.48 |
| `placeholderText` | 1.74 | 1.71 | — | — |

| Accent, light | vs white |
|---|---|
| system blue `#0088FF` | **3.52** |
| system blue, Increase Contrast `#1E6EF4` | 4.57 |
| system red `#FF383C` | **3.57** |
| system green `#34C759` | **2.22** |

What follows from that:

- **`secondaryLabel` is a 3:1 color in light mode, not a 4.5:1 one.** It is fine for 18 pt+
  or bold text, and for genuinely secondary information. It is *not* safe for small body
  text carrying meaning. In dark mode it clears AA comfortably, so a design that only ever
  gets checked in dark mode will pass and still fail in light.
- **`tertiaryLabel` and `placeholderText` clear nothing.** Treat them as decoration. A
  placeholder is never a label.
- **White on the default system blue is 3.52:1.** A prominent button whose label is 17 pt
  Regular fails AA. Either make the label semibold (3:1 applies), size it 18 pt+, or use
  the Increase-Contrast blue as the resting color.
- **Never put system green or yellow text on white.** Use them as fills with dark text, or
  as status colors paired with a shape.

This is the practical reason the HIG keeps saying "use system colors" *and* "check your
contrast" — the first doesn't guarantee the second.

### Control sizes

| Platform | Default | Minimum |
|---|---|---|
| iOS, iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| tvOS | 66×66 pt | 56×56 pt |
| visionOS | 60×60 pt | 28×28 pt |
| watchOS | 44×44 pt | 28×28 pt |

Spacing matters as much as size: about **12 pt** of padding around a bezeled element,
about **24 pt** around an unbezeled one.

**visionOS** states the same requirement two ways, and either satisfies it: a **16 pt**
margin around the bounds of each interactive item, **or** centers at least **60 pt** apart.
The margin form is the easier one to hit in a dense layout. See `inputs.md` → Eyes.

### The rest

- Text must be enlargeable to at least **200%** (140% on watchOS).
- Convey nothing by color alone.
- Give audio cues a haptic and a visual counterpart; give video captions, subtitles, audio
  descriptions, and transcripts.
- Keep gestures simple, and always offer a non-gesture path to the same outcome.
- Avoid views that auto-dismiss on a timer.
- Don't autoplay media without controls.
- Honor **Reduce Motion**: tighten springs, track gestures directly, don't animate z-axis
  depth, replace x/y/z transitions with fades, don't animate blurs.
- Honor **Increase Contrast** and **Reduce Transparency** — and test Dark Mode with both
  on, together and separately.
- Support Full Keyboard Access, Switch Control, Voice Control, VoiceOver.
- Assistive Access: strip to core functionality, one interaction per screen, confirm
  destructive actions twice.

---

## 6. Motion

- Motion must do a job. Gratuitous animation distracts and can make people unwell.
- Motion is never the only channel for important information — pair it with haptics or audio.
- Feedback motion should follow the gesture. If a view came down from the top, it goes back
  up, not sideways.
- Brief and precise beats prominent.
- Don't animate interactions that happen constantly — the system already does the subtle
  part.
- Let people cancel or skip an animation; never make them wait through it twice.
- 30–60 fps for games.
- **visionOS:** avoid motion in peripheral vision; fade rather than fly objects between
  positions; never rotate the virtual world; avoid sustained oscillation near 0.2 Hz.

---

## 7. Dark Mode

- Don't ship an in-app appearance switch. Follow the system setting, including Auto.
- Dark colors are not inversions of the light ones. Some invert, some don't.
- iOS defines two dark background sets: **base** (recessed) and **elevated** (advanced).
  The system swaps base → elevated automatically for popovers, sheets, and multitasking.
  Custom backgrounds break that signal.
- Darken white-background images slightly so they don't glow.
- Design separate light and dark interface icons when an outline is needed on one side only.
- **macOS:** with the graphite accent color, window backgrounds pick up the desktop picture
  ("desktop tinting"). Add slight transparency to custom neutral-state backgrounds so they
  harmonize; don't do it in colored states.

---

## 8. Icons and SF Symbols

- One concept per icon, simplified to the point of instant recognition.
- Consistent visual weight across the whole icon set; match the weight of adjacent text.
- Pad custom icons for optical alignment.
- Vector format (PDF or SVG). Always provide an alternative text label.
- Text inside an icon only when it's essential.
- Never replicate Apple hardware.
- Selected-state variants only when genuinely needed.
- Symbol animations: judicious, purposeful, in keeping with the app's tone.
- Variable color communicates *change*, not depth.

---

## 9. Writing and inclusion

- Decide the app's voice once; vary tone by context, not voice.
- Be action oriented. Lead with the verb.
- Pick a capitalization rule and hold it everywhere.
- Blank screens get a next step, not just an explanation.
- Error messages: what happened, and what to do about it.
- Text field hints instead of long instructions.
- Plain language over jargon and colloquialisms; define a technical term the first time.
- People-first language when writing about disability.
- Be careful with humor, and read the copy from more than one perspective.

---

## 10. Right to left

- Mirror the layout; don't mirror the content.
- Align a paragraph by its own language, not by the surrounding UI.
- **Flip:** progress indicators, navigation controls, back/forward, ordered lists,
  icons that depict text or reading direction, icons showing forward/backward motion.
- **Don't flip:** numerals within a number, photographs and artwork, logos, universal
  signs, controls pointing at a real onscreen location, most real-world objects.

---

## 11. Privacy

- Ask only for what you need, only when you need it. Not at launch.
- Say plainly in the permission copy what the data is for.
- Process on device where you can.
- If you show a priming screen before the system alert: one button, clearly explaining that
  the system prompt is next, no extra actions, never anything that could be mistaken for
  the system alert itself.
- Keychain for secrets. Never plain text. Never a home-grown auth scheme.
