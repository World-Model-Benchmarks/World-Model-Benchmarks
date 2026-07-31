#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
manifest_path = ASSETS / "benchmarks.json"
metadata_path = ASSETS / "metadata.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest.update(version="July 30, 2026 manuscript snapshot", schemaVersion=6, total=95, crossCategory=58)

remove = {"FETV", "VBench", "VBench++", "EvalCrafter", "T2V-CompBench"}
manifest["removed"] = sorted(set(manifest.get("removed", [])) | remove)
for name in remove:
    manifest["records"].pop(name, None)

papers = {
"WorldRoamBench":("WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models","2606.31672"),
"CrashTwin":("A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models","2606.28757"),
"MemoBench":("MemoBench: Benchmarking World Modeling in Dynamically Changing Environments","2606.27537"),
"RoboTrustBench":("RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation","2606.01600"),
"ContactWorld":("ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation","2606.13877"),
"ScratchWorld":("ScratchWorld: Evaluating if World Models Compute Executable Consequences","2606.31689"),
"MiraBench":("MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models","2605.29360"),
"Chess-World-Model":("Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences","2605.30100"),
"Apple-π":("Apple-π: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence","2607.16401"),
"KineBench":("KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding","2607.19876"),
"ReactSim-Bench":("ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving","2606.14058"),
"WMBench":("GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation (introduces WMBench)","2607.02642"),
}
for name, (title, arxiv_id) in papers.items():
    manifest.setdefault("added", {})[name] = {
        "id": name.lower().replace("π", "pi").replace(" ", "-").replace("_", "-").replace("--", "-"),
        "shortName": name,
        "title": title,
        "venue": "arXiv",
        "paperUrl": f"https://arxiv.org/abs/{arxiv_id}",
        "arxivId": arxiv_id,
        "reference": f"{title}, arXiv:{arxiv_id}, 2026.",
    }

manifest["records"].update({
"WorldRoamBench":[80,2026,"video+game","OL","P","HCP","T1+T2+T3+T4+T6","S1+S2+S6"],
"CrashTwin":[85,2026,"driving+video","OL","P","HCP","T1+T2+T4","S2"],
"MemoBench":[81,2026,"video","OL","P","HCP","T1+T2+T3+T4+T6","S1+S2+S5"],
"RoboTrustBench":[82,2026,"embodied","OL","P","HCP","T1+T2+T4+T5+T6","S1+S2+S4+S5"],
"ContactWorld":[95,2026,"embodied","CL","P+O","HCP","T2+T3+T4+T7","S9"],
"ScratchWorld":[96,2026,"game","OL","P","HCP","T2+T3+T5+T6","S3+S4+S5"],
"MiraBench":[97,2026,"embodied","OL","P","HCP","T2+T4+T5+T6","S4+S5"],
"Chess-World-Model":[98,2026,"game","OL","P","HCP","T2+T3+T6","S5"],
"Apple-π":[130,2026,"video","OL","P","HCP","T4+T5","S3"],
"KineBench":[131,2026,"embodied","CL","P+O","HCP","T4+T6+T7","S5+S9"],
"ReactSim-Bench":[132,2026,"driving","CL","P","HCP","T4+T5+T6","S4+S6"],
"WMBench":[148,2026,"embodied","CL","P+O","HCP","T7","S8"],
})

ordered = [
(35,"RoboWM-Bench"),(38,"World-in-World"),(39,"IntPhys"),(40,"CLEVRER"),(41,"Physion"),(42,"MIND"),(43,"WorldOlympiad"),(44,"WorldArena"),(45,"WorldArena 2.0"),
(64,"ChronoMagic-Bench"),(65,"WorldScore"),(66,"VMBench"),(67,"EWMBench"),(68,"GameWorld Score"),(69,"WorldMark"),(70,"4DWorldBench"),(71,"WorldLens"),(72,"DrivingGen"),(73,"PEDRA"),(74,"Gen-ViRe"),(75,"iWorld-Bench"),(76,"WoW-World-Eval"),(77,"RBench"),(78,"PAI-Bench"),(79,"EZS-Bench"),(80,"WorldRoamBench"),(81,"MemoBench"),(82,"RoboTrustBench"),(83,"TC-Bench"),(84,"WBench"),(85,"CrashTwin"),(86,"PDI-Bench"),(87,"LoopNav"),(88,"MBench"),(89,"STEVO-Bench"),(90,"CausalSpatial"),(91,"What-If World"),(92,"HOCA-Bench"),(93,"AutumnBench"),(94,"MVP"),(95,"ContactWorld"),(96,"ScratchWorld"),(97,"MiraBench"),(98,"Chess-World-Model"),(99,"WorldPrediction"),(100,"SmallWorlds"),(101,"WR-Arena"),(102,"HTEWorld"),(103,"IntPhys 2"),(104,"CoPhy"),(105,"PHYRE"),(106,"CRAFT"),(107,"Physion++"),(108,"ComPhy"),(109,"ContPhy"),(110,"PhyCoBench"),(111,"VideoPhy"),(112,"VideoPhy-2"),(113,"PhyGenBench"),(114,"T2VPhysBench"),(115,"Physics-IQ"),(116,"WorldBench"),(117,"PhyWorldBench"),(118,"T2VWorldBench"),(119,"WorldModelBench"),(120,"VBench-2.0"),(121,"RigidBench"),(122,"Morpheus"),(123,"DreamGen Bench"),(124,"PhyGround"),(125,"Physion-Eval"),(126,"CRONOS"),(127,"VACT"),(128,"PhysicsMind"),(129,"ACWM-Phys"),(130,"Apple-π"),(131,"KineBench"),(132,"ReactSim-Bench"),(133,"CATER"),(134,"NExT-QA"),(135,"Causal-VidQA"),(136,"IntentQA"),(137,"MMWorld"),(138,"CausalVQA"),(139,"VCRBench"),(140,"ACQUIRED"),(141,"StoryEval"),(142,"OSCBench"),(143,"MoveBench"),(144,"MagicBench"),(145,"ACT-Bench"),(146,"Omni-WorldBench"),(147,"WorldSimBench"),(148,"WMBench"),(149,"EVA-Bench")]
refs = {name: ref for ref, name in ordered}
assert set(refs) == set(manifest["records"]), (set(refs)-set(manifest["records"]), set(manifest["records"])-set(refs))
for name, ref in refs.items():
    manifest["records"][name][0] = ref

assert len(manifest["records"]) == 95
assert sum(len(row[6].split("+")) > 1 for row in manifest["records"].values()) == 58
assert Counter(row[1] for row in manifest["records"].values()) == Counter({2018:1,2019:1,2020:3,2021:2,2022:3,2023:3,2024:9,2025:31,2026:42})
counts = Counter(code for row in manifest["records"].values() for code in row[6].split("+") if code)
assert counts == Counter({"T1":24,"T2":31,"T3":19,"T4":53,"T5":32,"T6":40,"T7":13}), counts
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
metadata.update(version=manifest["version"], total=95, crossCategory=58)
metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Updated canonical corpus to 95 benchmarks and 58 cross-category benchmarks.")
