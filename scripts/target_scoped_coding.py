"""Joint target/role evidence coding transcribed from Supplementary Tables S1-S7."""
from __future__ import annotations
from collections import Counter
import hashlib
import html
import json

SCOPES = {
    "T1": {"target": "T1", "table": "S1", "page": 4},
    "T2": {"target": "T2", "table": "S2", "page": 7},
    "T3": {"target": "T3", "table": "S3", "page": 11},
    "T4": {"target": "T4", "table": "S4", "page": 13},
    "T5": {"target": "T5", "table": "S5", "page": 18},
    "S5": {"target": "T6", "table": "S6", "page": 20},
    "S6": {"target": "T6", "table": "S6", "page": 20},
    **{f"S{i}": {"target": "T7", "table": "S7", "page": 24} for i in range(7, 11)},
}
EXPECTED_TRACK_FINGERPRINT = "57506b97cd7eb30d66632bb51fef231635ad01661311b674294139332d4b9808"
EXPECTED_EVALUATION_RECORD_FINGERPRINT = "1a1b225a2d62e0d70637aef1e9c283b2a532b8f90e8152d62e864228ef7efc8e"
EXPECTED_TABLE4 = {
    "T6": {"n":55,"olOnly":51,"includesCL":4,"pOnly":51,"includesO":4},
    "S5": {"n":40,"olOnly":39,"includesCL":1,"pOnly":38,"includesO":2},
    "S6": {"n":15,"olOnly":12,"includesCL":3,"pOnly":13,"includesO":2},
    "T7": {"n":13,"olOnly":2,"includesCL":11,"pOnly":0,"includesO":13},
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
    by_scope = {}
    for record in manifest['evaluationRecords']:
        if record['benchmark'] == name:
            by_scope.setdefault(record['scope'], []).append(record)
    tracks = []
    for scope, info in SCOPES.items():
        combinations = by_scope.get(scope)
        if not combinations:
            continue
        codes = manifest['categoryRecords'][scope][name]
        data = []
        for value in ('RWD', 'SBG', 'SPTC', 'HCP'):
            if any(record['data'] == value for record in combinations):
                data.append(value)
        tracks.append(dict(
            scope=scope,
            target=manifest['targetLabels'][info['target']],
            label=scope_label(manifest, scope),
            table=info['table'],
            sourcePage=info['page'],
            sourcePages=sorted({page for record in combinations for page in record['sourcePages']}),
            protocols=codes[0].split('+'),
            metrics=codes[1].split('+'),
            evaluationData=data,
            hasUnresolvedData=any(record['dataStatus'] == 'unresolved' for record in combinations),
            combinations=[{
                'id': record['id'],
                'protocol': record['protocol'],
                'metric': record['metric'],
                'data': record['data'],
                'dataStatus': record['dataStatus'],
                'taskIds': record['taskIds'],
                'sourcePages': record['sourcePages'],
            } for record in combinations],
        ))
    return tracks

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
            'table4':{s:(target_coverage[s] if s.startswith('T') else coverage(manifest,[s])) for s in EXPECTED_TABLE4}}

def validate_scoped(manifest):
    assert set(manifest['categoryRecords'])==set(SCOPES)
    assert sum(len(x) for x in manifest['categoryRecords'].values())==307
    assert len(manifest['evaluationRecords'])==369
    assert len(manifest['taskRecords'])==403
    assert sum(not row['auxiliary'] for row in manifest['taskRecords'])==401
    assert all(row['data'] in ('RWD','SBG','SPTC','HCP') and row['dataStatus']=='classified'
               for row in manifest['taskRecords'] if not row['auxiliary'])
    for scope,info in SCOPES.items():
        expected={n for n,r in manifest['records'].items() if scope in r[6 if scope.startswith('T') else 7].split('+')}
        assert set(manifest['categoryRecords'][scope])==expected,scope
        for name,(p,m) in manifest['categoryRecords'][scope].items():
            assert p in ('OL','CL','OL+CL') and m in ('P','O','P+O'),(scope,name,p,m)
            combinations=[row for row in manifest['evaluationRecords'] if row['scope']==scope and row['benchmark']==name]
            assert combinations,(scope,name,'missing combinations')
            assert p=='+'.join(x for x in ('OL','CL') if any(row['protocol']==x for row in combinations))
            assert m=='+'.join(x for x in ('P','O') if any(row['metric']==x for row in combinations))
    for name,r in manifest['records'].items():
        tracks=evaluation_tracks(manifest,name)
        assert tracks,name
        for idx,field,order in [(3,'protocols',['OL','CL']),(4,'metrics',['P','O'])]:
            union='+'.join(x for x in order if any(x in t[field] for t in tracks))
            assert r[idx]==union,(name,field,r[idx],union)
    assert track_fingerprint(manifest)==EXPECTED_TRACK_FINGERPRINT,'PDF track fingerprint mismatch'
    assert manifest['evaluationTrackFingerprint']==EXPECTED_TRACK_FINGERPRINT
    assert manifest['evaluationRecordFingerprint']==EXPECTED_EVALUATION_RECORD_FINGERPRINT
    assert scoped_metadata(manifest)['table4']==EXPECTED_TABLE4,'Table 4 mismatch'

def readme_coding(manifest,name,section):
    scope={'S1':'T1','S2':'T1','S3':'T5','S4':'T5'}.get(section,section)
    return manifest['categoryRecords'][scope][name]

def coverage_html(manifest):
    rows=[]
    for scope,row in scoped_metadata(manifest)['table4'].items():
        cells=''.join(f'<td>{row[k]} ({100*row[k]/row["n"]:.1f}%)</td>' for k in ('olOnly','includesCL','pOnly','includesO'))
        rows.append(f'<tr><th scope="row">{html.escape(scope_label(manifest,scope))}</th><td>{row["n"]}</td>{cells}</tr>')
    return ('<div class="matrix-shell" id="protocol-evidence-coverage"><div class="matrix-heading">'
        '<div><p class="eyebrow">Manuscript Table 4</p><h3>Target-specific protocol and evidence coverage</h3></div></div>'
        '<p>Each benchmark is counted once per row, using only tracks relevant to that target or role. '
        'Includes CL and Includes O are separate marginal counts over records relevant to each target or role.</p>'
        '<div class="matrix-scroll"><table class="coverage-table"><thead><tr><th>Evaluation target</th><th>n</th>'
        '<th>OL only</th><th>Includes CL</th><th>P only</th><th>Includes O</th></tr></thead><tbody>'
        +''.join(rows)+'</tbody></table></div></div>')
