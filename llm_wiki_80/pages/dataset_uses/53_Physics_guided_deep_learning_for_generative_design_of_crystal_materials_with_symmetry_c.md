# 53_Physics guided deep learning for generative design of crystal materials with symmetry constraints - TST dataset

## Dataset Use

A test dataset of 9,441 newly released ternary materials from OQMD v1.5, filtered using the same criteria as MIO and disjoint from the training set. It is used to evaluate generalization performance — specifically to assess rediscovery rate, property distribution fidelity (via Wasserstein distance), match rate against Bayesian-optimized structures, and DFT validation success — thereby benchmarking the model’s ability to generate realistic, unseen crystal prototypes beyond the training distribution.

## Links

- Paper: [53 Physics guided deep learning for generative design of crystal materials with symmetry constraints](../papers/53_Physics_guided_deep_learning_for_generative_design_of_crystal_materials_with_symmetry_c.md)
- Task: [task page](../tasks/53_Physics_guided_deep_learning_for_generative_design_of_crystal_materials_with_symmetry_c.md)
- Dataset: [TST dataset](../datasets/TST_dataset.md)
- Dataset URL: https://oqmd.org

## Task Context

Generating novel, physically valid crystal structures with high structural diversity and symmetry constraints (including non-cubic space groups), while ensuring thermodynamic stability and synthesizability potential — specifically by learning from known materials to sample realistic, stable unit cells conditioned on chemical composition and space group.

## Metadata

- Dataset use ID: `dataset_use_aea58b60a403`
- Original dataset title: TST dataset
- Tags: crystal structure generation, generative design, symmetry-constrained generation
