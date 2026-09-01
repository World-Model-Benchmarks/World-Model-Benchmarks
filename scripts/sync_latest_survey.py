#!/usr/bin/env python3
"""Validate repository and website data against the latest 102-benchmark PDF."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
MANIFEST_PATH = ASSETS / "benchmarks.json"
METADATA_PATH = ASSETS / "metadata.json"
README_PATH = ROOT / "Readme.md"
INDEX_PATH = ROOT / "docs" / "index.html"

TOTAL = 102
CROSS_CATEGORY = 85
SCHEMA_VERSION = 9
SNAPSHOT_VERSION = "August 31, 2026 manuscript snapshot"
SNAPSHOT_DATE = "2026-08-31"
SOURCE_PDF_SHA256 = "c96efe634f70b1297e281e36786dc6a5fedd3b747bf4fc57ad58583c69a50dad"
EXPECTED_FINGERPRINT = "e30cf7f9b7bf39cb03baa6b9cddcbeb593b5821e1ba85a82fddff0787c7e4935"
SITE_URL = "https://world-model-benchmarks.github.io/World-Model-Benchmarks/"
EXPECTED_TARGET_COUNTS = {"T1": 46, "T2": 55, "T3": 24, "T4": 77, "T5": 33, "T6": 55, "T7": 13}
EXPECTED_SUBTARGET_COUNTS = {"S1": 40, "S2": 40, "S3": 26, "S4": 9, "S5": 40, "S6": 15, "S7": 2, "S8": 2, "S9": 12, "S10": 1}
EXPECTED_RELEASE_WINDOWS = {"2018–2021": 5, "2022–2023": 5, "2024": 9, "2025": 30, "2026": 53}
REMOVED = {"CATER", "NExT-QA", "IntentQA", "VCRBench"}
OBSOLETE_WORKFLOWS = {
    ".github/workflows/pdf-alignment-main-once.yml",
    ".github/workflows/pdf-alignment-repair.yml",
}


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
        raise AssertionError(message)


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    records = manifest["records"]

    require(manifest.get("total") == TOTAL and len(records) == TOTAL, "Corpus must contain 102 records")
    require(manifest.get("crossCategory") == CROSS_CATEGORY, "Cross-category total must be 85")
    require(manifest.get("schemaVersion") == SCHEMA_VERSION, "Schema version must be 9")
    require(manifest.get("version") == SNAPSHOT_VERSION, "Snapshot version is stale")
    require(manifest.get("snapshotDate") == SNAPSHOT_DATE, "Snapshot date is stale")
    require(manifest.get("sourcePdfSha256") == SOURCE_PDF_SHA256, "Source-PDF SHA-256 is stale")
    require(not (set(records) & REMOVED), f"Removed benchmarks remain in records: {sorted(set(records) & REMOVED)}")

    target_counts = Counter(code for row in records.values() for code in split_codes(row[6]))
    subtarget_counts = Counter(code for row in records.values() for code in split_codes(row[7]))
    cross_count = sum(len(split_codes(row[6])) > 1 for row in records.values())
    require(dict(target_counts) == EXPECTED_TARGET_COUNTS, f"Target counts differ from PDF: {target_counts}")
    require(dict(subtarget_counts) == EXPECTED_SUBTARGET_COUNTS, f"Subtarget counts differ from PDF: {subtarget_counts}")
    require(cross_count == CROSS_CATEGORY, f"Computed cross-category count is {cross_count}")
    require(fingerprint(records) == EXPECTED_FINGERPRINT, "Full benchmark-coding fingerprint differs from latest PDF")
    require(manifest.get("classificationFingerprint") == EXPECTED_FINGERPRINT, "Manifest classification fingerprint is stale")
    require(manifest.get("recordFingerprint") == EXPECTED_FINGERPRINT, "Manifest record fingerprint is stale")

    wr = records.get("WR-Arena")
    require(wr is not None, "WR-Arena is missing")
    require(wr[0] == 110 and wr[3] == "OL+CL" and wr[4] == "P+O", "WR-Arena must be ref. 110, OL+CL, P+O")

    for name, row in records.items():
        require(len(row) >= 8, f"Incomplete record: {name}")
        require(set(split_codes(row[3])) <= {"OL", "CL"}, f"Invalid protocol for {name}: {row[3]}")
        require(set(split_codes(row[4])) <= {"P", "O"}, f"Invalid metric level for {name}: {row[4]}")
        require(len(split_codes(row[5])) == 1 and set(split_codes(row[5])) <= {"RWD", "SBG", "SPTC", "HCP"}, f"Invalid data coding for {name}: {row[5]}")
        require(row[6], f"Benchmark has no top-level target: {name}")

    release_counts = {
        item["label"]: sum(row[1] in item["years"] for row in records.values())
        for item in manifest["timelineBins"]
    }
    require(release_counts == EXPECTED_RELEASE_WINDOWS, f"Release-window counts differ from PDF: {release_counts}")

    shard_records: list[dict] = []
    for index in range(1, 5):
        path = ASSETS / f"benchmarks-{index}.json"
        require(path.exists(), f"Missing shard: {path.name}")
        shard_records.extend(json.loads(path.read_text(encoding="utf-8")))
    require(len(shard_records) == TOTAL, f"Shards contain {len(shard_records)} records")
    shard_names = [item["shortName"] for item in shard_records]
    require(len(set(shard_names)) == TOTAL and set(shard_names) == set(records), "Shard and manifest benchmark sets differ")
    require(not (set(shard_names) & REMOVED), "Removed benchmarks remain in website shards")

    for item in shard_records:
        name = item["shortName"]
        row = records[name]
        require(item["ref"] == row[0], f"Reference mismatch for {name}")
        require(item["year"] == row[1], f"Year mismatch for {name}")
        require(item["domains"] == split_codes(row[2]), f"Domain mismatch for {name}")
        require(item["protocols"] == split_codes(row[3]), f"Protocol mismatch for {name}")
        require(item["metrics"] == split_codes(row[4]), f"Metric mismatch for {name}")
        require(item["evaluationData"] == split_codes(row[5]), f"Data mismatch for {name}")
        require(item["targets"] == [manifest["targetLabels"][code] for code in split_codes(row[6])], f"Target mismatch for {name}")
        require(item["subtargets"] == [manifest["subtargetLabels"][code] for code in split_codes(row[7])], f"Subtarget mismatch for {name}")
        require(item["crossCategory"] == (len(split_codes(row[6])) > 1), f"Cross-category flag mismatch for {name}")
        for legacy_field in ("evidence", "dataConstruction", "realWorldExecution"):
            require(legacy_field not in item, f"Legacy field {legacy_field} remains in {name}")

    require(metadata.get("total") == TOTAL and metadata.get("crossCategory") == CROSS_CATEGORY, "metadata.json totals are stale")
    require(metadata.get("version") == SNAPSHOT_VERSION and metadata.get("snapshotDate") == SNAPSHOT_DATE, "metadata.json snapshot is stale")
    require(metadata.get("sourcePdfSha256") == SOURCE_PDF_SHA256, "metadata.json source digest is stale")
    require(metadata.get("classificationFingerprint") == EXPECTED_FINGERPRINT, "metadata.json fingerprint is stale")
    require(metadata.get("targetCounts", {}).get("Causal & Counterfactual Reasoning") == 33, "metadata.json T5 count is stale")
    require(metadata.get("subtargetCounts", {}).get("Observation-Grounded Evaluation") == 26, "metadata.json S3 count is stale")
    require(metadata.get("releaseWindowCounts") == EXPECTED_RELEASE_WINDOWS, "metadata.json release-window counts are stale")

    readme = README_PATH.read_text(encoding="utf-8")
    require("**102 representative benchmarks**" in readme, "README total is stale")
    require("**85** span more than one" in readme, "README cross-category count is stale")
    require("| Causal & Counterfactual Reasoning | 33 |" in readme, "README T5 count is stale")
    for name in REMOVED:
        require(f"**{name}" not in readme, f"README still lists removed benchmark {name}")
    require(SITE_URL in readme, "README project URL is wrong")

    index = INDEX_PATH.read_text(encoding="utf-8")
    require("102 benchmarks · 85 cross-category · checked August 31, 2026" in index, "Website snapshot note is stale")
    require('id="stat-total">102<' in index, "Website total is stale")
    require('id="stat-cross">85<' in index, "Website cross-category total is stale")
    require("10 cumulative benchmarks by 2023" in index, "Website 2023 cumulative count is stale")
    require("30 new benchmarks in 2025" in index and "<strong>49</strong>" in index, "Website 2025 timeline copy is stale")
    require("<strong>102</strong>" in index, "Website final cumulative count is stale")
    require("106 benchmarks · 85 cross-category" not in index, "Old website corpus total remains")

    wrapper = (ASSETS / "app-v3.js").read_text(encoding="utf-8")
    require("102 benchmarks · 85 cross-category" in wrapper, "Explorer wrapper total is stale")
    require("the 102 representative benchmarks" in wrapper, "Explorer summary is stale")
    app = (ASSETS / "app.js").read_text(encoding="utf-8")
    require("app-v3.js?v=10" in app, "Fallback loader cache version is stale")

    # The canonical manifest intentionally records removals in its audit metadata,
    # so check user-facing website assets and shards rather than the manifest text.
    visible_site_paths = [
        INDEX_PATH,
        ASSETS / "app-v3.js",
        ASSETS / "app-v3-core.js",
        ASSETS / "app.js",
        ASSETS / "social-preview.svg",
        *(ASSETS / f"benchmarks-{index}.json" for index in range(1, 5)),
    ]
    visible_site_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore") for path in visible_site_paths
    )
    for name in REMOVED:
        require(name not in visible_site_text, f"User-facing website assets still contain removed benchmark {name}")

    for workflow in OBSOLETE_WORKFLOWS:
        require(not (ROOT / workflow).exists(), f"Obsolete 106-benchmark repair workflow remains: {workflow}")

    print(
        "Validated the latest PDF snapshot: 102 benchmarks, 85 cross-category, "
        "all Figure 4 / Tables 3–10 coding, and synchronized repository/website outputs."
    )


if __name__ == "__main__":
    main()
