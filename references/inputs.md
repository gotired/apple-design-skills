# Inputs — how people drive the interface

Every way people direct an Apple device: gestures, keyboards, pointing devices, focus
navigation, and platform-specific inputs (Digital Crown, eyes, remotes, Action button,
Camera Control, Apple Pencil, game controls, motion sensors, nearby interactions).
Platform deltas that don't fit here live in `platforms.md`.

---

## Gestures

Physical motion — touch, air, or a device's touch surface. All platforms.

- Never make a gesture the only way to do something important.
- Match expectations: tap activates/selects everywhere. Don't repurpose a standard gesture
  for an app-specific action, or invent one for something standard already covers.
- Respond immediately with feedback that predicts the result; show clearly when a gesture
  is unavailable.
- Custom gestures only for a frequent task with no standard equivalent (games, drawing):
  discoverable, distinct, and a supplement to standard navigation, never a replacement.
- Don't conflict with system gestures (edge swipe in watchOS, palm-roll in visionOS).

**iPadOS:** three-finger swipe = undo/redo; three-finger pinch = copy/paste; four-finger
swipe = switch apps; shake = undo/redo.

**visionOS:** **indirect** (look to target, pinch at a distance) vs. **direct** (touch the
object). Prefer indirect for UI/buttons; direct suits close-up, infrequent use. Custom hand
gestures need a Full Space plus hand-tracking permission; avoid a required hand, a complex
two-hand gesture, or a rolling wrist motion (reserved for the system overlay).

**watchOS 11+:** double tap scrolls lists/tabs or fires a view's one "primary action."
Never set a primary action in a scrolling or tabbed view.

---

## Keyboards

Physical keyboard, connectable to every device except Apple Watch. Onscreen (virtual)
keyboard covers devices without one; never supports shortcuts.

- Support **Full Keyboard Access** (iOS, iPadOS, macOS, visionOS).
- **iPadOS:** keyboard navigation only for content (text fields/views, sidebars, custom
  lists) — leave controls to Full Keyboard Access.
- Redefine a standard shortcut only if its action is meaningless in your app. Custom
  shortcuts only for the most frequent app-specific commands.
- Modifier order: **Control, Option, Shift, Command.** Command as main modifier, Shift
  secondary, Option sparingly; avoid Control (system-reserved).
- Don't stack a modifier onto an existing shortcut for an unrelated command; let the
  system localize/mirror shortcuts.
- **visionOS:** shortcuts surface in an overlay on holding Command; titles need to be
  self-explanatory (no submenu context).

**Virtual keyboard:** match the type to the content (numeric, email, URL, phone) via a
semantic content type; customize the Return key label when it clarifies the action (e.g.,
Search). A **custom input view** replaces the keyboard inside your app only. A **custom
keyboard** (app extension) replaces it everywhere; unusable in secure text/phone fields;
needs an obvious switch control; don't duplicate the Emoji/Globe/Dictation keys. Not
supported in macOS. tvOS: linear keyboard for the Siri Remote, grid otherwise. watchOS:
shown only if the screen is large enough, else dictation/Scribble.

---

## Pointing devices

Mouse and trackpad. Primary on macOS; supplementary on iPadOS and visionOS — never
replaces touch, eyes, or gestures.

- Never redefine a systemwide trackpad gesture, even in a game.
- Same experience regardless of gesture, eyes, pointer, or keyboard input.
- Let the pointer reveal auto-hiding controls (hover shows a minimized toolbar).
- A modifier-key behavior (Option-drag to duplicate) must match between touch and pointer.

**iPadOS:** three content effects — **highlight** (small, transparent bg: bar buttons),
**lift** (small, opaque bg: app icons), **hover** (large elements: custom scale/tint/
shadow). Magnetism applies by default to highlight/lift, not hover. Hit-region padding:
**~12 pt** around a bezeled element, **~24 pt** around an unbezeled one. Keep adjacent
bar-button hit regions contiguous. Avoid gratuitous pointer effects. For custom hover:
scale only where growth won't crowd a neighbor; shadow always needs scale to feel real.

**macOS** defines ~15 standard gestures (click, scroll, smart zoom, swipe between pages/
apps, Mission Control, force click, pinch zoom, rotate, Launchpad, Show Desktop) — don't
redefine any. Prefer standard pointer shapes over custom ones.

**visionOS:** gaze determines which window the pointer acts in; it hides during a trackpad/
mouse gesture and reappears where the person is looking.

---

## Focus and selection

The visual indicator of the object an interaction targets. Not supported in iOS or
watchOS.

- Rely on the system-provided focus effect; a custom one only if truly necessary.
- Don't move focus without user interaction — exception: a discrete-step device (keyboard,
  remote, controller) navigates to an item that then disappears, so focus jumps nearby.
- **iPadOS/macOS** need focus only for content elements (list items, text/search fields);
  **tvOS** needs every onscreen element focusable.
- Focus ring for a text/search field; full-row highlight in a list or collection.

