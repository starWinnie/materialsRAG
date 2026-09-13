# 10_CrystalFramer - JARVIS-DFT

## Dataset Use

A publicly available dataset of 55,723 crystalline materials, each represented by its 3D unit cell (atomic species, Cartesian coordinates, lattice vectors) and annotated with DFT-simulated properties: formation energy per atom, total energy (OptB88vdW), bandgap (OptB88vdW and TBmBJ), and energy above hull. Used in this paper to train and evaluate CrystalFramer on five regression tasks with fixed train/validation/test splits (44,578 / 5,572 / 5,572 for most targets; 14,537 / 1,817 / 1,817 for MBJ bandgap), serving as a benchmark for SE(3)-invariant crystal encoders.

## Links

- Paper: [10 CrystalFramer](../papers/10_CrystalFramer.md)
- Task: [task page](../tasks/10_CrystalFramer_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting multiple physical properties of crystalline materials from their 3D crystal structures, including formation energy, total energy, bandgap (under two DFT functionals), energy above hull, bulk modulus, and shear modulus — all requiring SE(3)-invariant representations that respect periodicity, rotational/translation symmetry, and unit-cell ambiguity.

## Metadata

- Dataset use ID: `dataset_use_90b21b3174ab`
- Original dataset title: JARVIS-DFT 3D 2021
- Tags: crystal property prediction, SE(3)-invariant modeling, materials property regression

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
