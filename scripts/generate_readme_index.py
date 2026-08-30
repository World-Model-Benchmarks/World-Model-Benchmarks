#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
MANIFEST_PATH = ASSETS / "benchmarks.json"
METADATA_PATH = ASSETS / "metadata.json"
README_PATH = ROOT / "Readme.md"

SNAPSHOT_VERSION = "August 27, 2026 manuscript snapshot"
SNAPSHOT_DATE = "August 27, 2026"
TOTAL = 106
CROSS_CATEGORY = 66

# Figure 4 and Tables 3 to 9 of the August 27, 2026 manuscript snapshot.
T1 = [
    "ChronoMagic-Bench", "WorldScore", "VMBench", "EWMBench", "WorldArena",
    "GameWorld Score", "WorldMark", "4DWorldBench", "TC-Bench", "WorldLens",
    "WorldArena 2.0", "DrivingGen", "WBench", "PEDRA", "Gen-ViRe",
    "iWorld-Bench", "WoW-World-Eval", "RBench", "PAI-Bench", "EZS-Bench",
    "WorldRoamBench", "CrashTwin", "MemoBench", "RoboTrustBench", "WorldExam",
    "SurgWMBench", "H2R-Bench", "PlayWorld", "XEWorld", "HarnessEval-W",
    "WorldEcho",
]
T2 = [
    "WorldMark", "WorldLens", "WorldArena", "WorldScore", "DrivingGen", "EWMBench",
    "What-If World", "4DWorldBench", "GameWorld Score", "LoopNav", "MIND", "MBench",
    "STEVO-Bench", "CausalSpatial", "PDI-Bench", "WorldOlympiad", "HOCA-Bench",
    "WoW-World-Eval", "RBench", "AutumnBench", "MVP", "PAI-Bench", "EZS-Bench",
    "ContactWorld", "WorldRoamBench", "ScratchWorld", "CrashTwin", "MemoBench",
    "RoboTrustBench", "MiraBench", "Chess-World-Model", "WorldExam", "SurgWMBench",
    "H2R-Bench", "PlayWorld", "XEWorld", "HarnessEval-W",
]
T3 = [
    "WorldPrediction", "SmallWorlds", "WR-Arena", "WorldMark", "MBench", "MIND",
    "WBench", "WorldOlympiad", "HTEWorld", "RoboWM-Bench", "iWorld-Bench",
    "WoW-World-Eval", "RBench", "AutumnBench", "ContactWorld", "WorldRoamBench",
    "ScratchWorld", "MemoBench", "Chess-World-Model", "PlayWorld", "HarnessEval-W",
]
T4 = [
    "IntPhys", "IntPhys 2", "CLEVRER", "CoPhy", "PHYRE", "CRAFT", "Physion",
    "Physion++", "ComPhy", "ContPhy", "PhyCoBench", "VideoPhy", "VideoPhy-2",
    "PhyGenBench", "T2VPhysBench", "Physics-IQ", "WorldBench", "PhyWorldBench",
    "T2VWorldBench", "WorldModelBench", "VBench-2.0", "4DWorldBench",
    "GameWorld Score", "RigidBench", "Morpheus", "What-If World", "RoboWM-Bench",
    "DreamGen Bench", "WorldLens", "PhyGround", "Physion-Eval", "CRONOS", "VACT",
    "STEVO-Bench", "PhysicsMind", "PDI-Bench", "HOCA-Bench", "WorldOlympiad",
    "ACWM-Phys", "WoW-World-Eval", "RBench", "MVP", "PAI-Bench", "EZS-Bench",
    "Apple-π", "ContactWorld", "KineBench", "WorldRoamBench", "CrashTwin",
    "MemoBench", "RoboTrustBench", "MiraBench", "ReactSim-Bench", "WorldExam",
    "GAUGE", "H2R-Bench", "PlayWorld", "CaliBench", "WorldSimProbe", "XEWorld",
    "ExPhy", "HarnessEval-W",
]
S3 = [
    "CLEVRER", "CATER", "NExT-QA", "Physion", "Causal-VidQA", "CRAFT",
    "IntentQA", "ACQUIRED", "MMWorld", "VCRBench", "Physics-IQ", "WorldPrediction",
    "T2VWorldBench", "VACT", "CausalVQA", "WR-Arena", "HOCA-Bench",
    "What-If World", "CRONOS", "WoW-World-Eval", "RBench", "MVP", "PAI-Bench",
    "Apple-π", "RoboTrustBench", "MiraBench", "PlayWorld", "HarnessEval-W",
]
S4 = [
    "CLEVRER", "CRAFT", "CoPhy", "ComPhy", "CausalSpatial", "AutumnBench",
    "ScratchWorld", "ReactSim-Bench", "WorldSimProbe",
]
S5 = [
    "TC-Bench", "StoryEval", "VideoPhy", "VideoPhy-2", "PhyGenBench",
    "PhyWorldBench", "OSCBench", "MoveBench", "MagicBench", "WorldScore",
    "4DWorldBench", "DrivingGen", "ACT-Bench", "What-If World", "Omni-WorldBench",
    "DreamGen Bench", "WorldModelBench", "VBench-2.0", "WoW-World-Eval", "RBench",
    "PAI-Bench", "EZS-Bench", "KineBench", "ScratchWorld", "MemoBench",
    "RoboTrustBench", "MiraBench", "Chess-World-Model", "WorldExam", "H2R-Bench",
    "WorldSimProbe", "XEWorld", "HarnessEval-W", "WorldEcho",
]
S6 = [
    "WorldMark", "WR-Arena", "WorldSimBench", "WBench", "iWorld-Bench", "MIND",
    "ACWM-Phys", "RoboWM-Bench", "WorldArena 2.0", "WorldOlympiad",
    "WorldRoamBench", "ReactSim-Bench", "PlayWorld",
]
S7 = ["WorldArena", "WorldArena 2.0"]
S8 = ["WorldArena", "WMBench"]
S9 = [
    "WorldArena", "WorldArena 2.0", "World-in-World", "EVA-Bench", "WorldLens",
    "RoboWM-Bench", "WorldSimBench", "WR-Arena", "WoW-World-Eval", "AutumnBench",
    "ContactWorld", "KineBench",
]
S10 = ["WorldArena 2.0"]