**iPadOS (15+):** Tab moves between focus groups (sidebar, grid, list); arrow keys move
within one group. The **halo** (focus ring) defaults to the item's shape; the
**highlighted** appearance (accent-colored text) signals focus but isn't a focus effect.
Focus order is leading-to-trailing, top-to-bottom; raise an item's priority to make it its
group's primary item.

**tvOS:** in full-screen content, gestures affect content, not focus. Never show a
free-roaming pointer for menu navigation. Design for five focus states — unfocused,
focused, chosen, selected/deselected, unavailable — with larger assets for the scaled-up
focused state and room around it.

**visionOS:** same focus system as iPadOS/tvOS for keyboard/controller nav; separate from
the gaze hover effect.

---

## Digital Crown

Apple Watch and Apple Vision Pro. Not supported elsewhere.

**Vision Pro:** system-reserved — volume, immersion level, recentering content,
Accessibility settings, exit to Home View. Apps never receive Crown events.

**Apple Watch** (primary navigation input since watchOS 10): turning it scrolls lists/
pages, switches vertical tabs, browses the Smart Stack, moves through Home Screen apps.
Apps never receive Crown *presses* (system-reserved).

- Anchor your app's navigation to vertical Crown scrolling; back every Crown interaction
  with an equivalent touch gesture.
- Use the Crown for data inspection where navigation isn't the point.
- Always give visual feedback for a turn; match update speed to turn speed.
- Haptic detents are on by default (linear); turn off if they clash with your animation;
  use linear detents for tables with uneven row heights.

---

## Eyes

Gaze targeting in visionOS. Not supported elsewhere.

- Looking at an element triggers the **hover effect**; the system never reports *where*
  someone is looking until they act (privacy). Unrelated to keyboard/controller focus.
- Always offer another way to interact besides gaze. Prefer standard components.
- Keep needed objects within the field of view; avoid repeated large eye jumps across a
  wide area or across depth. Place sustained content at least **1 meter** away.
- Minimize visual noise and peripheral motion (it involuntarily pulls gaze away); avoid a
  repeating pattern across the whole field of view (can appear to shift depth).
- Give interactive items **≥16 pt** margin, or space centers **≥60 pt** apart. Prefer
  rounded shapes — corners pull the eye away from center.
- Group a multi-element control (image + label) under one hit/highlight region.

**Custom hover effects** run out-of-process: you define two states and the system swaps
them, so a custom effect can never trigger app logic. Delay: none for subtle/inviting
effects; short for something quickly actionable (tab-bar expansion); long for extra info
most people won't need (tooltips). Keep one primary view unchanged across both states, and
test while actually wearing the device.

---

## Remotes

Siri Remote — clickpad plus touch surface. tvOS only.

- Prefer standard gestures for standard actions outside gameplay; move focus in the same
  direction as the gesture.
- Differentiate an intentional press from an incidental resting tap; ignore taps during
  live video playback.
- **Back** opens the parent of the current screen — except in active gameplay, where it
  should open a pause menu instead. Press-and-hold Back always returns to the Home Screen.
- **Play/Pause** must control media playback, whatever else it maps to in a game.

| Control | In an app | In a game |
|---|---|---|
| Touch surface swipe | Navigate, change focus | Directional pad |
| Touch surface press | Activate, navigate deeper | Primary button |
| Back | Previous screen / Home | Pause/resume; back / main menu |
| Play/Pause | Play, pause, resume | Secondary button; skip intro |

If your app provides an EPG, respond to guide/browse and page-up/down as expected;
page-up/down changes channel outside the guide.

---

## Action button

iPhone 15 Pro+ and Apple Watch Ultra. Not supported on iPadOS, macOS, tvOS, visionOS.

- Support essential app functions as App Shortcuts — no generic "open the app" action.
- Label each: title case, verb-first, present tense, no articles/prepositions,
  **max three words** ("Start Race," not "Started Race").
- Let the system handle onboarding/configuration in Settings.

**iOS:** prefer staying in context (a Live Activity or snippet, not a full app launch).

**watchOS:** first press picks the primary action (waypoint, dive/workout start). A
secondary action, if offered, should logically extend the first — never more than one, and
never a stop/end action. Action + side button together pauses the current activity, except
where pausing is unsafe (mid-dive).

---

## Camera Control

iPhone 16 / 16 Pro. Not supported elsewhere.

- Light press opens the overlay; light double-press reveals all controls; sliding a finger
  adjusts the selected control.
- Two control types: **slider** (continuous) and **picker** (discrete); standard zoom/
  exposure controls are available to opt into.
- SF Symbols only, representing function not current state. Keep names short. Show units
  on slider values (EV, %). Define **prominent values** the slider should snap to.
- Reserve the screen area next to Camera Control for the overlay; don't duplicate overlay
  controls elsewhere.
- Enable/disable controls per camera mode — can't add/remove controls at runtime.
- A locked camera capture extension launches your camera from the Lock Screen, Home
  Screen, or another app.

