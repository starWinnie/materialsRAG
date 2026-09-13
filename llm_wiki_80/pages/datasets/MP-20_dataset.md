# MP-20 dataset

## Metadata

- Dataset ID: `dataset_db3b359f185a`
- Aliases: MP-20 Dataset, MP-20 dataset
- Links: https://doi.org/10.1039/d5mh00010f, https://github.com/txie-93/cdvae
- Used by papers: 3
- Dataset usage records: 3

## Description Examples

- A curated subset of the Materials Project containing 45,229 crystal structures with 1–20 atoms per unit cell, covering 89 elements and representing structurally and chemically diverse experimentally known crystals. It is used as the primary benchmark for SLI2Cry reconstruction performance (both original and filtered versions: 40,330 crystals after excluding high-Z and low-dimensional cases), and as the training set for unconditional (ucRNN) and conditional (cRNN) generative models for material generation and property optimization evaluation.
- A curated subset of the Materials Project containing 45,231 stable (convex hull–stable) inorganic crystal structures, used as the standard training dataset for all four evaluated generative models (CrystaLLM, FTCP, CDVAE, MatterGen) to ensure consistent benchmarking; also used to train the CGCNN band gap and bulk modulus predictors and the CHGNet interatomic potential.
- A subset of the Materials Project database used specifically for benchmarking crystal structure prediction (CSP) performance. Employed to enable direct comparison of Chemeleon against state-of-the-art CSP models (e.g., DiffCSP, FlowMM) on composition matching and structure reconstruction accuracy, supporting evaluation of Chemeleon’s dual capability in text-guided generation and CSP-oriented tasks.

## Uses

- [54_An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](../dataset_uses/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md): [54 An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](../papers/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md), [task](../tasks/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md)
- [72_Establishing baselines for generative discovery of inorganic crystals](../dataset_uses/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_MP-20_Dataset_dat.md): [72 Establishing baselines for generative discovery of inorganic crystals](../papers/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals.md), [task](../tasks/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_task_1.md)
- [78_Exploration of crystal chemical space using text-guided generative artificial intelligence](../dataset_uses/78_Exploration_of_crystal_chemical_space_using_text-guided_generative_artificial_intellige.md): [78 Exploration of crystal chemical space using text-guided generative artificial intelligence](../papers/78_Exploration_of_crystal_chemical_space_using_text-guided_generative_artificial_intellige.md), [task](../tasks/78_Exploration_of_crystal_chemical_space_using_text-guided_generative_artificial_intellige.md)
