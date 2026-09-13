# 37_CrysGNN - Open Quantum Materials Database

## Dataset Use

A small experimental dataset of 1,500 materials with measured formation energy values, derived from the Open Quantum Materials Database. It is used specifically to evaluate how distilled knowledge from CrysGNN helps mitigate DFT-induced bias—by training models on mixed DFT + experimental data and testing on held-out experimental data—to quantify reduction in MAE against ground-truth experimental measurements.

## Links

- Paper: [37 CrysGNN](../papers/37_CrysGNN.md)
- Task: [task page](../tasks/37_CrysGNN_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org/

## Task Context

Predicting multiple physical and electronic properties of crystalline materials—including formation energy, bandgap, total energy, bulk modulus, shear modulus, Ehull, spillage, SLME, and dielectric-related properties—using graph neural network models enhanced by distilled knowledge from a pre-trained GNN on unlabeled crystal structures.

## Metadata

- Dataset use ID: `dataset_use_3cec11bf24e2`
- Original dataset title: OQMD-EXP
- Tags: property prediction, crystal structure modeling, knowledge distillation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