---

## Apple Pencil and Scribble

iPadOS only.

- Support real-world marking-instrument expectations (e.g., writing in margins); every
  touch-responsive control should also respond to Pencil.
- Mark the instant Pencil touches the screen — no mode switch first.
- Use tilt, pressure, orientation, and barrel roll to vary strokes; map pressure to
  continuous properties (opacity, brush size).
- Feedback must look directly and immediately connected to what Pencil touches.
- Design separately for left- and right-handed grips.

**Hover:** preview the mark before contact, without continuously changing as height
changes; never trigger an action from hover alone; preview near the middle of a dynamic
range; reserve it for Pencil, not a plain pointing device.

**Double tap:** respects the systemwide setting by default (switch tool/eraser, previous
tool, color picker); override only if the default doesn't fit, never on by default, never
bound to a destructive or hard-to-undo action.

**Squeeze** (Pencil Pro) works without touching the screen, so the result must be obvious:
one discrete action, shown near the tip, nondestructive and easy to undo. **Barrel roll**
(Pencil Pro) only changes the type of mark mid-stroke — never navigation or controls.

**Scribble:** works in any standard text field (not password fields), no tap-to-activate.
No autocomplete or placeholder text under active handwriting; field stays stationary, no
autoscroll while writing; size it generously in advance, no mid-write resize.

**PencilKit:** suppress automatic Dark Mode color adjustment when drawing over existing
content (photo/PDF); support standard three-finger undo/redo since the tool picker's own
buttons disappear in a compact layout.

---

## Game controls

Touch controls: iOS/iPadOS. Physical controllers: every platform except watchOS.

**Touch controls:** prefer direct interaction with game objects over a virtual button when
the mechanic allows it. Place buttons clear of safe areas, frequent ones near the thumb and
away from movement/camera zones, secondary controls (menus) at the top. Frequent controls
**≥ 44×44 pt**; secondary/menu controls **≥ 28×28 pt**. Always give a visible *and* tactile
press state. Use art depicting the action, not abstract shapes or controller-labels
(A/X/R1). Show/hide controls by context; combine multi-press/sequenced actions into one
control (touch-and-hold or double-tap for variants). Movement left, camera right, by
convention; let the virtual thumbstick appear wherever the thumb lands.

**Physical controllers:** always fall back to the platform's default input. tvOS and
visionOS may require a controller (App Store "Game Controller Required" badge) — still
detect its absence and prompt gracefully. Auto-detect a paired controller and label
controls using its own naming/branding.

| Button | Expected UI behavior |
|---|---|
| A | Activate a control |
| B | Cancel / return to previous screen |
| Left/right shoulder | Navigate left/right between screens |
| Left/right thumbstick, d-pad | Move selection |
| Home/logo | Reserved for the system |
| Menu | Open settings / pause |

(X, Y, and the triggers have no systemwide UI convention.) With multiple controllers, show
labels for the one in use; label per player in multiplayer. Prefer symbols over text.

**Keyboard (games):** prioritize single-key commands (first-letter mnemonics, Space for
the main action). Test bindings on an actual Apple keyboard — e.g., remap a non-Apple
^Control binding to ⌘Command next to WASD. Group related actions on physically close keys.
Let players remap bindings.

**visionOS:** spatial controllers (e.g., PS VR2 Sense) mirror hand input — look + trigger
indirect, reach + trigger direct.

---

## Gyroscope and accelerometer

Also known as motion sensors in earlier HIG versions. Use this section when an experience
responds to device orientation, acceleration, or movement; prefer standard system behavior
and provide a non-motion alternative for important actions.

Gyroscope and accelerometer. iOS, iPadOS, watchOS get raw device-motion data; tvOS can
read gyro data from the Siri Remote. Not on macOS; visionOS uses head pose separately.

- Use motion data only for a concrete benefit — never collect it just to have it.
- Show a permission-request string explaining why, the first time you access it.
- Outside active gameplay, avoid motion as the direct way to manipulate the interface —
  hard to replicate precisely, physically difficult for some people, costs battery.

---

## Nearby interactions

Devices with Ultra Wideband (U1 chip): iOS gets a peer's distance and direction, watchOS
gets distance only (app must stay foreground). Not on macOS, tvOS, or visionOS.

- Root the interaction in a real physical action (bring two devices together to transfer
  audio) rather than a pure onscreen flow.
- Feed distance, direction, and context into the interaction; make feedback continuous and
  sharpen as devices get closer (e.g., arrow → pulsing circle). Combine visual, audio, and
  haptic feedback.
- Never make it the only way to complete a task.
- Encourage portrait orientation (landscape reduces direction accuracy) with implicit
  visual cues rather than telling people outright.
- Sensor field of view roughly matches the iPhone 11+ Ultra Wide camera — outside it, you
  may get distance but not direction. Nearby people, animals, or large objects between two
  devices can degrade accuracy.
