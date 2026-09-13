# 55_Equivariant Diffusion for Crystal Structure Prediction - Task 1

## Task Description

Predicting the lattice parameters and fractional atomic coordinates of a crystal structure given its chemical composition, i.e., learning the conditional distribution p(C, F | A) to generate physically valid, stable crystal structures from elemental formulas without relying on expensive DFT-based energy minimization.

## Metadata

- Task ID: `task_283558a3d61e`
- Source paper: [55 Equivariant Diffusion for Crystal Structure Prediction](../papers/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction.md)
- Tags: crystal structure prediction, generative modeling, lattice parameter prediction, fractional coordinate prediction

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_Perov-5_dataset_use_69b41298fed6.md)
- Original title in paper: Perov-5
- Link: https://doi.org/10.1039/C2EE22742E

A dataset of 18,928 perovskite materials, each with a unit cell containing exactly 5 atoms and analogous structural configurations; used in this paper to train and evaluate EquiCSP on stable structure prediction, with a 60-20-20 train-validation-test split; supports the core CSP task by providing ground-truth (A, C, F) triples for learning the conditional distribution p(C, F | A).

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_MP-20_dataset_use_9386e9fb0cbf.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of 45,231 stable inorganic materials curated from the Materials Project database, limited to structures with ≤20 atoms per unit cell and experimentally verified stability; used for stable structure prediction evaluation with a 60-20-20 split; provides diverse, real-world crystal examples to benchmark generative performance on the p(C, F | A) prediction task.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_MPTS-52_dataset_use_2248ab2e7e09.md)
- Original title in paper: MPTS-52
- Link: None

An extension of MP-20 containing 40,476 crystal structures with up to 52 atoms per unit cell, ordered chronologically by earliest publication year; used as a more challenging benchmark for stable structure prediction, with 27,380 training, 5,000 validation, and 8,096 test entries; tests the scalability and robustness of EquiCSP’s equivariant diffusion framework on larger, more complex crystals.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_Carbon-24_dataset_use_7f9eb73ded.md)
- Original title in paper: Carbon-24
- Link: https://doi.org/10.5281/zenodo.3727277

A dataset of 10,153 carbon allotropes containing 6–24 atoms per unit cell, featuring multiple metastable structures per composition; used in ab initio generation experiments to evaluate EquiCSP’s ability to sample diverse, physically valid structures from scratch (i.e., without ground-truth reference), supporting the one-to-many structure generation task beyond stable prediction.
