# 50_Diffusion probabilistic models enhance variational autoencoder for crystal structure generative modeling - Task 1

## Task Description

Generating realistic, symmetry-preserving crystal structures that are close to their quantum-mechanically relaxed ground states—specifically, producing fractional atomic coordinates, lattice parameters, and atomic types for unseen crystals such that the generated structures exhibit low energy differences (< ~400 meV/atom) and small structural deviations (e.g., RMS displacement, volume error) relative to DFT-relaxed configurations.

## Metadata

- Task ID: `task_d174c041a113`
- Source paper: [50 Diffusion probabilistic models enhance variational autoencoder for crystal structure generative modeling](../papers/50_Diffusion_probabilistic_models_enhance_variational_autoencoder_for_crystal_structure_ge.md)
- Tags: crystal structure generation, ground-state structure prediction, generative modeling

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/50_Diffusion_probabilistic_models_enhance_variational_autoencoder_for_crystal_structure_ge.md)
- Original title in paper: Perov-5
- Link: None

A dataset of 53 perovskite materials with cubic crystal symmetry, containing variations in elemental composition while preserving the perovskite ABX₃ stoichiometry and structure type. It includes full crystallographic information: fractional atomic coordinates, lattice parameters, space group, and atomic identities. In this paper, Perov-5 is used to train and evaluate the DP-CDVAE model’s reconstruction and generation performance—specifically to assess match rate and ⟨δrms⟩ against ground-truth structures, and to benchmark validity, coverage, and property distribution fidelity (e.g., density, formation energy).

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/50_Diffusion_probabilistic_models_enhance_variational_autoencoder_for_crystal_structure_ge.md)
- Original title in paper: Carbon-24
- Link: https://doi.org/10.24435/MATERIALSCLOUD:2020.0026/V1

A dataset of 24 carbon allotropes generated via ab initio random structure searching at 10 GPa pressure, covering diverse crystal systems (e.g., diamond, graphite, BC8, R8). It contains DFT-optimized crystal structures—including fractional coordinates, lattice matrices, and atomic types—with known ground-state energies and volumes at 10 GPa. This dataset is central to the ground-state performance evaluation: 100 generated structures from DP-CDVAE are relaxed using DFT, and their energy differences (ΔE), RMS displacement (⟨δrms⟩), and volume errors (ΔVrms) relative to relaxed counterparts are computed to quantify proximity to true ground states.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/50_Diffusion_probabilistic_models_enhance_variational_autoencoder_for_crystal_structure_ge.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of the Materials Project database containing approximately 20,000 diverse inorganic compounds spanning multiple crystal systems, stoichiometries, and chemical spaces. It provides experimentally validated or DFT-optimized crystal structures with full structural metadata (lattice, sites, symmetry) and computed properties (formation energy, density). In this work, MP-20 serves as a broad-scale benchmark for generative performance—used to evaluate validity, COV-R/P, and Wasserstein distances of property distributions (density, formation energy, number of elements) between generated and real structures, thereby testing generalization across heterogeneous materials.
