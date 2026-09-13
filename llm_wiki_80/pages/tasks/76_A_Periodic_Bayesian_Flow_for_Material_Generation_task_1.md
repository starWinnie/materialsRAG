# 76_A Periodic Bayesian Flow for Material Generation - Task 1

## Task Description

Generating novel, physically valid crystal structures from scratch (ab initio generation) and predicting stable crystal structures given only atomic composition (stable structure prediction), while respecting the periodic E(3) symmetry constraints inherent to crystalline materials.

## Metadata

- Task ID: `task_3a66a72bd70b`
- Source paper: [76 A Periodic Bayesian Flow for Material Generation](../papers/76_A_Periodic_Bayesian_Flow_for_Material_Generation.md)
- Tags: crystal generation, ab initio generation, structure prediction, periodic symmetry modeling

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/76_A_Periodic_Bayesian_Flow_for_Material_Generation_Perov-5_dataset_use_32da26b8be7d.md)
- Original title in paper: Perov-5
- Link: https://doi.org/10.1039/C2EE22746F

A dataset of 18,928 perovskite crystals sharing the ABX3 chemical formula, each with exactly 5 atoms in the unit cell. It is used in this paper to evaluate both ab initio crystal generation and stable structure prediction tasks, serving as a benchmark for model performance on chemically homogeneous, structurally similar materials.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/76_A_Periodic_Bayesian_Flow_for_Material_Generation_Carbon-24_dataset_use_4f4ac4009505.md)
- Original title in paper: Carbon-24
- Link: https://doi.org/10.1038/s41524-020-00442-0

A dataset containing 10,153 carbon-only crystals with unit cells ranging from 6 to 24 atoms. It is used exclusively for ab initio generation evaluation to test the model's ability to generate diverse, stable all-carbon structures without compositional constraints, providing a challenging benchmark for structural diversity and validity.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/76_A_Periodic_Bayesian_Flow_for_Material_Generation_MP-20_dataset_use_cbf031f71234.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org/

A subset of 45,231 stable inorganic materials selected from the Materials Project database, limited to crystals with at most 20 atoms per unit cell and including experimentally verified compounds. It is used for both ab initio generation and stable structure prediction tasks, and is central to the paper’s efficiency experiments (e.g., 200× speedup claim) and ablation studies.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/76_A_Periodic_Bayesian_Flow_for_Material_Generation_MPTS-52_dataset_use_b08529e71d19.md)
- Original title in paper: MPTS-52
- Link: https://doi.org/10.48550/arXiv.2309.12345

A more challenging extension of MP-20 containing 40,476 crystals with up to 52 atoms per unit cell. It is used to evaluate robustness and scalability of CrysBFN on larger, more complex crystal structures, specifically for the stable structure prediction task where it achieves a 20.52% match rate.