TARGET_MEMBERS = {
    "T1": T1,
    "T2": T2,
    "T3": T3,
    "T4": T4,
    "T5": list(dict.fromkeys(S3 + S4)),
    "T6": list(dict.fromkeys(S5 + S6)),
    "T7": list(dict.fromkeys(S7 + S8 + S9 + S10)),
}
SUBTARGET_MEMBERS = {
    "S3": S3,
    "S4": S4,
    "S5": S5,
    "S6": S6,
    "S7": S7,
    "S8": S8,
    "S9": S9,
    "S10": S10,
}

NEW_ADDED = {
    "WorldExam": {
        "id": "worldexam",
        "shortName": "WorldExam",
        "title": "WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.02603",
        "arxivId": "2608.02603",
        "reference": "Y. Yang et al., “WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity,” arXiv:2608.02603, 2026.",
    },
    "SurgWMBench": {
        "id": "surgwmbench",
        "shortName": "SurgWMBench",
        "title": "SurgWMBench: A Vision-Based Benchmark for World-Modeling Surgical Instrument Motion Planning",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.08070",
        "arxivId": "2608.08070",
        "reference": "H. Liu et al., “SurgWMBench: A Vision-Based Benchmark for World-Modeling Surgical Instrument Motion Planning,” arXiv:2608.08070, 2026.",
    },
    "H2R-Bench": {
        "id": "h2r-bench",
        "shortName": "H2R-Bench",
        "title": "H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.13049",
        "arxivId": "2608.13049",
        "reference": "D. Rong et al., “H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models,” arXiv:2608.13049, 2026.",
    },
    "PlayWorld": {
        "id": "playworld",
        "shortName": "PlayWorld",
        "title": "PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.13552",
        "arxivId": "2608.13552",
        "reference": "K. Ding et al., “PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives,” arXiv:2608.13552, 2026.",
    },
    "XEWorld": {
        "id": "xeworld",
        "shortName": "XEWorld",
        "title": "XEWorld: Can Action-Conditioned World Models Generalize to Unseen Robot Embodiments?",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.05799",
        "arxivId": "2608.05799",
        "reference": "Y. Chen et al., “XEWorld: Can Action-Conditioned World Models Generalize to Unseen Robot Embodiments?” arXiv:2608.05799, 2026.",
    },
    "HarnessEval-W": {
        "id": "harnesseval-w",
        "shortName": "HarnessEval-W",
        "title": "HarnessEval-W: Agentifying the Evaluation of Visual Worlds",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.16859",
        "arxivId": "2608.16859",
        "reference": "W. Chen et al., “HarnessEval-W: Agentifying the Evaluation of Visual Worlds,” arXiv:2608.16859, 2026.",
    },
    "WorldEcho": {
        "id": "worldecho",
        "shortName": "WorldEcho",
        "title": "Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning (introduces WorldEcho)",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.24885",
        "arxivId": "2608.24885",
        "reference": "S. Chen et al., “Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning,” arXiv:2608.24885, 2026.",
    },
    "GAUGE": {
        "id": "gauge",
        "shortName": "GAUGE",
        "title": "GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.05948",
        "arxivId": "2608.05948",
        "reference": "S. Wang et al., “GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models,” arXiv:2608.05948, 2026.",
    },
    "CaliBench": {
        "id": "calibench",
        "shortName": "CaliBench",
        "title": "CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.16829",
        "arxivId": "2608.16829",
        "reference": "J. Sadeghi et al., “CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?” arXiv:2608.16829, 2026.",
    },
    "WorldSimProbe": {
        "id": "worldsimprobe",
        "shortName": "WorldSimProbe",
        "title": "WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.09298",
        "arxivId": "2608.09298",
        "reference": "P. Co et al., “WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation,” arXiv:2608.09298, 2026.",
    },
    "ExPhy": {
        "id": "exphy",
        "shortName": "ExPhy",
        "title": "ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2608.20009",
        "arxivId": "2608.20009",
        "reference": "R. Wang et al., “ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting,” arXiv:2608.20009, 2026.",
    },
}

