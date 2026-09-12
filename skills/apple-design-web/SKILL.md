---
name: apple-design-web
description: Build or change an Apple-inspired web interface using the bundled HIG-to-CSS mapping and design tokens. Use for HTML, CSS, React, or web mockups that should follow Apple design guidance.
---

# Apple Design Web

Read `../../references/web-mapping.md` and `../../assets/apple-tokens.css` before editing UI.

Start from semantic tokens, not raw hues. Preserve 44px hit areas, visible focus, light/dark behavior, and a transparency fallback. Treat the supplied px type scale as a visual baseline; use rem-based production text when browser font settings matter.

After HTML/CSS changes, run `$apple-design-qa` or render the relevant page with Chrome in light and dark modes. Report which widths and appearances were checked.
