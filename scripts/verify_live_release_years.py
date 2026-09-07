#!/usr/bin/env python3
"""Verify public Pages responses against the checked-out release-year source."""
from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs'
OUT = Path('live-verification')
OUT.mkdir(exist_ok=True)
sha = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
audit = json.loads((ROOT / 'scripts/release_years_20260907.json').read_text())
bases = {
    'project': 'https://world-model-benchmarks.github.io/World-Model-Benchmarks/',
    'root': 'https://world-model-benchmarks.github.io/',
}
paths = ['index.html', 'assets/metadata.json', 'assets/benchmarks.json', 'assets/release-years-20260907.json', 'assets/app-v3.js', 'assets/app-v3-core.js'] + [f'assets/benchmarks-{i}.json' for i in range(1,5)]
replacements = {
    'https://axbhb.github.io/world-model-evaluation-survey/': bases['root'],
    bases['project']: bases['root'],
    bases['project'].rstrip('/'): bases['root'].rstrip('/'),
    'https://github.com/axbhb/world-model-evaluation-survey': 'https://github.com/World-Model-Benchmarks/World-Model-Benchmarks',
}
checks = []
for site, base in bases.items():
    for rel in paths:
        expected = (ASSETS / rel).read_text(encoding='utf-8')
        if site == 'root':
            for old, new in replacements.items():
                expected = expected.replace(old, new)
        error = None
        for attempt in range(5):
            try:
                url = base + rel + f'?release_year_verify={sha}-{attempt}'
                req = Request(url, headers={'User-Agent':'World-Model-Benchmarks-release-year-check', 'Cache-Control':'no-cache'})
                with urlopen(req, timeout=30) as response:
                    body = response.read().decode('utf-8')
                if body != expected:
                    raise AssertionError('Published bytes do not yet match the checked-out source')
                target = OUT / site / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(body, encoding='utf-8')
                checks.append({'site':site,'path':rel,'status':'matched','sha256':hashlib.sha256(body.encode()).hexdigest()})
                error = None
                break
            except Exception as exc:
                error = str(exc)
                if attempt < 4:
                    time.sleep(8)
        if error:
            checks.append({'site':site,'path':rel,'status':'failed','error':error})
            break
for site in bases:
    p = OUT / site / 'assets/benchmarks.json'
    if p.exists():
        manifest = json.loads(p.read_text())
        assert {name: row[1] for name,row in manifest['records'].items()} == audit['years']
report = {'checkedAt':datetime.now(timezone.utc).isoformat(),'sourceCommit':sha,'releaseYearSourcePdfSha256':audit['sourcePdfSha256'],'checks':checks,'expectedChecks':len(paths)*len(bases)}
report['success'] = len(checks)==report['expectedChecks'] and all(x['status']=='matched' for x in checks)
(OUT/'report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
assert report['success'], 'Live verification failed; inspect live-verification/report.json'
