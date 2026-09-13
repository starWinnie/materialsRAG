# 20_GMTNet - Task 1

## Task Description

Predicting crystal tensor properties—including dielectric tensors (order-2), piezoelectric tensors (order-3), and elastic tensors (order-4)—in matrix form while ensuring predictions are equivariant under O(3) transformations (rotations/reflections) and invariant under the crystal’s space group symmetries, so that predicted tensors respect zero-element patterns, mutual element dependencies, and physical transformation rules dictated by intrinsic crystal symmetry.

## Metadata

- Task ID: `task_78314418eccc`
- Source paper: [20 GMTNet](../papers/20_GMTNet.md)
- Tags: tensor prediction, crystal symmetry enforcement, O(3) equivariance

## Supporting Datasets

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/20_GMTNet_JARVIS-DFT_dataset_use_af6839f5e534.md)
- Original title in paper: JARVIS-DFT dataset
- Link: https://jarvis.nist.gov/

A curated collection of DFT-computed crystal tensor properties sourced from the JARVIS-DFT database, containing 4,713 dielectric tensors (unitless relative dielectric constants), 4,998 piezoelectric tensors (in C/m²), and 14,220 elastic tensors (in GPa), each paired with its corresponding crystal structure (atomic positions, lattice vectors, and elemental features). The dataset is constructed by extracting both tensor values and structures directly from consistent DFT calculation files to guarantee alignment between structural symmetry and tensor symmetry constraints, and is used to train and evaluate GMTNet’s ability to predict symmetry-respecting tensors.
