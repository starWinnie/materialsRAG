# 50_Diffusion probabilistic models enhance variational autoencoder for crystal structure generative modeling - MP-20

## Dataset Use

A subset of the Materials Project database containing approximately 20,000 diverse inorganic compounds spanning multiple crystal systems, stoichiometries, and chemical spaces. It provides experimentally validated or DFT-optimized crystal structures with full structural metadata (lattice, sites, symmetry) and computed properties (formation energy, density). In this work, MP-20 serves as a broad-scale benchmark for generative performance—used to evaluate validity, COV-R/P, and Wasserstein distances of property distributions (density, formation energy, number of elements) between generated and real structures, thereby testing generalization across heterogeneous materials.

## Links

- Paper: [50 Diffusion probabilistic models enhance variational autoencoder for crystal structure generative modeling](../papers/50_Diffusion_probabilistic_models_enhance_variational_autoencoder_for_crystal_structure_ge.md)
- Task: [task page](../tasks/50_Diffusion_probabilistic_models_enhance_variational_autoencoder_for_crystal_structure_ge.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating realistic, symmetry-preserving crystal structures that are close to their quantum-mechanically relaxed ground states—specifically, producing fractional atomic coordinates, lattice parameters, and atomic types for unseen crystals such that the generated structures exhibit low energy differences (< ~400 meV/atom) and small structural deviations (e.g., RMS displacement, volume error) relative to DFT-relaxed configurations.

## Metadata

- Dataset use ID: `dataset_use_91df18231647`
- Original dataset title: MP-20
- Tags: crystal structure generation, ground-state structure prediction, generative modeling
