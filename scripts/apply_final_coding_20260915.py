#!/usr/bin/env python3
"""Apply the final September 15 joint coding snapshot to the site manifest."""
from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/assets/benchmarks.json"
TASK_RECORDS_PATH = ROOT / "scripts/task_records_20260915.json"

PROTOCOL_ORDER = ("OL", "CL")
METRIC_ORDER = ("P", "O")
DATA_ORDER = ("RWD", "SBG", "SPTC", "HCP")
SCOPE_ORDER = ("T1", "T2", "T3", "T4", "T5", "S5", "S6", "S7", "S8", "S9", "S10")

MAIN_PDF_SHA256 = "f261e719372af3fbbfc1ecec7f0386603edaff413e39e907ad27021205323db0"
SUPPLEMENTARY_PDF_SHA256 = "af6a8440614fe85d9505d5c6ec2b9283c16ea32d0078ed8b7be3492b26923d41"


def join_codes(values: set[str], order: tuple[str, ...]) -> str:
    return "+".join(value for value in order if value in values)


def benchmark_fingerprint(records: dict[str, list]) -> str:
    rows = [
        f"{name}|" + "|".join(str(value) for value in row[:8])
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def track_fingerprint(category_records: dict[str, dict[str, list]], records: dict[str, list]) -> str:
    rows = []
    for scope, scoped_records in sorted(category_records.items()):
        for name, (protocol, metrics) in sorted(scoped_records.items()):
            row = records[name]
            rows.append("|".join(map(str, [scope, name, row[0], row[1], row[2], protocol, metrics, row[5]])))
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def json_fingerprint(value: object) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    task_source = json.loads(TASK_RECORDS_PATH.read_text(encoding="utf-8"))
    all_task_records = task_source["records"]
    task_records = [record for record in all_task_records if not record["auxiliary"]]
    auxiliary_records = [record for record in all_task_records if record["auxiliary"]]

    if (len(task_records), len(auxiliary_records)) != (401, 2):
        raise RuntimeError("The final supplement must contain 401 target-task and 2 auxiliary records")

    # Two classification corrections explicitly recorded in the final paper.
    manifest["records"]["CausalSpatial"][2] = "video"
    manifest["records"]["ContPhy"][7] = "S3+S4"

    grouped: dict[tuple, list[dict]] = defaultdict(list)
    parent: dict[tuple[str, str], dict[str, set[str]]] = {}
    benchmark: dict[str, dict[str, set[str]]] = {}
    for record in task_records:
        key = (
            record["benchmark"], record["scope"], record["protocol"],
            record["metric"], record["data"], record["dataStatus"],
        )
        grouped[key].append(record)
        parent_values = parent.setdefault((record["scope"], record["benchmark"]), {
            "protocol": set(), "metric": set(), "data": set(),
        })
        benchmark_values = benchmark.setdefault(record["benchmark"], {
            "protocol": set(), "metric": set(), "data": set(),
        })
        for values in (parent_values, benchmark_values):
            values["protocol"].add(record["protocol"])
            values["metric"].add(record["metric"])
            if record["data"]:
                values["data"].add(record["data"])

    evaluation_records = []
    sort_key = lambda item: (
        SCOPE_ORDER.index(item[0][1]), manifest["records"][item[0][0]][0],
        PROTOCOL_ORDER.index(item[0][2]), METRIC_ORDER.index(item[0][3]),
        DATA_ORDER.index(item[0][4]) if item[0][4] else len(DATA_ORDER),
    )
    for index, (key, supporting_rows) in enumerate(sorted(grouped.items(), key=sort_key), start=1):
        name, scope, protocol, metric, data, data_status = key
        evaluation_records.append({
            "id": f"EC{index:04d}",
            "benchmark": name,
            "scope": scope,
            "protocol": protocol,
            "metric": metric,
            "data": data,
            "dataStatus": data_status,
            "taskIds": [row["taskId"] for row in supporting_rows],
            "sourceTable": supporting_rows[0]["source"]["table"],
            "sourcePages": sorted({row["source"]["page"] for row in supporting_rows}),
        })

    if len(evaluation_records) != 372 or len(parent) != 307:
        raise RuntimeError(f"Unexpected grouped totals: {len(evaluation_records)} combinations, {len(parent)} parent rows")

    expected_parents = {
        (scope, name)
        for scope, scoped_records in manifest["categoryRecords"].items()
        for name in scoped_records
    }
    if set(parent) != expected_parents:
        raise RuntimeError("Final task records do not cover the existing 307 target/role parent rows exactly")

    category_records = {scope: {} for scope in SCOPE_ORDER}
    for (scope, name), values in parent.items():
        category_records[scope][name] = [
            join_codes(values["protocol"], PROTOCOL_ORDER),
            join_codes(values["metric"], METRIC_ORDER),
        ]
    category_records = {
        scope: dict(sorted(category_records[scope].items(), key=lambda item: (manifest["records"][item[0]][0], item[0])))
        for scope in SCOPE_ORDER
    }

    for name, values in benchmark.items():
        row = manifest["records"][name]
        row[3] = join_codes(values["protocol"], PROTOCOL_ORDER)
        row[4] = join_codes(values["metric"], METRIC_ORDER)
        row[5] = join_codes(values["data"], DATA_ORDER)

    target_counts = Counter(
        code for row in manifest["records"].values() for code in row[6].split("+") if code
    )
    subtarget_counts = Counter(
        code for row in manifest["records"].values() for code in row[7].split("+") if code
    )
    manifest.update({
        "version": "August 31, 2026 corpus; joint task-level coding revised September 15, 2026",
        "schemaVersion": 11,
        "sourcePdfSha256": MAIN_PDF_SHA256,
        "sourceSupplementaryPdfSha256": SUPPLEMENTARY_PDF_SHA256,
        "sourceNote": (
            "The 102-benchmark corpus remains checked through August 31, 2026. "
            "Taxonomy membership follows Supplementary Fig. S1; 401 target-task records and "
            "their joint Protocol-Metrics-Data coding follow Supplementary Tables S1-S7 of "
            "the final September 15, 2026 manuscript. Two auxiliary records are retained for "
            "traceability and excluded from target-task statistics."
        ),
        "yearBasis": (
            "Benchmark release year as coded in Figure 2 of the final September 15, 2026 "
            "manuscript; distinct from formal publication year."
        ),
        "releaseYearRevision": {
            "sourcePdf": "main.pdf",
            "sourcePdfSha256": MAIN_PDF_SHA256,
            "date": "2026-09-15",
            "changedRecords": 0,
            "preservedFromPreviousAudit": 102,
        },
        "fingerprintFields": [
            "benchmark", "reference", "year", "domain", "protocol", "metrics",
            "data", "targets", "subtargets",
        ],
        "categoryRecords": category_records,
        "evaluationRecords": evaluation_records,
        "taskRecords": all_task_records,
        "taskRecordCounts": {
            "targetTasks": 401,
            "auxiliary": 2,
            "displayCombinations": 372,
            "classifiedData": 394,
            "unresolvedData": 7,
            "protocolMetric": {"OL/P": 346, "OL/O": 12, "CL/P": 17, "CL/O": 26},
            "data": {"RWD": 89, "SBG": 88, "SPTC": 71, "HCP": 146},
        },
        "targetCounts": {
            manifest["targetLabels"][code]: target_counts[code]
            for code in manifest["targetLabels"]
        },
        "subtargetCounts": {
            manifest["subtargetLabels"][code]: subtarget_counts[code]
            for code in manifest["subtargetLabels"]
        },
        "codingScope": (
            "Each evaluationRecords item is one observed Protocol-Metrics-Data combination "
            "within a target or downstream role. Filters match all selected evidence dimensions "
            "within the same combination; selections within a filter group use OR and selections "
            "across groups use AND. Benchmark-level records contain unions for overview only."
        ),
        "codingRevision": {
            "mainSourcePdf": "main.pdf",
            "mainSourcePdfSha256": MAIN_PDF_SHA256,
            "supplementarySourcePdf": "A Survey of World Model Benchmarks - Supplementary Material.pdf",
            "supplementarySourcePdfSha256": SUPPLEMENTARY_PDF_SHA256,
            "date": "2026-09-15",
            "targetRoleParentRows": 307,
            "targetTaskRecords": 401,
            "auxiliaryRecords": 2,
            "displayCombinations": 372,
            "changedTargetRoleRows": 23,
            "changedBenchmarkOverviewRecords": 31,
            "preservedReleaseYears": 102,
        },
    })

    classification_fingerprint = benchmark_fingerprint(manifest["records"])
    manifest["classificationFingerprint"] = classification_fingerprint
    manifest["recordFingerprint"] = classification_fingerprint
    manifest["evaluationTrackFingerprint"] = track_fingerprint(category_records, manifest["records"])
    manifest["evaluationRecordFingerprint"] = json_fingerprint(evaluation_records)
    manifest["taskRecordFingerprint"] = json_fingerprint(all_task_records)

    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Applied {len(task_records)} target-task rows as {len(evaluation_records)} joint combinations "
        f"across {len(parent)} target/role parents."
    )


if __name__ == "__main__":
    main()
