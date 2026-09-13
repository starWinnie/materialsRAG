# 37_CrysGNN - JARVIS-DFT

## Dataset Use

A DFT-based materials database comprising 55,722 crystalline materials with 19 computed properties—including formation energy, bandgap (MBJ and OPT), total energy, bulk modulus, shear modulus, Ehull, spillage, SLME, and electronic properties like epsilon_x/y/z and n-Seebeck. Used as an independent downstream evaluation dataset (not seen during pre-training) to assess generalization of distilled models across diverse structural and electronic properties.

## Links

- Paper: [37 CrysGNN](../papers/37_CrysGNN.md)
- Task: [task page](../tasks/37_CrysGNN_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting multiple physical and electronic properties of crystalline materials—including formation energy, bandgap, total energy, bulk modulus, shear modulus, Ehull, spillage, SLME, and dielectric-related properties—using graph neural network models enhanced by distilled knowledge from a pre-trained GNN on unlabeled crystal structures.

## Metadata

- Dataset use ID: `dataset_use_ba0c2a957168`
- Original dataset title: JARVIS-DFT (2021.8.18)
- Tags: property prediction, crystal structure modeling, knowledge distillation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
