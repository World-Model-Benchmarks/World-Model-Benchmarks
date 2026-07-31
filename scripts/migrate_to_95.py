#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
MANIFEST_PATH = ASSETS / "benchmarks.json"
METADATA_PATH = ASSETS / "metadata.json"
INDEX_PATH = ROOT / "docs" / "index.html"
APP_PATH = ASSETS / "app-v3.js"
SOCIAL_PATH = ASSETS / "social-preview.svg"
GENERATOR_PATH = ROOT / "scripts" / "generate_readme_index.py"
VALIDATOR_PATH = ROOT / "scripts" / "sync_latest_survey.py"

manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
manifest.update({
    "version": "July 30, 2026 manuscript snapshot",
    "schemaVersion": 6,
    "total": 95,
    "crossCategory": 58,
})

removed = set(manifest.get("removed", []))
removed.update({"FETV", "VBench", "VBench++", "EvalCrafter", "T2V-CompBench"})
manifest["removed"] = sorted(removed)
for name in ["FETV", "VBench", "VBench++", "EvalCrafter", "T2V-CompBench"]:
    manifest["records"].pop(name, None)

new_meta = {
    "WorldRoamBench": {
        "id": "worldroambench", "shortName": "WorldRoamBench",
        "title": "WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2606.31672", "arxivId": "2606.31672",
        "reference": "T.-B. Xu et al., WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models, 2026."
    },
    "CrashTwin": {
        "id": "crashtwin", "shortName": "CrashTwin",
        "title": "A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2606.28757", "arxivId": "2606.28757",
        "reference": "N. Chen et al., A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models, 2026."
    },
    "MemoBench": {
        "id": "memobench", "shortName": "MemoBench",
        "title": "MemoBench: Benchmarking World Modeling in Dynamically Changing Environments",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2606.27537", "arxivId": "2606.27537",
        "reference": "H. Chen et al., MemoBench: Benchmarking World Modeling in Dynamically Changing Environments, 2026."
    },
    "RoboTrustBench": {
        "id": "robotrustbench", "shortName": "RoboTrustBench",
        "title": "RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2606.01600", "arxivId": "2606.01600",
        "reference": "H. Li et al., RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation, 2026."
    },
    "ContactWorld": {
        "id": "contactworld", "shortName": "ContactWorld",
        "title": "ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2606.13877", "arxivId": "2606.13877",
        "reference": "Z. Zhang et al., ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation, 2026."
    },
    "ScratchWorld": {
        "id": "scratchworld", "shortName": "ScratchWorld",
        "title": "ScratchWorld: Evaluating if World Models Compute Executable Consequences",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2606.31689", "arxivId": "2606.31689",
        "reference": "Y. Lin and J. Zhang, ScratchWorld: Evaluating if World Models Compute Executable Consequences, 2026."
    },
    "MiraBench": {
        "id": "mirabench", "shortName": "MiraBench",
        "title": "MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2605.29360", "arxivId": "2605.29360",
        "reference": "T. Yang et al., MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models, 2026."
    },
    "Chess-World-Model": {
        "id": "chess-world-model", "shortName": "Chess-World-Model",
        "title": "Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2605.30100", "arxivId": "2605.30100",
        "reference": "B. Walker and T. Lyons, Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences, 2026."
    },
    "Apple-π": {
        "id": "apple-pi", "shortName": "Apple-π",
        "title": "Apple-π: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2607.16401", "arxivId": "2607.16401",
        "reference": "R. Yao et al., Apple-π: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence, 2026."
    },
    "KineBench": {
        "id": "kinebench", "shortName": "KineBench",
        "title": "KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2607.19876", "arxivId": "2607.19876",
        "reference": "Z. Liu et al., KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding, 2026."
    },
    "ReactSim-Bench": {
        "id": "reactsim-bench", "shortName": "ReactSim-Bench",
        "title": "ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2606.14058", "arxivId": "2606.14058",
        "reference": "Z. Zhang et al., ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving, 2026."
    },
    "WMBench": {
        "id": "wmbench-policy-evaluation", "shortName": "WMBench",
        "title": "GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation (introduces WMBench)",
        "venue": "arXiv", "paperUrl": "https://arxiv.org/abs/2607.02642", "arxivId": "2607.02642",
        "reference": "GigaWorld Team et al., GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation, 2026."
    },
}
manifest.setdefault("added", {}).update(new_meta)

