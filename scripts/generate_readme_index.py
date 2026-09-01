#!/usr/bin/env python3
"""Synchronize the repository and project page with the August 31, 2026 PDF.

The benchmark memberships below are a direct transcription of Figure 4 and
Tables 3--9 in the latest manuscript.  This file is the single source of truth
for generated repository and website artifacts.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
MANIFEST_PATH = ASSETS / "benchmarks.json"
METADATA_PATH = ASSETS / "metadata.json"
README_PATH = ROOT / "Readme.md"
INDEX_PATH = ROOT / "docs" / "index.html"
CORE_JS_PATH = ASSETS / "app-v3-core.js"
WRAPPER_JS_PATH = ASSETS / "app-v3.js"
APP_JS_PATH = ASSETS / "app.js"

SNAPSHOT_VERSION = "August 31, 2026 manuscript snapshot"
SNAPSHOT_DATE = "August 31, 2026"
SNAPSHOT_ISO_DATE = "2026-08-31"
SITE_URL = "https://world-model-benchmarks.github.io/World-Model-Benchmarks/"
REPOSITORY_URL = "https://github.com/World-Model-Benchmarks/World-Model-Benchmarks"
TOTAL = 106
CROSS_CATEGORY = 85
SCHEMA_VERSION = 8

TARGET_LABELS = {
    "T1": "Visual & Temporal Quality",
    "T2": "Spatial & State Consistency",
    "T3": "Long-Horizon Memory & State Persistence",
    "T4": "Physical Plausibility",
    "T5": "Causal & Counterfactual Reasoning",
    "T6": "Control Fidelity & Interactive Dynamics",
    "T7": "Functional Utility",
}
SUBTARGET_LABELS = {
    "S1": "Visual Quality",
    "S2": "Temporal Quality",
    "S3": "Observation-Grounded Evaluation",
    "S4": "Intervention-Grounded Evaluation",
    "S5": "Pre-specified Control Fidelity",
    "S6": "Interactive Action Fidelity",
    "S7": "Data Engine",
    "S8": "Policy Evaluator",
    "S9": "Planner",
    "S10": "Interactive Training Environment",
}

# Figure 4 / Table 3: Visual and Temporal Quality.
S1 = [
    "ChronoMagic-Bench", "WorldScore", "VMBench", "EWMBench", "WorldArena",
    "GameWorld Score", "WorldMark", "4DWorldBench", "WorldLens", "DrivingGen",
    "PEDRA", "Gen-ViRe", "iWorld-Bench", "WoW-World-Eval", "RBench",
    "PAI-Bench", "EZS-Bench", "WorldRoamBench", "MemoBench", "RoboTrustBench",
    "WorldExam", "SurgWMBench", "H2R-Bench", "PlayWorld", "XEWorld",
    "HarnessEval-W", "WorldEcho", "ACWM-Phys", "HTEWorld", "RigidBench",
    "MagicBench", "MIND", "MoveBench", "Omni-WorldBench", "OSCBench",
    "T2VWorldBench", "WMBench", "WorldModelBench", "WorldSimBench", "Apple-π",
]
S2 = [
    "ChronoMagic-Bench", "VMBench", "TC-Bench", "WorldScore", "4DWorldBench",
    "GameWorld Score", "WorldMark", "WBench", "EWMBench", "WorldArena",
    "WorldArena 2.0", "WorldLens", "DrivingGen", "PEDRA", "Gen-ViRe",
    "WoW-World-Eval", "RBench", "PAI-Bench", "EZS-Bench", "WorldRoamBench",
    "CrashTwin", "MemoBench", "RoboTrustBench", "WorldExam", "SurgWMBench",
    "H2R-Bench", "PlayWorld", "XEWorld", "HarnessEval-W", "WorldEcho",
    "EVA-Bench", "HTEWorld", "MagicBench", "MoveBench", "Omni-WorldBench",
    "T2VWorldBench", "WMBench", "WorldModelBench", "WR-Arena", "Apple-π",
]

# Figure 4 / Table 4: Spatial and State Consistency.
T2 = [
    "WorldMark", "GameWorld Score", "EWMBench", "WorldArena", "WorldLens",
    "DrivingGen", "WorldScore", "4DWorldBench", "PDI-Bench", "LoopNav", "MIND",
    "MBench", "STEVO-Bench", "CausalSpatial", "What-If World", "WorldOlympiad",
    "HOCA-Bench", "WoW-World-Eval", "RBench", "AutumnBench", "MVP", "PAI-Bench",
    "EZS-Bench", "ContactWorld", "WorldRoamBench", "ScratchWorld", "CrashTwin",
    "MemoBench", "RoboTrustBench", "MiraBench", "Chess-World-Model", "WorldExam",
    "SurgWMBench", "H2R-Bench", "PlayWorld", "XEWorld", "HarnessEval-W",
    "EVA-Bench", "Gen-ViRe", "HTEWorld", "IntPhys 2", "iWorld-Bench",
    "RigidBench", "Omni-WorldBench", "OSCBench", "PEDRA", "IntPhys",
    "WorldArena 2.0", "SmallWorlds", "WMBench", "VBench-2.0", "WBench",
    "WorldBench", "WorldSimBench", "Apple-π",
]

# Figure 4 / Table 5: Long-Horizon Memory and State Persistence.
T3 = [
    "WorldPrediction", "SmallWorlds", "WR-Arena", "WorldMark", "MBench", "MIND",
    "WBench", "WorldOlympiad", "HTEWorld", "RoboWM-Bench", "iWorld-Bench",
    "WoW-World-Eval", "RBench", "AutumnBench", "ContactWorld", "WorldRoamBench",
    "ScratchWorld", "MemoBench", "Chess-World-Model", "PlayWorld", "HarnessEval-W",
    "LoopNav", "ExPhy", "WMBench",
]

# Figure 4 / Table 6: Physical Plausibility.
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
    "ExPhy", "HarnessEval-W", "CausalSpatial", "Gen-ViRe", "HTEWorld", "MBench",
    "Omni-WorldBench", "PEDRA", "WorldArena 2.0", "SmallWorlds", "WMBench",
    "VMBench", "WBench", "WorldArena", "WorldSimBench", "DrivingGen", "EWMBench",
]

# Figure 4 / Table 7: Causal and Counterfactual Reasoning.
S3 = [
    "CLEVRER", "CATER", "NExT-QA", "Physion", "Causal-VidQA", "CRAFT",
    "IntentQA", "ACQUIRED", "MMWorld", "VCRBench", "Physics-IQ", "WorldPrediction",
    "T2VWorldBench", "VACT", "CausalVQA", "WR-Arena", "HOCA-Bench",
    "What-If World", "CRONOS", "WoW-World-Eval", "RBench", "MVP", "PAI-Bench",
    "RoboTrustBench", "MiraBench", "PlayWorld", "HarnessEval-W", "ContPhy",
    "PhysicsMind", "WorldExam",
]
S4 = [
    "CLEVRER", "CRAFT", "CoPhy", "ComPhy", "CausalSpatial", "AutumnBench",
    "ScratchWorld", "ReactSim-Bench", "WorldSimProbe",
]

# Figure 4 / Table 8: Control Fidelity and Interactive Dynamics.
S5 = [
    "TC-Bench", "StoryEval", "VideoPhy", "VideoPhy-2", "PhyGenBench",
    "PhyWorldBench", "OSCBench", "MoveBench", "MagicBench", "WorldScore",
    "4DWorldBench", "DrivingGen", "ACT-Bench", "What-If World", "Omni-WorldBench",
    "DreamGen Bench", "WorldModelBench", "VBench-2.0", "WoW-World-Eval", "RBench",
    "PAI-Bench", "EZS-Bench", "KineBench", "ScratchWorld", "MemoBench",
    "RoboTrustBench", "MiraBench", "Chess-World-Model", "WorldExam", "H2R-Bench",
    "WorldSimProbe", "XEWorld", "HarnessEval-W", "WorldEcho", "EWMBench",
    "GameWorld Score", "MBench", "STEVO-Bench", "VACT", "WorldArena",
]
S6 = [
    "WorldMark", "WR-Arena", "WorldSimBench", "WBench", "iWorld-Bench", "MIND",
    "ACWM-Phys", "RoboWM-Bench", "WorldArena 2.0", "WorldOlympiad",
    "WorldRoamBench", "ReactSim-Bench", "PlayWorld", "HTEWorld", "WMBench",
]

# Figure 4 / Table 9: Functional Utility.
S7 = ["WorldArena", "WorldArena 2.0"]
S8 = ["WorldArena", "WMBench"]
S9 = [
    "WorldArena", "WorldArena 2.0", "World-in-World", "EVA-Bench", "WorldLens",
    "RoboWM-Bench", "WorldSimBench", "WR-Arena", "WoW-World-Eval", "AutumnBench",
    "ContactWorld", "KineBench",
]
S10 = ["WorldArena 2.0"]

T1 = list(dict.fromkeys(S1 + S2))
T5 = list(dict.fromkeys(S3 + S4))
T6 = list(dict.fromkeys(S5 + S6))
T7 = list(dict.fromkeys(S7 + S8 + S9 + S10))
TARGET_MEMBERS = {"T1": T1, "T2": T2, "T3": T3, "T4": T4, "T5": T5, "T6": T6, "T7": T7}
SUBTARGET_MEMBERS = {
    "S1": S1, "S2": S2, "S3": S3, "S4": S4, "S5": S5,
    "S6": S6, "S7": S7, "S8": S8, "S9": S9, "S10": S10,
}
EXPECTED_TARGET_COUNTS = {"T1": 46, "T2": 55, "T3": 24, "T4": 77, "T5": 37, "T6": 55, "T7": 13}
EXPECTED_SUBTARGET_COUNTS = {"S1": 40, "S2": 40, "S3": 30, "S4": 9, "S5": 40, "S6": 15, "S7": 2, "S8": 2, "S9": 12, "S10": 1}

# Reference numbers in the latest PDF bibliography / Tables 3--9.
REFS = {
    "RoboWM-Bench": 35, "World-in-World": 38, "IntPhys": 39, "CLEVRER": 40,
    "Physion": 41, "MIND": 42, "WorldOlympiad": 43, "WorldArena": 44,
    "WorldArena 2.0": 45, "ChronoMagic-Bench": 64, "WorldScore": 65,
    "VMBench": 66, "EWMBench": 67, "GameWorld Score": 68, "WorldMark": 69,
    "4DWorldBench": 70, "WorldLens": 71, "DrivingGen": 72, "PEDRA": 73,
    "Gen-ViRe": 74, "iWorld-Bench": 75, "WoW-World-Eval": 76, "RBench": 77,
    "PAI-Bench": 78, "EZS-Bench": 79, "WorldRoamBench": 80, "MemoBench": 81,
    "RoboTrustBench": 82, "WorldExam": 83, "SurgWMBench": 84, "H2R-Bench": 85,
    "PlayWorld": 86, "XEWorld": 87, "HarnessEval-W": 88, "WorldEcho": 89,
    "ACWM-Phys": 90, "HTEWorld": 91, "RigidBench": 92, "MagicBench": 93,
    "MoveBench": 94, "Omni-WorldBench": 95, "OSCBench": 96, "T2VWorldBench": 97,
    "WMBench": 98, "WorldModelBench": 99, "WorldSimBench": 100, "Apple-π": 101,
    "TC-Bench": 102, "WBench": 103, "CrashTwin": 104, "EVA-Bench": 105,
    "WR-Arena": 106, "PDI-Bench": 107, "LoopNav": 108, "MBench": 109,
    "STEVO-Bench": 110, "CausalSpatial": 111, "What-If World": 112,
    "HOCA-Bench": 113, "AutumnBench": 114, "MVP": 115, "ContactWorld": 116,
    "ScratchWorld": 117, "MiraBench": 118, "Chess-World-Model": 119,
    "IntPhys 2": 120, "SmallWorlds": 121, "VBench-2.0": 122, "WorldBench": 123,
    "WorldPrediction": 124, "ExPhy": 125, "CoPhy": 126, "PHYRE": 127,
    "CRAFT": 128, "Physion++": 129, "ComPhy": 130, "ContPhy": 131,
    "PhyCoBench": 132, "VideoPhy": 133, "VideoPhy-2": 134, "PhyGenBench": 135,
    "T2VPhysBench": 136, "Physics-IQ": 137, "PhyWorldBench": 138,
    "Morpheus": 139, "DreamGen Bench": 140, "PhyGround": 141,
    "Physion-Eval": 142, "CRONOS": 143, "VACT": 144, "PhysicsMind": 145,
    "KineBench": 146, "ReactSim-Bench": 147, "GAUGE": 148, "CaliBench": 149,
    "WorldSimProbe": 150, "CATER": 151, "NExT-QA": 152, "Causal-VidQA": 153,
    "IntentQA": 154, "ACQUIRED": 155, "MMWorld": 156, "VCRBench": 157,
    "CausalVQA": 158, "StoryEval": 159, "ACT-Bench": 160,
}

# The aggregate website record uses the union of tracks when a benchmark has
# different protocol/metric levels in different tables or downstream roles.
AGGREGATE_OVERRIDES = {
    "WorldArena": {"protocol": "OL+CL", "metrics": "P+O", "data": "SBG"},
    "WorldArena 2.0": {"protocol": "OL+CL", "metrics": "P+O", "data": "HCP"},
    "WorldLens": {"protocol": "OL+CL", "metrics": "P+O", "data": "HCP"},
    "WorldSimBench": {"protocol": "OL+CL", "metrics": "P+O", "data": "HCP"},
    "WoW-World-Eval": {"protocol": "OL", "metrics": "P+O", "data": "HCP"},
    "AutumnBench": {"protocol": "CL", "metrics": "P+O", "data": "SBG"},
    "ContactWorld": {"protocol": "CL", "metrics": "P+O", "data": "HCP"},
    "KineBench": {"protocol": "CL", "metrics": "P+O", "data": "HCP"},
    "WMBench": {"protocol": "CL", "metrics": "P+O", "data": "HCP"},
    "PHYRE": {"protocol": "CL", "metrics": "O", "data": "SBG"},
    "RoboWM-Bench": {"protocol": "OL", "metrics": "O", "data": "HCP"},
    "World-in-World": {"protocol": "CL", "metrics": "O", "data": "HCP"},
    "EVA-Bench": {"protocol": "OL", "metrics": "O", "data": "HCP"},
    "PlayWorld": {"protocol": "CL", "metrics": "P", "data": "HCP"},
    "ReactSim-Bench": {"protocol": "CL", "metrics": "P", "data": "HCP"},
}

LEGACY_JS_FILES = ["app-1.js", "app-2.js", "app-3.js", "app-v2.js"]


def split_codes(value: str) -> list[str]:
    return [part for part in str(value or "").split("+") if part]


def ordered_codes(name: str, membership: dict[str, list[str]]) -> list[str]:
    return [code for code, names in membership.items() if name in names]


def validate_source_lists(record_names: set[str]) -> None:
    if set(REFS) != record_names:
        raise RuntimeError(
            f"Reference map mismatch: records-only={sorted(record_names - set(REFS))}; "
            f"refs-only={sorted(set(REFS) - record_names)}"
        )
    listed = set().union(*(set(names) for names in TARGET_MEMBERS.values()))
    if listed != record_names:
        raise RuntimeError(
            f"Target membership mismatch: records-only={sorted(record_names - listed)}; "
            f"lists-only={sorted(listed - record_names)}"
        )
    for code, names in TARGET_MEMBERS.items():
        if len(names) != len(set(names)):
            raise RuntimeError(f"Duplicate benchmark in {code}")
        if len(names) != EXPECTED_TARGET_COUNTS[code]:
            raise RuntimeError(f"{code} count {len(names)} != {EXPECTED_TARGET_COUNTS[code]}")
    for code, names in SUBTARGET_MEMBERS.items():
        if len(names) != len(set(names)):
            raise RuntimeError(f"Duplicate benchmark in {code}")
        if len(names) != EXPECTED_SUBTARGET_COUNTS[code]:
            raise RuntimeError(f"{code} count {len(names)} != {EXPECTED_SUBTARGET_COUNTS[code]}")

    cross_count = sum(
        sum(name in names for names in TARGET_MEMBERS.values()) > 1
        for name in record_names
    )
    if cross_count != CROSS_CATEGORY:
        raise RuntimeError(f"Cross-category count {cross_count} != {CROSS_CATEGORY}")


def classification_fingerprint(records: dict[str, list]) -> str:
    rows = [
        f"{name}|{row[0]}|{row[6]}|{row[7]}"
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def update_manifest() -> dict:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    records = manifest.get("records", {})
    validate_source_lists(set(records))

    manifest["version"] = SNAPSHOT_VERSION
    manifest["snapshotDate"] = SNAPSHOT_ISO_DATE
    manifest["schemaVersion"] = SCHEMA_VERSION
    manifest["total"] = TOTAL
    manifest["crossCategory"] = CROSS_CATEGORY
    manifest["targetLabels"] = TARGET_LABELS
    manifest["subtargetLabels"] = SUBTARGET_LABELS
    manifest["protocolLabels"] = {"OL": "Open-Loop Evaluation", "CL": "Closed-Loop Interaction"}
    manifest["metricLabels"] = {"P": "Prediction-Level Metrics", "O": "Downstream Outcome Metrics"}
    manifest["dataLabels"] = {
        "RWD": "Real-World Data Collection",
        "SBG": "Simulation-Based Generation",
        "SPTC": "Scenario, Prompt, and Task Curation",
        "HCP": "Hybrid Construction Pipelines",
    }
    manifest["targetCounts"] = {
        TARGET_LABELS[code]: EXPECTED_TARGET_COUNTS[code]
        for code in TARGET_LABELS
    }
    manifest["subtargetCounts"] = {
        SUBTARGET_LABELS[code]: EXPECTED_SUBTARGET_COUNTS[code]
        for code in SUBTARGET_LABELS
    }
    manifest["sourceNote"] = (
        "Aligned with Figure 4 and Tables 3–9 of the manuscript; "
        "the corpus was last checked on August 31, 2026."
    )

    for name, row in records.items():
        if len(row) < 8:
            row.extend([""] * (8 - len(row)))
        row[0] = REFS[name]
        override = AGGREGATE_OVERRIDES.get(name)
        if override:
            row[3] = override["protocol"]
            row[4] = override["metrics"]
            row[5] = override["data"]
        row[6] = "+".join(ordered_codes(name, TARGET_MEMBERS))
        row[7] = "+".join(ordered_codes(name, SUBTARGET_MEMBERS))

        protocols = set(split_codes(row[3]))
        metrics = set(split_codes(row[4]))
        data = set(split_codes(row[5]))
        if not protocols or not protocols <= {"OL", "CL"}:
            raise RuntimeError(f"Invalid protocol coding for {name}: {row[3]}")
        if not metrics or not metrics <= {"P", "O"}:
            raise RuntimeError(f"Invalid metric coding for {name}: {row[4]}")
        if len(data) != 1 or not data <= {"RWD", "SBG", "SPTC", "HCP"}:
            raise RuntimeError(f"Invalid data coding for {name}: {row[5]}")

    target_counts = Counter(code for row in records.values() for code in split_codes(row[6]))
    subtarget_counts = Counter(code for row in records.values() for code in split_codes(row[7]))
    cross_count = sum(len(split_codes(row[6])) > 1 for row in records.values())
    if dict(target_counts) != EXPECTED_TARGET_COUNTS:
        raise RuntimeError(f"Target counts differ from PDF: {target_counts}")
    if dict(subtarget_counts) != EXPECTED_SUBTARGET_COUNTS:
        raise RuntimeError(f"Sub-target counts differ from PDF: {subtarget_counts}")
    if len(records) != TOTAL or cross_count != CROSS_CATEGORY:
        raise RuntimeError(
            f"Corpus validation failed: {len(records)}/{TOTAL} records, "
            f"{cross_count}/{CROSS_CATEGORY} cross-category"
        )

    manifest["classificationFingerprint"] = classification_fingerprint(records)
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return manifest


def slugify(name: str) -> str:
    value = name.lower().replace("π", "pi")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "benchmark"


def load_canonical_metadata(manifest: dict) -> dict[str, dict]:
    aliases = manifest.get("aliases", {})
    removed = set(manifest.get("removed", []))
    metadata: dict[str, dict] = {}

    for shard_path in sorted(ASSETS.glob("benchmarks-[1-4].json")):
        for raw in json.loads(shard_path.read_text(encoding="utf-8")):
            original = raw.get("shortName")
            canonical = aliases.get(original, original)
            if not canonical or original in removed or canonical in removed:
                continue
            normalized = dict(raw)
            normalized["shortName"] = canonical
            metadata.setdefault(canonical, normalized)

    for name, raw in manifest.get("added", {}).items():
        metadata.setdefault(name, dict(raw))

    missing = sorted(set(manifest["records"]) - set(metadata))
    if missing:
        raise RuntimeError(f"Missing publication metadata for: {', '.join(missing)}")
    return metadata


def canonical_record(name: str, manifest: dict, raw: dict) -> dict:
    row = manifest["records"][name]
    targets = [manifest["targetLabels"][code] for code in split_codes(row[6])]
    subtargets = [manifest["subtargetLabels"][code] for code in split_codes(row[7])]
    added = manifest.get("added", {}).get(name, {})

    def choose(key: str, default=None):
        value = raw.get(key)
        return value if value not in (None, "") else added.get(key, default)

    return {
        "id": choose("id", slugify(name)),
        "shortName": name,
        "title": choose("title", name),
        "ref": row[0],
        "year": row[1],
        "venue": choose("venue", "arXiv"),
        "domains": split_codes(row[2]),
        "protocols": split_codes(row[3]),
        "metrics": split_codes(row[4]),
        "evaluationData": split_codes(row[5]),
        "targets": targets,
        "subtargets": subtargets,
        "crossCategory": len(targets) > 1,
        "paperUrl": choose("paperUrl", ""),
        "arxivId": choose("arxivId"),
        "reference": choose("reference", ""),
    }


def rewrite_shards(manifest: dict) -> list[dict]:
    metadata = load_canonical_metadata(manifest)
    corpus = [
        canonical_record(name, manifest, metadata[name])
        for name in sorted(manifest["records"], key=lambda item: (REFS[item], item))
    ]
    if len(corpus) != TOTAL or len({item["shortName"] for item in corpus}) != TOTAL:
        raise RuntimeError("Canonical shard corpus is incomplete or duplicated")

    chunk_size = math.ceil(len(corpus) / 4)
    chunks = [corpus[index:index + chunk_size] for index in range(0, len(corpus), chunk_size)]
    while len(chunks) < 4:
        chunks.append([])
    if len(chunks) != 4:
        raise RuntimeError(f"Expected four shards, generated {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        path = ASSETS / f"benchmarks-{index}.json"
        path.write_text(json.dumps(chunk, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return corpus


ROW_PATTERN = re.compile(
    r"^\| \[\*\*(?P<label>.+?)\*\*\]\((?P<paper>[^)]+)\) \| "
    r"(?P<year>\d{4}) \| (?P<venue>.*?) \| (?P<code>.*?) \| (?P<project>.*?) \|$",
    re.MULTILINE,
)


def existing_row_metadata() -> dict[str, dict[str, str]]:
    if not README_PATH.exists():
        return {}
    result: dict[str, dict[str, str]] = {}
    for match in ROW_PATTERN.finditer(README_PATH.read_text(encoding="utf-8")):
        label = match.group("label")
        name = label[:-2] if label.endswith(" △") else label
        result.setdefault(name, {
            "paper": match.group("paper"),
            "venue": match.group("venue"),
            "code": match.group("code"),
            "project": match.group("project"),
        })
    return result


def generate_readme(manifest: dict, corpus: list[dict]) -> None:
    cached = existing_row_metadata()
    by_name = {item["shortName"]: item for item in corpus}

    def row(name: str) -> str:
        item = by_name[name]
        cached_row = cached.get(name, {})
        paper = cached_row.get("paper") or item.get("paperUrl")
        if not paper:
            query = re.sub(r"\s+", "+", item.get("title") or name)
            paper = f"https://scholar.google.com/scholar?q={query}"
        venue = cached_row.get("venue") or item.get("venue") or "arXiv"
        code = cached_row.get("code", "-")
        project = cached_row.get("project", "-")
        marker = " △" if item["crossCategory"] else ""
        return f"| [**{name}{marker}**]({paper}) | {item['year']} | {venue} | {code} | {project} |"

    def table(names: list[str]) -> list[str]:
        return [
            "| Article | Year | Venue | Code | Project Page |",
            "|:--|:--:|:--:|:--:|:--:|",
            *[row(name) for name in names],
        ]

    lines = [
        "# A Survey of World Model Benchmarks",
        "",
        f"[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)]({SITE_URL}) "
        f"[![Benchmarks](https://img.shields.io/badge/Benchmarks-{TOTAL}-2f8f63)]({SITE_URL}#benchmarks)",
        "",
        "This repository accompanies **A Survey of World Model Benchmarks**. "
        f"The latest manuscript covers **{TOTAL} representative benchmarks** published from **2018–2026**; "
        f"**{CROSS_CATEGORY}** span more than one evaluation-target category. "
        f"The corpus was last checked on {SNAPSHOT_DATE}.",
        "",
        "The classification below follows Figure 4 and Tables 3–9 of the latest PDF. "
        "Rows are intentionally repeated when a benchmark belongs to multiple evaluation targets or sub-targets. "
        "`△` marks a benchmark assigned to more than one top-level evaluation target.",
        "",
        "Each table is a literature index with **Article**, **Year**, **Venue**, **Code**, and **Project Page**. "
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
        *[f"| {TARGET_LABELS[code]} | {EXPECTED_TARGET_COUNTS[code]} |" for code in TARGET_LABELS],
        "",
        "Counts overlap because cross-category benchmarks appear in more than one top-level target.",
        "",
    ]

    sections: list[tuple[str | None, str | None, list[str]]] = [
        ("Visual and Temporal Quality", "Visual Quality", S1),
        (None, "Temporal Quality", S2),
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

    lines.extend([
        "## Machine-readable data",
        "",
        "- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical taxonomy manifest and compact record coding",
        "- [`docs/assets/benchmarks-1.json`](docs/assets/benchmarks-1.json)–[`benchmarks-4.json`](docs/assets/benchmarks-4.json): normalized benchmark records used by the explorer",
        "- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels, counts, and release-window definitions",
        f"- [Interactive project page]({SITE_URL})",
        "",
    ])
    README_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_metadata(manifest: dict) -> None:
    metadata = {
        "title": manifest["title"],
        "version": manifest["version"],
        "snapshotDate": manifest["snapshotDate"],
        "framework": manifest["framework"],
        "total": manifest["total"],
        "crossCategory": manifest["crossCategory"],
        "protocolLabels": manifest["protocolLabels"],
        "metricLabels": manifest["metricLabels"],
        "dataLabels": manifest["dataLabels"],
        "timelineBins": manifest["timelineBins"],
        "targetCounts": manifest["targetCounts"],
        "subtargetCounts": manifest["subtargetCounts"],
        "classificationFingerprint": manifest["classificationFingerprint"],
        "dimensions": 4,
        "yearMin": 2018,
        "yearMax": 2026,
        "targets": [TARGET_LABELS[f"T{i}"] for i in range(1, 8)],
    }
    METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_regex(text: str, pattern: str, replacement: str, *, count: int = 0) -> str:
    updated, substitutions = re.subn(pattern, replacement, text, count=count, flags=re.MULTILINE | re.DOTALL)
    if substitutions == 0:
        raise RuntimeError(f"Pattern not found while updating website: {pattern}")
    return updated


def update_index() -> None:
    text = INDEX_PATH.read_text(encoding="utf-8")
    social_url = f"{SITE_URL}assets/social-preview.svg"

    text = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{SITE_URL}">', text)
    text = re.sub(r'<meta property="og:url" content="[^"]+">', f'<meta property="og:url" content="{SITE_URL}">', text)
    text = re.sub(r'<meta property="og:image" content="[^"]+">', f'<meta property="og:image" content="{social_url}">', text)
    text = re.sub(r'<meta name="twitter:image" content="[^"]+">', f'<meta name="twitter:image" content="{social_url}">', text)
    text = re.sub(r'"url": "https://world-model-benchmarks\.github\.io/[^"]*"', f'"url": "{SITE_URL}"', text)
    text = re.sub(r'"image": "https://world-model-benchmarks\.github\.io/[^"]*"', f'"image": "{social_url}"', text)

    text = replace_regex(
        text,
        r'<div class="snapshot-note">.*?</div>',
        f'<div class="snapshot-note"><span class="status-dot"></span> Latest manuscript snapshot · {TOTAL} benchmarks · {CROSS_CATEGORY} cross-category · checked {SNAPSHOT_DATE}</div>',
        count=1,
    )
    text = re.sub(r'(<strong id="stat-total">)\d+(</strong>)', rf'\g<1>{TOTAL}\2', text)
    text = re.sub(r'(<strong id="stat-cross">)\d+(</strong>)', rf'\g<1>{CROSS_CATEGORY}\2', text)
    text = re.sub(r'(<strong id="result-count">)\d+(</strong>)', rf'\g<1>{TOTAL}\2', text)
    text = re.sub(
        r'<meta property="og:description" content="[^"]+">',
        f'<meta property="og:description" content="Explore {TOTAL} world-model benchmarks through the Target–Protocol–Metrics–Data taxonomy.">',
        text,
    )
    text = re.sub(r'assets/app-v3\.js\?v=\d+', 'assets/app-v3.js?v=9', text)
    text = text.replace("66 cross-category", f"{CROSS_CATEGORY} cross-category")
    text = text.replace("August 27, 2026", SNAPSHOT_DATE)
    INDEX_PATH.write_text(text, encoding="utf-8")


def write_wrapper_js() -> None:
    content = f'''(() => {{
  const LABELS = {{
    protocol: {{ OL: "Open-Loop Evaluation", CL: "Closed-Loop Interaction" }},
    metrics: {{ P: "Prediction-Level Metrics", O: "Downstream Outcome Metrics" }},
    data: {{
      RWD: "Real-World Data Collection",
      SBG: "Simulation-Based Generation",
      SPTC: "Scenario, Prompt, and Task Curation",
      HCP: "Hybrid Construction Pipelines",
    }},
  }};

  function setTextIfChanged(element, nextText) {{
    if (element && element.textContent !== nextText) element.textContent = nextText;
  }}

  function expandCodes(text, prefix, labels) {{
    const raw = String(text || "").replace(new RegExp(`^${{prefix}}\\\\s*:?\\\\s*`, "i"), "").trim();
    const expanded = raw.split(/\\s*[·+]\\s*/).filter(Boolean).map((code) => labels[code] || code).join(" · ");
    return expanded ? `${{prefix}}: ${{expanded}}` : prefix;
  }}

  function loadLatestStyles() {{
    if (document.querySelector('link[href*="latest-schema.css"]')) return;
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = new URL("latest-schema.css?v=2", document.currentScript?.src || document.baseURI).href;
    document.head.append(link);
  }}

  function rewriteStaticPageCopy() {{
    setTextIfChanged(document.querySelector(".protocol-node .viz-caption"), "open-loop · closed-loop");
    setTextIfChanged(document.querySelector(".metrics-node .viz-caption"), "prediction-level · downstream");

    const stats = [...document.querySelectorAll(".stat-strip > div")];
    if (stats[0]) {{
      setTextIfChanged(stats[0].querySelector("strong"), "{TOTAL}");
      setTextIfChanged(stats[0].querySelector("span"), "representative benchmarks");
    }}
    if (stats[1]) {{
      setTextIfChanged(stats[1].querySelector("strong"), "{CROSS_CATEGORY}");
      setTextIfChanged(stats[1].querySelector("span"), "cross-category benchmarks");
    }}
    if (stats[3]) {{
      setTextIfChanged(stats[3].querySelector("strong"), "2 / 2");
      setTextIfChanged(stats[3].querySelector("span"), "protocol classes / metric levels");
    }}

    const snapshot = document.querySelector(".snapshot-note");
    if (snapshot) snapshot.innerHTML = '<span class="status-dot"></span> Latest manuscript snapshot · {TOTAL} benchmarks · {CROSS_CATEGORY} cross-category · checked {SNAPSHOT_DATE}';

    const benchmarkSummary = document.querySelector("#benchmarks .benchmark-heading > p");
    if (benchmarkSummary) benchmarkSummary.textContent = "Search and filter the {TOTAL} representative benchmarks coded in Figure 4 and Tables 3–9 of the latest manuscript.";

    const resultCount = document.querySelector("#result-count");
    if (resultCount && resultCount.textContent !== "{TOTAL}") resultCount.textContent = "{TOTAL}";
    const chart = document.querySelector("#timeline-chart");
    if (chart) chart.setAttribute("aria-label", "Unique benchmark totals by release window");
    const clearPeriod = document.querySelector("#clear-year");
    if (clearPeriod) setTextIfChanged(clearPeriod, "Clear period filter");
  }}

  function updateCard(card) {{
    const pills = [...card.querySelectorAll(".card-meta .meta-pill")];
    if (pills[1]) setTextIfChanged(pills[1], expandCodes(pills[1].textContent, "Protocol", LABELS.protocol));
    if (pills[2]) setTextIfChanged(pills[2], expandCodes(pills[2].textContent, "Metrics", LABELS.metrics));
    if (pills[3]) setTextIfChanged(pills[3], expandCodes(pills[3].textContent, "Data", LABELS.data));

    const footerLabel = card.querySelector(".card-footer small");
    if (footerLabel) {{
      const cleaned = footerLabel.textContent.replace(/^Ref\\.\\s*\\[\\d+\\]\\s*·\\s*/i, "").trim();
      if (cleaned) setTextIfChanged(footerLabel, cleaned);
      else footerLabel.remove();
    }}
  }}

  function updateCards(root = document) {{
    root.querySelectorAll(".benchmark-card").forEach(updateCard);
  }}

  async function loadCanonicalExplorer() {{
    const sourceUrl = new URL("app-v3-core.js?v=11", document.currentScript?.src || document.baseURI);
    const response = await fetch(sourceUrl, {{ cache: "no-store" }});
    if (!response.ok) throw new Error(`HTTP ${{response.status}} while loading explorer core`);
    new Function(await response.text())();
  }}

  loadLatestStyles();
  rewriteStaticPageCopy();
  const grid = document.querySelector("#benchmark-grid");
  if (grid) new MutationObserver(() => updateCards(grid)).observe(grid, {{ childList: true, subtree: true }});

  loadCanonicalExplorer().then(() => {{
    rewriteStaticPageCopy();
    updateCards();
  }}).catch((error) => {{
    console.error(error);
    if (grid) grid.innerHTML = `<div class="empty-state"><h3>Benchmark data could not be loaded.</h3><p>${{String(error.message || error)}}</p></div>`;
  }});
}})();
'''
    WRAPPER_JS_PATH.write_text(content, encoding="utf-8")


def update_core_js() -> None:
    text = CORE_JS_PATH.read_text(encoding="utf-8")
    text = re.sub(r'const PROTOCOLS = \[[^\]]*\];', 'const PROTOCOLS = ["OL", "CL"];', text, count=1)
    text = re.sub(r'const METRICS = \[[^\]]*\];', 'const METRICS = ["P", "O"];', text, count=1)
    text = re.sub(
        r'link\.download = "world-model-benchmarks-[^"]+\.json";',
        'link.download = "world-model-benchmarks-2026-08-31.json";',
        text,
        count=1,
    )
    if '"CR"' in text or 'const METRICS = ["A", "J", "O"]' in text:
        raise RuntimeError("Legacy protocol or metric taxonomy remains in app-v3-core.js")
    CORE_JS_PATH.write_text(text, encoding="utf-8")


def write_app_loader() -> None:
    APP_JS_PATH.write_text(
        '''(() => {\n  const script = document.createElement("script");\n  script.src = "assets/app-v3.js?v=9";\n  script.defer = true;\n  script.onerror = () => console.error("Could not load app-v3.js");\n  document.head.append(script);\n})();\n''',
        encoding="utf-8",
    )


def update_site_support_files() -> None:
    (ROOT / "docs" / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n",
        encoding="utf-8",
    )
    (ROOT / "docs" / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url>\n'
        f'    <loc>{SITE_URL}</loc>\n'
        '    <changefreq>monthly</changefreq>\n'
        '    <priority>1.0</priority>\n'
        '  </url>\n'
        '</urlset>\n',
        encoding="utf-8",
    )
    (ROOT / "docs" / "deployment-status.txt").write_text(
        f"GitHub Pages deployment trigger\nUpdated: {SNAPSHOT_ISO_DATE}\n",
        encoding="utf-8",
    )
    for filename in LEGACY_JS_FILES:
        (ASSETS / filename).unlink(missing_ok=True)


def update_website(manifest: dict) -> None:
    update_index()
    write_wrapper_js()
    update_core_js()
    write_app_loader()
    update_site_support_files()


def validate_release_windows(manifest: dict) -> None:
    bins = manifest["timelineBins"]
    expected = {"2018–2021": 7, "2022–2023": 6, "2024": 9, "2025": 31, "2026": 53}
    counts = {
        bin_info["label"]: sum(row[1] in bin_info["years"] for row in manifest["records"].values())
        for bin_info in bins
    }
    if counts != expected:
        raise RuntimeError(f"Release-window counts differ from Figure 2: {counts} != {expected}")


def main() -> None:
    manifest = update_manifest()
    validate_release_windows(manifest)
    corpus = rewrite_shards(manifest)
    generate_readme(manifest, corpus)
    write_metadata(manifest)
    update_website(manifest)
    print(
        f"Generated PDF-aligned repository and website data for {TOTAL} benchmarks "
        f"({CROSS_CATEGORY} cross-category; {SNAPSHOT_DATE}).\n"
        f"Classification fingerprint: {manifest['classificationFingerprint']}"
    )


if __name__ == "__main__":
    main()
