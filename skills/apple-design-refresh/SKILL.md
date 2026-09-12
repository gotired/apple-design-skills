---
name: apple-design-refresh
description: Fetch a fresh Apple Human Interface Guidelines snapshot and safely regenerate the bundled derived references. Use when Apple guidance needs updating.
---

# Apple Design Refresh

Run from the suite root:

```sh
python3 scripts/refresh-hig.py
scripts/verify.sh
```

Review generated diffs before accepting them. The default fetches a fresh source snapshot; `--use-cache` is only for an intentional offline or repeatable run. Hand-written references and CSS need a human comparison with the cached Markdown source before changes are accepted.
