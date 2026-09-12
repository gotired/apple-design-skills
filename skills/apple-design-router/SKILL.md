---
name: apple-design-router
description: Guide a user to the right Apple Design Suite workflow and explain the recommended path. Use when someone asks which Apple-design skill to use or how to begin an Apple UI task.
---

# Ask Apple Design

Start by naming the recommended route in one sentence. Ask a question only when the platform
or desired outcome changes the route.

## Main flow: idea → verified UI

Most product work follows this path.

1. **Decide the platform and flow.** Use `$apple-design` for the platform, foundations,
   components, patterns, and input rules that constrain the design.
2. **Build.** For web UI, use `$apple-design-web`. For native UI, apply the selected HIG
   reference directly with the platform's standard components.
3. **Verify.** Use `$apple-design-qa` after visual work. It checks rendered light, dark,
   and narrow states; it does not replace an audit.
4. **Audit.** Use `$apple-design-review` before handoff. Section A accessibility failures
   are blockers.

## Starting points

| User’s situation | Recommended route | Why |
|---|---|---|
| “What should this iOS/iPadOS/macOS screen do?” | `$apple-design` | Start with the platform and standard patterns. |
| “Build a page that feels like Apple.” | `$apple-design-web` → `$apple-design-qa` | Tokens and web mapping guide implementation; rendered states prove it holds up. |
| “Review this Figma, screenshot, HTML, or app.” | `$apple-design-review` | The checklist turns HIG guidance into actionable findings. |
| “The UI looks wrong in dark mode/mobile.” | `$apple-design-qa` | Inspect the rendered state before changing rules. |
| “Are our HIG references current?” | `$apple-design-refresh` → `$apple-design-review` | Refresh source-derived files, then review generated diffs. |
| “Which one should I use?” | This skill | Route from outcome, not from a memorized skill name. |

## Side paths

- A disputed interaction or layout direction: make a small prototype first, then join the
  main flow at `$apple-design`.
- A source/API availability question: confirm it on the relevant official Apple page before
  treating the local condensation as current.
- A code-quality or spec question outside design: use the host project’s normal engineering
  workflow; this suite owns design guidance and visual verification.

## Completion

The user should leave with one next skill, the reason it fits, and the next verification step.
