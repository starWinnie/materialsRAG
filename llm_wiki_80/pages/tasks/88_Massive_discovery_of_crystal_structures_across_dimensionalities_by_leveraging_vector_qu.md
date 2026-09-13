# 88_Massive discovery of crystal structures across dimensionalities by leveraging vector quantization - Task 1

## Task Description

Discovering novel, stable, and property-targeted crystalline materials across dimensionalities (3D and 2D) by generating valid crystal structures that satisfy user-specified physical property constraints—specifically, bandgap between 0.5–2.5 eV and formation energy below −0.5 eV/atom for 3D semiconductors, and formation energy below −1 eV/atom for 2D materials—via inverse design in a discrete latent space.

## Metadata

- Task ID: `task_70569589bf05`
- Source paper: [88 Massive discovery of crystal structures across dimensionalities by leveraging vector quantization](../papers/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md)
- Tags: crystal structure generation, inverse design, materials discovery

## Supporting Datasets

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md)
- Original title in paper: MP-20
- Link: https://github.com/txie-93/cdvae

A curated subset of the Materials Project database containing 45,231 stable inorganic crystals with ≤20 atoms per unit cell, selected for training and benchmarking crystal generative models; used in this paper to train VQCrystal for 3D material discovery, evaluate reconstruction accuracy (match rate, RMS), validate generated structures against known entries, and perform property-targeted inverse design (e.g., bandgap and formation energy filtering).

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md)
- Original title in paper: Perov-5
- Link: https://github.com/txie-93/cdvae

A dataset of 18,928 perovskite crystal structures, each containing exactly five atoms per unit cell, derived from the Materials Project; used in this paper to benchmark VQCrystal’s structural reconstruction fidelity (e.g., 95.60% match rate, 0.0438 Å RMS) and interpretability (e.g., probing local latent encoding of atomic identity and position in ABX₃ frameworks).

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md)
- Original title in paper: Carbon-24
- Link: https://github.com/txie-93/cdvae

A dataset of 10,153 carbon-based crystal structures with 6–24 atoms per unit cell, compiled from computational sources including ab initio random structure searching; used in this paper to evaluate VQCrystal’s generalization across elemental systems and structural diversity (e.g., 70.03% match rate, superior Fréchet distance of 0.515 vs. baselines), and assess validity metrics like force and composition validity.

### [C2DB](../datasets/C2DB.md)

- Usage page: [usage note](../dataset_uses/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md)
- Original title in paper: C2DB
- Link: https://www.c2db.org/

The Computational 2D Materials Database, containing 3,521 experimentally and computationally validated 2D materials; used in this paper to train a dedicated VQCrystal model for 2D crystal generation, generate ~12,000 candidate structures, and perform stability-driven inverse design (e.g., filtering for formation energy < −1 eV/atom, validated via DFT on 23 relaxed structures with 73.91% success rate).
