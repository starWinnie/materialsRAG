# JARVIS-DFT

## Ontology Type
DatasetUse

## Usage Description
A curated collection of DFT-computed crystal tensor properties sourced from the JARVIS-DFT database, containing 4,713 dielectric tensors (unitless relative dielectric constants), 4,998 piezoelectric tensors (in C/m²), and 14,220 elastic tensors (in GPa), each paired with its corresponding crystal structure (atomic positions, lattice vectors, and elemental features). The dataset is constructed by extracting both tensor values and structures directly from consistent DFT calculation files to guarantee alignment between structural symmetry and tensor symmetry constraints, and is used to train and evaluate GMTNet’s ability to predict symmetry-respecting tensors.

## Dataset
- [JARVIS-DFT](../datasets/jarvis_dft.md)

## Task
- [20_GMTNet.pdf](../tasks/20_gmtnet_pdf.md)

## Paper
- [20 GMTNet](../papers/20_gmtnet.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [lattice vectors](../representations/lattice_vectors.md)
- [space group](../representations/space_group.md)
- [descriptor](../representations/descriptor.md)
- [spectrum or tensor](../representations/spectrum_or_tensor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)

## Evidence
- A curated collection of DFT-computed crystal tensor properties sourced from the JARVIS-DFT database, containing 4,713 dielectric tensors (unitless relative dielectric constants), 4,998 piezoelectric tensors (in C/m²), and 14,220 elastic tensors (in GPa), each paired with its corresponding crystal structure (atomic positions, lattice vectors, and elemental features). The dataset is constructed by extracting both tensor values and structures directly from consistent DFT calculation files to guarantee alignment between structural symmetry and tensor symmetry constraints, and is used to train and evaluate GMTNet’s ability to predict symmetry-respecting tensors.

## Metadata
dataset_use_id: `dataset_use_af6839f5e534`
link: https://jarvis.nist.gov/
