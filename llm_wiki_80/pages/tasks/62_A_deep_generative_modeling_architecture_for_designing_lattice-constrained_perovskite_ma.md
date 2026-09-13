# 62_A deep generative modeling architecture for designing lattice-constrained perovskite materials - Task 1

## Task Description

Designing novel and polymorphic perovskite materials with crystal lattice conformities that strictly satisfy predefined geometrical (e.g., crystal system, space group) and thermodynamic (e.g., formation energy ≤ −1.5 eV/atom) stability constraints — specifically for ABX₃ and A₂BB′X₆ stoichiometries — while avoiding lattice reconstruction artifacts such as low-symmetry, unfeasible atomic coordination, or triclinic distortions during generative decoding.

## Metadata

- Task ID: `task_02b8faa0769a`
- Source paper: [62 A deep generative modeling architecture for designing lattice-constrained perovskite materials](../papers/62_A_deep_generative_modeling_architecture_for_designing_lattice-constrained_perovskite_ma.md)
- Tags: perovskite design, inverse materials design, lattice-constrained generation, crystal symmetry control, thermodynamic stability screening

## Supporting Datasets

### [Open Quantum Materials Database (OQMD) v1.0](../datasets/Open_Quantum_Materials_Database_OQMD_v1.0.md)

- Usage page: [usage note](../dataset_uses/62_A_deep_generative_modeling_architecture_for_designing_lattice-constrained_perovskite_ma.md)
- Original title in paper: Open Quantum Materials Database (OQMD) v1.0
- Link: https://oqmd.org/

A high-throughput computational database containing ~72,747 perovskite-like structures (35,325 ABX₃ and 37,422 A₂BB′X₆), each with DFT-calculated formation energies, crystal structures (in CIF format), space groups, and thermodynamic properties. In this paper, 63,016 samples (29,881 ABX₃ and 33,135 A₂BB′X₆) were curated — filtered for Ef ≤ 0 eV/atom, converted to conventional unit cells, limited to ≤40 atoms/cell, and restricted to cubic, monoclinic, orthorhombic, tetragonal, and trigonal Bravais systems — to train the LCMGM’s SS-VAE phase and support lattice-constrained generative modeling of stable, symmetry-compliant perovskites.

### [Materials Project (MP) v2021.05.13](../datasets/Materials_Project_MP_v2021.05.13.md)

- Usage page: [usage note](../dataset_uses/62_A_deep_generative_modeling_architecture_for_designing_lattice-constrained_perovskite_ma.md)
- Original title in paper: Materials Project (MP) v2021.05.13
- Link: https://materialsproject.org/

A widely used materials database providing DFT-computed properties for ~8,238 perovskite entries (4,358 ABX₃ and 3,880 A₂BB′X₆), including relaxed crystal structures, formation energies, space groups, and convex hull stability metrics. In this work, 6,540 preprocessed samples (3,283 ABX₃ and 3,257 A₂BB′X₆) — similarly filtered for Ef ≤ 0 eV/atom, converted to conventional cells, and capped at 40 atoms/cell — were used as a higher-fidelity test set for transfer learning evaluation, model benchmarking, and final validation of generated candidates’ structural and energetic consistency.

### [Mendeley Data Repository (LCMGM-designed materials)](../datasets/Mendeley_Data_Repository_LCMGM-designed_materials.md)

- Usage page: [usage note](../dataset_uses/62_A_deep_generative_modeling_architecture_for_designing_lattice-constrained_perovskite_ma.md)
- Original title in paper: Mendeley Data Repository (LCMGM-designed materials)
- Link: https://doi.org/10.17632/m262xxpgn2.1

An author-curated public repository containing Crystallographic Information Files (CIFs) and Quantum Espresso output files for 124 newly designed inorganic perovskites (65 ABX₃ and 59 A₂BB′X₆), all DFT-validated and confirmed to satisfy lattice constraints (e.g., cubic-Fm-3m, tetragonal-P4/mmm) and thermodynamic stability (e.g., Ehull ≤ 0.08 eV/atom). This dataset serves as the final output of the LCMGM pipeline and is used to support experimental reproducibility, property analysis (e.g., bandgaps, phonons), and community access to the discovered materials.
