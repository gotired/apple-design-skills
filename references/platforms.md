# Platforms — what changes per OS

The foundations are shared. This file holds the deltas. Read the section for the platform
you are targeting; if you're building for the web with an Apple look, read **iOS** and
**macOS** and pick the one your layout resembles.

---

## Design principles (all platforms)

The current HIG frames cross-platform decisions around eight principles:

1. **Purpose** — make something meaningful and focus on what matters to people.
2. **Agency** — let people act freely, understand what is happening, and recover from
   mistakes.
3. **Responsibility** — prioritize safety, privacy, transparency, and people’s well-being.
4. **Familiarity** — build on patterns people already know and use them consistently.
5. **Flexibility** — adapt to diverse contexts, needs, devices, and input methods.
6. **Simplicity** — make the experience clear, direct, and free of unnecessary complexity.
7. **Craft** — care about the details and iterate until the result feels intentional.
8. **Delight** — make the experience human without confusing decoration for value.

---

## iOS

**Device.** Medium, high-resolution display. Held in one or both hands, rotated freely.
Viewing distance one to two feet.

**Inputs.** Multi-Touch, virtual keyboard, voice, gyroscope/accelerometer.

**Sessions.** Alternate between one-minute checks and hour-long stretches. Many apps open
at once, switched between constantly.

**System features to integrate.** Widgets, Home Screen quick actions, Spotlight, Shortcuts,
activity views.

**Design consequences**

- Limit onscreen controls. Make secondary actions discoverable in one interaction.
- Adapt to orientation, Dark Mode, and Dynamic Type without being asked.
- Put frequent controls in the middle or lower part of the screen — that's where thumbs
  reach. Support swipe-back and swipe actions in list rows.
- Use platform capabilities (payments, biometrics, location) instead of making people type.
- Avoid full-width buttons; respect the side margins.
- Keep the status bar unless the experience is immersive.

**Numbers.** 17 pt body. 44×44 pt touch target. 16 pt side gutter.

## iPhone Duo

iPhone Duo is still an iOS experience, but it can move between an outer display, an inner
display, and several folded poses. Use the iOS rules first, then add these constraints:

- Build to resize with size classes, layout margins, and safe-area insets. Avoid fixed widths
  and display-specific dependencies.
- Keep information hierarchy and state consistent across displays. Expand to a split view on
  the inner display when the content benefits from it; collapse naturally on the outer one.
- Respect reserved regions such as the hinge, camera, Dynamic Island, and status bar. Make
  only the smallest layout changes needed as the device folds.
- Keep toolbar and tab-bar placement predictable on the vertical axis. Use system overflow
  behavior when space is limited, and prioritize frequently used or status-bearing controls.
- Group related toolbar items with system item groups rather than hand-tuned fixed spacing.
- Test closed, partially folded, open, portrait, landscape, and Split View configurations.

---

## iPadOS

Everything from iOS, plus:

- Windows are freely resizable down to a minimum, the way macOS windows are. Design for
  the whole range, not two breakpoints.
- Design the full-screen layout first. Switch to the compact layout as late as possible —
  a stable, familiar UI beats an eagerly-collapsing one.
- In split views, hide the tertiary column (inspector) before collapsing anything else.
- Test at halves, thirds, and quadrants — those are the system's own window sizes.
- Consider a **convertible tab bar** (`sidebarAdaptable`): launches as a tab bar or a
  sidebar, and people can switch; the presentation follows the window width.
- Support Apple Pencil and Scribble where text or drawing is involved.

---

## macOS

**Device.** Large, high-resolution, often multiple displays. Stationary use, one to three
feet away.

**Inputs.** Keyboard, pointing devices, game controllers, Siri. High precision expected.

**Sessions.** Minutes to hours. Many apps open, frequent switching, clear active/inactive
window states.

**System features to integrate.** The menu bar, file management, full-screen mode, Dock
menus.

**Design consequences**

- Use the space: fewer nested levels, less modality, more content visible at once — but
  don't crowd it.
- Windows must be resizable, hideable, movable. Support full screen.
- Every command in the app belongs in the menu bar.
- Support keyboard shortcuts and keyboard-only workflows.
- Let people customize toolbars.
- Nothing critical at the bottom edge of a window — people drag windows off-screen there.
- Nothing under the camera housing at the top edge.

**Numbers.** 13 pt body. 28×28 pt pointer target (20×20 minimum). No Dynamic Type.

---

## watchOS

**Design consequences**

- Content runs edge to edge; the bezel supplies the padding. Minimize internal padding.
- Max three glyph buttons, or two text buttons, side by side. A full-width text button is
  usually better.
- The Digital Crown is a primary input, not a nicety.
- Full-screen modal views are normal here — keep their default material backgrounds; they
  are how people stay oriented.
- Background color should say something, not decorate. Avoid full-screen color in views
  that stay up a long time (workouts, audio).
- Support autorotation for views people show to someone else (a QR code, a photo).

**Numbers.** 16 pt body (SF Compact). 44×44 pt target. Text must enlarge to 140%.

---

## tvOS

**Design consequences**

- Layouts do **not** adapt to screen size — the same interface ships to every TV. Design
  once, carefully.
- Safe area: inset primary content **60 pt** top and bottom, **80 pt** left and right.
- Focus, not color, communicates interactivity: subtle scaling and responsive animation.
- Leave padding between focusable items so a focused (enlarged) item doesn't overlap
  anything.
- Keep partially-hidden offscreen content symmetrical on both sides.
- Test on multiple TV brands and display settings.

**Numbers.** 29 pt body (23 pt minimum). 66×66 pt focus target.

---

## visionOS

**Design consequences**

- Center important content and controls; large windows push the edges out of comfortable
  view.
- Keep content inside the window bounds — system controls (share, resize, close) live just
  outside them.
- Extra controls go in an **ornament**, not in the window.
- Interactive element centers at least **60 pt** apart, so the gaze hover effect doesn't
  swallow its neighbors.
- Prefer 2D text. Depth makes text harder to read.
- Windows use the system **glass** material. Prefer translucency; opaque areas block the
  room and feel constricting. There is no Dark Mode — glass adapts to luminance.
- Text defaults to white for contrast against glass. Bold unbacked text rather than
  shadowing it.
- Billboard any text anchored to a point in space so it always faces the wearer.
- Prioritize comfort: minimal physical movement, no head-anchored content, no world
  rotation, no peripheral motion.
- Prefer standard indirect gestures (look + pinch) over custom ones.

**Numbers.** 17 pt body (12 pt minimum). 60×60 pt target. Uses the **dark** system colors.

---

## Games (all platforms)

- Test text legibility on every platform the game ships to; game text often fails where UI
  text passes.
- 30–60 fps for a smooth feel. Set good defaults per device rather than making people
  configure first.
- Offer difficulty accommodations, control assistance, and reaction-time adjustment.
- Let people opt out of flashing lights; honor Dim Flashing Lights.
- Full-bleed on iOS, but accommodate the corner radius, sensor housing, and Dynamic Island.
