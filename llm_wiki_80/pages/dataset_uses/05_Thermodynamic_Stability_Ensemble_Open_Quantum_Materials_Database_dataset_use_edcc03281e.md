# 05_Thermodynamic_Stability_Ensemble - Open Quantum Materials Database

## Dataset Use

A DFT-generated database of predicted inorganic materials, providing formation energies and structural data for over 400,000 compounds. Used alongside MP and JARVIS for cross-database performance validation of ECSG, particularly to assess robustness under class imbalance (11.3% stable samples) and to serve as a reference convex hull for DFT validation of predicted perovskite oxides.

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: None

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_edcc03281ee7`
- Original dataset title: Open Quantum Materials Database (OQMD)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation
