# 05_Thermodynamic_Stability_Ensemble - JARVIS Database

## Dataset Use

A DFT-based materials database offering structural, electronic, and thermodynamic properties for ~100,000+ materials, curated for data-driven design. Used to benchmark ECSG’s classification performance (achieving AUC = 0.988) and as an independent convex hull reference for validating DFT-predicted stability of double perovskite oxides selected by ECSG.

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- Dataset: [JARVIS Database](../datasets/JARVIS_Database.md)
- Dataset URL: None

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_992fc756b44d`
- Original dataset title: JARVIS (Joint Automated Repository for Various Integrated Simulations)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