NEW_ROWS = {
    "WorldExam": [83, 2026, "video", "OL", "P", "HCP", "", "S1+S2+S5"],
    "SurgWMBench": [84, 2026, "embodied", "OL", "P", "RWD", "", "S1+S2"],
    "H2R-Bench": [85, 2026, "embodied", "OL", "P", "HCP", "", "S1+S2+S5"],
    "PlayWorld": [86, 2026, "game+video", "CL", "P", "HCP", "", "S1+S2+S3+S6"],
    "XEWorld": [87, 2026, "embodied", "OL", "P", "SBG", "", "S1+S2+S5"],
    "HarnessEval-W": [88, 2026, "video", "OL", "P", "HCP", "", "S1+S2+S3+S5"],
    "WorldEcho": [89, 2026, "embodied", "OL", "P", "SBG", "", "S1+S2+S5"],
    "GAUGE": [140, 2026, "video", "OL", "P", "HCP", "", ""],
    "CaliBench": [141, 2026, "video", "OL", "P", "HCP", "", ""],
    "WorldSimProbe": [142, 2026, "embodied", "OL", "P", "SBG", "", "S4+S5"],
    "ExPhy": [143, 2026, "embodied", "OL", "P", "SBG", "", ""],
}

REF_OVERRIDES = {
    "RoboWM-Bench": 35,
    "World-in-World": 38,
    "IntPhys": 39,
    "CLEVRER": 40,
    "Physion": 41,
    "MIND": 42,
    "WorldOlympiad": 43,
    "WorldArena": 44,
    "WorldArena 2.0": 45,
    "ChronoMagic-Bench": 64,
    "WorldScore": 65,
    "VMBench": 66,
    "EWMBench": 67,
    "GameWorld Score": 68,
    "WorldMark": 69,
    "4DWorldBench": 70,
    "WorldLens": 71,
    "DrivingGen": 72,
    "PEDRA": 73,
    "Gen-ViRe": 74,
    "iWorld-Bench": 75,
    "WoW-World-Eval": 76,
    "RBench": 77,
    "PAI-Bench": 78,
    "EZS-Bench": 79,
    "WorldRoamBench": 80,
    "MemoBench": 81,
    "RoboTrustBench": 82,
    "WorldExam": 83,
    "SurgWMBench": 84,
    "H2R-Bench": 85,
    "PlayWorld": 86,
    "XEWorld": 87,
    "HarnessEval-W": 88,
    "WorldEcho": 89,
    "TC-Bench": 90,
    "WBench": 91,
    "CrashTwin": 92,
    "PDI-Bench": 93,
    "LoopNav": 94,
    "MBench": 95,
    "STEVO-Bench": 96,
    "CausalSpatial": 97,
    "What-If World": 98,
    "HOCA-Bench": 99,
    "AutumnBench": 100,
    "MVP": 101,
    "ContactWorld": 102,
    "ScratchWorld": 103,
    "MiraBench": 104,
    "Chess-World-Model": 105,
    "WorldPrediction": 106,
    "SmallWorlds": 107,
    "WR-Arena": 108,
    "HTEWorld": 109,
    "IntPhys 2": 110,
    "CoPhy": 111,
    "PHYRE": 112,
    "CRAFT": 113,
    "Physion++": 114,
    "ComPhy": 115,
    "ContPhy": 116,
    "PhyCoBench": 117,
    "VideoPhy": 118,
    "VideoPhy-2": 119,
    "PhyGenBench": 120,
    "T2VPhysBench": 121,
    "Physics-IQ": 122,
    "WorldBench": 123,
    "PhyWorldBench": 124,
    "T2VWorldBench": 125,
    "WorldModelBench": 126,
    "VBench-2.0": 127,
    "RigidBench": 128,
    "Morpheus": 129,
    "DreamGen Bench": 130,
    "PhyGround": 131,
    "Physion-Eval": 132,
    "CRONOS": 133,
    "VACT": 134,
    "PhysicsMind": 135,
    "ACWM-Phys": 136,
    "Apple-π": 137,
    "KineBench": 138,
    "ReactSim-Bench": 139,
    "GAUGE": 140,
    "CaliBench": 141,
    "WorldSimProbe": 142,
    "ExPhy": 143,
    "CATER": 144,
    "NExT-QA": 145,
    "Causal-VidQA": 146,
    "IntentQA": 147,
    "ACQUIRED": 148,
    "MMWorld": 149,
    "VCRBench": 150,
    "CausalVQA": 151,
    "StoryEval": 152,
    "OSCBench": 153,
    "MoveBench": 154,
    "MagicBench": 155,
    "ACT-Bench": 156,
    "Omni-WorldBench": 157,
    "WorldSimBench": 158,
    "WMBench": 159,
    "EVA-Bench": 160,
}


