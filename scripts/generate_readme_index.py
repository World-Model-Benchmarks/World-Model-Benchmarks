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

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
MANIFEST_PATH = ASSETS / "benchmarks.json"
METADATA_PATH = ASSETS / "metadata.json"
README_PATH = ROOT / "Readme.md"
INDEX_PATH = ROOT / "docs" / "index.html"
WRAPPER_JS_PATH = ASSETS / "app-v3.js"
APP_JS_PATH = ASSETS / "app.js"
SOCIAL_PATH = ASSETS / "social-preview.svg"

TOTAL = 102
CROSS_CATEGORY = 85
SCHEMA_VERSION = 9
SNAPSHOT_VERSION = "August 31, 2026 manuscript snapshot"
SNAPSHOT_DATE = "August 31, 2026"
SNAPSHOT_ISO_DATE = "2026-08-31"
SOURCE_PDF_SHA256 = "c96efe634f70b1297e281e36786dc6a5fedd3b747bf4fc57ad58583c69a50dad"
EXPECTED_FINGERPRINT = "e30cf7f9b7bf39cb03baa6b9cddcbeb593b5821e1ba85a82fddff0787c7e4935"
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
EXPECTED_TARGET_COUNTS = {"T1": 46, "T2": 55, "T3": 24, "T4": 77, "T5": 33, "T6": 55, "T7": 13}
EXPECTED_SUBTARGET_COUNTS = {"S1": 40, "S2": 40, "S3": 26, "S4": 9, "S5": 40, "S6": 15, "S7": 2, "S8": 2, "S9": 12, "S10": 1}
EXPECTED_RELEASE_WINDOWS = {"2018–2021": 5, "2022–2023": 5, "2024": 9, "2025": 30, "2026": 53}
REMOVED_FROM_FORMAL_CORPUS = {"CATER", "NExT-QA", "IntentQA", "VCRBench"}

# Figure 4 order in the latest PDF.  The four removed observation-grounded
# datasets are intentionally absent from S3.
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
        "CLEVRER", "CRAFT", "CoPhy", "ComPhy", "CausalSpatial", "AutumnBench",
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

