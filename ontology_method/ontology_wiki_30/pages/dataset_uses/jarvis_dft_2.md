# JARVIS-DFT

## Ontology Type
DatasetUse

## Usage Description
A publicly available dataset of 55,723 crystalline materials, each represented by its 3D unit cell (atomic species, Cartesian coordinates, lattice vectors) and annotated with DFT-simulated properties: formation energy per atom, total energy (OptB88vdW), bandgap (OptB88vdW and TBmBJ), and energy above hull. Used in this paper to train and evaluate CrystalFramer on five regression tasks with fixed train/validation/test splits (44,578 / 5,572 / 5,572 for most targets; 14,537 / 1,817 / 1,817 for MBJ bandgap), serving as a benchmark for SE(3)-invariant crystal encoders.

## Dataset
- [JARVIS-DFT](../datasets/jarvis_dft.md)

## Task
- [10_CrystalFramer.pdf](../tasks/10_crystalframer_pdf.md)

## Paper
- [10 CrystalFramer](../papers/10_crystalframer.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [atomic coordinates](../representations/atomic_coordinates.md)
- [lattice vectors](../representations/lattice_vectors.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Validation](../stages/validation.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- A publicly available dataset of 55,723 crystalline materials, each represented by its 3D unit cell (atomic species, Cartesian coordinates, lattice vectors) and annotated with DFT-simulated properties: formation energy per atom, total energy (OptB88vdW), bandgap (OptB88vdW and TBmBJ), and energy above hull. Used in this paper to train and evaluate CrystalFramer on five regression tasks with fixed train/validation/test splits (44,578 / 5,572 / 5,572 for most targets; 14,537 / 1,817 / 1,817 for MBJ bandgap), serving as a benchmark for SE(3)-invariant crystal encoders.

## Metadata
dataset_use_id: `dataset_use_90b21b3174ab`
link: https://jarvis.nist.gov/
