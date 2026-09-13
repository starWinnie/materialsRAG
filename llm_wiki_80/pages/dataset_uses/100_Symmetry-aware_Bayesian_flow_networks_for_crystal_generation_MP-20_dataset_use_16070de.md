# 100_Symmetry-aware Bayesian flow networks for crystal generation - MP-20

## Dataset Use

A subset of the Materials Project database containing 40,476 experimentally observed or DFT-validated crystal structures, each with up to 20 atoms per unit cell. It is used as the primary training, validation, and test set (60-20-20 split) for SymmBFN to train the symmetry-aware Bayesian flow network for de novo crystal generation and property-conditioned generation; formation energy per atom and bandgap labels—computed via M3GNet—are used to condition generation on target properties.

## Links

- Paper: [100 Symmetry-aware Bayesian flow networks for crystal generation](../papers/100_Symmetry-aware_Bayesian_flow_networks_for_crystal_generation.md)
- Task: [task page](../tasks/100_Symmetry-aware_Bayesian_flow_networks_for_crystal_generation_task_1.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel, stable, and synthetically plausible crystalline material structures conditioned on desired physical properties (e.g., formation energy per atom or bandgap), while accurately reproducing the natural distribution of space groups observed in experimentally validated crystals.

## Metadata

- Dataset use ID: `dataset_use_16070dead164`
- Original dataset title: MP-20
- Tags: crystal generation, property-conditioned generation, space group modeling
