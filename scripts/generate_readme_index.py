#!/usr/bin/env python3
"""Generate repository and website artifacts for the latest survey PDF snapshot.

The compact manifest in ``docs/assets/benchmarks.json`` is the canonical source
of benchmark coding.  This script validates that source, rebuilds the website
shards and metadata, and regenerates the README while preserving verified paper,
code, and project-page links already present in the repository.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json
import math
import re
from target_scoped_coding import evaluation_tracks, validate_scoped, readme_coding, scoped_metadata, coverage_html

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
MANIFEST_PATH = ASSETS / "benchmarks.json"
METADATA_PATH = ASSETS / "metadata.json"
README_PATH = ROOT / "Readme.md"
INDEX_PATH = ROOT / "docs" / "index.html"
WRAPPER_JS_PATH = ASSETS / "app-v3.js"
APP_JS_PATH = ASSETS / "app.js"
SOCIAL_PATH = ASSETS / "social-preview.svg"

TOTAL = 130
CROSS_CATEGORY = 108
SCHEMA_VERSION = 12
SNAPSHOT_VERSION = 'October 18, 2026 corpus; joint task-level coding finalized November 8, 2026'
SNAPSHOT_DATE = 'October 18, 2026'
SNAPSHOT_ISO_DATE = '2026-10-18'
SOURCE_PDF_SHA256 = '950eb41ec9e26e9181502e3d2e87837daf3d783301db5f546e45d3d83fdc369c'
SUPPLEMENTARY_PDF_SHA256 = '42180ccbb41a01508d6a8bb79059e414c0dd8d99dd8d79412cce77b1d26cdd8d'
EXPECTED_FINGERPRINT = 'af6a8bc9e9bca01c2b35e2cbf65c2ef1104739fa3a38061237f55da7923ac4c3'
SITE_URL = "https://world-model-benchmarks.github.io/World-Model-Benchmarks/"

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
EXPECTED_TARGET_COUNTS = {'T1': 63, 'T2': 76, 'T3': 34, 'T4': 92, 'T5': 39, 'T6': 74, 'T7': 15}
EXPECTED_SUBTARGET_COUNTS = {'S1': 53, 'S2': 53, 'S3': 31, 'S4': 12, 'S5': 56, 'S6': 22, 'S7': 2, 'S8': 2, 'S9': 14, 'S10': 2}
EXPECTED_RELEASE_WINDOWS = {'2018–2021': 6, '2022–2023': 4, '2024': 10, '2025': 30, '2026': 80}
REMOVED_FROM_FORMAL_CORPUS = {"CATER", "NExT-QA", "IntentQA", "VCRBench"}

# Preserve the existing index order; append verified additions within each section.
SECTION_ORDER = {
    "S1": [
        "ChronoMagic-Bench", "WorldScore", "VMBench", "EWMBench", "WorldArena",
        "GameWorld Score", "WorldMark", "4DWorldBench", "WorldLens", "DrivingGen",
        "PEDRA", "Gen-ViRe", "iWorld-Bench", "WoW-World-Eval", "RBench",
        "PAI-Bench", "EZS-Bench", "WorldRoamBench", "MemoBench", "RoboTrustBench",
        "WorldExam", "SurgWMBench", "H2R-Bench", "PlayWorld", "XEWorld",
        "HarnessEval-W", "WorldEcho", "ACWM-Phys", "HTEWorld", "RigidBench",
        "MagicBench", "MIND", "MoveBench", "Omni-WorldBench", "OSCBench",
        "T2VWorldBench", "WMBench", "WorldModelBench", "WorldSimBench", "Apple-π",
    ],
    "S2": [
        "ChronoMagic-Bench", "VMBench", "TC-Bench", "WorldScore", "4DWorldBench",
        "GameWorld Score", "WorldMark", "WBench", "EWMBench", "WorldArena",
        "WorldArena 2.0", "WorldLens", "DrivingGen", "PEDRA", "Gen-ViRe",
        "WoW-World-Eval", "RBench", "PAI-Bench", "EZS-Bench", "WorldRoamBench",
        "CrashTwin", "MemoBench", "RoboTrustBench", "WorldExam", "SurgWMBench",
        "H2R-Bench", "PlayWorld", "XEWorld", "HarnessEval-W", "WorldEcho",
        "EVA-Bench", "HTEWorld", "MagicBench", "MoveBench", "Omni-WorldBench",
        "T2VWorldBench", "WMBench", "WorldModelBench", "WR-Arena", "Apple-π",
    ],
    "T2": [
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
    ],
    "T3": [
        "WorldPrediction", "SmallWorlds", "WR-Arena", "WorldMark", "MBench", "MIND",
        "WBench", "WorldOlympiad", "HTEWorld", "RoboWM-Bench", "iWorld-Bench",
        "WoW-World-Eval", "RBench", "AutumnBench", "ContactWorld", "WorldRoamBench",
        "ScratchWorld", "MemoBench", "Chess-World-Model", "PlayWorld", "HarnessEval-W",
        "LoopNav", "ExPhy", "WMBench",
    ],
    "T4": [
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
    ],
    "S3": [
        "CLEVRER", "Physion", "Causal-VidQA", "CRAFT", "ACQUIRED", "MMWorld",
        "Physics-IQ", "WorldPrediction", "T2VWorldBench", "VACT", "CausalVQA",
        "WR-Arena", "HOCA-Bench", "What-If World", "CRONOS", "WoW-World-Eval",
        "RBench", "MVP", "PAI-Bench", "RoboTrustBench", "MiraBench", "PlayWorld",
        "HarnessEval-W", "ContPhy", "PhysicsMind", "WorldExam",
    ],
    "S4": [
        "CLEVRER", "CRAFT", "CoPhy", "ComPhy", "ContPhy", "CausalSpatial", "AutumnBench",
        "ScratchWorld", "ReactSim-Bench", "WorldSimProbe",
    ],
    "S5": [
        "TC-Bench", "StoryEval", "VideoPhy", "VideoPhy-2", "PhyGenBench",
        "PhyWorldBench", "OSCBench", "MoveBench", "MagicBench", "WorldScore",
        "4DWorldBench", "DrivingGen", "ACT-Bench", "What-If World", "Omni-WorldBench",
        "DreamGen Bench", "WorldModelBench", "VBench-2.0", "WoW-World-Eval", "RBench",
        "PAI-Bench", "EZS-Bench", "KineBench", "ScratchWorld", "MemoBench",
        "RoboTrustBench", "MiraBench", "Chess-World-Model", "WorldExam", "H2R-Bench",
        "WorldSimProbe", "XEWorld", "HarnessEval-W", "WorldEcho", "EWMBench",
        "GameWorld Score", "MBench", "STEVO-Bench", "VACT", "WorldArena",
    ],
    "S6": [
        "WorldMark", "WR-Arena", "WorldSimBench", "WBench", "iWorld-Bench", "MIND",
        "ACWM-Phys", "RoboWM-Bench", "WorldArena 2.0", "WorldOlympiad",
        "WorldRoamBench", "ReactSim-Bench", "PlayWorld", "HTEWorld", "WMBench",
    ],
    "S7": ["WorldArena", "WorldArena 2.0"],
    "S8": ["WorldArena", "WMBench"],
    "S9": [
        "WorldArena", "WorldArena 2.0", "World-in-World", "EVA-Bench", "WorldLens",
        "RoboWM-Bench", "WorldSimBench", "WR-Arena", "WoW-World-Eval", "AutumnBench",
        "ContactWorld", "KineBench",
    ],
    "S10": ["WorldArena 2.0"],
}

for _section, _names in {'S1': ['WorldReasonBench', 'TailOR', 'StateBench', 'VWG-Bench', 'HappyWorld-Bench', 'TriWorldBench', 'WROP', 'VehDyn', 'PROWBench', 'WorldOracle', 'CausalCascade', 'Orbia', 'WorldMemBench'], 'S2': ['WorldReasonBench', 'TailOR', 'VWG-Bench', 'HappyWorld-Bench', 'TriWorldBench', 'WROP', 'VehDyn', 'CoDrive-Bench', 'PROWBench', 'AffectWorld', 'Orbia', 'R2M-Bench', 'WRBench'], 'T2': ['ICAT', 'WorldReasonBench', 'TailOR', 'StateBench', 'VWG-Bench', 'HappyWorld-Bench', 'TriWorldBench', 'VehDyn', 'CoDrive-Bench', 'OPIS', 'Ego2Act', 'PROWBench', 'WorldOracle', 'AffectWorld', 'CausalCascade', 'WorldCast', 'Orbia', 'MultiWorldBench', 'R2M-Bench', 'WRBench', 'LiveBench'], 'T3': ['StateBench', 'HappyWorld-Bench', 'WROP', 'WorldOracle', 'Orbia', 'WorldMemBench', 'MultiWorldBench', 'R2M-Bench', 'WRBench', 'LiveBench'], 'T4': ['ICAT', 'WorldReasonBench', 'TailOR', 'Principia', 'VWG-Bench', 'HappyWorld-Bench', 'TriWorldBench', 'WROP', 'VehDyn', 'Ego2Act', 'PhysicsLENS', 'Last Exam in Physics', 'CausalCascade', 'WorldCast', 'WorldMemBench'], 'S3': ['ICAT', 'HappyWorld-Bench', 'Ego2Act', 'AffectWorld', 'CausalCascade'], 'S4': ['VehDyn', 'CausalCascade'], 'S5': ['ICAT', 'TailOR', 'StateBench', 'VWG-Bench', 'HappyWorld-Bench', 'WROP', 'VehDyn', 'CoDrive-Bench', 'Ego2Act', 'PhysicsLENS', 'PROWBench', 'WorldCast', 'Orbia', 'WorldMemBench', 'WRBench', 'LiveBench'], 'S6': ['HappyWorld-Bench', 'TriWorldBench', 'WorldOracle', 'Orbia', 'WorldMemBench', 'MultiWorldBench', 'WRBench'], 'S7': [], 'S8': [], 'S9': ['Compositional continual learning', 'MapShift'], 'S10': ['Compositional continual learning']}.items():
    SECTION_ORDER[_section].extend(_names)

ROW_PATTERN = re.compile(
    r"^\| \[\*\*(?P<label>.+?)\*\*\]\((?P<paper>[^)]+)\) \| "
    r"(?P<year>\d{4}) \| (?P<venue>.*?) \| (?P<code>.*?) \| (?P<project>.*?)(?: \| (?:OL|CL|OL\+CL) \| (?:P|O|P\+O))? \|$",
    re.MULTILINE,
)


def split_codes(value: str) -> list[str]:
    return [part for part in str(value or "").split("+") if part]


def fingerprint(records: dict[str, list]) -> str:
    rows = [
        f"{name}|" + "|".join(str(value) for value in row[:8])
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_manifest() -> dict:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    records = manifest["records"]
    require(len(records) == TOTAL == manifest.get("total"), "The canonical corpus must contain 130 records")
    require(manifest.get("crossCategory") == CROSS_CATEGORY, "Cross-category total must be 108")
    require(manifest.get("schemaVersion") == SCHEMA_VERSION, f"Schema version must be {SCHEMA_VERSION}")
    require(manifest.get("version") == SNAPSHOT_VERSION, "Snapshot version is stale")
    require(manifest.get("snapshotDate") == SNAPSHOT_ISO_DATE, "Snapshot date is stale")
    require(manifest.get("sourcePdfSha256") == SOURCE_PDF_SHA256, "Source-PDF digest is stale")
    require(not (set(records) & REMOVED_FROM_FORMAL_CORPUS), "A benchmark removed by the latest PDF remains in the corpus")

    target_counts = Counter(code for row in records.values() for code in split_codes(row[6]))
    subtarget_counts = Counter(code for row in records.values() for code in split_codes(row[7]))
    cross_count = sum(len(split_codes(row[6])) > 1 for row in records.values())
    require(dict(target_counts) == EXPECTED_TARGET_COUNTS, f"Top-level target counts are wrong: {target_counts}")
    require(dict(subtarget_counts) == EXPECTED_SUBTARGET_COUNTS, f"Subtarget counts are wrong: {subtarget_counts}")
    require(cross_count == CROSS_CATEGORY, f"Computed cross-category count is {cross_count}")
    require(fingerprint(records) == EXPECTED_FINGERPRINT, "Canonical record fingerprint differs from the latest PDF transcription")
    require(manifest.get("classificationFingerprint") == EXPECTED_FINGERPRINT, "Manifest fingerprint is stale")
    require(manifest.get("recordFingerprint") == EXPECTED_FINGERPRINT, "Manifest record fingerprint is stale")

    wr = records.get("WR-Arena")
    require(wr is not None and wr[3] == "OL+CL" and wr[4] == "P+O", "WR-Arena must be OL+CL / P+O")

    windows = {
        item["label"]: sum(row[1] in item["years"] for row in records.values())
        for item in manifest["timelineBins"]
    }
    require(windows == EXPECTED_RELEASE_WINDOWS, f"Release-window counts are wrong: {windows}")
    validate_scoped(manifest)
    return manifest


def load_shard_metadata() -> dict[str, dict]:
    return json.loads((ROOT / "scripts/benchmark_metadata_20261108.json").read_text(encoding="utf-8"))


def rebuild_shards(manifest: dict) -> list[dict]:
    metadata = load_shard_metadata()
    records = manifest["records"]
    require(set(metadata) == set(records), "Existing shard and manifest benchmark sets differ")
    corpus: list[dict] = []
    for name, row in sorted(records.items(), key=lambda pair: (pair[1][0], pair[0])):
        item = metadata[name]
        item.update({
            "shortName": name,
            "ref": row[0],
            "year": row[1],
            "releaseYear": row[1],
            "domains": split_codes(row[2]),
            "protocols": split_codes(row[3]),
            "metrics": split_codes(row[4]),
            "evaluationData": split_codes(row[5]),
            "targets": [manifest["targetLabels"][code] for code in split_codes(row[6])],
            "subtargets": [manifest["subtargetLabels"][code] for code in split_codes(row[7])],
            "crossCategory": len(split_codes(row[6])) > 1,
        })
        item.update(manifest.get("publicationMetadata", {}).get(name, {}))
        for legacy_field in ("evidence", "dataConstruction", "realWorldExecution"):
            item.pop(legacy_field, None)
        item["evaluationTracks"] = evaluation_tracks(manifest, name)
        corpus.append(item)

    chunk_size = math.ceil(TOTAL / 4)
    chunks = [corpus[start:start + chunk_size] for start in range(0, TOTAL, chunk_size)]
    require([len(chunk) for chunk in chunks] == [33, 33, 33, 31], "Unexpected shard sizes")
    for index, chunk in enumerate(chunks, start=1):
        (ASSETS / f"benchmarks-{index}.json").write_text(
            json.dumps(chunk, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return corpus


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

    def row(name: str, section: str) -> str:
        item = by_name[name]
        old = cached.get(name, {})
        paper = old.get("paper") or item.get("paperUrl")
        if not paper:
            query = re.sub(r"\s+", "+", item.get("title") or name)
            paper = f"https://scholar.google.com/scholar?q={query}"
        venue = item.get("venue") or old.get("venue") or "arXiv"
        if item.get("publicationYear") and str(item["publicationYear"]) not in venue:
            venue = f"{venue} {item['publicationYear']}"
        code = old.get("code") or (f"[{item.get('codeLabel', 'Code')}]({item['codeUrl']})" if item.get("codeUrl") else "-")
        project = old.get("project") or (f"[{item.get('projectLabel', 'Project')}]({item['projectUrl']})" if item.get("projectUrl") else "-")
        marker = " △" if item["crossCategory"] else ""
        protocol, metrics = readme_coding(manifest, name, section)
        return f"| [**{name}{marker}**]({paper}) | {item['year']} | {venue} | {code} | {project} | {protocol} | {metrics} |"

    def table(names: list[str], section: str) -> list[str]:
        require(all(name in by_name for name in names), "README section contains a benchmark absent from the corpus")
        return [
            "| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |",
            "|:--|:--:|:--:|:--:|:--:|:--:|:--:|",
            *[row(name, section) for name in names],
        ]

    lines = [
        "# A Survey of World Model Benchmarks",
        "",
        f"[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)]({SITE_URL}) "
        f"[![Benchmarks](https://img.shields.io/badge/Benchmarks-{TOTAL}-2f8f63)]({SITE_URL}#benchmarks)",
        "",
        "This repository accompanies **A Survey of World Model Benchmarks**. "
        f"The latest manuscript covers **{TOTAL} representative benchmarks** released from **2018–2026**; "
        f"**{CROSS_CATEGORY}** span more than one evaluation-target category. "
        f"The corpus was last checked on {SNAPSHOT_DATE}.",
        "",
        "The classification below follows the survey taxonomy and the task-level evidence summarized in Supplementary Tables S1–S7. "
        "Rows are intentionally repeated when a benchmark belongs to multiple evaluation targets or sub-targets. "
        "`△` marks a benchmark assigned to more than one top-level evaluation target.",
        "",
        "Each table is a literature index with **Article**, **Release Year**, **Venue**, **Code**, and **Project Page**. "
        "Release Year follows the final manuscript's corpus coding, not the formal publication year; the latter is shown separately with the venue where recorded. `-` means that no verified public link is currently recorded.",
        "",
        "Protocol and Metrics are coded for the target or role of each section, not inherited from other tracks. The machine-readable manifest additionally preserves 808 fully classified task-level Protocol–Metrics–Data records and 482 distinct display combinations so joint filters never form unsupported cross-products.",
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

    sections = [
        ("Visual and Temporal Quality", "Visual Quality", "S1"),
        (None, "Temporal Quality", "S2"),
        ("Spatial and State Consistency", None, "T2"),
        ("Long-Horizon Memory and State Persistence", None, "T3"),
        ("Physical Plausibility", None, "T4"),
        ("Causal and Counterfactual Reasoning", "Observation-Grounded Evaluation", "S3"),
        (None, "Intervention-Grounded Evaluation", "S4"),
        ("Control Fidelity and Interactive Dynamics", "Pre-specified Control Fidelity", "S5"),
        (None, "Interactive Action Fidelity", "S6"),
        ("Functional Utility", "World Model as Data Engine", "S7"),
        (None, "World Model as Policy Evaluator", "S8"),
        (None, "World Model as Planner", "S9"),
        (None, "World Model as Interactive Training Environment", "S10"),
    ]
    for h2, h3, code in sections:
        if h2:
            lines.extend([f"## {h2}", ""])
        if h3:
            lines.extend([f"### {h3}", ""])
        lines.extend(table(SECTION_ORDER[code], code))
        lines.append("")

    lines.extend([
        "## Machine-readable data",
        "",
        "- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical taxonomy manifest and compact record coding",
        "- [`docs/assets/benchmarks-1.json`](docs/assets/benchmarks-1.json)–[`benchmarks-4.json`](docs/assets/benchmarks-4.json): normalized benchmark records used by the explorer",
        "- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels, counts, and release-window definitions",
        "- [`scripts/task_records_20261108.json`](scripts/task_records_20261108.json): 808 target-task records plus two explicitly excluded auxiliary records transcribed from Supplementary Tables S1–S7",
        f"- [Interactive project page]({SITE_URL})",
        "",
    ])
    README_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_metadata(manifest: dict) -> None:
    metadata = {
        "title": manifest["title"],
        "schemaVersion": SCHEMA_VERSION,
        "version": SNAPSHOT_VERSION,
        "snapshotDate": SNAPSHOT_ISO_DATE,
        "sourcePdfSha256": SOURCE_PDF_SHA256,
        "sourceSupplementaryPdfSha256": SUPPLEMENTARY_PDF_SHA256,
        "sourceArchive": manifest["sourceArchive"],
        "sourceArchiveSha256": manifest["sourceArchiveSha256"],
        "codingChecklist": manifest["codingChecklist"],
        "codingChecklistSha256": manifest["codingChecklistSha256"],
        "framework": manifest["framework"],
        "total": TOTAL,
        "crossCategory": CROSS_CATEGORY,
        "protocolLabels": manifest["protocolLabels"],
        "metricLabels": manifest["metricLabels"],
        "dataLabels": manifest["dataLabels"],
        "timelineBins": manifest["timelineBins"],
        "releaseWindowCounts": EXPECTED_RELEASE_WINDOWS,
        "targetCounts": {TARGET_LABELS[code]: EXPECTED_TARGET_COUNTS[code] for code in TARGET_LABELS},
        "subtargetCounts": {SUBTARGET_LABELS[code]: EXPECTED_SUBTARGET_COUNTS[code] for code in SUBTARGET_LABELS},
        "classificationFingerprint": EXPECTED_FINGERPRINT,
        "recordFingerprint": EXPECTED_FINGERPRINT,
        "evaluationRecordFingerprint": manifest["evaluationRecordFingerprint"],
        "taskRecordFingerprint": manifest["taskRecordFingerprint"],
        "taskRecordCounts": manifest["taskRecordCounts"],
        "fingerprintFields": manifest["fingerprintFields"],
        "dimensions": 4,
        "yearMin": 2018,
        "yearMax": 2026,
        "targets": list(TARGET_LABELS.values()),
    }
    metadata.update({key: manifest[key] for key in ("yearBasis", "releaseYearRevision", "publicationMetadata", "sourceNote")})
    metadata.update(scoped_metadata(manifest))
    METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_website_copy(manifest: dict) -> None:
    index = INDEX_PATH.read_text(encoding="utf-8").replace("August 31, 2026", SNAPSHOT_DATE).replace("September 15, 2026", "November 8, 2026")
    index = re.sub(r"Explore \d+ world-model benchmarks", f"Explore {TOTAL} world-model benchmarks", index)
    index = re.sub(r"\d+ benchmarks · \d+ cross-category", f"{TOTAL} benchmarks · {CROSS_CATEGORY} cross-category", index)
    index = re.sub(r'(<strong id="stat-total">)\d+(</strong>)', rf"\g<1>{TOTAL}\2", index)
    index = re.sub(r'(<strong id="stat-cross">)\d+(</strong>)', rf"\g<1>{CROSS_CATEGORY}\2", index)
    index = re.sub(r'(<strong id="result-count">)\d+(</strong>)', rf"\g<1>{TOTAL}\2", index)
    index = re.sub(r"\d+ cumulative benchmarks by 2023", "10 cumulative benchmarks by 2023", index)
    index = re.sub(r"\d+ new benchmarks in 2025", "30 new benchmarks in 2025", index)
    index = re.sub(r"\d+ new benchmarks in 2024", "10 new benchmarks in 2024", index)
    index = re.sub(r"\d+ new benchmarks in 2026", "80 new benchmarks in 2026", index)
    index = re.sub(r"raising the cumulative corpus to <strong>\d+</strong>", "raising the cumulative corpus to <strong>50</strong>", index)
    index = re.sub(r"bringing the corpus to <strong>\d+</strong>", "bringing the corpus to <strong>130</strong>", index)
    index = index.replace("Supplementary Figure S1 and Tables S1–S7", "Supplementary Tables S1–S7")
    index = re.sub(r"Search and filter the \d+ representative benchmarks", "Search and filter the 130 representative benchmarks", index)
    index = re.sub(r"assets/app-v3\.js\?v=\d+", "assets/app-v3.js?v=2026110801", index)
    index = re.sub(r"<!-- TARGET-SCOPED COVERAGE START -->.*?<!-- TARGET-SCOPED COVERAGE END -->", "<!-- TARGET-SCOPED COVERAGE START -->" + coverage_html(manifest) + "<!-- TARGET-SCOPED COVERAGE END -->", index, flags=re.S)
    INDEX_PATH.write_text(index, encoding="utf-8")

    wrapper = WRAPPER_JS_PATH.read_text(encoding="utf-8").replace("August 31, 2026", SNAPSHOT_DATE).replace("September 15, 2026", "November 8, 2026")
    wrapper = re.sub(r'const sourceUrl = new URL\("app-v3-core\.js\?v=\d+"', 'const sourceUrl = new URL("app-v3-core.js?v=2026110801"', wrapper)
    wrapper = re.sub(r'(?:Latest|Final) manuscript snapshot · \d+ benchmarks · \d+ cross-category', f'Final manuscript snapshot · {TOTAL} benchmarks · {CROSS_CATEGORY} cross-category', wrapper)
    wrapper = re.sub(r'the \d+ representative benchmarks', f'the {TOTAL} representative benchmarks', wrapper)
    # Only the first stat-strip strong literal is the total; avoid replacing years or unrelated values.
    wrapper = re.sub(r'(setTextIfChanged\(stats\[0\]\.querySelector\("strong"\), ")\d+("\);)', rf'\g<1>{TOTAL}\2', wrapper)
    wrapper = re.sub(r'(setTextIfChanged\(stats\[1\]\.querySelector\("strong"\), ")\d+("\);)', rf'\g<1>{CROSS_CATEGORY}\2', wrapper)
    wrapper = re.sub(r'(resultCount\.textContent !== ")\d+("\))', rf'\g<1>{TOTAL}\2', wrapper)
    wrapper = re.sub(r'(resultCount\.textContent = ")\d+(";)', rf'\g<1>{TOTAL}\2', wrapper)
    WRAPPER_JS_PATH.write_text(wrapper, encoding="utf-8")

    app = APP_JS_PATH.read_text(encoding="utf-8")
    app = re.sub(r"app-v3\.js\?v=\d+", "app-v3.js?v=2026110801", app)
    APP_JS_PATH.write_text(app, encoding="utf-8")

    social = SOCIAL_PATH.read_text(encoding="utf-8")
    social = re.sub(r">\d+</text>", f">{TOTAL}</text>", social, count=1)
    SOCIAL_PATH.write_text(social, encoding="utf-8")

    (ROOT / "docs" / "deployment-status.txt").write_text(
        "Local preview snapshot\n"
        "Updated: 2026-11-08\n"
        f"Corpus: {TOTAL} benchmarks / {CROSS_CATEGORY} cross-category\n"
        f"Fingerprint: {EXPECTED_FINGERPRINT}\n",
        encoding="utf-8",
    )


def main() -> None:
    manifest = load_manifest()
    corpus = rebuild_shards(manifest)
    generate_readme(manifest, corpus)
    write_metadata(manifest)
    update_website_copy(manifest)
    print(
        f"Generated the latest-PDF snapshot: {TOTAL} benchmarks, {CROSS_CATEGORY} cross-category; "
        f"fingerprint {EXPECTED_FINGERPRINT}."
    )


if __name__ == "__main__":
    main()
