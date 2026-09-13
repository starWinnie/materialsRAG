# 100_Symmetry-aware Bayesian flow networks for crystal generation - Task 1

## Task Description

Generating novel, stable, and synthetically plausible crystalline material structures conditioned on desired physical properties (e.g., formation energy per atom or bandgap), while accurately reproducing the natural distribution of space groups observed in experimentally validated crystals.

## Metadata

- Task ID: `task_6d36b9c58ce2`
- Source paper: [100 Symmetry-aware Bayesian flow networks for crystal generation](../papers/100_Symmetry-aware_Bayesian_flow_networks_for_crystal_generation.md)
- Tags: crystal generation, property-conditioned generation, space group modeling

## Supporting Datasets

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/100_Symmetry-aware_Bayesian_flow_networks_for_crystal_generation_MP-20_dataset_use_16070de.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of the Materials Project database containing 40,476 experimentally observed or DFT-validated crystal structures, each with up to 20 atoms per unit cell. It is used as the primary training, validation, and test set (60-20-20 split) for SymmBFN to train the symmetry-aware Bayesian flow network for de novo crystal generation and property-conditioned generation; formation energy per atom and bandgap labels—computed via M3GNet—are used to condition generation on target properties.

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/100_Symmetry-aware_Bayesian_flow_networks_for_crystal_generation_Perov-5_dataset_use_aa511.md)
- Original title in paper: Perov-5
- Link: https://doi.org/10.1039/C2EE22122D

A dataset of 18,928 perovskite materials, each with exactly five atoms per unit cell and compositions drawn from a set of 56 elements; all share the perovskite prototype structure. It is used to evaluate SymmBFN’s generalization on a structurally constrained but compositionally diverse material class, though stability and S.U.N. metrics are not applicable due to high instability prevalence in the set.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/100_Symmetry-aware_Bayesian_flow_networks_for_crystal_generation_MPTS-52_dataset_use_a0da5.md)
- Original title in paper: MPTS-52
- Link: https://doi.org/10.21105/joss.05618

A challenging subset of the Materials Project containing 40,476 crystal structures with up to 52 atoms per unit cell, chronologically split into 27,380 training, 5,000 validation, and 8,096 test samples. It is used to benchmark SymmBFN’s scalability and performance on larger, more complex crystals, particularly assessing stability, S.U.N. rate, and computational efficiency relative to symmetry-agnostic baselines.
