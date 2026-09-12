---
name: apple-design-qa
description: Render and visually inspect Apple Design Suite HTML examples or Apple-inspired web UI in light, dark, and narrow layouts.
---

# Apple Design QA

For the bundled Settings reference, run:

```sh
CI=1 scripts/preview.sh 320 /tmp/apple-design-320
CI=1 scripts/preview.sh 390 /tmp/apple-design-390
```

Inspect both appearances. Check clipping, wrapping, 44px targets, contrast-sensitive text, focus visibility, and the navigation/content layering. Use the project’s own renderer for other pages, with the same states where possible.

State what was rendered and what could not be verified. Do not call fixed-width comparison case studies responsive production templates.
