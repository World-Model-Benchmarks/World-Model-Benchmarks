# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://world-model-benchmarks.github.io/World-Model-Benchmarks/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-106-2f8f63)](https://world-model-benchmarks.github.io/World-Model-Benchmarks/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **106 representative benchmarks** published from **2018–2026**; **85** span more than one evaluation-target category. The corpus was last checked on August 31, 2026.

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
| Causal & Counterfactual Reasoning | 37 |
| Control Fidelity & Interactive Dynamics | 55 |
| Functional Utility | 13 |

Counts overlap because cross-category benchmarks appear in more than one top-level target.

## Visual and Temporal Quality

### Visual Quality

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | NeurIPS Datasets and Benchmarks Spotlight | [Code](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) | [Project Page](https://pku-yuangroup.github.io/ChronoMagic-Bench/) |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | [Code](https://github.com/haoyi-duan/WorldScore) | [Project Page](https://haoyi-duan.github.io/WorldScore/) |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | ICCV | [Code](https://github.com/AMAP-ML/VMBench) | [Project Page](https://amap-ml.github.io/VMBench-Website/) |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | BMVC | [Code](https://github.com/AgibotTech/EWMBench) | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | CVPR | - | - |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | [Code](https://github.com/DAGroup-PKU/ReVidgen) | [Project Page](https://dagroup-pku.github.io/ReVidgen.github.io/) |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | [Code](https://github.com/SHI-Labs/physical-ai-bench) | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | [Code](https://github.com/amap-cvlab/ABot-PhysWorld) | - |
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
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | ICCV | [Code](https://github.com/quanhaol/MagicMotion) | [Project Page](https://quanhaol.github.io/magicmotion-site/) |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | NeurIPS | [Code](https://github.com/ali-vilab/Wan-Move) | [Project Page](https://wan-move.github.io/) |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | [Code](https://github.com/AMAP-ML/Omni-WorldBench) | - |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | ACL | - | - |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | WACV | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | NeurIPS | [Code](https://github.com/WorldModelBench-Team/WorldModelBench) | [Project Page](https://worldmodelbench-team.github.io) |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | ICML | - | [Project Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - |

### Temporal Quality

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | NeurIPS Datasets and Benchmarks Spotlight | [Code](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) | [Project Page](https://pku-yuangroup.github.io/ChronoMagic-Bench/) |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | ICCV | [Code](https://github.com/AMAP-ML/VMBench) | [Project Page](https://amap-ml.github.io/VMBench-Website/) |
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | ACL Findings | [Code](https://github.com/weixi-feng/TC-Bench) | [Project Page](https://weixi-feng.github.io/tc-bench/) |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | [Code](https://github.com/haoyi-duan/WorldScore) | [Project Page](https://haoyi-duan.github.io/WorldScore/) |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | BMVC | [Code](https://github.com/AgibotTech/EWMBench) | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | CVPR | - | - |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | [Code](https://github.com/DAGroup-PKU/ReVidgen) | [Project Page](https://dagroup-pku.github.io/ReVidgen.github.io/) |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | [Code](https://github.com/SHI-Labs/physical-ai-bench) | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | [Code](https://github.com/amap-cvlab/ABot-PhysWorld) | - |
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
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | ICML | [Code](https://github.com/litwellchi/EmbodiedVideoAnticipator) | [Project Page](https://sites.google.com/view/eva-public) |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | ICCV | [Code](https://github.com/quanhaol/MagicMotion) | [Project Page](https://quanhaol.github.io/magicmotion-site/) |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | NeurIPS | [Code](https://github.com/ali-vilab/Wan-Move) | [Project Page](https://wan-move.github.io/) |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | [Code](https://github.com/AMAP-ML/Omni-WorldBench) | - |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | WACV | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | NeurIPS | [Code](https://github.com/WorldModelBench-Team/WorldModelBench) | [Project Page](https://worldmodelbench-team.github.io) |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - |

## Spatial and State Consistency

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | BMVC | [Code](https://github.com/AgibotTech/EWMBench) | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | [Code](https://github.com/haoyi-duan/WorldScore) | [Project Page](https://haoyi-duan.github.io/WorldScore/) |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
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
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | [Code](https://github.com/DAGroup-PKU/ReVidgen) | [Project Page](https://dagroup-pku.github.io/ReVidgen.github.io/) |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | [Code](https://github.com/facebookresearch/minimal_video_pairs) | [Project Page](https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/) |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | [Code](https://github.com/SHI-Labs/physical-ai-bench) | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | [Code](https://github.com/amap-cvlab/ABot-PhysWorld) | - |
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
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | ICML | [Code](https://github.com/litwellchi/EmbodiedVideoAnticipator) | [Project Page](https://sites.google.com/view/eva-public) |
| [**Gen-ViRe △**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**IntPhys 2 △**](https://arxiv.org/abs/2506.09849) | 2025 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/facebookresearch/IntPhys2) | - |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | [Code](https://github.com/AMAP-ML/Omni-WorldBench) | - |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | ACL | - | - |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | CVPR | - | - |
| [**IntPhys △**](https://arxiv.org/abs/1803.07616) | 2018 | IEEE TPAMI | - | [Project Page](https://intphys.cognitive-ml.fr/download.html) |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**WorldBench △**](https://arxiv.org/abs/2601.21282) | 2026 | arXiv | - | [Project Page](https://world-bench.github.io/) |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | ICML | - | [Project Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**Apple-π △**](https://arxiv.org/abs/2607.16401) | 2026 | arXiv | - | - |

## Long-Horizon Memory and State Persistence

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | ICML Workshop | - | [Project Page](https://github.com/worldprediction/worldprediction.github.io) |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**HTEWorld △**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | [Code](https://github.com/DAGroup-PKU/ReVidgen) | [Project Page](https://dagroup-pku.github.io/ReVidgen.github.io/) |
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
| [**IntPhys △**](https://arxiv.org/abs/1803.07616) | 2018 | IEEE TPAMI | - | [Project Page](https://intphys.cognitive-ml.fr/download.html) |
| [**IntPhys 2 △**](https://arxiv.org/abs/2506.09849) | 2025 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/facebookresearch/IntPhys2) | - |
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | [Code](https://github.com/chuangg/CLEVRER) | [Project Page](http://clevrer.csail.mit.edu) |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**PHYRE**](https://scholar.google.com/scholar?q=PHYRE%3A%20A%20new%20benchmark%20for%20physical%20reasoning) | 2019 | NeurIPS | [Code](https://github.com/facebookresearch/phyre) | [Project Page](https://player.phyre.ai) |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | [Code](https://github.com/hucvl/craft) | - |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) | [Project Page](https://physion-benchmark.github.io/) |
| [**Physion++**](https://scholar.google.com/scholar?q=Physion%2B%2B%3A%20Evaluating%20physical%20scene%20understanding%20that%20requires%20online%20inference%20of%20different%20physical%20properties) | 2023 | NeurIPS | - | [Project Page](https://dingmyu.github.io/physion_v2/) |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**ContPhy △**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | ICML | - | [Project Page](https://physical-reasoning-project.github.io/) |
| [**PhyCoBench**](https://arxiv.org/abs/2502.05503) | 2025 | arXiv | [Code](https://github.com/Jeckinchen/PhyCoBench) | - |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | - |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | [Project Page](https://videophy2.github.io/) |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | ICML | [Code](https://github.com/OpenGVLab/PhyGenBench) | [Project Page](https://phygenbench123.github.io/) |
| [**T2VPhysBench**](https://arxiv.org/abs/2505.00337) | 2025 | arXiv | - | - |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | WACV | [Code](https://github.com/google-deepmind/physics-iq-benchmark) | [Project Page](https://physics-iq.github.io/) |
| [**WorldBench △**](https://arxiv.org/abs/2601.21282) | 2026 | arXiv | - | [Project Page](https://world-bench.github.io/) |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | ICLR | [Code](https://github.com/g-jing/phy-world-bench) | [Project Page](https://research.nvidia.com/labs/dir/phyworldbench/) |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | WACV | - | - |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | NeurIPS | [Code](https://github.com/WorldModelBench-Team/WorldModelBench) | [Project Page](https://worldmodelbench-team.github.io) |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**RigidBench △**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - |
| [**Morpheus**](https://arxiv.org/abs/2504.02918) | 2025 | arXiv | - | - |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | CoRL | [Code](https://github.com/NVIDIA/GR00T-Dreams) | [Project Page](https://research.nvidia.com/labs/gear/dreamgen/) |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
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
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | [Code](https://github.com/DAGroup-PKU/ReVidgen) | [Project Page](https://dagroup-pku.github.io/ReVidgen.github.io/) |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | [Code](https://github.com/facebookresearch/minimal_video_pairs) | [Project Page](https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/) |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | [Code](https://github.com/SHI-Labs/physical-ai-bench) | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | [Code](https://github.com/amap-cvlab/ABot-PhysWorld) | - |
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
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | [Code](https://github.com/AMAP-ML/Omni-WorldBench) | - |
| [**PEDRA △**](https://arxiv.org/abs/2510.20182) | 2025 | CVPR | - | - |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**SmallWorlds △**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |
| [**VMBench △**](https://arxiv.org/abs/2503.10076) | 2025 | ICCV | [Code](https://github.com/AMAP-ML/VMBench) | [Project Page](https://amap-ml.github.io/VMBench-Website/) |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | ICML | - | [Project Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | BMVC | [Code](https://github.com/AgibotTech/EWMBench) | - |

## Causal and Counterfactual Reasoning

### Observation-Grounded Evaluation

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | [Code](https://github.com/chuangg/CLEVRER) | [Project Page](http://clevrer.csail.mit.edu) |
| [**CATER**](https://scholar.google.com/scholar?q=CATER%3A%20A%20diagnostic%20dataset%20for%20compositional%20actions%20and%20temporal%20reasoning) | 2020 | ICLR | [Code](https://github.com/rohitgirdhar/CATER) | - |
| [**NExT-QA**](https://arxiv.org/abs/2105.08276) | 2021 | CVPR | [Code](https://github.com/doc-doc/NExT-QA) | - |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) | [Project Page](https://physion-benchmark.github.io/) |
| [**Causal-VidQA**](https://arxiv.org/abs/2205.14895) | 2022 | CVPR | [Code](https://github.com/bcmi/Causal-VidQA) | - |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | [Code](https://github.com/hucvl/craft) | - |
| [**IntentQA**](https://scholar.google.com/scholar?q=IntentQA%3A%20Context-aware%20video%20intent%20reasoning) | 2023 | ICCV | [Code](https://github.com/JoseponLee/IntentQA) | - |
| [**ACQUIRED**](https://arxiv.org/abs/2311.01620) | 2023 | EMNLP | [Code](https://github.com/PlusLabNLP/acquired) | - |
| [**MMWorld**](https://scholar.google.com/scholar?q=MMWorld%3A%20Towards%20multi-discipline%20multi-faceted%20world%20model%20evaluation%20in%20videos) | 2025 | ICLR | [Code](https://github.com/UCSB-AI/MMWorld) | [Project Page](https://mmworld-bench.github.io/) |
| [**VCRBench**](https://arxiv.org/abs/2505.08455) | 2025 | CVPR Workshop | [Code](https://github.com/pritamqu/VCRBench) | [Project Page](https://pritamqu.github.io/VCRBench/) |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | WACV | [Code](https://github.com/google-deepmind/physics-iq-benchmark) | [Project Page](https://physics-iq.github.io/) |
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | ICML Workshop | - | [Project Page](https://github.com/worldprediction/worldprediction.github.io) |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | WACV | - | - |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - |
| [**CausalVQA**](https://arxiv.org/abs/2506.09943) | 2025 | arXiv | [Code](https://github.com/facebookresearch/CausalVQA) | [Project Page](https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/) |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | arXiv | - | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | [Code](https://github.com/DAGroup-PKU/ReVidgen) | [Project Page](https://dagroup-pku.github.io/ReVidgen.github.io/) |
| [**MVP △**](https://arxiv.org/abs/2506.09987) | 2025 | arXiv | [Code](https://github.com/facebookresearch/minimal_video_pairs) | [Project Page](https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/) |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | [Code](https://github.com/SHI-Labs/physical-ai-bench) | - |
| [**RoboTrustBench △**](https://arxiv.org/abs/2606.01600) | 2026 | arXiv | - | - |
| [**MiraBench △**](https://arxiv.org/abs/2605.29360) | 2026 | arXiv | - | - |
| [**PlayWorld △**](https://arxiv.org/abs/2608.13552) | 2026 | arXiv | - | - |
| [**HarnessEval-W △**](https://arxiv.org/abs/2608.16859) | 2026 | arXiv | - | - |
| [**ContPhy △**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | ICML | - | [Project Page](https://physical-reasoning-project.github.io/) |
| [**PhysicsMind △**](https://arxiv.org/abs/2601.16007) | 2026 | arXiv | - | - |
| [**WorldExam △**](https://arxiv.org/abs/2608.02603) | 2026 | arXiv | - | - |

### Intervention-Grounded Evaluation

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | [Code](https://github.com/chuangg/CLEVRER) | [Project Page](http://clevrer.csail.mit.edu) |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | [Code](https://github.com/hucvl/craft) | - |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - |
| [**ScratchWorld △**](https://arxiv.org/abs/2606.31689) | 2026 | arXiv | - | - |
| [**ReactSim-Bench △**](https://arxiv.org/abs/2606.14058) | 2026 | arXiv | - | - |
| [**WorldSimProbe △**](https://arxiv.org/abs/2608.09298) | 2026 | arXiv | - | - |

## Control Fidelity and Interactive Dynamics

### Pre-specified Control Fidelity

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | ACL Findings | [Code](https://github.com/weixi-feng/TC-Bench) | [Project Page](https://weixi-feng.github.io/tc-bench/) |
| [**StoryEval**](https://arxiv.org/abs/2412.16211) | 2024 | CVPR | [Code](https://github.com/ypwang61/StoryEval) | [Project Page](https://ypwang61.github.io/project/StoryEval/) |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | - |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | [Project Page](https://videophy2.github.io/) |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | ICML | [Code](https://github.com/OpenGVLab/PhyGenBench) | [Project Page](https://phygenbench123.github.io/) |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | ICLR | [Code](https://github.com/g-jing/phy-world-bench) | [Project Page](https://research.nvidia.com/labs/dir/phyworldbench/) |
| [**OSCBench △**](https://arxiv.org/abs/2603.11698) | 2026 | ACL | - | - |
| [**MoveBench △**](https://arxiv.org/abs/2512.08765) | 2025 | NeurIPS | [Code](https://github.com/ali-vilab/Wan-Move) | [Project Page](https://wan-move.github.io/) |
| [**MagicBench △**](https://arxiv.org/abs/2503.16421) | 2025 | ICCV | [Code](https://github.com/quanhaol/MagicMotion) | [Project Page](https://quanhaol.github.io/magicmotion-site/) |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | [Code](https://github.com/haoyi-duan/WorldScore) | [Project Page](https://haoyi-duan.github.io/WorldScore/) |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**ACT-Bench**](https://arxiv.org/abs/2412.05337) | 2024 | arXiv | - | - |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**Omni-WorldBench △**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | [Code](https://github.com/AMAP-ML/Omni-WorldBench) | - |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | CoRL | [Code](https://github.com/NVIDIA/GR00T-Dreams) | [Project Page](https://research.nvidia.com/labs/gear/dreamgen/) |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | NeurIPS | [Code](https://github.com/WorldModelBench-Team/WorldModelBench) | [Project Page](https://worldmodelbench-team.github.io) |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**RBench △**](https://arxiv.org/abs/2601.15282) | 2026 | ICML | [Code](https://github.com/DAGroup-PKU/ReVidgen) | [Project Page](https://dagroup-pku.github.io/ReVidgen.github.io/) |
| [**PAI-Bench △**](https://arxiv.org/abs/2512.01989) | 2025 | CVPR | [Code](https://github.com/SHI-Labs/physical-ai-bench) | - |
| [**EZS-Bench △**](https://arxiv.org/abs/2603.23376) | 2026 | arXiv | [Code](https://github.com/amap-cvlab/ABot-PhysWorld) | - |
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
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | BMVC | [Code](https://github.com/AgibotTech/EWMBench) | - |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |

### Interactive Action Fidelity

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | ICML | - | [Project Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
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
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |

### World Model as Policy Evaluator

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WMBench △**](https://arxiv.org/abs/2607.02642) | 2026 | arXiv | - | - |

### World Model as Planner

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**World-in-World**](https://arxiv.org/abs/2510.18135) | 2025 | ICLR | [Code](https://github.com/World-In-World/world-in-world) | [Project Page](https://world-in-world.github.io/) |
| [**EVA-Bench △**](https://arxiv.org/abs/2410.15461) | 2024 | ICML | [Code](https://github.com/litwellchi/EmbodiedVideoAnticipator) | [Project Page](https://sites.google.com/view/eva-public) |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | ICML | - | [Project Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**WoW-World-Eval △**](https://arxiv.org/abs/2601.04137) | 2026 | arXiv | - | - |
| [**AutumnBench △**](https://arxiv.org/abs/2510.19788) | 2025 | ICML | - | - |
| [**ContactWorld △**](https://arxiv.org/abs/2606.13877) | 2026 | arXiv | - | - |
| [**KineBench △**](https://arxiv.org/abs/2607.19876) | 2026 | arXiv | - | - |

### World Model as Interactive Training Environment

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |

## Machine-readable data

- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical taxonomy manifest and compact record coding
- [`docs/assets/benchmarks-1.json`](docs/assets/benchmarks-1.json)–[`benchmarks-4.json`](docs/assets/benchmarks-4.json): normalized benchmark records used by the explorer
- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels, counts, and release-window definitions
- [Interactive project page](https://world-model-benchmarks.github.io/World-Model-Benchmarks/)
