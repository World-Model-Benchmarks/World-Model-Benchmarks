# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://world-model-benchmarks.github.io/World-Model-Benchmarks/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-102-2f8f63)](https://world-model-benchmarks.github.io/World-Model-Benchmarks/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **102 representative benchmarks** published from **2018–2026**; **85** span more than one evaluation-target category. The corpus was last checked on August 31, 2026.

The classification below follows Figure 4 and Tables 3–9 of the latest PDF. Rows are intentionally repeated when a benchmark belongs to multiple evaluation targets or sub-targets. `△` marks a benchmark assigned to more than one top-level evaluation target.

Each table is a literature index with **Article**, **Year**, **Venue**, **Code**, and **Project Page**. `-` means that no verified public link is currently recorded.

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

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | NeurIPS D&B Spotlight | - | - |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | arXiv | - | - |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | arXiv | - | - |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - |
| [**SurgWMBench △**](https://arxiv.org/abs/2608.08070) | 2026 | arXiv | - | - |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**WorldEcho △**](https://arxiv.org/abs/2608.24885) | 2026 | arXiv | - | - |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | arXiv | - | - |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | arXiv | - | - |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | arXiv | - | - |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - |

### Temporal Quality

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | NeurIPS D&B Spotlight | - | - |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | arXiv | - | - |
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | arXiv | - | - |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | arXiv | - | - |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - |
| [**CrashTwin △**](https://arxiv.org/abs/2606.28757) | 2026 | arXiv | - | - |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - |
| [**SurgWMBench △**](https://arxiv.org/abs/2608.08070) | 2026 | arXiv | - | - |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**WorldEcho △**](https://arxiv.org/abs/2608.24885) | 2026 | arXiv | - | - |
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | arXiv | - | - |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | arXiv | - | - |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - |

## Spatial and State Consistency

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | arXiv | - | - |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | arXiv | - | - |
| [**LoopNav △**](https://arxiv.org/abs/2505.22976) | 2025 | arXiv | - | - |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | - | - |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - |
| [**CrashTwin △**](https://arxiv.org/abs/2606.28757) | 2026 | arXiv | - | - |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - |
| [**Chess-World-Model △**](https://arxiv.org/abs/2605.30100) | 2026 | arXiv | - | - |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - |
| [**SurgWMBench △**](https://arxiv.org/abs/2608.08070) | 2026 | arXiv | - | - |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | arXiv | - | - |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**IntPhys 2 △**](https://arxiv.org/abs/2506.09849) | 2025 | arXiv | - | - |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | arXiv | - | - |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - |
| [**IntPhys △**](https://arxiv.org/abs/1803.07616) | 2018 | arXiv | - | - |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | - | - |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**WorldBench △**](https://arxiv.org/abs/2601.21282) | 2026 | arXiv | - | - |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - |

## Long-Horizon Memory and State Persistence

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | arXiv | - | - |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - |
| [**Chess-World-Model △**](https://arxiv.org/abs/2605.30100) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**LoopNav △**](https://arxiv.org/abs/2505.22976) | 2025 | arXiv | - | - |
| [**ExPhy △**](https://arxiv.org/abs/2608.20009) | 2026 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |

## Physical Plausibility

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**IntPhys △**](https://arxiv.org/abs/1803.07616) | 2018 | arXiv | - | - |
| [**IntPhys 2 △**](https://arxiv.org/abs/2506.09849) | 2025 | arXiv | - | - |
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | - | - |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | ICLR | - | - |
| [**PHYRE**](https://scholar.google.com/scholar?q=PHYRE%3A%20A%20new%20benchmark%20for%20physical%20reasoning) | 2019 | NeurIPS | - | - |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | - | - |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS D&B | - | - |
| [**Physion++**](https://scholar.google.com/scholar?q=Physion%2B%2B%3A%20Evaluating%20physical%20scene%20understanding%20that%20requires%20online%20inference%20of%20different%20physical%20properties) | 2023 | NeurIPS | - | - |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | - |
| [**ContPhy △**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | ICML | - | - |
| [**PhyCoBench**](https://arxiv.org/abs/2502.05503) | 2025 | arXiv | - | - |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | arXiv | - | - |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | arXiv | - | - |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | arXiv | - | - |
| [**T2VPhysBench**](https://arxiv.org/abs/2505.00337) | 2025 | arXiv | - | - |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | arXiv | - | - |
| [**WorldBench △**](https://arxiv.org/abs/2601.21282) | 2026 | arXiv | - | - |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | arXiv | - | - |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | - | - |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - |
| [**Morpheus**](https://arxiv.org/abs/2504.02918) | 2025 | arXiv | - | - |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | arXiv | - | - |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | arXiv | - | - |
| [**PhyGround**](https://arxiv.org/abs/2605.10806) | 2026 | arXiv | - | - |
| [**Physion-Eval**](https://arxiv.org/abs/2603.19607) | 2026 | arXiv | - | - |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | arXiv | - | - |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - |
| [**PhysicsMind △**](https://arxiv.org/abs/2601.16007) | 2026 | arXiv | - | - |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | arXiv | - | - |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | - | - |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - |
| [**KineBench △**](https://arxiv.org/abs/2607.19876) | 2026 | arXiv | - | - |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - |
| [**CrashTwin △**](https://arxiv.org/abs/2606.28757) | 2026 | arXiv | - | - |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - |
| [**ReactSim-Bench △**](https://arxiv.org/abs/2606.14058) | 2026 | arXiv | - | - |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - |
| [**GAUGE**](https://arxiv.org/abs/2608.05948) | 2026 | arXiv | - | - |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**CaliBench**](https://arxiv.org/abs/2608.16829) | 2026 | arXiv | - | - |
| [**WorldSimProbe △**](https://arxiv.org/abs/2608.09298) | 2026 | arXiv | - | - |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - |
| [**ExPhy △**](https://arxiv.org/abs/2608.20009) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | arXiv | - | - |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | arXiv | - | - |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - |

## Causal and Counterfactual Reasoning

### Observation-Grounded Evaluation

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | - | - |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS D&B | - | - |
| [**Causal-VidQA**](https://arxiv.org/abs/2205.14895) | 2022 | arXiv | - | - |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | - | - |
| [**ACQUIRED**](https://arxiv.org/abs/2311.01620) | 2023 | arXiv | - | - |
| [**MMWorld**](https://scholar.google.com/scholar?q=MMWorld%3A%20Towards%20multi-discipline%20multi-faceted%20world%20model%20evaluation%20in%20videos) | 2025 | ICLR | - | - |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | arXiv | - | - |
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | arXiv | - | - |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | arXiv | - | - |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - |
| [**CausalVQA**](https://arxiv.org/abs/2506.09943) | 2025 | arXiv | - | - |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | - | - |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**ContPhy △**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | ICML | - | - |
| [**PhysicsMind △**](https://arxiv.org/abs/2601.16007) | 2026 | arXiv | - | - |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - |

### Intervention-Grounded Evaluation

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | - | - |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | - | - |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | ICLR | - | - |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | - |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - |
| [**ReactSim-Bench △**](https://arxiv.org/abs/2606.14058) | 2026 | arXiv | - | - |
| [**WorldSimProbe △**](https://arxiv.org/abs/2608.09298) | 2026 | arXiv | - | - |

## Control Fidelity and Interactive Dynamics

### Pre-specified Control Fidelity

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | arXiv | - | - |
| [**StoryEval**](https://arxiv.org/abs/2412.16211) | 2024 | arXiv | - | - |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | arXiv | - | - |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | arXiv | - | - |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | arXiv | - | - |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | arXiv | - | - |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | arXiv | - | - |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | arXiv | - | - |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | arXiv | - | - |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | - | - |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | arXiv | - | - |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | arXiv | - | - |
| [**ACT-Bench**](https://arxiv.org/abs/2412.05337) | 2024 | arXiv | - | - |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | - | - |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | arXiv | - | - |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | arXiv | - | - |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | - | - |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | - | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | - | - |
| [**KineBench △**](https://arxiv.org/abs/2607.19876) | 2026 | arXiv | - | - |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - |
| [**MemoBench △**](https://arxiv.org/abs/2606.27537) | 2026 | arXiv | - | - |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - |
| [**Chess-World-Model △**](https://arxiv.org/abs/2605.30100) | 2026 | arXiv | - | - |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - |
| [**H2R-Bench △**](https://arxiv.org/abs/2608.13049) | 2026 | arXiv | - | - |
| [**WorldSimProbe △**](https://arxiv.org/abs/2608.09298) | 2026 | arXiv | - | - |
| [**XEWorld △**](https://arxiv.org/abs/2608.05799) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**WorldEcho △**](https://arxiv.org/abs/2608.24885) | 2026 | arXiv | - | - |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | arXiv | - | - |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | - | - |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |

### Interactive Action Fidelity

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | - | - |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**WorldRoamBench △**](https://arxiv.org/abs/2606.31672) | 2026 | arXiv | - | - |
| [**ReactSim-Bench △**](https://arxiv.org/abs/2606.14058) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |

## Functional Utility

### World Model as Data Engine

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - |

### World Model as Policy Evaluator

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |

### World Model as Planner

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | - | - |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - |
| [**World-in-World**](https://arxiv.org/abs/2510.18135) | 2025 | arXiv | - | - |
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | arXiv | - | - |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | arXiv | - | - |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | arXiv | - | - |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | arXiv | - | - |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - |
| [**KineBench △**](https://arxiv.org/abs/2607.19876) | 2026 | arXiv | - | - |

### World Model as Interactive Training Environment

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | - | - |

## Machine-readable data

- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical taxonomy manifest and compact record coding
- [`docs/assets/benchmarks-1.json`](docs/assets/benchmarks-1.json)–[`benchmarks-4.json`](docs/assets/benchmarks-4.json): normalized benchmark records used by the explorer
- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels, counts, and release-window definitions
- [Interactive project page](https://world-model-benchmarks.github.io/World-Model-Benchmarks/)
