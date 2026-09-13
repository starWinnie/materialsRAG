# 69_Shotgun crystal structure prediction using machine-learned formation energies - Task 1

## Task Description

Predicting stable or metastable crystal structures from a given chemical composition by identifying global or local minima of the energy surface across a broad space of atomic configurations, using machine-learned formation energies to avoid iterative first-principles relaxation.

## Metadata

- Task ID: `task_c0ebf6615131`
- Source paper: [69 Shotgun crystal structure prediction using machine-learned formation energies](../papers/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies.md)
- Tags: crystal structure prediction, energy minimization, formation energy prediction

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies_Materials.md)
- Original title in paper: Materials Project database
- Link: https://next-gen.materialsproject.org/

A publicly available database containing DFT-calculated formation energies, crystal structures, and properties for 126,210 stable and metastable inorganic compounds. It was used to pretrain the global CGCNN energy predictor and to extract template structures (33,040 stable crystals) for element substitution (ShotgunCSP-GT), space-group prediction (33,040 instances with 213 distinct space groups), and Wyckoff-letter assignment modeling (same 33,040 instances, excluding 120 benchmark crystals). The dataset supported training surrogate energy models, generating candidate structures, and predicting space groups and Wyckoff patterns.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies_Open_Quan.md)
- Original title in paper: OQMD (Open Quantum Materials Database)
- Link: https://oqmd.org

A computational materials database containing formation energies and structures for ~1,021,917 compounds, including both relaxed and unrelaxed configurations. It was used experimentally to test the generalization capability of the global CGCNN model — specifically, to demonstrate that models trained on relaxed structures from OQMD (like Materials Project) fail to predict pre-relaxed conformational energies accurately, justifying the need for transfer learning on system-specific unrelaxed data.

### [ShotgunCSP Benchmark Datasets I–III](../datasets/ShotgunCSP_Benchmark_Datasets_I-III.md)

- Usage page: [usage note](../dataset_uses/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies_ShotgunCS.md)
- Original title in paper: ShotgunCSP Benchmark Datasets I–III
- Link: https://doi.org/10.6084/m9.figshare.26536375

Three curated benchmark sets totaling 120 experimentally or theoretically confirmed stable crystal structures: Dataset I (40 structures selected for diversity in space group, elements, unit-cell size, and application domain), Dataset II (50 randomly sampled structures from Materials Project), and Dataset III (30 structures with no template analogues in Materials Project, featuring large unit cells). These datasets were used to evaluate prediction success (i.e., whether the true stable structure was recovered among top-K DFT-relaxed candidates) and to assess generalization across composition, symmetry, and system size.
