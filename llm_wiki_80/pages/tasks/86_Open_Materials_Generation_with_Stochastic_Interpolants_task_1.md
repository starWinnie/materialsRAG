# 86_Open Materials Generation with Stochastic Interpolants - Task 1

## Task Description

Predicting stable crystal structures for given chemical compositions (Crystal Structure Prediction) and generating novel, stable, and unique inorganic crystalline materials from scratch without composition constraints (de novo generation), both requiring joint modeling of atomic species, fractional coordinates, and lattice vectors under periodic boundary conditions.

## Metadata

- Task ID: `task_290b84374dd5`
- Source paper: [86 Open Materials Generation with Stochastic Interpolants](../papers/86_Open_Materials_Generation_with_Stochastic_Interpolants.md)
- Tags: Crystal Structure Prediction, De Novo Generation, Materials Discovery

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/86_Open_Materials_Generation_with_Stochastic_Interpolants_perov-5_dataset_use_cd467f20e406.md)
- Original title in paper: perov-5
- Link: https://doi.org/10.1039/C2EE22341D

A dataset of 18,928 perovskite crystal structures, each containing exactly five atoms per unit cell, with variation only in lattice lengths and atomic types; used to benchmark Crystal Structure Prediction performance by evaluating match rate and RMSE between generated and known structures for fixed compositions.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/86_Open_Materials_Generation_with_Stochastic_Interpolants_MP-20_dataset_use_744685cb9af1.md)
- Original title in paper: MP-20
- Link: https://doi.org/10.1063/1.4812323

A subset of the Materials Project database containing 45,231 crystal structures with up to 20 atoms per unit cell; used for both Crystal Structure Prediction and de novo generation benchmarks, including match rate, validity, coverage, property distribution fidelity (density, Nary, coordination number), and S.U.N. (stable, unique, novel) rates after DFT relaxation.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/86_Open_Materials_Generation_with_Stochastic_Interpolants_MPTS-52_dataset_use_0be0e8f32970.md)
- Original title in paper: MPTS-52
- Link: https://doi.org/10.21105/joss.05618

A chronological time-split variant of the Materials Project with 40,476 structures containing up to 52 atoms per unit cell, designed to be more challenging for learning due to increased structural complexity and temporal distribution shift; used to evaluate generalization in Crystal Structure Prediction under difficult conditions.

### [Alex-MP-20](../datasets/Alex-MP-20.md)

- Usage page: [usage note](../dataset_uses/86_Open_Materials_Generation_with_Stochastic_Interpolants_Alex-MP-20_dataset_use_85cfb7304.md)
- Original title in paper: Alex-MP-20
- Link: https://doi.org/10.1038/s41597-022-01177-w

A large-scale hybrid dataset combining 675,204 structures from the Alexandria database and MP-20, filtered to ≤20 atoms per unit cell and split 80-10-10; used to establish the first Crystal Structure Prediction baseline for high-capacity generative models and assess scalability and robustness on a massive, diverse materials corpus.
