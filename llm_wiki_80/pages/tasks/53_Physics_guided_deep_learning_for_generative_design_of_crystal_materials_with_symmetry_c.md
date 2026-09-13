# 53_Physics guided deep learning for generative design of crystal materials with symmetry constraints - Task 1

## Task Description

Generating novel, physically valid crystal structures with high structural diversity and symmetry constraints (including non-cubic space groups), while ensuring thermodynamic stability and synthesizability potential — specifically by learning from known materials to sample realistic, stable unit cells conditioned on chemical composition and space group.

## Metadata

- Task ID: `task_9ff121e34959`
- Source paper: [53 Physics guided deep learning for generative design of crystal materials with symmetry constraints](../papers/53_Physics_guided_deep_learning_for_generative_design_of_crystal_materials_with_symmetry_c.md)
- Tags: crystal structure generation, generative design, symmetry-constrained generation

## Supporting Datasets

### [MIO dataset](../datasets/MIO_dataset.md)

- Usage page: [usage note](../dataset_uses/53_Physics_guided_deep_learning_for_generative_design_of_crystal_materials_with_symmetry_c.md)
- Original title in paper: MIO dataset
- Link: http://www.materialsproject.org

A curated dataset of 42,072 ternary inorganic crystal structures drawn from Materials Project (MP), Inorganic Crystal Structure Database (ICSD), and Open Quantum Materials Database (OQMD v1.4), covering 20 space groups across 5 crystal systems. It serves as the primary training and validation set for the PGCGM model, used to train the physics-guided generative adversarial network to learn atomic coordination patterns, lattice parameter distributions, and symmetry-compliant base atom site configurations under physical constraints.

### [TST dataset](../datasets/TST_dataset.md)

- Usage page: [usage note](../dataset_uses/53_Physics_guided_deep_learning_for_generative_design_of_crystal_materials_with_symmetry_c.md)
- Original title in paper: TST dataset
- Link: https://oqmd.org

A test dataset of 9,441 newly released ternary materials from OQMD v1.5, filtered using the same criteria as MIO and disjoint from the training set. It is used to evaluate generalization performance — specifically to assess rediscovery rate, property distribution fidelity (via Wasserstein distance), match rate against Bayesian-optimized structures, and DFT validation success — thereby benchmarking the model’s ability to generate realistic, unseen crystal prototypes beyond the training distribution.
