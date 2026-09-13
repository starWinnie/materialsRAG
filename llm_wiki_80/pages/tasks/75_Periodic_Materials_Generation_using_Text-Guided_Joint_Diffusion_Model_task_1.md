# 75_Periodic Materials Generation using Text-Guided Joint Diffusion Model - Task 1

## Task Description

Generating stable 3D periodic crystal structures (atom types, fractional coordinates, and lattice matrix) that align with user-specified textual descriptions of material properties, composition, symmetry, and structural features — enabling controllable, text-guided inverse design of novel crystalline materials.

## Metadata

- Task ID: `task_327a40f105df`
- Source paper: [75 Periodic Materials Generation using Text-Guided Joint Diffusion Model](../papers/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model.md)
- Tags: crystal structure generation, text-guided generation, inverse materials design

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model_Perov-5_dataset_u.md)
- Original title in paper: Perov-5
- Link: https://doi.org/10.1039/C2EE22462J

A dataset of 18,928 perovskite materials, each containing exactly 5 atoms in the unit cell and represented as ABX₃ stoichiometries. Structures are derived from quantum mechanical simulations and correspond to local energy minima; most are hypothetical. Used in this paper for both Crystal Structure Prediction (CSP) and Random Material Generation (Gen) tasks — specifically to train and evaluate TGDMat’s ability to generate structures matching textual prompts (e.g., chemical formula, space group 227, cubic system) and to benchmark validity, coverage, and property statistics.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model_Carbon-24_dataset.md)
- Original title in paper: Carbon-24
- Link: https://www.materialscloud.org/archive/2020.0026/v1

A dataset of 10,153 carbon-only crystal structures, with 6–24 atoms per unit cell, generated via ab initio random structure searching (AIRSS) at 10 GPa. All structures are at local energy minima and share identical composition but vary in geometry. Used in this paper for CSP and Gen tasks to evaluate TGDMat’s text-guided generation fidelity — especially for matching prompts specifying elemental identity (C), crystal system (e.g., orthorhombic), space group number (e.g., 62), and formation energy sign — and to assess structural validity and coverage metrics.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model_MP-20_dataset_use.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of 45,231 materials curated from the Materials Project database, each with ≤20 atoms per unit cell and covering diverse chemistries and crystal systems. Includes experimentally known and globally stable inorganic compounds. Used in this paper as the most realistic benchmark for Gen and CSP tasks — to test TGDMat’s ability to generate synthetically plausible structures matching detailed textual prompts (e.g., 'La(NiGe)₂', tetragonal, space group 138, negative formation energy) and to measure correctness against ground-truth global features (formula, space group, band gap).
