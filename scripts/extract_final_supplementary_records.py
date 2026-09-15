#!/usr/bin/env python3
"""Extract the joint task-level coding from the final supplementary PDF.

The PDF tables are typeset without ruling lines, so extraction uses the stable
column coordinates of Tables S1-S7.  The output is a reviewable source snapshot
for the website generator; it is not intended to replace the published PDF.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import pdfplumber


PROTOCOL_RE = re.compile(r"^(?:OL|CL)[a-z]?$")
DATA_RE = re.compile(r"^(?:RWD|SBG|SPTC|HCP|NR)[a-z]?$")


def join_words(words: list[dict]) -> str:
    lines: dict[float, list[dict]] = {}
    for word in words:
        lines.setdefault(round(word["top"], 1), []).append(word)
    text_lines = [
        " ".join(word["text"] for word in sorted(line, key=lambda item: item["x0"]))
        for _, line in sorted(lines.items())
    ]
    return " ".join(text_lines).strip()


def scope_for(page_number: int, top: float) -> tuple[str, str]:
    if 4 <= page_number <= 6:
        return "T1", "S1"
    if 7 <= page_number <= 10:
        return "T2", "S2"
    if 11 <= page_number <= 12:
        return "T3", "S3"
    if 13 <= page_number <= 17:
        return "T4", "S4"
    if 18 <= page_number <= 19:
        return "T5", "S5"
    if page_number in (20, 21) or (page_number == 22 and top < 400):
        return "S5", "S6"
    if page_number in (22, 23):
        return "S6", "S6"
    if page_number == 24 and top < 180:
        return "S7", "S7"
    if page_number == 24 and top < 260:
        return "S8", "S7"
    if page_number == 24 or (page_number == 25 and top < 175):
        return "S9", "S7"
    if page_number == 25:
        return "S10", "S7"
    raise ValueError(f"No table scope for supplementary page {page_number}, y={top}")


def extract(pdf_path: Path, manifest_path: Path) -> dict:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    names_by_ref = {int(row[0]): name for name, row in manifest["records"].items()}
    if len(names_by_ref) != len(manifest["records"]):
        raise ValueError("Benchmark references must be unique")

    records: list[dict] = []
    table_indexes = Counter()
    with pdfplumber.open(pdf_path) as pdf:
        for page_index in range(3, 25):
            page_number = page_index + 1
            words = pdf.pages[page_index].extract_words(x_tolerance=1, y_tolerance=2)
            protocol_words = [
                word for word in words
                if 430 < word["x0"] < 530 and PROTOCOL_RE.fullmatch(word["text"])
                and not (page_number == 4 and word["top"] < 100)
            ]
            for row_index, protocol_word in enumerate(protocol_words):
                top = protocol_word["top"]
                next_top = protocol_words[row_index + 1]["top"] if row_index + 1 < len(protocol_words) else 744
                row_words = [word for word in words if top - 2 <= word["top"] < next_top - 2]
                metric_words = [
                    word for word in words
                    if 490 <= word["x0"] < 530 and abs(word["top"] - top) < 4
                    and word["text"] in {"P", "O"}
                ]
                data_words = [
                    word for word in words
                    if word["x0"] >= 525 and abs(word["top"] - top) < 4
                    and DATA_RE.fullmatch(word["text"])
                ]
                refs = [
                    int(match.group(1))
                    for word in row_words if word["x0"] < 154
                    if (match := re.fullmatch(r"\[(\d+)\]", word["text"]))
                ]
                if len(metric_words) != 1 or len(data_words) != 1 or len(refs) != 1:
                    raise ValueError(
                        f"Could not decode row on page {page_number} at y={top}: "
                        f"metrics={metric_words}, data={data_words}, refs={refs}"
                    )

                scope, table = scope_for(page_number, top)
                table_indexes[table] += 1
                raw_protocol = protocol_word["text"]
                raw_data = data_words[0]["text"]
                task_words = [word for word in row_words if 145 <= word["x0"] < 276]
                readout_words = [word for word in row_words if 276 <= word["x0"] < 445]
                task = join_words(task_words)
                readout = join_words(readout_words)
                auxiliary = "comparator*" in task or "pool*" in task
                records.append({
                    "taskId": f"{table}-{table_indexes[table]:03d}",
                    "benchmark": names_by_ref[refs[0]],
                    "scope": scope,
                    "protocol": raw_protocol[:2],
                    "metric": metric_words[0]["text"],
                    "data": None if raw_data.startswith("NR") else re.match(r"[A-Z]+", raw_data).group(0),
                    "dataStatus": "unresolved" if raw_data.startswith("NR") else "classified",
                    "taskBranch": task,
                    "measuredReadout": readout,
                    "source": {
                        "table": table,
                        "page": page_number,
                        "tableRow": table_indexes[table],
                    },
                    "auxiliary": auxiliary,
                })

    task_records = [record for record in records if not record["auxiliary"]]
    auxiliary_records = [record for record in records if record["auxiliary"]]
    pmd = Counter((r["protocol"], r["metric"]) for r in task_records)
    data = Counter(r["data"] for r in task_records if r["data"])
    unresolved = sum(r["data"] is None for r in task_records)
    expected_pmd = Counter({("OL", "P"): 346, ("OL", "O"): 12, ("CL", "P"): 17, ("CL", "O"): 26})
    expected_data = Counter({"RWD": 89, "SBG": 88, "SPTC": 71, "HCP": 146})
    if len(records) != 403 or len(task_records) != 401 or len(auxiliary_records) != 2:
        raise ValueError(f"Unexpected record totals: {len(records)}/{len(task_records)}/{len(auxiliary_records)}")
    if pmd != expected_pmd:
        raise ValueError(f"Unexpected protocol/metric totals: {pmd}")
    if data != expected_data or unresolved != 7:
        raise ValueError(f"Unexpected data totals: {data}, unresolved={unresolved}")

    return {
        "schemaVersion": 1,
        "source": {
            "title": "A Survey of World Model Benchmarks - Supplementary Material",
            "tables": "S1-S7",
            "fileSha256": "af6a8440614fe85d9505d5c6ec2b9283c16ea32d0078ed8b7be3492b26923d41",
        },
        "counts": {
            "allRecords": len(records),
            "targetTaskRecords": len(task_records),
            "auxiliaryRecords": len(auxiliary_records),
            "classifiedDataRecords": len(task_records) - unresolved,
            "unresolvedDataRecords": unresolved,
        },
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "docs/assets/benchmarks.json",
    )
    args = parser.parse_args()
    payload = extract(args.pdf, args.manifest)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Extracted {payload['counts']['targetTaskRecords']} target-task records and "
        f"{payload['counts']['auxiliaryRecords']} auxiliary records."
    )


if __name__ == "__main__":
    main()
