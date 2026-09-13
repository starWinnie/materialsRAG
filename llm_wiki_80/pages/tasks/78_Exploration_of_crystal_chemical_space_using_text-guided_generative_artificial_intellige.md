# 78_Exploration of crystal chemical space using text-guided generative artificial intelligence - Task 1

## Task Description

Generating novel crystal structures and chemical compositions guided by textual descriptions, such as elemental composition and crystal system, to explore uncharted regions of crystal chemical space for materials discovery — specifically targeting multi-component inorganic systems (e.g., ternary Zn-Ti-O and quaternary Li-P-S-Cl) where stable or metastable phases are underrepresented in existing databases.

## Metadata

- Task ID: `task_89cc0e5401c9`
- Source paper: [78 Exploration of crystal chemical space using text-guided generative artificial intelligence](../papers/78_Exploration_of_crystal_chemical_space_using_text-guided_generative_artificial_intellige.md)
- Tags: crystal structure generation, text-guided generation, materials discovery

## Supporting Datasets

### [Materials Project (MP-40 dataset)](../datasets/Materials_Project_MP-40_dataset.md)

- Usage page: [usage note](../dataset_uses/78_Exploration_of_crystal_chemical_space_using_text-guided_generative_artificial_intellige.md)
- Original title in paper: Materials Project (MP-40 dataset)
- Link: https://doi.org/10.5281/zenodo.15090949

A curated collection of 32,525 experimentally observed inorganic crystal structures (version 2023.11.01), each with ≤40 atoms in the primitive unit cell, energy above convex hull < 0.25 eV/atom, cell lengths ≤20 Å, and excluding gaseous elements (e.g., H₂, O₂). Used to train and evaluate Chemeleon’s diffusion model and Crystal CLIP contrastive learning framework; provides ground-truth structural data (lattice vectors, atom types, coordinates), composition, crystal system, and thermodynamic stability metrics. Serves as the primary source for learning structure–composition–text alignments and validating generated candidates against known materials.

### [MP-20 dataset](../datasets/MP-20_dataset.md)

- Usage page: [usage note](../dataset_uses/78_Exploration_of_crystal_chemical_space_using_text-guided_generative_artificial_intellige.md)
- Original title in paper: MP-20 dataset
- Link: None

A subset of the Materials Project database used specifically for benchmarking crystal structure prediction (CSP) performance. Employed to enable direct comparison of Chemeleon against state-of-the-art CSP models (e.g., DiffCSP, FlowMM) on composition matching and structure reconstruction accuracy, supporting evaluation of Chemeleon’s dual capability in text-guided generation and CSP-oriented tasks.
