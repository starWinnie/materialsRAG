# 54_An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning - Task 1

## Task Description

Designing novel direct narrow-gap semiconductor crystal structures for optoelectronic applications, subject to constraints on bandgap (0.325 ± 0.225 eV at PBE level), thermodynamic stability (energy above hull < 50 meV/atom), compositional novelty (not present in the Materials Project database), and structural uniqueness (low similarity to training structures).

## Metadata

- Task ID: `task_25bd06f908bc`
- Source paper: [54 An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](../papers/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md)
- Tags: inverse design, semiconductor discovery, bandgap engineering, materials screening

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md)
- Original title in paper: Materials Project (MP) database
- Link: https://materialsproject.org

A large-scale computational materials database containing over 100,000 DFT-calculated crystal structures with associated properties (e.g., formation energy, bandgap, energy above hull). In this paper, subsets of MP are used: (1) the 'general dataset' (30,085 crystals with 1–10 atoms/unit cell, negative formation energy, atomic number ≤ 86, no low-dimensional units) to train a general RNN for SLICES syntax; (2) the 'transfer dataset' (364 direct narrow-gap semiconductors with PBE bandgap in [0.1, 0.55] eV) to fine-tune a specialized RNN for property-targeted generation; and (3) the full MP database as a reference for composition/structure novelty filtering during candidate screening.

### [MP-20 dataset](../datasets/MP-20_dataset.md)

- Usage page: [usage note](../dataset_uses/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md)
- Original title in paper: MP-20 dataset
- Link: https://github.com/txie-93/cdvae

A curated subset of the Materials Project containing 45,229 crystal structures with 1–20 atoms per unit cell, covering 89 elements and representing structurally and chemically diverse experimentally known crystals. It is used as the primary benchmark for SLI2Cry reconstruction performance (both original and filtered versions: 40,330 crystals after excluding high-Z and low-dimensional cases), and as the training set for unconditional (ucRNN) and conditional (cRNN) generative models for material generation and property optimization evaluation.

### [MP-21-40 dataset](../datasets/MP-21-40_dataset.md)

- Usage page: [usage note](../dataset_uses/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md)
- Original title in paper: MP-21-40 dataset
- Link: https://materialsproject.org

A Materials Project subset comprising 24,959 materials with 21–40 atoms per unit cell. After filtering for stability (formation energy < 2 eV/atom, energy above hull < 0.08 eV/atom), atomic number ≤ 86, and absence of low-dimensional structural units, it yields the 'filtered MP-21-40' dataset of 23,560 crystals. This dataset is used to evaluate the generalizability of the SLI2Cry reconstruction pipeline beyond the MP-20 size range, demonstrating high match rates (87.88% loose, 83.73% strict).

### [Quantum MOF (QMOF) database](../datasets/Quantum_MOF_QMOF_database.md)

- Usage page: [usage note](../dataset_uses/54_An_invertible_invariant_crystal_representation_for_inverse_design_of_solid-state_materi.md)
- Original title in paper: Quantum MOF (QMOF) database
- Link: https://quantum-mof.org

A database of quantum-chemically computed metal–organic framework (MOF) structures. Specifically, the 'filtered QMOF-21-40' subset — 339 MOFs with 21–40 atoms per unit cell — is used to assess SLI2Cry's reconstruction capability on complex, porous frameworks. The low match rates (6.19% loose, 2.95% strict) reveal current limitations in handling MOFs and motivate future hierarchical graph extensions (MOF-SLICES).
