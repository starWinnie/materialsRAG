# 06_Transformer_Atomic_Embeddings - Materials Project

## Dataset Use

The 2018.6.1 version contains 69,239 crystalline materials with computed formation energies (Ef) and PBE bandgaps (Eg); used for training and evaluating back-end models (e.g., CGCNN, ALIGNN, MEGNET) and benchmarking ct-UAE performance on formation energy and bandgap prediction. The dataset is split into 60,000 training, 5,000 validation, and 4,239 test samples. It supports the core task by providing ground-truth labels for supervised pretraining of front-end embeddings and downstream property prediction evaluation.

## Links

- Paper: [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md)
- Task: [task page](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating universal atomic embeddings that serve as transferable, task-agnostic atomic fingerprints to improve the accuracy of machine learning models predicting crystal properties—including formation energy, bandgap, total energy, and total magnetization—across diverse material systems and data-scarce domains such as hybrid organic-inorganic perovskites.

## Metadata

- Dataset use ID: `dataset_use_b6c12572d788`
- Original dataset title: Materials Project (MP) database
- Tags: atomic embedding, crystal property prediction, transfer learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
