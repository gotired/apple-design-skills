#!/usr/bin/env bash
# Validate the repository without fetching HIG content or rewriting references.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

bash -n scripts/preview.sh scripts/verify.sh
python3 -m py_compile scripts/refresh-hig.py
git diff --check

python3 - <<'PY'
from pathlib import Path
import re

missing = []
for file in Path('.').rglob('*.md'):
    if {'.git', '.hig-cache', 'graphify-out'} & set(file.parts):
        continue
    for raw in re.findall(r'\]\(([^)]+)\)', file.read_text()):
        link = raw.split()[0].strip('<>')
        if link.startswith(('#', 'http:', 'https:', 'mailto:')):
            continue
        if not (file.parent / link).resolve().exists():
            missing.append(f'{file}: {link}')

if missing:
    raise SystemExit('Broken local Markdown links:\n' + '\n'.join(missing))
print('Local Markdown links: OK')
PY

python3 - <<'PY'
import importlib.util
import json
from pathlib import Path
import tempfile

spec = importlib.util.spec_from_file_location('refresh_hig', 'scripts/refresh-hig.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.time.sleep = lambda _: None

with tempfile.TemporaryDirectory() as directory:
    cache = Path(directory)
    path = '/design/human-interface-guidelines/test'
    cached = cache / 'hig' / 'design__human-interface-guidelines__test.json'
    cached.parent.mkdir(parents=True)
    cached.write_text(json.dumps({'snapshot': 'cached'}))
    module.get = lambda *_args, **_kwargs: {'snapshot': 'fresh'}
    assert module.page_json(str(cache), path, use_cache=True)['snapshot'] == 'cached'
    assert module.page_json(str(cache), path, use_cache=False)['snapshot'] == 'fresh'

print('Refresh cache policy: OK')
PY

python3 - <<'PY'
from pathlib import Path
import re

css = Path('assets/apple-tokens.css').read_text()
match = re.search(r'--label-secondary-accessible:\s*rgb\(60 60 67 / ([0-9.]+)\)', css)
assert match and float(match.group(1)) >= .75, 'Accessible secondary token is too light'
print('Accessible secondary token: OK')
PY

echo 'Verification complete.'