new_records = {
    "WorldRoamBench": [80, 2026, "video+game", "OL", "P", "HCP", "T1+T2+T3+T4+T6", "S1+S2+S6"],
    "CrashTwin": [85, 2026, "driving+video", "OL", "P", "HCP", "T1+T2+T4", "S2"],
    "MemoBench": [81, 2026, "video", "OL", "P", "HCP", "T1+T2+T3+T4+T6", "S1+S2+S5"],
    "RoboTrustBench": [82, 2026, "embodied", "OL", "P", "HCP", "T1+T2+T4+T5+T6", "S1+S2+S4+S5"],
    "ContactWorld": [95, 2026, "embodied", "CL", "P+O", "HCP", "T2+T3+T4+T7", "S9"],
    "ScratchWorld": [96, 2026, "game", "OL", "P", "HCP", "T2+T3+T5+T6", "S3+S4+S5"],
    "MiraBench": [97, 2026, "embodied", "OL", "P", "HCP", "T2+T4+T5+T6", "S4+S5"],
    "Chess-World-Model": [98, 2026, "game", "OL", "P", "HCP", "T2+T3+T6", "S5"],
    "Apple-π": [130, 2026, "video", "OL", "P", "HCP", "T4+T5", "S3"],
    "KineBench": [131, 2026, "embodied", "CL", "P+O", "HCP", "T4+T6+T7", "S5+S9"],
    "ReactSim-Bench": [132, 2026, "driving", "CL", "P", "HCP", "T4+T5+T6", "S4+S6"],
    "WMBench": [148, 2026, "embodied", "CL", "P+O", "HCP", "T7", "S8"],
}
manifest["records"].update(new_records)

ref_order = [
    (35,"RoboWM-Bench"),(38,"World-in-World"),(39,"IntPhys"),(40,"CLEVRER"),(41,"Physion"),(42,"MIND"),(43,"WorldOlympiad"),(44,"WorldArena"),(45,"WorldArena 2.0"),
    (64,"ChronoMagic-Bench"),(65,"WorldScore"),(66,"VMBench"),(67,"EWMBench"),(68,"GameWorld Score"),(69,"WorldMark"),(70,"4DWorldBench"),(71,"WorldLens"),(72,"DrivingGen"),(73,"PEDRA"),(74,"Gen-ViRe"),(75,"iWorld-Bench"),(76,"WoW-World-Eval"),(77,"RBench"),(78,"PAI-Bench"),(79,"EZS-Bench"),(80,"WorldRoamBench"),(81,"MemoBench"),(82,"RoboTrustBench"),(83,"TC-Bench"),(84,"WBench"),(85,"CrashTwin"),(86,"PDI-Bench"),(87,"LoopNav"),(88,"MBench"),(89,"STEVO-Bench"),(90,"CausalSpatial"),(91,"What-If World"),(92,"HOCA-Bench"),(93,"AutumnBench"),(94,"MVP"),(95,"ContactWorld"),(96,"ScratchWorld"),(97,"MiraBench"),(98,"Chess-World-Model"),(99,"WorldPrediction"),(100,"SmallWorlds"),(101,"WR-Arena"),(102,"HTEWorld"),(103,"IntPhys 2"),(104,"CoPhy"),(105,"PHYRE"),(106,"CRAFT"),(107,"Physion++"),(108,"ComPhy"),(109,"ContPhy"),(110,"PhyCoBench"),(111,"VideoPhy"),(112,"VideoPhy-2"),(113,"PhyGenBench"),(114,"T2VPhysBench"),(115,"Physics-IQ"),(116,"WorldBench"),(117,"PhyWorldBench"),(118,"T2VWorldBench"),(119,"WorldModelBench"),(120,"VBench-2.0"),(121,"RigidBench"),(122,"Morpheus"),(123,"DreamGen Bench"),(124,"PhyGround"),(125,"Physion-Eval"),(126,"CRONOS"),(127,"VACT"),(128,"PhysicsMind"),(129,"ACWM-Phys"),(130,"Apple-π"),(131,"KineBench"),(132,"ReactSim-Bench"),(133,"CATER"),(134,"NExT-QA"),(135,"Causal-VidQA"),(136,"IntentQA"),(137,"MMWorld"),(138,"CausalVQA"),(139,"VCRBench"),(140,"ACQUIRED"),(141,"StoryEval"),(142,"OSCBench"),(143,"MoveBench"),(144,"MagicBench"),(145,"ACT-Bench"),(146,"Omni-WorldBench"),(147,"WorldSimBench"),(148,"WMBench"),(149,"EVA-Bench"),
]
ref_map = {name: ref for ref, name in ref_order}
assert set(ref_map) == set(manifest["records"]), (set(ref_map)-set(manifest["records"]), set(manifest["records"])-set(ref_map))
for name, ref in ref_map.items():
    manifest["records"][name][0] = ref

# Canonical validation against the latest paper.
assert len(manifest["records"]) == 95
assert sum(len(str(row[6]).split("+")) > 1 for row in manifest["records"].values()) == 58
assert Counter(row[1] for row in manifest["records"].values()) == Counter({2018:1,2019:1,2020:3,2021:2,2022:3,2023:3,2024:9,2025:31,2026:42})
target_counts = Counter(code for row in manifest["records"].values() for code in str(row[6]).split("+") if code)
assert target_counts == Counter({"T1":24,"T2":31,"T3":19,"T4":53,"T5":32,"T6":40,"T7":13}), target_counts
MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
metadata.update({"version": manifest["version"], "total": 95, "crossCategory": 58})
METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Static page copy and canonical links.
index = INDEX_PATH.read_text(encoding="utf-8")n