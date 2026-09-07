#!/usr/bin/env python3
"""One-time, guarded alignment with the 2026-09-07 PDF; no taxonomy changes."""
from pathlib import Path
import json
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs/assets'
audit = json.loads((ROOT / 'scripts/release_years_20260907.json').read_text())
manifest_path = ASSETS / 'benchmarks.json'
manifest = json.loads(manifest_path.read_text())
old_records = json.loads(json.dumps(manifest['records']))
old_fp = 'e30cf7f9b7bf39cb03baa6b9cddcbeb593b5821e1ba85a82fddff0787c7e4935'
new_fp = audit['recordFingerprint']
assert manifest['classificationFingerprint'] in (old_fp, new_fp), 'Unexpected source snapshot; review before applying.'
assert set(manifest['records']) == set(audit['years']) and len(audit['years']) == 102
for name, year in audit['years'].items():
    old = manifest['records'][name][1]
    assert old == year or audit['changes'].get(name, {}).get('from') == old, (name, old, year)
    manifest['records'][name][1] = year
assert all(row[:1] + row[2:] == old_records[name][:1] + old_records[name][2:] for name, row in manifest['records'].items())
rows = [name + '|' + '|'.join(map(str, row[:8])) for name, row in sorted(manifest['records'].items())]
assert hashlib.sha256('\n'.join(rows).encode()).hexdigest() == new_fp
old_version = 'August 31, 2026 manuscript snapshot'
new_version = 'August 31, 2026 corpus; release years revised September 7, 2026'
manifest['version'] = new_version
manifest['classificationFingerprint'] = manifest['recordFingerprint'] = new_fp
manifest['yearBasis'] = 'Benchmark release year as coded in Figure 2 and Tables 3-9 of the September 7, 2026 manuscript; distinct from formal publication year.'
manifest['releaseYearRevision'] = {key: audit[key] for key in ('sourcePdf', 'sourcePdfSha256', 'manuscriptDate', 'scope', 'changes', 'retainedCandidates')}
manifest['releaseWindowCounts'] = audit['releaseWindowCounts']
# Keep the previous sourcePdfSha256 as provenance for non-year coding.
manifest['sourceNote'] = 'Non-year benchmark coding retains its preceding manuscript source (sourcePdfSha256). Release years are aligned with the September 7, 2026 PDF identified in releaseYearRevision. The corpus cutoff remains August 31, 2026.'
manifest['publicationMetadata'] = {
    'CLEVRER': {'venue': 'ICLR', 'publicationYear': 2020},
    'CoPhy': {'venue': 'ICLR', 'publicationYear': 2020},
    'CRAFT': {'venue': 'Findings of ACL', 'publicationYear': 2022},
    'MMWorld': {'venue': 'ICLR', 'publicationYear': 2025},
    'WorldLens': {'venue': 'CVPR', 'publicationYear': 2026},
}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, separators=(',', ':')) + '\n')
(ASSETS / 'release-years-20260907.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')


def replace(text, old, new):
    if old in text:
        return text.replace(old, new)
    assert new in text, 'Expected source pattern is missing: ' + old[:100]
    return text

