# Foundations — extended topics

This file covers the HIG foundation pages that do not fit the numeric foundation tables in
`foundations.md`. Use it with `foundations.md`; the official Apple pages remain authoritative
for platform-specific details and change logs.

## Branding

- Let content and the task lead. Branding should be recognizable without taking space from
  information or controls people came to use.
- Use accent color intentionally for primary actions and status, not across every control.
  Keep the content layer expressive while navigation and Liquid Glass surfaces stay calm.
- Use a custom font only when it is legible at every size and supports Bold Text and Dynamic
  Type. System fonts are usually best for body copy and captions.
- Preserve familiar component size, placement, behavior, symbols, navigation, and modality
  when applying a brand treatment.
- Put brand voice in copy, not repeated logos. A launch screen is for startup, not a splash
  advertisement; put a branded welcome moment in onboarding when it has real value.

## Images

- Ship high-resolution bitmap assets for every supported device and use the platform scale
  factors (`@1x`, `@2x`, `@3x`) in asset catalogs.
- Prefer vector artwork for flat scalable UI art. Include color profiles and test on real
  devices, because scaling, gamut, and viewing distance change the result.
- Use layered images for tvOS focus/parallax: keep the background opaque, keep text in the
  foreground, keep depth subtle, and leave a safe zone around essential foreground content.
- In visionOS, prefer vector art; use sufficiently high-resolution raster assets only when
  needed and balance sharpness against memory and rendering cost.
- Treat spatial photos and scenes as spatial content: use stereo HEIC, prefer the feathered
  glass background for overlaid text, give depth changes room, and avoid dense inline use.

## Immersive experiences

- Prefer Shared Space or `mixed` immersion as the starting point. Reserve Full Space and
  stronger immersion for content that genuinely benefits from it.
- Let people choose when to enter and exit immersion. Make the exit action explicit and
  explain whether it returns to a less immersive context or quits the experience.
- Design for visual and physical comfort: keep important content in the field of view,
  avoid peripheral motion, avoid requiring people to move, and keep passthrough visible in
  `mixed` immersion.
- Use subtle tinting and environmental detail. Reduce distracting motion and contrast away
  from the primary task, and make interactive objects distinguishable from decoration.
- When tracking is interrupted, fade virtual hands or other tracked representations instead
  of leaving them frozen and unresponsive.

## Spatial layout

- Treat space as a hierarchy: place important content in the field of view, keep windows and
  volumes comfortable to inspect, and avoid forcing people to move their head or body.
- Use standard windows, volumes, ornaments, and system placement behavior before inventing a
  custom spatial arrangement. Keep navigation outside arrangement views.
- Keep spatial content stable and predictable. Avoid world rotation, head-locked content,
  excessive depth changes, and motion in peripheral vision.
- Use depth to clarify relationships, not to decorate. Keep text readable and avoid placing
  important labels where perspective or parallax reduces legibility.
- Test seated and standing use, different room layouts, varied interpupillary distances, and
  accessibility settings. A spatial design is not complete until it remains comfortable in
  the physical context where it runs.

## Sources

- [Branding](https://developer.apple.com/design/human-interface-guidelines/branding)
- [Images](https://developer.apple.com/design/human-interface-guidelines/images)
- [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences)
- [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)
