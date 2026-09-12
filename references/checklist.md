# HIG review checklist

Work top to bottom. **Section A is a gate** — a failure there is a defect, not a
preference, and gets reported regardless of what else is good. B through H are
craft: report what actually fails, don't pad the list.

For each finding give: the rule, where it fails, and the fix. Cite the HIG page
(`https://developer.apple.com/design/human-interface-guidelines/<slug>`) when the rule
isn't obvious.

---

## A. Gate — accessibility and safety

- [ ] **Contrast.** Text up to 17 pt hits 4.5:1. Text 18 pt+ or bold hits 3:1. Checked in
      *both* light and dark. (Dark Mode target for custom colors: 7:1.)
      Watch two specific traps: `secondaryLabel` is only 3.4:1 in light mode, and white on
      the default system blue is 3.5:1. See the measured table in `foundations.md` §5.
- [ ] **Nothing by color alone.** Every state, category, and error also has a shape, an
      icon, or a label.
- [ ] **Touch targets.** 44×44 pt on iOS/iPadOS/watchOS, 28×28 on macOS, 66×66 on tvOS,
      60×60 on visionOS. Measured on the *hit area*.
- [ ] **Target spacing.** ~12 pt around bezeled controls, ~24 pt around unbezeled ones.
- [ ] **Text scales to 200%** (140% on watchOS) without truncation, overlap, or a broken
      hierarchy.
- [ ] **Reduce Motion** is honored: no springs, no z-axis animation, transitions become
      fades, blurs don't animate.
- [ ] **Increase Contrast** and **Reduce Transparency** are honored, including together.
- [ ] **Keyboard.** Every action reachable, focus order sane, focus indicator visible.
      On iPadOS the scope is narrower than it looks: keyboard navigation covers content
      (text, sidebars, custom lists); controls are Full Keyboard Access's job. See
      `inputs.md` → Keyboards.
- [ ] **Labels.** Every icon-only control has an accessible label. Custom symbols too.
- [ ] **Gestures have an alternative.** No swipe-only or multi-finger-only action.
- [ ] **No timed dismissal** of anything carrying information.
- [ ] **Media** doesn't autoplay without controls; video has captions.

## B. Typography

- [ ] Body text at the platform default (iOS 17 pt, macOS 13 pt, tvOS 29 pt, watchOS 16 pt).
      Nothing below the platform minimum.
- [ ] Weights are Regular / Medium / Semibold / Bold. No Thin, Light, or Ultralight.
- [ ] Tracking follows the SF table — negative from 13–23 pt, positive above 24 pt.
- [ ] One typeface, two at the outside.
- [ ] The size steps are the Dynamic Type steps, not arbitrary numbers.
- [ ] Hierarchy holds at the largest accessibility size.

## C. Color

- [ ] System / semantic colors where they exist; no hard-coded values in a native app.
- [ ] Every custom color has a light variant, a dark variant, and an increased-contrast
      variant of each.
- [ ] Semantic colors used for their meaning only (`separator` is not text; secondary label
      is not a background).
- [ ] One color, one meaning, across the whole product.
- [ ] Dark colors are chosen, not inverted.
- [ ] Grouped vs. plain background set chosen deliberately and used consistently on a screen.

## D. Materials, layout, depth

- [ ] Liquid Glass appears **only** on the control and navigation layer. None in the
      content layer.
- [ ] At most one or two custom glass surfaces.
- [ ] Clear glass only over media, and with the 35% dark scrim when the media is bright.
- [ ] Content scrolls *under* the bars; a scroll edge effect handles the transition, not a
      solid bar background.
- [ ] Backgrounds and artwork extend to the display edges.
- [ ] Safe areas respected — Dynamic Island, camera housing, home indicator, tvOS 60/80 pt.
- [ ] Elements are aligned to each other; the grid is real.
- [ ] Most important content top-leading; logical properties so RTL mirrors correctly.
- [ ] Layout survives rotation, window resize, and the platform's standard window fractions.

## E. Components and patterns

- [ ] One prominent button per view (two at the most).
- [ ] Preferred option distinguished by *style*, never by size.
- [ ] Every custom button has a visible press state.
- [ ] Destructive actions are red, confirmed, and never the primary/default button.
- [ ] Sheets: one at a time, an explicit way out beyond "Done", not used for long flows.
- [ ] Alerts are rare, and each one is genuinely blocking.
- [ ] Loading states show progress where the duration is known, activity where it isn't.
- [ ] Empty states say what to do next.
- [ ] Error messages say what happened *and* what to do.
- [ ] Onboarding is skippable and doesn't front-load a tour.
- [ ] Permissions requested in context, never at launch, with copy explaining why.
- [ ] Settings hold preferences people set rarely, not the app's actual controls.
- [ ] Standard components used unless there's a real reason not to.

## F. Inputs

- [ ] No gesture is the only way to do something.
- [ ] No custom gesture where a standard one exists; none that collide with system
      gestures (watchOS edge swipe, visionOS wrist roll).
- [ ] Standard keyboard shortcuts not redefined; modifier order Control, Option, Shift,
      Command.
- [ ] Virtual keyboard type matches the field's content.
- [ ] The platform's own primary input is supported, not just touch — Digital Crown,
      Siri Remote, pointer hover, gaze, Apple Pencil.
- [ ] Full detail in `inputs.md`.

## G. Platform fit

- [ ] The app uses the platform's own navigation model (tab bar / sidebar / menu bar /
      focus engine) rather than one carried over from another OS.
- [ ] **iOS:** no full-width edge-to-edge buttons; reachable primary controls; status bar
      kept.
- [ ] **iPadOS:** full layout preferred, compact deferred; tested at halves/thirds/quadrants.
- [ ] **iPhone Duo:** resized across outer/inner displays and folded poses; hinge, camera,
      Dynamic Island, vertical toolbar/tab-bar placement, overflow, and Split View tested.
- [ ] **macOS:** all commands in the menu bar; keyboard shortcuts; resizable windows;
      nothing critical at the window's bottom edge.
- [ ] **watchOS:** edge-to-edge, ≤3 glyph buttons per row, Digital Crown supported.
- [ ] **tvOS:** focus-driven, identical layout on every screen size, safe area respected.
- [ ] **visionOS:** content centered and inside window bounds, ornaments for extra controls,
      60 pt between interactive centers, 2D text.

## H. Voice and content

- [ ] Buttons and titles are action-oriented, verb-first.
- [ ] Capitalization rule applied consistently.
- [ ] Plain language; technical terms defined on first use.
- [ ] Copy reads acceptably from more than one cultural perspective.
- [ ] Branding defers to content; no logo scattered through the UI; the launch screen isn't
      a splash ad.

---

## Reporting

Write findings as:

```
[severity] rule — location
  what's wrong
  → fix
```

Severity: **blocker** (a Section A failure), **defect** (a clear HIG rule broken),
**polish** (a preference, or a rule that admits judgment). Sort blockers first. If a
section passes cleanly, say so in one line rather than listing every item.
