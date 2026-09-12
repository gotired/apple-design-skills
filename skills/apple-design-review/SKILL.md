---
name: apple-design-review
description: Audit an interface against the bundled Apple HIG checklist and report actionable accessibility, platform, component, and content findings.
---

# Apple Design Review

Read `../../references/checklist.md`, then the platform and component references needed by the UI under review.

When reviewing this suite itself, run `scripts/verify.sh` from the suite root. For another project, run its safe existing checks. Inspect rendered UI when it exists; do not claim a visual check from source alone.

Report only real findings using the checklist format: severity, rule, location, problem, and fix. Section A failures are blockers. End with the checks performed and any unverified states.
