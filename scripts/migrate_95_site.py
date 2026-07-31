#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"

# Update website copy, links, counts, and cache keys.
index_path = ROOT / "docs" / "index.html"
index = index_path.read_text(encoding="utf-8")
for old, new in {
    "https://axbhb.github.io/world-model-evaluation-survey/": "https://world-model-benchmarks.github.io/",
    "https://github.com/axbhb/world-model-evaluation-survey": "https://github.com/World-Model-Benchmarks/World-Model-Benchmarks",
    "Explore 88 world-model benchmarks": "Explore 95 world-model benchmarks",
    "Latest manuscript snapshot · 88 benchmarks · 49 cross-category · checked July 2026": "Latest manuscript snapshot · 95 benchmarks · 58 cross-category · checked July 30, 2026",
    '<strong id="stat-total">88</strong>': '<strong id="stat-total">95</strong>',
    '<strong id="stat-cross">49</strong>': '<strong id="stat-cross">58</strong>',
    "Search and filter the 88 representative benchmarks": "Search and filter the 95 representative benchmarks",
    '<strong id="result-count">88</strong>': '<strong id="result-count">95</strong>',
    'src="assets/app-v3.js?v=6"': 'src="assets/app-v3.js?v=7"',
}.items():
    index = index.replace(old, new)
index = index.replace(
    "Early benchmarks mainly focus on visual &amp; temporal quality, physical plausibility, and causal reasoning.",
    "Early benchmarks mainly focus on physical plausibility and causal reasoning."
)
index = re.sub(r"<p><strong>14/14 pre-2024 benchmarks</strong>.*?</p>",
               "<p><strong>13 cumulative benchmarks by 2023</strong>, concentrated in physical and causal evaluation.</p>", index)
index = re.sub(r"<p>First appearing in 2024:.*?</p>",
               "<p><strong>9 new benchmarks in 2024</strong>, including broader control and functional-utility evaluation.</p>", index)
index = re.sub(r"<p><strong>32 new in 2025.*?</p>",
               "<p><strong>31 new benchmarks in 2025</strong>, raising the cumulative corpus to <strong>53</strong>.</p>", index)
index = re.sub(r"<p>2026 contributes <strong>11/14 long-horizon</strong>.*?</p>",
               "<p><strong>42 new benchmarks in 2026</strong>, bringing the corpus to <strong>95</strong>.</p>", index)
index_path.write_text(index, encoding="utf-8")

app_path = ASSETS / "app-v3.js"
app = app_path.read_text(encoding="utf-8")
app = app.replace('setTextIfChanged(stats[0].querySelector("strong"), "88");', 'setTextIfChanged(stats[0].querySelector("strong"), "95");')
app = app.replace('setTextIfChanged(stats[1].querySelector("strong"), "49");', 'setTextIfChanged(stats[1].querySelector("strong"), "58");')
app = app.replace("Latest manuscript snapshot · 88 benchmarks · 49 cross-category · checked July 2026", "Latest manuscript snapshot · 95 benchmarks · 58 cross-category · checked July 30, 2026")
app = re.sub(r"'<strong>32 new in 2025.*?;", "'<strong>31 new benchmarks in 2025</strong>, raising the cumulative corpus to <strong>53</strong>.;", app)
app = app.replace("2026 contributes <strong>11/14 long-horizon</strong> and <strong>6/10 utility</strong> benchmarks.", "<strong>42 new benchmarks in 2026</strong>, bringing the corpus to <strong>95</strong>.")
app = app.replace("Search and filter the 88 representative benchmarks", "Search and filter the 95 representative benchmarks")
app = app.replace('if (resultCount && resultCount.textContent === "82") resultCount.textContent = "88";', 'if (resultCount && resultCount.textContent !== "95") resultCount.textContent = "95";')
app = app.replace('app-v3-core.js?v=8', 'app-v3-core.js?v=9')
app_path.write_text(app, encoding="utf-8")

social_path = ASSETS / "social-preview.svg"
social = social_path.read_text(encoding="utf-8").replace('>88</text>', '>95</text>')
social_path.write_text(social, encoding="utf-8")

