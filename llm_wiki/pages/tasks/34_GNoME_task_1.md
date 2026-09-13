# 34_GNoME - Task 1

## Task Description

Predicting the thermodynamic stability of inorganic crystal structures by estimating their decomposition energy relative to the convex hull of competing phases, enabling high-throughput screening and discovery of previously unknown stable materials.

## Metadata

- Task ID: `task_c8d4cab9baf2`
- Source paper: [34 GNoME](../papers/34_GNoME.md)
- Tags: stability prediction, convex hull analysis, materials discovery, decomposition energy estimation

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/34_GNoME_Materials_Project_dataset_use_42c27bb87ebc.md)
- Original title in paper: Materials Project (2021 snapshot)
- Link: https://materialsproject.org

A curated database of ~69,000 computationally stable inorganic crystals as of March 2021, containing DFT-calculated total energies, structures (lattice, atomic positions, space groups), and formation energies. This dataset served as the initial training set for GNoME structural models and as the foundational reference for computing decomposition energies during active learning and convex hull updates.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/34_GNoME_Open_Quantum_Materials_Database_dataset_use_a828569e0e3b.md)
- Original title in paper: Open Quantum Materials Database (OQMD, 2021 snapshot)
- Link: http://oqmd.org

A high-throughput DFT database containing ~250,000+ computed inorganic compounds as of June 2021, including energies, structures, and phase diagrams. Used alongside the Materials Project snapshot as a source of known stable and metastable structures for candidate generation (e.g., SAPS), convex hull benchmarking, and filtering out already-known compositions during discovery.

### [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)

- Usage page: [usage note](../dataset_uses/34_GNoME_Inorganic_Crystal_Structure_Database_dataset_use_8d4d6ddfa002.md)
- Original title in paper: Inorganic Crystal Structure Database (ICSD)
- Link: https://icsd.fiz-karlsruhe.de

An experimental database of >200,000 published inorganic crystal structures, with ~20,000 computationally stable entries. Used exclusively for *validation*: 736 experimentally realized ICSD structures were matched to GNoME predictions to confirm real-world synthesizability and validate model accuracy, serving as ground-truth experimental evidence for discovered stability.

### [Wang-Botti-Marques (WBM) dataset](../datasets/Wang-Botti-Marques_WBM_dataset.md)

- Usage page: [usage note](../dataset_uses/34_GNoME_Wang-Botti-Marques_WBM_dataset_dataset_use_cd018cfb193b.md)
- Original title in paper: Wang–Botti–Marques (WBM) dataset
- Link: https://doi.org/10.1038/s41524-020-00472-z

A DFT-computed dataset of ~200,000+ inorganic crystals, used as an additional reference source for known stable structures in convex hull construction and comparative analysis. It was included in the agglomerated 'previous work' baseline (with MP and OQMD) against which GNoME’s 2.2 million new stable structures were evaluated for stability.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->
