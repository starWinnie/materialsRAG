# 05_Thermodynamic_Stability_Ensemble - Task 1

## Task Description

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Task ID: `task_134b6e57d77b`
- Source paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Materials_Project_dataset_use_75e15c27a639.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

A large-scale DFT-computed database containing thermodynamic properties (e.g., formation energy, decomposition energy) for 85,014 inorganic crystalline compounds, including experimentally observed and hypothetical materials. Used as the primary training and benchmarking dataset to train and evaluate the ECSG ensemble model for binary classification of compound stability; also used to construct convex hulls for ΔHd labeling and to extract composition-only samples for sample efficiency analysis.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Open_Quantum_Materials_Database_dataset_use_edcc03281e.md)
- Original title in paper: Open Quantum Materials Database (OQMD)
- Link: None

A DFT-generated database of predicted inorganic materials, providing formation energies and structural data for over 400,000 compounds. Used alongside MP and JARVIS for cross-database performance validation of ECSG, particularly to assess robustness under class imbalance (11.3% stable samples) and to serve as a reference convex hull for DFT validation of predicted perovskite oxides.

### [JARVIS Database](../datasets/JARVIS_Database.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_JARVIS_Database_dataset_use_992fc756b44d.md)
- Original title in paper: JARVIS (Joint Automated Repository for Various Integrated Simulations)
- Link: None

A DFT-based materials database offering structural, electronic, and thermodynamic properties for ~100,000+ materials, curated for data-driven design. Used to benchmark ECSG’s classification performance (achieving AUC = 0.988) and as an independent convex hull reference for validating DFT-predicted stability of double perovskite oxides selected by ECSG.

### [C2DB](../datasets/C2DB.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_C2DB_dataset_use_6e03492b67fb.md)
- Original title in paper: C2DB (Computational 2D Materials Database)
- Link: None

A high-throughput DFT database containing structural, electronic, and thermodynamic data for over 4,000 atomically thin 2D materials. Used to train a specialized ECSG variant for predicting thermodynamic stability of 2D materials, supporting the case study on wide-bandgap semiconductor screening.

### [2DMatPedia](../datasets/2DMatPedia.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_2DMatPedia_dataset_use_cc2c8c8cc41b.md)
- Original title in paper: 2DMatPedia
- Link: None

A computational database of 4,743 2D materials with precomputed bandgaps and stability labels derived from DFT. Used as an independent test set to evaluate ECSG’s stability predictions for 2D materials and to validate the joint screening pipeline (ECSG + DARWIN-7B LLM) for wide-bandgap semiconductors, yielding 313 experimentally stable candidates out of 393 predicted.

### [Perovskite Halides Dataset (literature-curated)](../datasets/Perovskite_Halides_Dataset_literature-curated.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Perovskite_Halides_Dataset_literature-curated_dataset_.md)
- Original title in paper: Perovskite Halides Dataset (literature-curated)
- Link: None

A manually compiled dataset of thermodynamic stability labels for 496 perovskite halides (ABX₃, X = Cl/Br/I) extracted from prior literature; duplicates present in MP were removed to ensure independence. Used to evaluate ECSG’s generalization to unknown chemical space — specifically, its ability to predict stability for perovskite halides not represented in the MP training set.

### [Li-containing Oxides Dataset (MP-derived)](../datasets/Li-containing_Oxides_Dataset_MP-derived.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Li-containing_Oxides_Dataset_MP-derived_dataset_use_f2.md)
- Original title in paper: Li-containing Oxides Dataset (MP-derived)
- Link: None

A subset of 6,168 lithium-containing oxides (750 stable) extracted from the MP database, fully excluded from the MP training set to create a zero-shot evaluation scenario. Used to test ECSG’s predictive capability in a completely unfamiliar compositional space (Li–O systems), demonstrating its utility for cathode material discovery in Li-ion batteries.

### [Transition Metal Oxides Dataset (MP-derived)](../datasets/Transition_Metal_Oxides_Dataset_MP-derived.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Transition_Metal_Oxides_Dataset_MP-derived_dataset_use.md)
- Original title in paper: Transition Metal Oxides Dataset (MP-derived)
- Link: None

A subset of 7,137 transition metal oxides (1,211 stable) extracted from MP, with all samples withheld from training to form an out-of-distribution test set. Used to assess ECSG’s generalization to Fe- and Mn-containing oxides — representing another unknown space — and to confirm robust stability prediction under moderate class imbalance (17.0% stable).

### [Double Perovskite Oxides Database (Talapatra et al.)](../datasets/Double_Perovskite_Oxides_Database_Talapatra_et_al.md)

- Usage page: [usage note](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Double_Perovskite_Oxides_Database_Talapatra_et_al._dat.md)
- Original title in paper: Double Perovskite Oxides Database (Talapatra et al.)
- Link: None

A custom-curated database of 1,333 single and double perovskite oxides with DFT-calculated stability labels, used to train a specialized ECSG variant incorporating site-specific features for perovskite A/B-site discrimination. Served as the foundation for high-throughput prediction across a candidate space of >4.5 million compositions and subsequent DFT validation of top-ranked predictions.
