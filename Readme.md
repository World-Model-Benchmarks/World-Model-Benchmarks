# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://world-model-benchmarks.github.io/World-Model-Benchmarks/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-102-2f8f63)](https://world-model-benchmarks.github.io/World-Model-Benchmarks/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **102 representative benchmarks** released from **2018–2026**; **85** span more than one evaluation-target category. The corpus was last checked on August 31, 2026.

The classification below follows Figure 4 and Tables 3–9 of the latest PDF. Rows are intentionally repeated when a benchmark belongs to multiple evaluation targets or sub-targets. `△` marks a benchmark assigned to more than one top-level evaluation target.

Each table is a literature index with **Article**, **Release Year**, **Venue**, **Code**, and **Project Page**. Release Year follows the September 7, 2026 manuscript, not the formal publication year; the latter is shown separately with the venue where recorded. `-` means that no verified public link is currently recorded.

Protocol and Metrics are coded for the target or role of each section, not inherited from other tracks. P = Prediction-Level Metrics; O = Downstream Outcome Metrics. P+O and OL+CL retain both relevant evidence/protocol types. See the target-scoped coding in the machine-readable manifest.

## Contents

- [Visual and Temporal Quality](#visual-and-temporal-quality)
- [Spatial and State Consistency](#spatial-and-state-consistency)
- [Long-Horizon Memory and State Persistence](#long-horizon-memory-and-state-persistence)
- [Physical Plausibility](#physical-plausibility)
- [Causal and Counterfactual Reasoning](#causal-and-counterfactual-reasoning)
- [Control Fidelity and Interactive Dynamics](#control-fidelity-and-interactive-dynamics)
- [Functional Utility](#functional-utility)

## Evaluation-target coverage

| Evaluation target | Benchmarks |
|:--|--:|
| Visual & Temporal Quality | 46 |
| Spatial & State Consistency | 55 |
| Long-Horizon Memory & State Persistence | 24 |
| Physical Plausibility | 77 |
| Causal & Counterfactual Reasoning | 33 |
| Control Fidelity & Interactive Dynamics | 55 |
| Functional Utility | 13 |

Counts overlap because cross-category benchmarks appear in more than one top-level target.

## Visual and Temporal Quality

### Visual Quality

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | NeurIPS D&B Spotlight | - | - | OL | P |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - | OL | P |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | arXiv | - | - | OL | P |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - | OL | P |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | OL | P |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - | OL | P |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - | OL | P |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - | OL | P |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2025 | CVPR 2026 | - | - | OL | P |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - | OL | P |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - | OL | P |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - | OL | P |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - | OL | P |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - | OL | P |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - | OL | P |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - | OL | P |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - | OL | P |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - | OL | P |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - | OL | P |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - | OL | P |
| [**SurgWMBench △**](https://arxiv.org/abs/2608.08070) | 2026 | arXiv | - | - | OL | P |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - | OL | P |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - | CL | P |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - | OL | P |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - | OL | P |
| [**WorldEcho △**](https://arxiv.org/abs/2608.24885) | 2026 | arXiv | - | - | OL | P |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - | OL | P |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - | OL | P |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - | OL | P |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | arXiv | - | - | OL | P |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - | OL | P |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | arXiv | - | - | OL | P |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - | OL | P |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | arXiv | - | - | OL | P |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - | OL | P |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - | CL | P |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - | OL | P |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - | OL | P |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - | OL | P |

### Temporal Quality

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | NeurIPS D&B Spotlight | - | - | OL | P |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | arXiv | - | - | OL | P |
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | arXiv | - | - | OL | P |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - | OL | P |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - | OL | P |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - | OL | P |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - | OL | P |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - | OL | P |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - | OL | P |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | OL | P |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - | OL | P |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2025 | CVPR 2026 | - | - | OL | P |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - | OL | P |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - | OL | P |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - | OL | P |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - | OL | P |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - | OL | P |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - | OL | P |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - | OL | P |
| [**CrashTwin △**](https://arxiv.org/abs/2606.28757) | 2026 | arXiv | - | - | OL | P |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - | OL | P |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - | OL | P |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - | OL | P |
| [**SurgWMBench △**](https://arxiv.org/abs/2608.08070) | 2026 | arXiv | - | - | OL | P |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - | OL | P |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - | CL | P |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - | OL | P |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - | OL | P |
| [**WorldEcho △**](https://arxiv.org/abs/2608.24885) | 2026 | arXiv | - | - | OL | P |
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | arXiv | - | - | OL | P |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - | OL | P |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | arXiv | - | - | OL | P |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | arXiv | - | - | OL | P |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - | OL | P |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - | OL | P |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - | CL | P |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - | OL | P |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - | OL | P |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - | OL | P |

## Spatial and State Consistency

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - | OL | P |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - | OL | P |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - | OL | P |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | OL | P |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2025 | CVPR 2026 | - | - | OL | P |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - | OL | P |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - | OL | P |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - | OL | P |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | arXiv | - | - | OL | P |
| [**LoopNav △**](https://arxiv.org/abs/2505.22976) | 2025 | arXiv | - | - | OL | P |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - | OL | P |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - | OL | P |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - | OL | P |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - | OL | P |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - | OL | P |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - | OL | P |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - | OL | P |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - | OL | P |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - | CL | P+O |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | - | - | OL | P |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - | OL | P |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - | OL | P |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - | CL | P+O |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - | OL | P |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - | OL | P |
| [**CrashTwin △**](https://arxiv.org/abs/2606.28757) | 2026 | arXiv | - | - | OL | P |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - | OL | P |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - | OL | P |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - | OL | P |
| [**Chess-World-Model △**](https://arxiv.org/abs/2605.30100) | 2026 | arXiv | - | - | OL | P |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - | OL | P |
| [**SurgWMBench △**](https://arxiv.org/abs/2608.08070) | 2026 | arXiv | - | - | OL | P |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - | OL | P |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - | CL | P |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - | OL | P |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - | OL | P |
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | arXiv | - | - | OL | P |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - | OL | P |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - | OL | P |
| [**IntPhys 2 △**](https://arxiv.org/abs/2506.09849) | 2025 | arXiv | - | - | OL | P |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - | OL | P |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - | OL | P |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - | OL | P |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | arXiv | - | - | OL | P |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - | OL | P |
| [**IntPhys △**](https://arxiv.org/abs/1803.07616) | 2018 | arXiv | - | - | OL | P |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - | OL | P |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - | OL | P |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - | CL | P |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | - | - | OL | P |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - | OL | P |
| [**WorldBench △**](https://arxiv.org/abs/2601.21282) | 2026 | arXiv | - | - | OL | P |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - | OL | P |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - | OL | P |

## Long-Horizon Memory and State Persistence

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | arXiv | - | - | OL | P |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - | OL | P |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - | OL | P |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - | OL | P |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - | OL | P |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - | OL | P |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - | OL | P |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - | OL | P |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - | OL | P |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - | OL | O |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - | OL | P |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - | OL | P |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - | CL | P+O |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - | CL | P+O |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - | OL | P |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - | OL | P |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - | OL | P |
| [**Chess-World-Model △**](https://arxiv.org/abs/2605.30100) | 2026 | arXiv | - | - | OL | P |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - | CL | P |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - | OL | P |
| [**LoopNav △**](https://arxiv.org/abs/2505.22976) | 2025 | arXiv | - | - | OL | P |
| [**ExPhy △**](https://arxiv.org/abs/2608.20009) | 2026 | arXiv | - | - | OL | P |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - | CL | P |

## Physical Plausibility

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**IntPhys △**](https://arxiv.org/abs/1803.07616) | 2018 | arXiv | - | - | OL | P |
| [**IntPhys 2 △**](https://arxiv.org/abs/2506.09849) | 2025 | arXiv | - | - | OL | P |
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2019 | ICLR 2020 | - | - | OL | P |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2019 | ICLR 2020 | - | - | OL | P |
| [**PHYRE**](https://scholar.google.com/scholar?q=PHYRE%3A%20A%20new%20benchmark%20for%20physical%20reasoning) | 2019 | NeurIPS | - | - | CL | O |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2020 | Findings of ACL 2022 | - | - | OL | P |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS D&B | - | - | OL | P |
| [**Physion++**](https://scholar.google.com/scholar?q=Physion%2B%2B%3A%20Evaluating%20physical%20scene%20understanding%20that%20requires%20online%20inference%20of%20different%20physical%20properties) | 2023 | NeurIPS | - | - | OL | P |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | - | OL | P |
| [**ContPhy △**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | ICML | - | - | OL | P |
| [**PhyCoBench**](https://arxiv.org/abs/2502.05503) | 2025 | arXiv | - | - | OL | P |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | arXiv | - | - | OL | P |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | arXiv | - | - | OL | P |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | arXiv | - | - | OL | P |
| [**T2VPhysBench**](https://arxiv.org/abs/2505.00337) | 2025 | arXiv | - | - | OL | P |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | arXiv | - | - | OL | P |
| [**WorldBench △**](https://arxiv.org/abs/2601.21282) | 2026 | arXiv | - | - | OL | P |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | arXiv | - | - | OL | P |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - | OL | P |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - | OL | P |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | - | - | OL | P |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - | OL | P |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - | OL | P |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - | OL | P |
| [**Morpheus**](https://arxiv.org/abs/2504.02918) | 2025 | arXiv | - | - | OL | P |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - | OL | P |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - | OL | O |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | arXiv | - | - | OL | P |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2025 | CVPR 2026 | - | - | OL | P |
| [**PhyGround**](https://arxiv.org/abs/2605.10806) | 2026 | arXiv | - | - | OL | P |
| [**Physion-Eval**](https://arxiv.org/abs/2603.19607) | 2026 | arXiv | - | - | OL | P |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | arXiv | - | - | OL | P |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - | OL | P |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - | OL | P |
| [**PhysicsMind △**](https://arxiv.org/abs/2601.16007) | 2026 | arXiv | - | - | OL | P |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | arXiv | - | - | OL | P |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - | OL | P |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - | OL | P |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - | OL | P |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P+O |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - | OL | P |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | - | - | OL | P |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - | OL | P |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - | OL | P |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - | OL | P |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - | CL | P+O |
| [**KineBench △**](https://arxiv.org/abs/2607.19876) | 2026 | arXiv | - | - | CL | P+O |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - | OL | P |
| [**CrashTwin △**](https://arxiv.org/abs/2606.28757) | 2026 | arXiv | - | - | OL | P |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - | OL | P |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - | OL | P |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - | OL | P |
| [**ReactSim-Bench △**](https://arxiv.org/abs/2606.14058) | 2026 | arXiv | - | - | CL | P |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - | OL | P |
| [**GAUGE**](https://arxiv.org/abs/2608.05948) | 2026 | arXiv | - | - | OL | P |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - | OL | P |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - | CL | P |
| [**CaliBench**](https://arxiv.org/abs/2608.16829) | 2026 | arXiv | - | - | OL | P |
| [**WorldSimProbe △**](https://arxiv.org/abs/2608.09298) | 2026 | arXiv | - | - | OL | P |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - | OL | P |
| [**ExPhy △**](https://arxiv.org/abs/2608.20009) | 2026 | arXiv | - | - | OL | P |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - | OL | P |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - | OL | P |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - | OL | P |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - | OL | P |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - | OL | P |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - | OL | P |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - | OL | P |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - | OL | P |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - | OL | P |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - | CL | P |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | arXiv | - | - | OL | P |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - | OL | P |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | OL | P |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - | OL+CL | P+O |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - | OL | P |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - | OL | P |

## Causal and Counterfactual Reasoning

### Observation-Grounded Evaluation

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2019 | ICLR 2020 | - | - | OL | P |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS D&B | - | - | OL | P |
| [**Causal-VidQA**](https://arxiv.org/abs/2205.14895) | 2022 | arXiv | - | - | OL | P |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2020 | Findings of ACL 2022 | - | - | OL | P |
| [**ACQUIRED**](https://arxiv.org/abs/2311.01620) | 2023 | arXiv | - | - | OL | P |
| [**MMWorld**](https://scholar.google.com/scholar?q=MMWorld%3A%20Towards%20multi-discipline%20multi-faceted%20world%20model%20evaluation%20in%20videos) | 2024 | ICLR 2025 | - | - | OL | P |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | arXiv | - | - | OL | P |
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | arXiv | - | - | OL | P |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - | OL | P |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - | OL | P |
| [**CausalVQA**](https://arxiv.org/abs/2506.09943) | 2025 | arXiv | - | - | OL | P |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - | OL | P |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - | OL | P |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - | OL | P |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | arXiv | - | - | OL | P |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - | OL | P |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | - | - | OL | P |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - | OL | P |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - | OL | P |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - | OL | P |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - | CL | P |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - | OL | P |
| [**ContPhy △**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | ICML | - | - | OL | P |
| [**PhysicsMind △**](https://arxiv.org/abs/2601.16007) | 2026 | arXiv | - | - | OL | P |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - | OL | P |

### Intervention-Grounded Evaluation

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2019 | ICLR 2020 | - | - | OL | P |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2020 | Findings of ACL 2022 | - | - | OL | P |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2019 | ICLR 2020 | - | - | OL | P |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | - | OL | P |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - | OL | P |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - | CL | P |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - | OL | P |
| [**ReactSim-Bench △**](https://arxiv.org/abs/2606.14058) | 2026 | arXiv | - | - | CL | P |
| [**WorldSimProbe △**](https://arxiv.org/abs/2608.09298) | 2026 | arXiv | - | - | OL | P |

## Control Fidelity and Interactive Dynamics

### Pre-specified Control Fidelity

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | arXiv | - | - | OL | P |
| [**StoryEval**](https://arxiv.org/abs/2412.16211) | 2024 | arXiv | - | - | OL | P |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | arXiv | - | - | OL | P |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | arXiv | - | - | OL | P |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | arXiv | - | - | OL | P |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | arXiv | - | - | OL | P |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | arXiv | - | - | OL | P |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | arXiv | - | - | OL | P |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | arXiv | - | - | OL | P |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - | OL | P |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - | OL | P |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - | OL | P |
| [**ACT-Bench**](https://arxiv.org/abs/2412.05337) | 2024 | arXiv | - | - | OL | P |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - | OL | P |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - | OL | P |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | arXiv | - | - | OL | P |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - | OL | P |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | - | - | OL | P |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P+O |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - | OL | P |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - | OL | P |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - | OL | P |
| [**KineBench △**](https://arxiv.org/abs/2607.19876) | 2026 | arXiv | - | - | CL | P+O |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - | OL | P |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - | OL | P |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - | OL | P |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - | OL | P |
| [**Chess-World-Model △**](https://arxiv.org/abs/2605.30100) | 2026 | arXiv | - | - | OL | P |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - | OL | P |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - | OL | P |
| [**WorldSimProbe △**](https://arxiv.org/abs/2608.09298) | 2026 | arXiv | - | - | OL | P |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - | OL | P |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - | OL | P |
| [**WorldEcho △**](https://arxiv.org/abs/2608.24885) | 2026 | arXiv | - | - | OL | P |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - | OL | P |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - | OL | P |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - | OL | P |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - | OL | P |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - | OL | P |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | OL | P |

### Interactive Action Fidelity

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - | OL | P |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - | OL | P |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - | OL+CL | P+O |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - | OL | P |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - | OL | P |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - | OL | P |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - | OL | P |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - | OL | O |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - | OL | P |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - | OL | P |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - | OL | P |
| [**ReactSim-Bench △**](https://arxiv.org/abs/2606.14058) | 2026 | arXiv | - | - | CL | P |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - | CL | P |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - | OL | P |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - | CL | P |

## Functional Utility

### World Model as Data Engine

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | OL | O |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - | OL | O |

### World Model as Policy Evaluator

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | CL | O |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - | CL | P+O |

### World Model as Planner

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - | CL | O |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - | OL+CL | O |
| [**World-in-World**](https://arxiv.org/abs/2510.18135) | 2025 | arXiv | - | - | CL | O |
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | arXiv | - | - | OL | O |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2025 | CVPR 2026 | - | - | CL | O |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - | OL | O |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - | CL | O |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - | OL+CL | P+O |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - | OL | P+O |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - | CL | P+O |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - | CL | P+O |
| [**KineBench △**](https://arxiv.org/abs/2607.19876) | 2026 | arXiv | - | - | CL | P+O |

### World Model as Interactive Training Environment

| Article | Release Year | Venue | Code | Project Page | Protocol | Metrics |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - | CL | O |

## Machine-readable data

- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical taxonomy manifest and compact record coding
- [`docs/assets/benchmarks-1.json`](docs/assets/benchmarks-1.json)–[`benchmarks-4.json`](docs/assets/benchmarks-4.json): normalized benchmark records used by the explorer
- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels, counts, and release-window definitions
- [Interactive project page](https://world-model-benchmarks.github.io/World-Model-Benchmarks/)
