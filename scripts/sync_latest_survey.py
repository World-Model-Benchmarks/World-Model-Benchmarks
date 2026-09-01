#!/usr/bin/env python3
"""Validate the repository against the August 31, 2026 survey PDF."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
MANIFEST_PATH = ASSETS / "benchmarks.json"
METADATA_PATH = ASSETS / "metadata.json"
README_PATH = ROOT / "Readme.md"
INDEX_PATH = ROOT / "docs" / "index.html"

TOTAL = 106
CROSS_CATEGORY = 85
SCHEMA_VERSION = 8
SNAPSHOT_VERSION = "August 31, 2026 manuscript snapshot"
SNAPSHOT_DATE = "2026-08-31"
SITE_URL = "https://world-model-benchmarks.github.io/World-Model-Benchmarks/"
EXPECTED_FINGERPRINT = "42c3efbc20e9f821e1e130a13d18fee7abb696b4ad293ef59f643148caec0008"
EXPECTED_TARGET_COUNTS = {
    "T1": 46,
    "T2": 55,
    "T3": 24,
    "T4": 77,
    "T5": 37,
    "T6": 55,
    "T7": 13,
}
EXPECTED_SUBTARGET_COUNTS = {
    "S1": 40,
    "S2": 40,
    "S3": 30,
    "S4": 9,
    "S5": 40,
    "S6": 15,
    "S7": 2,
    "S8": 2,
    "S9": 12,
    "S10": 1,
}
EXPECTED_RELEASE_WINDOWS = {
    "2018–2021": 7,
    "2022–2023": 6,
    "2024": 9,
    "2025": 31,
    "2026": 53,
}
LEGACY_JS_FILES = ["app-1.js", "app-2.js", "app-3.js", "app-v2.js"]


def split_codes(value: str) -> list[str]:
    return [part for part in str(value or "").split("+") if part]


def fingerprint(records: dict[str, list]) -> str:
    rows = [
        f"{name}|{row[0]}|{row[6]}|{row[7]}"
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    records = manifest["records"]

    require(manifest["total"] == TOTAL and len(records) == TOTAL, "Corpus must contain 106 records")
    require(manifest["crossCategory"] == CROSS_CATEGORY, "Cross-category total must be 85")
    require(manifest["schemaVersion"] == SCHEMA_VERSION, "Schema version must be 8")
    require(manifest["version"] == SNAPSHOT_VERSION, "Snapshot version is stale")
    require(manifest["snapshotDate"] == SNAPSHOT_DATE, "Snapshot date is stale")

    target_counts = Counter(code for row in records.values() for code in split_codes(row[6]))
    subtarget_counts = Counter(code for row in records.values() for code in split_codes(row[7]))
    cross_count = sum(len(split_codes(row[6])) > 1 for row in records.values())
    require(dict(target_counts) == EXPECTED_TARGET_COUNTS, f"Target counts differ from PDF: {target_counts}")
    require(dict(subtarget_counts) == EXPECTED_SUBTARGET_COUNTS, f"Sub-target counts differ from PDF: {subtarget_counts}")
    require(cross_count == CROSS_CATEGORY, f"Computed cross-category count is {cross_count}, expected 85")
    require(fingerprint(records) == EXPECTED_FINGERPRINT, "Reference/category classification fingerprint differs from the PDF transcription")
    require(manifest.get("classificationFingerprint") == EXPECTED_FINGERPRINT, "Manifest fingerprint is missing or stale")

    for name, row in records.items():
        require(len(row) >= 8, f"Incomplete compact record: {name}")
        require(set(split_codes(row[3])) <= {"OL", "CL"}, f"Legacy/invalid protocol code for {name}: {row[3]}")
        require(set(split_codes(row[4])) <= {"P", "O"}, f"Legacy/invalid metric code for {name}: {row[4]}")
        require(set(split_codes(row[5])) <= {"RWD", "SBG", "SPTC", "HCP"}, f"Invalid data code for {name}: {row[5]}")
        require(row[6], f"Benchmark has no top-level target: {name}")

    window_counts = {
        bin_info["label"]: sum(row[1] in bin_info["years"] for row in records.values())
        for bin_info in manifest["timelineBins"]
    }
    require(window_counts == EXPECTED_RELEASE_WINDOWS, f"Release-window counts differ from Figure 2: {window_counts}")

    shard_records: list[dict] = []
    for index in range(1, 5):
        path = ASSETS / f"benchmarks-{index}.json"
        require(path.exists(), f"Missing shard: {path.name}")
        shard_records.extend(json.loads(path.read_text(encoding="utf-8")))
    shard_names = [item["shortName"] for item in shard_records]
    require(len(shard_records) == TOTAL, f"Shards contain {len(shard_records)} records, expected 106")
    require(len(set(shard_names)) == TOTAL, "Shard records are duplicated")
    require(set(shard_names) == set(records), "Shard and manifest record sets differ")

    target_labels = manifest["targetLabels"]
    subtarget_labels = manifest["subtargetLabels"]
    for item in shard_records:
        name = item["shortName"]
        row = records[name]
        require(item["ref"] == row[0], f"Reference mismatch in shard for {name}")
        require(item["year"] == row[1], f"Year mismatch in shard for {name}")
        require(item["domains"] == split_codes(row[2]), f"Domain mismatch in shard for {name}")
        require(item["protocols"] == split_codes(row[3]), f"Protocol mismatch in shard for {name}")
        require(item["metrics"] == split_codes(row[4]), f"Metric mismatch in shard for {name}")
        require(item["evaluationData"] == split_codes(row[5]), f"Data mismatch in shard for {name}")
        require(item["targets"] == [target_labels[code] for code in split_codes(row[6])], f"Target mismatch in shard for {name}")
        require(item["subtargets"] == [subtarget_labels[code] for code in split_codes(row[7])], f"Sub-target mismatch in shard for {name}")
        require(item["crossCategory"] == (len(split_codes(row[6])) > 1), f"Cross-category flag mismatch for {name}")
        for legacy_field in ("evidence", "dataConstruction", "realWorldExecution"):
            require(legacy_field not in item, f"Legacy field {legacy_field} remains in shard record {name}")

    require(metadata["total"] == TOTAL and metadata["crossCategory"] == CROSS_CATEGORY, "metadata.json totals are stale")
    require(metadata["version"] == SNAPSHOT_VERSION and metadata["snapshotDate"] == SNAPSHOT_DATE, "metadata.json snapshot is stale")
    require(metadata["classificationFingerprint"] == EXPECTED_FINGERPRINT, "metadata.json fingerprint differs")

    readme = README_PATH.read_text(encoding="utf-8")
    require("**106 representative benchmarks**" in readme, "README benchmark total is stale")
    require("**85** span more than one" in readme, "README cross-category total is stale")
    require("August 31, 2026" in readme and "August 27, 2026" not in readme, "README date is stale")
    for label, count in (
        ("Visual & Temporal Quality", 46),
        ("Spatial & State Consistency", 55),
        ("Long-Horizon Memory & State Persistence", 24),
        ("Physical Plausibility", 77),
        ("Causal & Counterfactual Reasoning", 37),
        ("Control Fidelity & Interactive Dynamics", 55),
        ("Functional Utility", 13),
    ):
        require(f"| {label} | {count} |" in readme, f"README count is wrong for {label}")
    for heading in (
        "### Visual Quality", "### Temporal Quality", "### Observation-Grounded Evaluation",
        "### Intervention-Grounded Evaluation", "### Pre-specified Control Fidelity",
        "### Interactive Action Fidelity", "### World Model as Data Engine",
        "### World Model as Policy Evaluator", "### World Model as Planner",
        "### World Model as Interactive Training Environment",
    ):
        require(heading in readme, f"README is missing {heading}")
    require(SITE_URL in readme, "README project-page URL is wrong")

    index = INDEX_PATH.read_text(encoding="utf-8")
    require(f'<link rel="canonical" href="{SITE_URL}">' in index, "Canonical site URL is wrong")
    require("106 benchmarks · 85 cross-category · checked August 31, 2026" in index, "Website snapshot note is stale")
    require('id="stat-cross">85<' in index, "Website cross-category statistic is stale")
    require("August 27, 2026" not in index and "66 cross-category" not in index, "Old website snapshot copy remains")

    core_js = (ASSETS / "app-v3-core.js").read_text(encoding="utf-8")
    wrapper_js = (ASSETS / "app-v3.js").read_text(encoding="utf-8")
    app_js = (ASSETS / "app.js").read_text(encoding="utf-8")
    require('const PROTOCOLS = ["OL", "CL"];' in core_js, "Explorer protocol taxonomy is stale")
    require('const METRICS = ["P", "O"];' in core_js, "Explorer metric taxonomy is stale")
    require('"CR"' not in core_js and '["A", "J", "O"]' not in core_js, "Legacy explorer codes remain")
    require("85 cross-category" in wrapper_js and "August 31, 2026" in wrapper_js, "Explorer wrapper copy is stale")
    require("app-v3.js?v=9" in app_js and "app-v2.js" not in app_js, "Fallback app loader is stale")

    for filename in LEGACY_JS_FILES:
        require(not (ASSETS / filename).exists(), f"Unused legacy script remains: {filename}")

    robots = (ROOT / "docs" / "robots.txt").read_text(encoding="utf-8")
    sitemap = (ROOT / "docs" / "sitemap.xml").read_text(encoding="utf-8")
    require(f"Sitemap: {SITE_URL}sitemap.xml" in robots, "robots.txt sitemap URL is wrong")
    require(f"<loc>{SITE_URL}</loc>" in sitemap, "sitemap.xml project URL is wrong")
    require("axbhb.github.io" not in robots + sitemap, "Legacy deployment URL remains")

    print(
        "Validated the August 31, 2026 PDF snapshot: "
        "106 benchmarks, 85 cross-category, exact Figure 4/Table 3–9 classification."
    )


if __name__ == "__main__":
    main()
