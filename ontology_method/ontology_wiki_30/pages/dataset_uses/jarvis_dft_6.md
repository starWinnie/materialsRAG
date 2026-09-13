# JARVIS-DFT

## Ontology Type
DatasetUse

## Usage Description
A publicly available materials database containing 55,722 DFT-calculated crystalline materials, each with 19 computed properties including formation energy, bandgap (OPT and MBJ), total energy, Ehull, bulk modulus (Kv), shear modulus (Gv), SLME (%), and spillage. It provides full 3D structural information: atom types (A), fractional coordinates (F), and lattice vectors (L). In this paper, JARVIS-DFT is used exclusively for the downstream fine-tuning and evaluation phase — i.e., to train and test the crystal property prediction models on nine target properties under standard train/val/test splits (80%/10%/10%).

## Dataset
- [JARVIS-DFT](../datasets/jarvis_dft.md)

## Task
- [23_CrysDiff.pdf](../tasks/23_crysdiff_pdf.md)

## Paper
- [23 CrysDiff](../papers/23_crysdiff.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [atomic coordinates](../representations/atomic_coordinates.md)
- [lattice vectors](../representations/lattice_vectors.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- A publicly available materials database containing 55,722 DFT-calculated crystalline materials, each with 19 computed properties including formation energy, bandgap (OPT and MBJ), total energy, Ehull, bulk modulus (Kv), shear modulus (Gv), SLME (%), and spillage. It provides full 3D structural information: atom types (A), fractional coordinates (F), and lattice vectors (L). In this paper, JARVIS-DFT is used exclusively for the downstream fine-tuning and evaluation phase — i.e., to train and test the crystal property prediction models on nine target properties under standard train/val/test splits (80%/10%/10%).

## Metadata
dataset_use_id: `dataset_use_8fe9915f1b57`
link: https://jarvis.nist.gov/
