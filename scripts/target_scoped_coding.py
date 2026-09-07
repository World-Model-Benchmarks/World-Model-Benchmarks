"""Target/role-scoped protocol and metric coding transcribed from Tables 3-9."""
from __future__ import annotations
from collections import Counter
import hashlib
import html
import json

SCOPES = {**{f"T{i}": {"target": f"T{i}", "table": i+2, "page": p} for i,p in enumerate([11,12,14,15,18],1)},
          "S5": {"target":"T6","table":8,"page":20}, "S6": {"target":"T6","table":8,"page":20},
          **{f"S{i}": {"target":"T7","table":9,"page":23} for i in range(7,11)}}
EXPECTED_TRACK_FINGERPRINT = "8c8538ee487b515fcc25c54f2002736735c443db1fe1a5a133bcf5496b290077"
EXPECTED_TABLE10 = {
    "T6": {"n":55,"olOnly":50,"includesCL":5,"pOnly":51,"includesO":4},
    "S5": {"n":40,"olOnly":39,"includesCL":1,"pOnly":38,"includesO":2},
    "S6": {"n":15,"olOnly":11,"includesCL":4,"pOnly":13,"includesO":2},
    "T7": {"n":13,"olOnly":3,"includesCL":10,"pOnly":0,"includesO":13},
}

def scope_label(manifest, scope):
    return manifest['targetLabels'].get(scope) or manifest['subtargetLabels'][scope]

def track_fingerprint(manifest):
    rows=[]
    for scope, records in sorted(manifest['categoryRecords'].items()):
        for name, (protocol,metrics) in sorted(records.items()):
            r=manifest['records'][name]
            rows.append('|'.join(map(str,[scope,name,r[0],r[1],r[2],protocol,metrics,r[5]])))
    return hashlib.sha256('\n'.join(rows).encode()).hexdigest()

def evaluation_tracks(manifest, name):
    return [dict(scope=scope,target=manifest['targetLabels'][info['target']],label=scope_label(manifest,scope),
                 table=info['table'],sourcePage=info['page'],protocols=codes[0].split('+'),metrics=codes[1].split('+'))
            for scope,info in SCOPES.items() if (codes:=manifest['categoryRecords'][scope].get(name))]

def coverage(manifest, scopes):
    grouped={}
    for scope in scopes:
        for name,(p,m) in manifest['categoryRecords'][scope].items():
            a=grouped.setdefault(name,[set(),set()]);a[0].update(p.split('+'));a[1].update(m.split('+'))
    return {'n':len(grouped),'olOnly':sum('CL' not in p for p,m in grouped.values()),
            'includesCL':sum('CL' in p for p,m in grouped.values()),
            'pOnly':sum('O' not in m for p,m in grouped.values()),'includesO':sum('O' in m for p,m in grouped.values())}

def scoped_metadata(manifest):
    target_coverage={t:coverage(manifest,[s for s,v in SCOPES.items() if v['target']==t]) for t in manifest['targetLabels']}
    return {'categoryRecords':manifest['categoryRecords'],'categoryScopeLabels':{s:scope_label(manifest,s) for s in SCOPES},
            'codingScope':manifest['codingScope'],'codingRevision':manifest['codingRevision'],
            'evaluationTrackFingerprint':track_fingerprint(manifest),'targetCoverage':target_coverage,
            'subtargetCoverage':{s:coverage(manifest,[s]) for s in SCOPES if s.startswith('S')},
            'table10':{s:(target_coverage[s] if s.startswith('T') else coverage(manifest,[s])) for s in EXPECTED_TABLE10}}

def validate_scoped(manifest):
    assert set(manifest['categoryRecords'])==set(SCOPES)
    assert sum(len(x) for x in manifest['categoryRecords'].values())==307
    for scope,info in SCOPES.items():
        expected={n for n,r in manifest['records'].items() if scope in r[6 if scope.startswith('T') else 7].split('+')}
        assert set(manifest['categoryRecords'][scope])==expected,scope
        for name,(p,m) in manifest['categoryRecords'][scope].items():
            assert p in ('OL','CL','OL+CL') and m in ('P','O','P+O'),(scope,name,p,m)
    for name,r in manifest['records'].items():
        tracks=evaluation_tracks(manifest,name)
        assert tracks,name
        for idx,field,order in [(3,'protocols',['OL','CL']),(4,'metrics',['P','O'])]:
            union='+'.join(x for x in order if any(x in t[field] for t in tracks))
            assert r[idx]==union,(name,field,r[idx],union)
    assert track_fingerprint(manifest)==EXPECTED_TRACK_FINGERPRINT,'PDF track fingerprint mismatch'
    assert manifest['evaluationTrackFingerprint']==EXPECTED_TRACK_FINGERPRINT
    assert scoped_metadata(manifest)['table10']==EXPECTED_TABLE10,'Table 10 mismatch'

def readme_coding(manifest,name,section):
    scope={'S1':'T1','S2':'T1','S3':'T5','S4':'T5'}.get(section,section)
    return manifest['categoryRecords'][scope][name]

def coverage_html(manifest):
    rows=[]
    for scope,row in scoped_metadata(manifest)['table10'].items():
        cells=''.join(f'<td>{row[k]} ({100*row[k]/row["n"]:.1f}%)</td>' for k in ('olOnly','includesCL','pOnly','includesO'))
        rows.append(f'<tr><th scope="row">{html.escape(scope_label(manifest,scope))}</th><td>{row["n"]}</td>{cells}</tr>')
    return ('<div class="matrix-shell" id="protocol-evidence-coverage"><div class="matrix-heading">'
            '<div><p class="eyebrow">Manuscript Table 10</p><h3>Target-specific protocol and evidence coverage</h3></div></div>'
            '<p>Each benchmark is counted once per row, using only tracks relevant to that target or role. '
            'Includes CL/O also counts OL+CL/P+O. Protocol and evidence columns are separate marginal counts.</p>'
            '<div class="matrix-scroll"><table class="coverage-table"><thead><tr><th>Evaluation target</th><th>n</th>'
            '<th>OL only</th><th>Includes CL</th><th>P only</th><th>Includes O</th></tr></thead><tbody>'
            +''.join(rows)+'</tbody></table></div></div>')