def split_codes(value: str) -> list[str]:
    return [part for part in str(value or "").split("+") if part]


def update_manifest() -> dict:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    manifest.setdefault("added", {}).update(NEW_ADDED)
    manifest.setdefault("records", {}).update({name: list(row) for name, row in NEW_ROWS.items()})
    if set(REF_OVERRIDES) != set(manifest["records"]):
        raise RuntimeError("Reference map does not match the 106-record corpus")
    for name, ref in REF_OVERRIDES.items():
        manifest["records"][name][0] = ref
    manifest["version"] = SNAPSHOT_VERSION
    manifest["schemaVersion"] = max(int(manifest.get("schemaVersion", 0)), 7)
    manifest["total"] = TOTAL
    manifest["crossCategory"] = CROSS_CATEGORY
    manifest.setdefault("subtargetLabels", {})["S3"] = "Observation-Grounded Evaluation"
    manifest.setdefault("subtargetLabels", {})["S4"] = "Intervention-Grounded Evaluation"

    # Rebuild top-level and leaf assignments from the current manuscript lists.
    all_record_names = set(manifest["records"])
    listed_names = set().union(*(set(names) for names in TARGET_MEMBERS.values()))
    if listed_names != all_record_names:
        missing_from_lists = sorted(all_record_names - listed_names)
        missing_from_records = sorted(listed_names - all_record_names)
        raise RuntimeError(
            f"Target membership mismatch; records-only={missing_from_lists}, lists-only={missing_from_records}"
        )

    for name, row in manifest["records"].items():
        target_codes = [code for code, names in TARGET_MEMBERS.items() if name in names]
        old_subtargets = split_codes(row[7])
        preserved_visual = [code for code in old_subtargets if code in {"S1", "S2"}]
        other_subtargets = [code for code, names in SUBTARGET_MEMBERS.items() if name in names]
        row[6] = "+".join(target_codes)
        row[7] = "+".join(dict.fromkeys(preserved_visual + other_subtargets))

    counts = {code: sum(code in split_codes(row[6]) for row in manifest["records"].values()) for code in TARGET_MEMBERS}
    expected_counts = {"T1": 31, "T2": 37, "T3": 21, "T4": 62, "T5": 35, "T6": 47, "T7": 13}
    cross_count = sum(len(split_codes(row[6])) > 1 for row in manifest["records"].values())
    if counts != expected_counts:
        raise RuntimeError(f"Category count validation failed: {counts} != {expected_counts}")
    if len(manifest["records"]) != TOTAL or cross_count != CROSS_CATEGORY:
        raise RuntimeError(
            f"Corpus validation failed: {len(manifest['records'])}/{TOTAL} records, "
            f"{cross_count}/{CROSS_CATEGORY} cross-category"
        )

    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return manifest