old_windows = '{"2018–2021": 5, "2022–2023": 5, "2024": 9, "2025": 30, "2026": 53}'
new_windows = '{"2018–2021": 6, "2022–2023": 4, "2024": 10, "2025": 30, "2026": 52}'
for filename in ('generate_readme_index.py', 'sync_latest_survey.py'):
    path = ROOT / 'scripts' / filename
    text = path.read_text()
    for a, b in ((old_fp, new_fp), (old_version, new_version), (old_windows, new_windows), ('<strong>49</strong>', '<strong>50</strong>'), ('app-v3.js?v=10', 'app-v3.js?v=20260907')):
        text = replace(text, a, b)
    if filename == 'generate_readme_index.py':
        for a, b in (
            ('"year": row[1],', '"year": row[1],\n            "releaseYear": row[1],'),
            ('        for legacy_field in', '        item.update(manifest.get("publicationMetadata", {}).get(name, {}))\n        for legacy_field in'),
            ('| Article | Year | Venue |', '| Article | Release Year | Venue |'),
            ('**Article**, **Year**, **Venue**', '**Article**, **Release Year**, **Venue**'),
            ('representative benchmarks** published from', 'representative benchmarks** released from'),
            ('`-` means that no verified public link is currently recorded.', 'Release Year follows the September 7, 2026 manuscript, not the formal publication year; the latter is shown separately with the venue where recorded. `-` means that no verified public link is currently recorded.'),
            ('        code = old.get("code", "-")', '        if item.get("publicationYear") and str(item["publicationYear"]) not in venue:\n            venue = f"{venue} {item[\'publicationYear\']}"\n        code = old.get("code", "-")'),
            ('    METADATA_PATH.write_text(', '    metadata.update({key: manifest[key] for key in ("yearBasis", "releaseYearRevision", "publicationMetadata", "sourceNote")})\n    METADATA_PATH.write_text('),
            ('app-v3-core.js?v=12', 'app-v3-core.js?v=20260907'),
        ):
            text = replace(text, a, b)
    else:
        text = replace(text, '        "all Figure 4 / Tables 3–10 coding, and synchronized repository/website outputs."', '        "preserved non-year coding and synchronized September 7 release-year outputs."')
        anchor = '    print(\n'
        check = '''    audit = json.loads((ROOT / "scripts/release_years_20260907.json").read_text(encoding="utf-8"))
    require({name: row[1] for name, row in records.items()} == audit["years"], "Release years differ from the 102 PDF transcriptions")
    require(manifest["releaseYearRevision"]["sourcePdfSha256"] == audit["sourcePdfSha256"], "Release-year source PDF is stale")
    require(metadata["releaseYearRevision"] == manifest["releaseYearRevision"], "Release-year metadata differs")
    require(all(item.get("releaseYear") == item["year"] for item in shard_records), "Exported releaseYear differs from canonical year")
    require("| Article | Release Year | Venue |" in readme, "README release-year heading is missing")
    require("<strong>49</strong>" not in index, "The old cumulative count remains")

'''
        if check not in text:
            assert anchor in text
            text = text.replace(anchor, check + anchor, 1)
    path.write_text(text)

core_path = ASSETS / 'app-v3-core.js'
core = core_path.read_text()
assert 'WEBSITE_DOMAIN_OVERRIDES' in core, 'Do not overwrite the recent maintainer-requested domain grouping.'
for a, b in (
    ('    year,\n    domains:', '    year,\n    releaseYear: year,\n    domains:'),
    ('    item.venue,\n', '    item.venue,\n    String(item.year),\n    String(item.publicationYear || ""),\n'),
    ('const venue = item.venue || "Publication";', 'const venue = (item.venue || "Publication") + (item.publicationYear ? ` ${item.publicationYear}` : "");'),
    ('<span class="card-year">${item.year} · ${escapeHtml(venue)}</span>', '<span class="card-year">Release Year: ${item.year} · ${escapeHtml(venue)}</span>'),
    ('world-model-benchmarks-2026-08-31.json', 'world-model-benchmarks-2026-09-07-release-years.json'),
):
    core = replace(core, a, b)
core_path.write_text(core)
# Keep the existing verified reference strings except the stale WorldLens arXiv-2026 entry.
for i in range(1, 5):
    path = ASSETS / f'benchmarks-{i}.json'
    shard = json.loads(path.read_text())
    for item in shard:
        if item['shortName'] == 'WorldLens':
            item['reference'] = 'A. Liang, L. Kong, T. Yan, H. Liu, Y. Yang, Z. Huang, W. Yin, J. Zuo, Y. Hu, D. Zhu et al., “WorldLens: Full-spectrum evaluations of driving world models in real world,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2026, pp. 36385–36399.'
    path.write_text(json.dumps(shard, ensure_ascii=False, indent=2) + '\n')

index_path = ROOT / 'docs/index.html'
index = index_path.read_text()
anchor = '<span>Unique benchmark totals by release window</span>'
new = '<span title="Release years follow Figure 2 and Tables 3–9 of the September 7, 2026 manuscript, not formal publication years.">Unique benchmark totals by release window</span>'
index = replace(index, anchor, new)
index_path.write_text(index)
subprocess.run(['python', str(ROOT / 'scripts/generate_readme_index.py')], check=True)
subprocess.run(['python', str(ROOT / 'scripts/sync_latest_survey.py')], check=True)
subprocess.run(['node', '--check', str(core_path)], check=True)
subprocess.run(['node', '--check', str(ASSETS / 'app-v3.js')], check=True)
subprocess.run(['node', str(ROOT / 'scripts/test_website_domains.cjs')], check=True)
print('PASS: all 102 release years match the newest PDF; exactly five year changes; taxonomy and domain grouping preserved.')
