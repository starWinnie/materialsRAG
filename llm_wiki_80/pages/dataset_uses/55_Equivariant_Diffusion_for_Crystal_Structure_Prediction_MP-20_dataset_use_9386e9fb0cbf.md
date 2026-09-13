# 55_Equivariant Diffusion for Crystal Structure Prediction - MP-20

## Dataset Use

A subset of 45,231 stable inorganic materials curated from the Materials Project database, limited to structures with ≤20 atoms per unit cell and experimentally verified stability; used for stable structure prediction evaluation with a 60-20-20 split; provides diverse, real-world crystal examples to benchmark generative performance on the p(C, F | A) prediction task.

## Links

- Paper: [55 Equivariant Diffusion for Crystal Structure Prediction](../papers/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction.md)
- Task: [task page](../tasks/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_task_1.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the lattice parameters and fractional atomic coordinates of a crystal structure given its chemical composition, i.e., learning the conditional distribution p(C, F | A) to generate physically valid, stable crystal structures from elemental formulas without relying on expensive DFT-based energy minimization.

## Metadata

- Dataset use ID: `dataset_use_9386e9fb0cbf`
- Original dataset title: MP-20
- Tags: crystal structure prediction, generative modeling, lattice parameter prediction, fractional coordinate prediction