ROW_PATTERN = re.compile(
    r"^\| \[\*\*(?P<label>.+?)\*\*\]\((?P<paper>[^)]+)\) \| "
    r"(?P<year>\d{4}) \| (?P<venue>.*?) \| (?P<code>.*?) \| (?P<project>.*?) \|$",
    re.MULTILINE,
)


def existing_row_metadata() -> dict[str, dict[str, str]]:
    if not README_PATH.exists():
        return {}
    text = README_PATH.read_text(encoding="utf-8")
    result: dict[str, dict[str, str]] = {}
    for match in ROW_PATTERN.finditer(text):
        label = match.group("label")
        name = label[:-2] if label.endswith(" △") else label
        result.setdefault(
            name,
            {
                "paper": match.group("paper"),
                "venue": match.group("venue"),
                "code": match.group("code"),
                "project": match.group("project"),
            },
        )
    return result


def generate_readme(manifest: dict) -> None:
    cached = existing_row_metadata()
    target_sets = {code: set(names) for code, names in TARGET_MEMBERS.items()}

    def row(name: str) -> str:
        record = manifest["records"][name]
        metadata = manifest.get("added", {}).get(name, {})
        cached_row = cached.get(name, {})
        paper = cached_row.get("paper") or metadata.get("paperUrl")
        if not paper:
            title = metadata.get("title") or name
            paper = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"
        venue = cached_row.get("venue") or metadata.get("venue") or "arXiv"
        code = cached_row.get("code", "-")
        project = cached_row.get("project", "-")
        marker = " △" if sum(name in names for names in target_sets.values()) > 1 else ""
        return f"| [**{name}{marker}**]({paper}) | {record[1]} | {venue} | {code} | {project} |"

    def table(names: list[str]) -> list[str]:
        return [
            "| Article | Year | Venue | Code | Project Page |",
            "|:--|:--:|:--:|:--:|:--:|",
            *[row(name) for name in names],
        ]

    lines = [
        "# A Survey of World Model Benchmarks",
        "",
        "[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://world-model-benchmarks.github.io/) "
        "[![Benchmarks](https://img.shields.io/badge/Benchmarks-106-2f8f63)](https://world-model-benchmarks.github.io/#benchmarks)",
        "",
        "This repository accompanies **A Survey of World Model Benchmarks**. "
        "The latest manuscript covers **106 representative benchmarks** published from **2018–2026**; "
        "**66** span more than one evaluation-target category. "
        "The corpus was last checked on August 27, 2026.",
        "",
        "The category membership below follows the latest survey taxonomy and Figure 4. "
        "Rows are intentionally repeated when a benchmark belongs to multiple evaluation targets or sub-targets. "
        "`△` marks a benchmark assigned to more than one top-level evaluation target.",
        "",
        "Each table is designed as a literature index rather than a copy of Tables 3–9: "
        "**Article**, **Year**, **Venue**, **Code**, and **Project Page**. "
        "`-` means that no verified public link is currently recorded.",
        "",
        "## Contents",
        "",
        "- [Visual and Temporal Quality](#visual-and-temporal-quality)",
        "- [Spatial and State Consistency](#spatial-and-state-consistency)",
        "- [Long-Horizon Memory and State Persistence](#long-horizon-memory-and-state-persistence)",
        "- [Physical Plausibility](#physical-plausibility)",
        "- [Causal and Counterfactual Reasoning](#causal-and-counterfactual-reasoning)",
        "- [Control Fidelity and Interactive Dynamics](#control-fidelity-and-interactive-dynamics)",
        "- [Functional Utility](#functional-utility)",
        "",
        "## Evaluation-target coverage",
        "",
        "| Evaluation target | Benchmarks |",
        "|:--|--:|",
        "| Visual & Temporal Quality | 31 |",
        "| Spatial & State Consistency | 37 |",
        "| Long-Horizon Memory & State Persistence | 21 |",
        "| Physical Plausibility | 62 |",
        "| Causal & Counterfactual Reasoning | 35 |",
        "| Control Fidelity & Interactive Dynamics | 47 |",
        "| Functional Utility | 13 |",
        "",
        "Counts overlap because cross-category benchmarks appear in more than one top-level target.",
        "",
    ]

    sections = [
        ("Visual and Temporal Quality", None, T1),
        ("Spatial and State Consistency", None, T2),
        ("Long-Horizon Memory and State Persistence", None, T3),
        ("Physical Plausibility", None, T4),
        ("Causal and Counterfactual Reasoning", "Observation-Grounded Evaluation", S3),
        (None, "Intervention-Grounded Evaluation", S4),
        ("Control Fidelity and Interactive Dynamics", "Pre-specified Control Fidelity", S5),
        (None, "Interactive Action Fidelity", S6),
        ("Functional Utility", "World Model as Data Engine", S7),
        (None, "World Model as Policy Evaluator", S8),
        (None, "World Model as Planner", S9),
        (None, "World Model as Interactive Training Environment", S10),
    ]
    for h2, h3, names in sections:
        if h2:
            lines.extend([f"## {h2}", ""])
        if h3:
            lines.extend([f"### {h3}", ""])
        lines.extend(table(names))
        lines.append("")

    lines.extend(
        [
            "## Machine-readable data",
            "",
            "- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical benchmark, target, sub-target, protocol, metric, data-source, year, and domain metadata",
            "- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels and release-window definitions",
            "- [Interactive project page](https://world-model-benchmarks.github.io/)",
            "",
        ]
    )
    README_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_metadata(manifest: dict) -> None:
    metadata = {
        "title": manifest["title"],
        "version": manifest["version"],
        "framework": manifest["framework"],
        "total": manifest["total"],
        "crossCategory": manifest["crossCategory"],
        "protocolLabels": manifest["protocolLabels"],
        "metricLabels": manifest["metricLabels"],
        "dataLabels": manifest["dataLabels"],
        "timelineBins": manifest["timelineBins"],
        "dimensions": 4,
        "yearMin": 2018,
        "yearMax": 2026,
        "targets": [manifest["targetLabels"][f"T{i}"] for i in range(1, 8)],
    }
    METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_in_file(relative_path: str, replacements: list[tuple[str, str]]) -> None:
    path = ROOT / relative_path
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in replacements:
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def update_website_files() -> None:
    common_copy = [
        ("95 benchmarks · 58 cross-category · checked July 30, 2026", "106 benchmarks · 66 cross-category · checked August 27, 2026"),
        ("95 representative benchmarks", "106 representative benchmarks"),
        ("95 world-model benchmarks", "106 world-model benchmarks"),
        ("42 new benchmarks in 2026", "53 new benchmarks in 2026"),
        ("bringing the corpus to <strong>95</strong>", "bringing the corpus to <strong>106</strong>"),
    ]

    replace_in_file(
        "docs/index.html",
        common_copy
        + [
            ('<strong id="stat-total">95</strong>', '<strong id="stat-total">106</strong>'),
            ('<strong id="stat-cross">58</strong>', '<strong id="stat-cross">66</strong>'),
            ('id="result-count">95<', 'id="result-count">106<'),
            ('assets/app-v3.js?v=7', 'assets/app-v3.js?v=8'),
        ],
    )
    replace_in_file(
        "docs/assets/app-v3.js",
        common_copy
        + [
            ('setTextIfChanged(stats[0].querySelector("strong"), "95");', 'setTextIfChanged(stats[0].querySelector("strong"), "106");'),
            ('setTextIfChanged(stats[1].querySelector("strong"), "58");', 'setTextIfChanged(stats[1].querySelector("strong"), "66");'),
            ('resultCount.textContent !== "95"', 'resultCount.textContent !== "106"'),
            ('resultCount.textContent = "95"', 'resultCount.textContent = "106"'),
            ('app-v3-core.js?v=9', 'app-v3-core.js?v=10'),
        ],
    )
    replace_in_file(
        "docs/assets/app-v3-core.js",
        [("world-model-benchmarks-july-2026.json", "world-model-benchmarks-august-2026.json")],
    )
    replace_in_file(
        "docs/assets/social-preview.svg",
        [('font-size="30" font-weight="800">95</text>', 'font-size="30" font-weight="800">106</text>')],
    )
    status_path = ROOT / "docs" / "deployment-status.txt"
    status_path.write_text("GitHub Pages deployment trigger\nUpdated: 2026-08-27\n", encoding="utf-8")


def main() -> None:
    manifest = update_manifest()
    generate_readme(manifest)
    write_metadata(manifest)
    update_website_files()
    print(
        f"Generated README and website data for {manifest['total']} benchmarks "
        f"({manifest['crossCategory']} cross-category)."
    )


if __name__ == "__main__":
    main()
