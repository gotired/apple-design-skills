#!/usr/bin/env bash
# Render examples/settings.html in both appearances and open the screenshots.
#
#   scripts/preview.sh [width] [outdir]
#
# Two headless-Chrome gotchas this works around, both of which produce screenshots
# that look like CSS bugs but aren't:
#
#   1. Headless Chrome clamps the viewport to a 500px minimum. Ask for --window-size=320
#      and it renders at 500, then crops the screenshot to 320 — the result looks like
#      horizontal overflow. To test narrow layouts, render wide and constrain the page
#      with CSS instead. That's what CONSTRAIN does below.
#   2. Headless Chrome defaults to dark mode, so prefers-color-scheme never reports light.
#      Both shots therefore set data-theme explicitly rather than relying on the media query.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONSTRAIN="${1:-390}"                       # simulated screen width, in CSS px
OUT="${2:-$REPO/.preview}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VIEWPORT=900                                # must stay above Chrome's 500px floor

[ -x "$CHROME" ] || { echo "Google Chrome not found at $CHROME" >&2; exit 1; }

mkdir -p "$OUT"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

cp "$REPO/assets/apple-tokens.css" "$work/"

for theme in light dark; do
  sed -e 's|\.\./assets/apple-tokens\.css|apple-tokens.css|' \
      -e "s|<html lang=\"en\">|<html lang=\"en\" data-theme=\"$theme\">|" \
      -e "s|</head>|<style>.screen{max-width:${CONSTRAIN}px !important}</style></head>|" \
      "$REPO/examples/settings.html" > "$work/$theme.html"

  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
            --window-size=$VIEWPORT,1000 \
            --screenshot="$OUT/$theme.png" \
            "file://$work/$theme.html" >/dev/null 2>&1

  echo "  $OUT/$theme.png"
done

echo "rendered at ${CONSTRAIN}px inside a ${VIEWPORT}px viewport"
[ "${CI:-}" ] || open "$OUT/light.png" "$OUT/dark.png"
