# 20_GMTNet - JARVIS-DFT

## Dataset Use

A curated collection of DFT-computed crystal tensor properties sourced from the JARVIS-DFT database, containing 4,713 dielectric tensors (unitless relative dielectric constants), 4,998 piezoelectric tensors (in C/m²), and 14,220 elastic tensors (in GPa), each paired with its corresponding crystal structure (atomic positions, lattice vectors, and elemental features). The dataset is constructed by extracting both tensor values and structures directly from consistent DFT calculation files to guarantee alignment between structural symmetry and tensor symmetry constraints, and is used to train and evaluate GMTNet’s ability to predict symmetry-respecting tensors.

## Links

- Paper: [20 GMTNet](../papers/20_GMTNet.md)
- Task: [task page](../tasks/20_GMTNet_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting crystal tensor properties—including dielectric tensors (order-2), piezoelectric tensors (order-3), and elastic tensors (order-4)—in matrix form while ensuring predictions are equivariant under O(3) transformations (rotations/reflections) and invariant under the crystal’s space group symmetries, so that predicted tensors respect zero-element patterns, mutual element dependencies, and physical transformation rules dictated by intrinsic crystal symmetry.

## Metadata

- Dataset use ID: `dataset_use_af6839f5e534`
- Original dataset title: JARVIS-DFT dataset
- Tags: tensor prediction, crystal symmetry enforcement, O(3) equivariance

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->
