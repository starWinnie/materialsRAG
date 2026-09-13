# 37_CrysGNN - Materials Project

## Dataset Use

A DFT-calculated dataset containing 69,239 crystalline materials with two key properties: formation energy and optical bandgap. It is used as a property-tagged downstream dataset for training and evaluating distilled SOTA property predictors (e.g., CGCNN, ALIGNN). The paper explicitly states this version is a subset of the pre-training data and serves as a benchmark for measuring MAE improvements from knowledge distillation.

## Links

- Paper: [37 CrysGNN](../papers/37_CrysGNN.md)
- Task: [task page](../tasks/37_CrysGNN_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting multiple physical and electronic properties of crystalline materials—including formation energy, bandgap, total energy, bulk modulus, shear modulus, Ehull, spillage, SLME, and dielectric-related properties—using graph neural network models enhanced by distilled knowledge from a pre-trained GNN on unlabeled crystal structures.

## Metadata

- Dataset use ID: `dataset_use_b2263e9f177d`
- Original dataset title: Materials Project (MP) 2018.6.1
- Tags: property prediction, crystal structure modeling, knowledge distillation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
