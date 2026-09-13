# 48_Crystal Structure Prediction by Joint Equivariant Diffusion - Task 1

## Task Description

Predicting the stable 3D crystal structure—including the lattice matrix and fractional atomic coordinates—for a given chemical composition, by learning the conditional distribution p(L, F | A) from known stable crystals.

## Metadata

- Task ID: `task_05d462cc36f3`
- Source paper: [48 Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion.md)
- Tags: Crystal Structure Prediction, Structure Generation, Conditional Generation

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_Perov-5_dataset_use_278dd71.md)
- Original title in paper: Perov-5
- Link: None

A dataset of 18,928 perovskite materials, each with exactly 5 atoms in the unit cell. It contains stable crystal structures (lattice matrices, fractional coordinates, and atom types) curated from computational screening of perovskite metal oxides. In this paper, it is used to train and evaluate the DiffCSP model for the crystal structure prediction task, specifically to assess performance on compositions with highly symmetric, small-unit-cell structures.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_Carbon-24_dataset_use_a536e.md)
- Original title in paper: Carbon-24
- Link: None

A dataset of 10,153 carbon-based materials containing 6–24 atoms per unit cell, generated via ab initio random structure searching (AIRSS) at 10 GPa. It includes stable crystal structures (lattice, fractional coordinates, atom types) and is used in this paper to evaluate DiffCSP’s ability to predict complex, variable-size carbon allotropes—serving as a challenging test case for the CSP task due to structural diversity and lack of compositional variation (all carbon).

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_MP-20_dataset_use_10056cf71.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of 45,231 stable inorganic materials from the Materials Project database, filtered to include only those with ≤20 atoms per unit cell and experimentally validated or DFT-stable structures. It provides ground-truth crystal structures (lattice, fractional coordinates, composition) and is used in this paper as the primary benchmark for training and evaluating DiffCSP on general inorganic CSP, enabling comparison against DFT-based and learning-based baselines.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_MPTS-52_dataset_use_fa9db54.md)
- Original title in paper: MPTS-52
- Link: https://github.com/sparks-baird/mp-time-split

An extension of MP-20 containing 40,476 crystal structures with up to 52 atoms per unit cell, sorted chronologically by first publication date to enable time-based train/val/test splits. It serves as a more scalable and challenging CSP benchmark in this paper, used to stress-test DiffCSP’s generalization to large-unit-cell systems and validate robustness under increased structural complexity.