ROW_PATTERN = re.compile(
    r"^\| \[\*\*(?P<label>.+?)\*\*\]\((?P<paper>[^)]+)\) \| "
    r"(?P<year>\d{4}) \| (?P<venue>.*?) \| (?P<code>.*?) \| (?P<project>.*?) \|$",
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
    require(len(records) == TOTAL == manifest.get("total"), "The canonical corpus must contain 102 records")
    require(manifest.get("crossCategory") == CROSS_CATEGORY, "Cross-category total must be 85")
    require(manifest.get("schemaVersion") == SCHEMA_VERSION, "Schema version must be 9")
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
    return manifest


def load_shard_metadata() -> dict[str, dict]:
    metadata: dict[str, dict] = {}
    for index in range(1, 5):
        path = ASSETS / f"benchmarks-{index}.json"
        for item in json.loads(path.read_text(encoding="utf-8")):
            metadata[item["shortName"]] = dict(item)
    return metadata


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
            "domains": split_codes(row[2]),
            "protocols": split_codes(row[3]),
            "metrics": split_codes(row[4]),
            "evaluationData": split_codes(row[5]),
            "targets": [manifest["targetLabels"][code] for code in split_codes(row[6])],
            "subtargets": [manifest["subtargetLabels"][code] for code in split_codes(row[7])],
            "crossCategory": len(split_codes(row[6])) > 1,
        })
        for legacy_field in ("evidence", "dataConstruction", "realWorldExecution"):
            item.pop(legacy_field, None)
        corpus.append(item)

    chunk_size = math.ceil(TOTAL / 4)
    chunks = [corpus[start:start + chunk_size] for start in range(0, TOTAL, chunk_size)]
    require([len(chunk) for chunk in chunks] == [26, 26, 26, 24], "Unexpected shard sizes")
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

    def row(name: str) -> str:
        item = by_name[name]
        old = cached.get(name, {})
        paper = old.get("paper") or item.get("paperUrl")
        if not paper:
            query = re.sub(r"\s+", "+", item.get("title") or name)
            paper = f"https://scholar.google.com/scholar?q={query}"
        venue = item.get("venue") or old.get("venue") or "arXiv"
        code = old.get("code", "-")
        project = old.get("project", "-")
        marker = " △" if item["crossCategory"] else ""
        return f"| [**{name}{marker}**]({paper}) | {item['year']} | {venue} | {code} | {project} |"

    def table(names: list[str]) -> list[str]:
        require(all(name in by_name for name in names), "README section contains a benchmark absent from the corpus")
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
        lines.extend(table(SECTION_ORDER[code]))
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
        "version": SNAPSHOT_VERSION,
        "snapshotDate": SNAPSHOT_ISO_DATE,
        "sourcePdfSha256": SOURCE_PDF_SHA256,
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
        "fingerprintFields": manifest["fingerprintFields"],
        "dimensions": 4,
        "yearMin": 2018,
        "yearMax": 2026,
        "targets": list(TARGET_LABELS.values()),
    }
    METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_website_copy() -> None:
    index = INDEX_PATH.read_text(encoding="utf-8")
    index = re.sub(r"Explore \d+ world-model benchmarks", f"Explore {TOTAL} world-model benchmarks", index)
    index = re.sub(r"\d+ benchmarks · \d+ cross-category", f"{TOTAL} benchmarks · {CROSS_CATEGORY} cross-category", index)
    index = re.sub(r'(<strong id="stat-total">)\d+(</strong>)', rf"\g<1>{TOTAL}\2", index)
    index = re.sub(r'(<strong id="stat-cross">)\d+(</strong>)', rf"\g<1>{CROSS_CATEGORY}\2", index)
    index = re.sub(r'(<strong id="result-count">)\d+(</strong>)', rf"\g<1>{TOTAL}\2", index)
    index = re.sub(r"\d+ cumulative benchmarks by 2023", "10 cumulative benchmarks by 2023", index)
    index = re.sub(r"\d+ new benchmarks in 2025", "30 new benchmarks in 2025", index)
    index = re.sub(r"raising the cumulative corpus to <strong>\d+</strong>", "raising the cumulative corpus to <strong>49</strong>", index)
    index = re.sub(r"bringing the corpus to <strong>\d+</strong>", "bringing the corpus to <strong>102</strong>", index)
    index = re.sub(r"Search and filter the \d+ representative benchmarks", "Search and filter the 102 representative benchmarks", index)
    index = re.sub(r"assets/app-v3\.js\?v=\d+", "assets/app-v3.js?v=10", index)
    INDEX_PATH.write_text(index, encoding="utf-8")

    wrapper = WRAPPER_JS_PATH.read_text(encoding="utf-8")
    wrapper = re.sub(r'const sourceUrl = new URL\("app-v3-core\.js\?v=\d+"', 'const sourceUrl = new URL("app-v3-core.js?v=12"', wrapper)
    wrapper = re.sub(r'Latest manuscript snapshot · \d+ benchmarks · \d+ cross-category', f'Latest manuscript snapshot · {TOTAL} benchmarks · {CROSS_CATEGORY} cross-category', wrapper)
    wrapper = re.sub(r'the \d+ representative benchmarks', f'the {TOTAL} representative benchmarks', wrapper)
    # Only the first stat-strip strong literal is the total; avoid replacing years or unrelated values.
    wrapper = re.sub(r'(setTextIfChanged\(stats\[0\]\.querySelector\("strong"\), ")\d+("\);)', rf'\g<1>{TOTAL}\2', wrapper)
    wrapper = re.sub(r'(setTextIfChanged\(stats\[1\]\.querySelector\("strong"\), ")\d+("\);)', rf'\g<1>{CROSS_CATEGORY}\2', wrapper)
    wrapper = re.sub(r'(resultCount\.textContent !== ")\d+("\))', rf'\g<1>{TOTAL}\2', wrapper)
    wrapper = re.sub(r'(resultCount\.textContent = ")\d+(";)', rf'\g<1>{TOTAL}\2', wrapper)
    WRAPPER_JS_PATH.write_text(wrapper, encoding="utf-8")

    app = APP_JS_PATH.read_text(encoding="utf-8")
    app = re.sub(r"app-v3\.js\?v=\d+", "app-v3.js?v=10", app)
    APP_JS_PATH.write_text(app, encoding="utf-8")

    social = SOCIAL_PATH.read_text(encoding="utf-8")
    social = re.sub(r">\d+</text>", f">{TOTAL}</text>", social, count=1)
    SOCIAL_PATH.write_text(social, encoding="utf-8")

    (ROOT / "docs" / "deployment-status.txt").write_text(
        "GitHub Pages deployment trigger\n"
        f"Updated: {SNAPSHOT_ISO_DATE}\n"
        f"Corpus: {TOTAL} benchmarks / {CROSS_CATEGORY} cross-category\n"
        f"Fingerprint: {EXPECTED_FINGERPRINT}\n",
        encoding="utf-8",
    )


def main() -> None:
    manifest = load_manifest()
    corpus = rebuild_shards(manifest)
    generate_readme(manifest, corpus)
    write_metadata(manifest)
    update_website_copy()
    print(
        f"Generated the latest-PDF snapshot: {TOTAL} benchmarks, {CROSS_CATEGORY} cross-category; "
        f"fingerprint {EXPECTED_FINGERPRINT}."
    )


if __name__ == "__main__":
    main()
