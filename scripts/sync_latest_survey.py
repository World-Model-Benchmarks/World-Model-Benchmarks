#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'docs/assets/benchmarks.json').read_text(encoding='utf-8'))
meta=json.loads((ROOT/'docs/assets/metadata.json').read_text(encoding='utf-8'))
readme=(ROOT/'Readme.md').read_text(encoding='utf-8')
assert m['total']==95 and m['crossCategory']==58 and len(m['records'])==95
assert m['schemaVersion']==6
assert sum(len(r[6].split('+'))>1 for r in m['records'].values())==58
assert Counter(r[1] for r in m['records'].values())==Counter({2018:1,2019:1,2020:3,2021:2,2022:3,2023:3,2024:9,2025:31,2026:42})
assert Counter(c for r in m['records'].values() for c in r[6].split('+') if c)==Counter({'T1':24,'T2':31,'T3':19,'T4':53,'T5':32,'T6':40,'T7':13})
for n in ['WorldRoamBench','CrashTwin','MemoBench','RoboTrustBench','ContactWorld','ScratchWorld','MiraBench','Chess-World-Model','Apple-π','KineBench','ReactSim-Bench','WMBench']:
    assert n in m['records'] and n in m['added']
for n in ['FETV','VBench','VBench++','EvalCrafter','T2V-CompBench']:
    assert n not in m['records'] and n in m['removed']
assert meta['total']==95 and meta['crossCategory']==58
assert '**95 representative benchmarks**' in readme and '**58** span' in readme
assert '| Spatial & State Consistency | 31 |' in readme
assert '| Functional Utility | 13 |' in readme
print('Validated 95 benchmarks, 58 cross-category assignments, and the July 30, 2026 snapshot.')