# Align the README generator with Figure 4 of the 95-benchmark paper.
gen_path = ROOT / "scripts" / "generate_readme_index.py"
gen = gen_path.read_text(encoding="utf-8")
lists = {
"T1": ['ChronoMagic-Bench','WorldScore','VMBench','EWMBench','WorldArena','GameWorld Score','WorldMark','4DWorldBench','TC-Bench','WorldLens','WorldArena 2.0','DrivingGen','WBench','PEDRA','Gen-ViRe','iWorld-Bench','WoW-World-Eval','RBench','PAI-Bench','EZS-Bench','WorldRoamBench','CrashTwin','MemoBench','RoboTrustBench'],
"T2": ['WorldMark','GameWorld Score','EWMBench','WorldArena','WorldLens','DrivingGen','WorldScore','4DWorldBench','PDI-Bench','LoopNav','MIND','MBench','STEVO-Bench','CausalSpatial','What-If World','WorldOlympiad','HOCA-Bench','WoW-World-Eval','RBench','AutumnBench','MVP','PAI-Bench','EZS-Bench','ContactWorld','WorldRoamBench','ScratchWorld','CrashTwin','MemoBench','RoboTrustBench','MiraBench','Chess-World-Model'],
"T3": ['WorldPrediction','SmallWorlds','WR-Arena','WorldMark','MBench','MIND','WBench','WorldOlympiad','HTEWorld','RoboWM-Bench','iWorld-Bench','WoW-World-Eval','RBench','AutumnBench','ContactWorld','WorldRoamBench','ScratchWorld','MemoBench','Chess-World-Model'],
"T4": ['IntPhys','IntPhys 2','CLEVRER','CoPhy','PHYRE','CRAFT','Physion','Physion++','ComPhy','ContPhy','PhyCoBench','VideoPhy','VideoPhy-2','PhyGenBench','T2VPhysBench','Physics-IQ','WorldBench','PhyWorldBench','T2VWorldBench','WorldModelBench','VBench-2.0','4DWorldBench','GameWorld Score','RigidBench','Morpheus','What-If World','RoboWM-Bench','DreamGen Bench','WorldLens','PhyGround','Physion-Eval','CRONOS','VACT','STEVO-Bench','PhysicsMind','PDI-Bench','HOCA-Bench','WorldOlympiad','ACWM-Phys','WoW-World-Eval','RBench','MVP','PAI-Bench','EZS-Bench','Apple-π','ContactWorld','KineBench','WorldRoamBench','CrashTwin','MemoBench','RoboTrustBench','MiraBench','ReactSim-Bench'],
"S3": ['CLEVRER','CATER','NExT-QA','Causal-VidQA','CRAFT','IntentQA','CoPhy','MMWorld','CausalVQA','VCRBench','Physion','Physics-IQ','WorldPrediction','WR-Arena','CausalSpatial','T2VWorldBench','VACT','HOCA-Bench','WoW-World-Eval','RBench','PAI-Bench','Apple-π','ScratchWorld'],
"S4": ['CLEVRER','CRAFT','CoPhy','ComPhy','ACQUIRED','Causal-VidQA','MMWorld','CausalVQA','What-If World','WR-Arena','CRONOS','AutumnBench','MVP','ScratchWorld','RoboTrustBench','MiraBench','ReactSim-Bench'],
"S5": ['TC-Bench','StoryEval','VideoPhy','VideoPhy-2','PhyGenBench','PhyWorldBench','OSCBench','MoveBench','MagicBench','WorldScore','4DWorldBench','DrivingGen','ACT-Bench','What-If World','Omni-WorldBench','DreamGen Bench','WorldModelBench','VBench-2.0','WoW-World-Eval','RBench','PAI-Bench','EZS-Bench','KineBench','ScratchWorld','MemoBench','RoboTrustBench','MiraBench','Chess-World-Model'],
"S6": ['WorldMark','WR-Arena','WorldSimBench','WBench','iWorld-Bench','MIND','ACWM-Phys','RoboWM-Bench','WorldArena 2.0','WorldOlympiad','WorldRoamBench','ReactSim-Bench'],
"S7": ['WorldArena','WorldArena 2.0'],
"S8": ['WorldArena','WMBench'],
"S9": ['WorldArena','WorldArena 2.0','World-in-World','EVA-Bench','WorldLens','RoboWM-Bench','WorldSimBench','WR-Arena','WoW-World-Eval','AutumnBench','ContactWorld','KineBench'],
"S10": ['WorldArena 2.0'],
}
for name, values in lists.items():
    gen = re.sub(rf"^{name}=.*$", f"{name}={values!r}", gen, flags=re.MULTILINE)
gen = gen.replace('assert len(meta) == manifest["total"] == 88', 'assert len(meta) == manifest["total"] == 95')
gen = gen.replace('latest 88-benchmark manuscript', 'latest 95-benchmark manuscript')
gen = gen.replace('==88', '==95').replace('==49', '==58')
gen = gen.replace('https://axbhb.github.io/world-model-evaluation-survey/', 'https://world-model-benchmarks.github.io/')
gen = gen.replace('Benchmarks-88-2f8f63', 'Benchmarks-95-2f8f63')
gen = gen.replace('**88 representative benchmarks**', '**95 representative benchmarks**')
gen = gen.replace('**49** span', '**58** span')
for old, new in {
'| Visual & Temporal Quality | 24 |':'| Visual & Temporal Quality | 24 |',
'| Spatial & State Consistency | 25 |':'| Spatial & State Consistency | 31 |',
'| Long-Horizon Memory & State Persistence | 14 |':'| Long-Horizon Memory & State Persistence | 19 |',
'| Physical Plausibility | 44 |':'| Physical Plausibility | 53 |',
'| Causal & Counterfactual Reasoning | 27 |':'| Causal & Counterfactual Reasoning | 32 |',
'| Control Fidelity & Interactive Dynamics | 33 |':'| Control Fidelity & Interactive Dynamics | 40 |',
'| Functional Utility | 10 |':'| Functional Utility | 13 |',
}.items(): gen = gen.replace(old, new)
gen = gen.replace('The corpus was last checked in July 2026.', 'The corpus was last checked on July 30, 2026.')
gen_path.write_text(gen, encoding="utf-8")

validator = '''#!/usr/bin/env python3
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
'''
(ROOT / "scripts" / "sync_latest_survey.py").write_text(validator, encoding="utf-8")

subprocess.run([sys.executable, str(gen_path)], check=True)
print("Updated website copy, README generator, README, and validation rules.")
