#!/usr/bin/env python3
"""Idempotently integrate all PDF Table 3--9 record fields into the generator."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_readme_index.py"
VALIDATOR = ROOT / "scripts" / "sync_latest_survey.py"
EXPECTED_FINGERPRINT = "d38c6018cfb278050d00a39b06e44dc252bd40c6bb6c7a0c338e30e36be1572c"

ATTRIBUTE_ROWS = """RoboWM-Bench	2026	embodied	OL	O	HCP
World-in-World	2025	embodied	CL	O	HCP
IntPhys	2018	video	OL	P	SBG
CLEVRER	2020	video	OL	P	SBG
Physion	2021	video	OL	P	SBG
MIND	2026	video	OL	P	SBG
WorldOlympiad	2026	video	OL	P	HCP
WorldArena	2026	embodied	OL+CL	P+O	SBG
WorldArena 2.0	2026	embodied	OL+CL	P+O	HCP
ChronoMagic-Bench	2024	video	OL	P	SPTC
WorldScore	2025	video	OL	P	HCP
VMBench	2025	video	OL	P	SPTC
EWMBench	2025	embodied	OL	P	HCP
GameWorld Score	2025	game	OL	P	SBG
WorldMark	2026	game+video	OL	P	HCP
4DWorldBench	2025	video	OL	P	HCP
WorldLens	2026	driving	OL+CL	P+O	HCP
DrivingGen	2026	driving	OL	P	RWD
PEDRA	2025	video	OL	P	RWD
Gen-ViRe	2025	video	OL	P	HCP
iWorld-Bench	2026	video	OL	P	HCP
WoW-World-Eval	2026	embodied	OL	P+O	HCP
RBench	2026	embodied	OL	P	RWD
PAI-Bench	2025	video	OL	P	HCP
EZS-Bench	2026	embodied	OL	P	HCP
WorldRoamBench	2026	video+game	OL	P	HCP
MemoBench	2026	video	OL	P	HCP
RoboTrustBench	2026	embodied	OL	P	HCP
WorldExam	2026	video	OL	P	HCP
SurgWMBench	2026	embodied	OL	P	RWD
H2R-Bench	2026	embodied	OL	P	HCP
PlayWorld	2026	game+video	CL	P	HCP
XEWorld	2026	embodied	OL	P	SBG
HarnessEval-W	2026	video	OL	P	HCP
WorldEcho	2026	embodied	OL	P	SBG
ACWM-Phys	2026	video	OL	P	SBG
HTEWorld	2026	embodied	OL	P	SBG
RigidBench	2026	video	OL	P	SBG
MagicBench	2025	video	OL	P	RWD
MoveBench	2025	video	OL	P	RWD
Omni-WorldBench	2026	video	OL	P	HCP
OSCBench	2026	video	OL	P	SPTC
T2VWorldBench	2025	video	OL	P	SPTC
WMBench	2026	embodied	CL	P+O	HCP
WorldModelBench	2025	video	OL	P	SPTC
WorldSimBench	2024	game+driving+embodied	OL+CL	P+O	HCP
Apple-π	2026	video	OL	P	HCP
TC-Bench	2024	video	OL	P	HCP
WBench	2026	video	OL	P	HCP
CrashTwin	2026	driving+video	OL	P	HCP
EVA-Bench	2024	embodied	OL	O	HCP
WR-Arena	2026	driving+embodied	OL	P	HCP
PDI-Bench	2026	video	OL	P	HCP
LoopNav	2025	game	OL	P	SBG
MBench	2026	video	OL	P	RWD
STEVO-Bench	2026	video	OL	P	HCP
CausalSpatial	2026	image	OL	P	SBG
What-If World	2026	driving+embodied	OL	P	RWD
HOCA-Bench	2026	video	OL	P	HCP
AutumnBench	2025	game	CL	P+O	SBG
MVP	2025	video	OL	P	HCP
ContactWorld	2026	embodied	CL	P+O	HCP
ScratchWorld	2026	game	OL	P	HCP
MiraBench	2026	embodied	OL	P	HCP
Chess-World-Model	2026	game	OL	P	HCP
IntPhys 2	2025	video	OL	P	SBG
SmallWorlds	2025	video	OL	P	SBG
VBench-2.0	2025	video	OL	P	SPTC
WorldBench	2026	video	OL	P	HCP
WorldPrediction	2025	video	OL	P	RWD
ExPhy	2026	embodied	OL	P	SBG
CoPhy	2020	video	OL	P	SBG
PHYRE	2019	video	CL	O	SBG
CRAFT	2022	video	OL	P	SBG
Physion++	2023	video	OL	P	SBG
ComPhy	2022	video	OL	P	SBG
ContPhy	2024	video	OL	P	SBG
PhyCoBench	2025	video	OL	P	SPTC
VideoPhy	2024	video	OL	P	SPTC
VideoPhy-2	2025	video	OL	P	SPTC
PhyGenBench	2024	video	OL	P	SPTC
T2VPhysBench	2025	video	OL	P	SPTC
Physics-IQ	2025	video	OL	P	RWD
PhyWorldBench	2025	video	OL	P	SPTC
Morpheus	2025	video	OL	P	RWD
DreamGen Bench	2025	embodied	OL	P	HCP
PhyGround	2026	video	OL	P	SPTC
Physion-Eval	2026	video	OL	P	HCP
CRONOS	2026	video	OL	P	HCP
VACT	2025	video	OL	P	SPTC
PhysicsMind	2026	video	OL	P	HCP
KineBench	2026	embodied	CL	P+O	HCP
ReactSim-Bench	2026	driving	CL	P	HCP
GAUGE	2026	video	OL	P	HCP
CaliBench	2026	video	OL	P	HCP
WorldSimProbe	2026	embodied	OL	P	SBG
CATER	2020	video	OL	P	SBG
NExT-QA	2021	video	OL	P	RWD
Causal-VidQA	2022	video	OL	P	RWD
IntentQA	2023	video	OL	P	RWD
ACQUIRED	2023	video	OL	P	RWD
MMWorld	2025	video	OL	P	HCP
VCRBench	2025	video	OL	P	RWD
CausalVQA	2025	video	OL	P	RWD
StoryEval	2024	video	OL	P	SPTC
ACT-Bench	2024	driving	OL	P	RWD"""
ATTRIBUTES = {}
for line in ATTRIBUTE_ROWS.splitlines():
    name, year, domain, protocol, metrics, data = line.split("\t")
    ATTRIBUTES[name] = (int(year), domain, protocol, metrics, data)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} block, found {count}")
    return text.replace(old, new, 1)


def render_attribute_block() -> str:
    lines = [
        "# Year, domain, protocol, metric level, and data construction are transcribed",
        "# from Tables 3--9. For repeated functional-utility roles, protocol and metric",
        "# codes are the ordered union across the benchmark's table rows.",
        "ATTRIBUTES = {",
    ]
    for name, values in ATTRIBUTES.items():
        year, domain, protocol, metrics, data = values
        lines.append(
            f"    {name!r}: ({year}, {domain!r}, {protocol!r}, {metrics!r}, {data!r}),"
        )
    lines.append("}")
    return "\n".join(lines)


def patch_generator() -> None:
    text = GENERATOR.read_text(encoding="utf-8")
    if "ATTRIBUTES = {" in text:
        required = [
            'row[:6] = [REFS[name], year, domain, protocol, metrics, data]',
            'manifest["recordFingerprint"] = manifest["classificationFingerprint"]',
            '"fingerprintFields": manifest["fingerprintFields"]',
        ]
        missing = [needle for needle in required if needle not in text]
        if missing:
            raise RuntimeError(f"Generator is partially patched; missing: {missing}")
        return

    start_marker = "# The aggregate website record uses the union of tracks when a benchmark has"
    end_marker = "LEGACY_JS_FILES ="
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    text = text[:start] + render_attribute_block() + "\n\n" + text[end:]

    text = replace_once(
        text,
        """    if set(REFS) != record_names:
        raise RuntimeError(
            f"Reference map mismatch: records-only={sorted(record_names - set(REFS))}; "
            f"refs-only={sorted(set(REFS) - record_names)}"
        )
""",
        """    if set(REFS) != record_names:
        raise RuntimeError(
            f"Reference map mismatch: records-only={sorted(record_names - set(REFS))}; "
            f"refs-only={sorted(set(REFS) - record_names)}"
        )
    if set(ATTRIBUTES) != record_names:
        raise RuntimeError(
            f"Attribute map mismatch: records-only={sorted(record_names - set(ATTRIBUTES))}; "
            f"attributes-only={sorted(set(ATTRIBUTES) - record_names)}"
        )
""",
        "source-validation",
    )

    text = replace_once(
        text,
        """def classification_fingerprint(records: dict[str, list]) -> str:
    rows = [
        f"{name}|{row[0]}|{row[6]}|{row[7]}"
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\\n".join(rows).encode("utf-8")).hexdigest()
""",
        """def classification_fingerprint(records: dict[str, list]) -> str:
    \"\"\"Hash every PDF-coded field: reference, year, domain, protocol, metrics, data, and targets.\"\"\"
    rows = [
        f"{name}|" + "|".join(str(value) for value in row[:8])
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\\n".join(rows).encode("utf-8")).hexdigest()
""",
        "generator fingerprint",
    )

    text = replace_once(
        text,
        """        row[0] = REFS[name]
        override = AGGREGATE_OVERRIDES.get(name)
        if override:
            row[3] = override["protocol"]
            row[4] = override["metrics"]
            row[5] = override["data"]
        row[6] = "+".join(ordered_codes(name, TARGET_MEMBERS))
        row[7] = "+".join(ordered_codes(name, SUBTARGET_MEMBERS))
""",
        """        year, domain, protocol, metrics, data = ATTRIBUTES[name]
        row[:6] = [REFS[name], year, domain, protocol, metrics, data]
        row[6] = "+".join(ordered_codes(name, TARGET_MEMBERS))
        row[7] = "+".join(ordered_codes(name, SUBTARGET_MEMBERS))
""",
        "record update",
    )

    text = replace_once(
        text,
        """    manifest["classificationFingerprint"] = classification_fingerprint(records)
    MANIFEST_PATH.write_text(
""",
        """    manifest["classificationFingerprint"] = classification_fingerprint(records)
    manifest["recordFingerprint"] = manifest["classificationFingerprint"]
    manifest["fingerprintFields"] = [
        "benchmark", "reference", "year", "domain", "protocol",
        "metrics", "data", "targets", "subtargets",
    ]
    MANIFEST_PATH.write_text(
""",
        "manifest fingerprint",
    )

    text = replace_once(
        text,
        """        "classificationFingerprint": manifest["classificationFingerprint"],
        "dimensions": 4,
""",
        """        "classificationFingerprint": manifest["classificationFingerprint"],
        "recordFingerprint": manifest["recordFingerprint"],
        "fingerprintFields": manifest["fingerprintFields"],
        "dimensions": 4,
""",
        "metadata fingerprint",
    )
    GENERATOR.write_text(text, encoding="utf-8")


def patch_validator() -> None:
    text = VALIDATOR.read_text(encoding="utf-8")
    text = re.sub(
        r'EXPECTED_FINGERPRINT = "[0-9a-f]{64}"',
        f'EXPECTED_FINGERPRINT = "{EXPECTED_FINGERPRINT}"',
        text,
        count=1,
    )

    old_fingerprint = """def fingerprint(records: dict[str, list]) -> str:
    rows = [
        f"{name}|{row[0]}|{row[6]}|{row[7]}"
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\\n".join(rows).encode("utf-8")).hexdigest()
"""
    new_fingerprint = """def fingerprint(records: dict[str, list]) -> str:
    \"\"\"Hash every PDF-coded field in the compact benchmark records.\"\"\"
    rows = [
        f"{name}|" + "|".join(str(value) for value in row[:8])
        for name, row in sorted(records.items())
    ]
    return hashlib.sha256("\\n".join(rows).encode("utf-8")).hexdigest()
"""
    if old_fingerprint in text:
        text = text.replace(old_fingerprint, new_fingerprint, 1)
    elif new_fingerprint not in text:
        raise RuntimeError("Validator fingerprint function was not recognized")

    old_checks = """    require(fingerprint(records) == EXPECTED_FINGERPRINT, "Reference/category classification fingerprint differs from the PDF transcription")
    require(manifest.get("classificationFingerprint") == EXPECTED_FINGERPRINT, "Manifest fingerprint is missing or stale")
"""
    new_checks = """    require(fingerprint(records) == EXPECTED_FINGERPRINT, "Full PDF record fingerprint differs from the Tables 3–9 transcription")
    require(manifest.get("classificationFingerprint") == EXPECTED_FINGERPRINT, "Manifest classification fingerprint is missing or stale")
    require(manifest.get("recordFingerprint") == EXPECTED_FINGERPRINT, "Manifest record fingerprint is missing or stale")
    require(manifest.get("fingerprintFields") == [
        "benchmark", "reference", "year", "domain", "protocol",
        "metrics", "data", "targets", "subtargets",
    ], "Manifest fingerprint field declaration is missing or stale")
"""
    if old_checks in text:
        text = text.replace(old_checks, new_checks, 1)
    elif new_checks not in text:
        raise RuntimeError("Validator manifest checks were not recognized")

    old_metadata = '    require(metadata["classificationFingerprint"] == EXPECTED_FINGERPRINT, "metadata.json fingerprint differs")\n'
    new_metadata = """    require(metadata["classificationFingerprint"] == EXPECTED_FINGERPRINT, "metadata.json classification fingerprint differs")
    require(metadata["recordFingerprint"] == EXPECTED_FINGERPRINT, "metadata.json record fingerprint differs")
    require(metadata["fingerprintFields"] == manifest["fingerprintFields"], "metadata.json fingerprint fields differ")
"""
    if old_metadata in text:
        text = text.replace(old_metadata, new_metadata, 1)
    elif new_metadata not in text:
        raise RuntimeError("Validator metadata checks were not recognized")

    text = text.replace(
        '"106 benchmarks, 85 cross-category, exact Figure 4/Table 3–9 classification."',
        '"106 benchmarks, 85 cross-category, and every Table 3–9 record field."',
    )
    VALIDATOR.write_text(text, encoding="utf-8")


def main() -> None:
    patch_generator()
    patch_validator()
    print(
        "Integrated exact Tables 3–9 year/domain/protocol/metrics/data fields; "
        f"full record fingerprint: {EXPECTED_FINGERPRINT}"
    )


if __name__ == "__main__":
    main()
