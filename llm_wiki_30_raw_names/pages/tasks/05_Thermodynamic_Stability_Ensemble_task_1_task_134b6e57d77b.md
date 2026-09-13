# 05_Thermodynamic_Stability_Ensemble - Task 1

## Task Description

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Task ID: `task_134b6e57d77b`
- Source paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble_paper_dfa00819e2d0.md)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation

## Supporting Datasets

### [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Materials_Project_MP_dataset_use_set_use_8d0cb093180d.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

A large-scale DFT-computed database containing thermodynamic properties (e.g., formation energy, decomposition energy) for 85,014 inorganic crystalline compounds, including experimentally observed and hypothetical materials. Used as the primary training and benchmarking dataset to train and evaluate the ECSG ensemble model for binary classification of compound stability; also used to construct convex hulls for ΔHd labeling and to extract composition-only samples for sample efficiency analysis.

### [Open Quantum Materials Database (OQMD)](../datasets/Open_Quantum_Materials_Database_OQMD_dataset_443302f4d44c.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Open_Quantum_Materials_Database_O_set_use_4cbf254eebe5.md)
- Original title in paper: Open Quantum Materials Database (OQMD)
- Link: None

A DFT-generated database of predicted inorganic materials, providing formation energies and structural data for over 400,000 compounds. Used alongside MP and JARVIS for cross-database performance validation of ECSG, particularly to assess robustness under class imbalance (11.3% stable samples) and to serve as a reference convex hull for DFT validation of predicted perovskite oxides.

### [JARVIS (Joint Automated Repository for Various Integrated Simulations)](../datasets/JARVIS_Joint_Automated_Repository_for_Various_Integrated_Simulations_dataset_bbdab7ef4ee7.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_JARVIS_Joint_Automated_Repository_set_use_e7632e80ee1b.md)
- Original title in paper: JARVIS (Joint Automated Repository for Various Integrated Simulations)
- Link: None

A DFT-based materials database offering structural, electronic, and thermodynamic properties for ~100,000+ materials, curated for data-driven design. Used to benchmark ECSG’s classification performance (achieving AUC = 0.988) and as an independent convex hull reference for validating DFT-predicted stability of double perovskite oxides selected by ECSG.

### [C2DB (Computational 2D Materials Database)](../datasets/C2DB_Computational_2D_Materials_Database_dataset_73ff91b25d14.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_C2DB_Computational_2D_Materials_D_set_use_0cd4d0bce666.md)
- Original title in paper: C2DB (Computational 2D Materials Database)
- Link: None

A high-throughput DFT database containing structural, electronic, and thermodynamic data for over 4,000 atomically thin 2D materials. Used to train a specialized ECSG variant for predicting thermodynamic stability of 2D materials, supporting the case study on wide-bandgap semiconductor screening.

### [2DMatPedia](../datasets/2DMatPedia_dataset_fb64b91da67e.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_2DMatPedia_dataset_use_cc2c8c8cc4_set_use_cc2c8c8cc41b.md)
- Original title in paper: 2DMatPedia
- Link: None

A computational database of 4,743 2D materials with precomputed bandgaps and stability labels derived from DFT. Used as an independent test set to evaluate ECSG’s stability predictions for 2D materials and to validate the joint screening pipeline (ECSG + DARWIN-7B LLM) for wide-bandgap semiconductors, yielding 313 experimentally stable candidates out of 393 predicted.

### [Perovskite Halides Dataset (literature-curated)](../datasets/Perovskite_Halides_Dataset_literature-curated_dataset_12a3418563ef.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Perovskite_Halides_Dataset_litera_set_use_519dded6e7f0.md)
- Original title in paper: Perovskite Halides Dataset (literature-curated)
- Link: None

A manually compiled dataset of thermodynamic stability labels for 496 perovskite halides (ABX₃, X = Cl/Br/I) extracted from prior literature; duplicates present in MP were removed to ensure independence. Used to evaluate ECSG’s generalization to unknown chemical space — specifically, its ability to predict stability for perovskite halides not represented in the MP training set.

### [Li-containing Oxides Dataset (MP-derived)](../datasets/Li-containing_Oxides_Dataset_MP-derived_dataset_b8405d6f3030.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Li-containing_Oxides_Dataset_MP-d_set_use_f23cb13e399f.md)
- Original title in paper: Li-containing Oxides Dataset (MP-derived)
- Link: None

A subset of 6,168 lithium-containing oxides (750 stable) extracted from the MP database, fully excluded from the MP training set to create a zero-shot evaluation scenario. Used to test ECSG’s predictive capability in a completely unfamiliar compositional space (Li–O systems), demonstrating its utility for cathode material discovery in Li-ion batteries.

### [Transition Metal Oxides Dataset (MP-derived)](../datasets/Transition_Metal_Oxides_Dataset_MP-derived_dataset_c106bbbaba02.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Transition_Metal_Oxides_Dataset_M_set_use_4ca1b02de040.md)
- Original title in paper: Transition Metal Oxides Dataset (MP-derived)
- Link: None

A subset of 7,137 transition metal oxides (1,211 stable) extracted from MP, with all samples withheld from training to form an out-of-distribution test set. Used to assess ECSG’s generalization to Fe- and Mn-containing oxides — representing another unknown space — and to confirm robust stability prediction under moderate class imbalance (17.0% stable).

### [Double Perovskite Oxides Database (Talapatra et al.)](../datasets/Double_Perovskite_Oxides_Database_Talapatra_et_al_dataset_3398d43c9118.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Double_Perovskite_Oxides_Database_set_use_4c3fc1a3278e.md)
- Original title in paper: Double Perovskite Oxides Database (Talapatra et al.)
- Link: None

A custom-curated database of 1,333 single and double perovskite oxides with DFT-calculated stability labels, used to train a specialized ECSG variant incorporating site-specific features for perovskite A/B-site discrimination. Served as the foundation for high-throughput prediction across a candidate space of >4.5 million compositions and subsequent DFT validation of top-ranked predictions.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Candidate Space Construction
- Screening / Prediction
<!-- RD_STAGES_END -->
