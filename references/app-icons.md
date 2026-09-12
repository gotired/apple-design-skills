# App icons

Your app icon is your app's identity everywhere the system shows it: Home Screen, search,
notifications, Settings, share sheets. It has to read instantly at small sizes and hold up
across five appearance variants.

---

## What makes a good one

- One concept, expressed simply. Fine detail turns to mush at small sizes and under
  system-applied shadows and highlights.
- A simple background — solid color or gradient — that pushes emphasis onto the primary
  design. Don't feel obliged to fill the whole canvas.
- Same design language across every platform you ship on, so people recognize the app
  everywhere it appears.
- Filled, overlapping shapes read as depth, especially with transparency and blur.
- Illustration over photography. Photos carry detail that breaks apart across appearances,
  small sizes, and layer splitting.
- No text unless it's essential to the brand. Text doesn't localize, doesn't scale down,
  and the app name is usually already shown next to the icon. A single mnemonic letter is
  fine; instructional words ("Watch", "Play") or context words ("New", "For visionOS") are
  not.
- Never replicate Apple hardware — it's copyrighted.
- Don't replicate your own UI or use a screenshot as the icon.
- Avoid extremely thin line weights and sharp corners — they lose crispness at small,
  low-resolution sizes.

---

## Layers and Icon Composer

Providing a flattened image still works, but layers give the system material to work with:
specular highlights, refraction, translucency, parallax. Layer counts and effects vary by
platform:

| Platform | Layers | Effect |
|---|---|---|
| iOS, iPadOS, macOS, watchOS | Background + one or more foreground layers | Liquid Glass: specular highlights, refraction, translucency. Adapts to icon size and can vary between system versions. |
| tvOS | 2–5 layers | Parallax: icon elevates and sways in response to remote/finger movement; layer separation and transparency create depth. |
| visionOS | Background + 1–2 layers | 3D: subtly expands on view; shadows between layers plus alpha-channel embossing on upper layers. |

Workflow:

- **iOS, iPadOS, macOS, watchOS:** build foreground layers in any design tool, import into
  **Icon Composer** (ships with Xcode, also on the Apple Developer site). There you set the
  background, position foreground layers, apply specular/refraction effects, annotate
  default/dark/mono variants, preview across system versions, and export for Xcode.
- **tvOS, visionOS:** add layers directly to an image stack in an Xcode asset catalog. Use
  the Parallax Previewer / Parallax Exporter plug-ins (Apple Design Resources) for preview.

Rules for layer construction:

- Clearly defined edges on foreground shapes — soft or feathered edges break system-drawn
  highlights and shadows.
- Vary opacity across foreground layers for depth. Import fully opaque layers and adjust
  translucency inside Icon Composer so you can preview the interaction with system effects.
- A custom background layer (instead of Icon Composer's built-in solid/gradient) must be
  full-bleed and opaque.
- Prefer vector (SVG, PDF) for layers — scales cleanly at any size; outline artwork and
  convert text to outlines. PNG only for mesh gradients and raster art.
- Group layers in Icon Composer when they should share one effect — grouping unlocks
  group-level Liquid Glass controls (specular highlights, refraction, translucency).
- Let the system apply blur, shadows, bevels, glows. Custom effects are static; the
  system's are dynamic. If you add custom effects anyway, test them in Icon Composer,
  Device Hub, or on a real device.
- tvOS: text goes above other layers, or the parallax crop cuts it.

---

## Appearances

iOS, iPadOS, and macOS let people pick their Home Screen icon appearance: **default, dark,
clear, or tinted**. You can supply a variant for each; the system generates any you skip.

Rules:

- Keep the same core visual features across all four appearances. Don't swap elements in
  and out per variant — that makes the app harder to spot after someone switches
  appearance.
- Dark, clear, and tinted are progressively more subdued than default. Design so the icon
  stays visible, legible, and recognizable in all of them.
- Build the dark variant from the light one: same palette, complementary colors, avoid
  excessively bright fills. Color backgrounds give the best contrast in dark icons.
- **Alternate app icons** (iOS, iPadOS, tvOS, and visionOS apps that support them) each need
  their own dark, clear, and tinted variants too — and each one goes through App Review
  independently. Keep every alternate closely tied to your actual content; don't design one
  that could be mistaken for a different app.
- watchOS: don't use black as the icon background — it disappears into the black watch
  face bezel. Lighten it.

---

## Platform shapes and specs

| Platform | Layout shape | Shape after system masking | Canvas size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle | 1024×1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle | 800×480 px | Layered (parallax) | N/A |
| visionOS | Square | Circular | 1024×1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088×1088 px | Layered | N/A |

The system masks all layer edges to produce the final shape — always supply **unmasked,
full square (or rectangular, for tvOS) layers** and let the system round or circle them.
Pre-masked layers wreck specular highlights and leave jagged edges.

The exact icon grid overlay (where the mask lines fall, corner-radius curvature) is
published only as reference images layered over the Settings app icon, one per shape
family — **not published as text or numbers**. Use the app icon production templates in
Apple Design Resources for precise placement instead of estimating from the images.

Color spaces supported: **sRGB** (color), **Gray Gamma 2.2** (grayscale), and **Display
P3** (wide gamut — iOS, iPadOS, macOS, tvOS, watchOS only, not visionOS).

The system auto-generates smaller scaled variants for Settings, notifications, and similar
spots — you don't produce those sizes yourself.

---

## Per-platform notes

**iOS, iPadOS, macOS** — no extra platform considerations beyond the shared rules above.

**tvOS** — leave a safe zone around your content. On focus, the icon scales and moves, and
the system crops around the edges as it does — foreground layers get cropped more than the
background. The safe zone size isn't fixed; it varies with image size, layer depth, and
motion.

**visionOS** — don't add a shape meant to read as a hole or a concave area on the
background layer. The system's own shadow and specular highlights will make it pop forward
instead of recede.

**watchOS** — avoid a black background (see Appearances above). Center primary content
carefully — watchOS icons get circular masking, so anything near the corners is cut.

**macOS document icons** (adjacent to the app icon, not it): traditionally a
folded-top-right-corner page. Skip it and macOS composites your app icon plus the file
extension automatically. Background fill sizes run 16×16 up to 512×512 px @1x (each with a
@2x); the center image is half that canvas and should occupy about **80%** of it (a **10%**
margin), staying out of the top-right corner where the folded-corner mask draws.

---

## App icons vs interface icons

**App icon** — one per app, rich and detailed: shading, texture, highlights, layered depth.
It's branding. Use it only as the app's identity on Home Screen, Settings, etc. — never as
an in-UI glyph.

**Interface icons** (glyphs) — the small icons inside your UI for actions and content:
toolbars, tab bars, buttons, menus. Streamlined shapes, touches of color, black-and-clear
source art the system recolors. Use SF Symbols for these first; design custom glyphs only
when no symbol fits, and match their weight and detail level to the rest of your icon set.

Rule of thumb: if it identifies the app from outside, it's an app icon. If it labels an
action or a piece of content inside the app, it's an interface icon. Never substitute one
for the other.

---

## Common mistakes

- [ ] Feathered or soft edges on foreground layer shapes.
- [ ] Pre-masking layers yourself (rounded corners, circular crop) instead of supplying
      full square/rectangular art and letting the system mask it.
- [ ] A custom background layer that isn't full-bleed and opaque.
- [ ] Baking in shadows, bevels, glows, or highlights that duplicate system effects.
- [ ] Non-essential text — instructional words, "New", platform names.
- [ ] Photos or app screenshots used as the icon; replicas of Apple hardware.
- [ ] Dark/clear/tinted variants that swap design elements instead of toning down the
      same ones.
- [ ] An alternate icon loose enough from the app's content that it could pass for a
      different app.
- [ ] tvOS: text under other layers (parallax crop cuts it), or content with no safe zone.
- [ ] visionOS: a background shape meant to read as a hole or recess.
- [ ] watchOS: a black background that blends into the bezel.
