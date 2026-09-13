# 10_CrystalFramer - Materials Project (MP)

## Dataset Use

A large-scale database of ~69,239 synthetically feasible crystalline materials, providing DFT-calculated properties including formation energy, PBE bandgap, bulk modulus, and shear modulus. In this paper, it is used for crystal property prediction across four regression tasks using standardized data splits (60,000 / 5,000 / 4,239 for formation energy and bandgap; ~4,664 / ~393 / ~393 for moduli), enabling comparison against state-of-the-art models and validation of generalization beyond JARVIS.

## Links

- Paper: [10 CrystalFramer](../papers/10_CrystalFramer_paper_376c54bdb055.md)
- Task: [task page](../tasks/10_CrystalFramer_task_1_task_f4a8c4f8f856.md)
- Dataset: [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting multiple physical properties of crystalline materials from their 3D crystal structures, including formation energy, total energy, bandgap (under two DFT functionals), energy above hull, bulk modulus, and shear modulus — all requiring SE(3)-invariant representations that respect periodicity, rotational/translation symmetry, and unit-cell ambiguity.

## Metadata

- Dataset use ID: `dataset_use_f5d1c7f17083`
- Original dataset title: Materials Project (MP)
- Tags: crystal property prediction, SE(3)-invariant modeling, materials property regression

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
