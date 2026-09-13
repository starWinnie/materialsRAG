# 06_Transformer_Atomic_Embeddings - HOIP Dataset

## Dataset Use

A merged dataset of 2,103 HOIP crystals compiled from two prior sources (Kim et al., 2017 and Nakajima & Sawada, 2017); used to evaluate ct-UAEs in data-scarce regimes where traditional ML models underperform. Supports the task by serving as a low-data target domain for transfer learning—ct-UAEs pretrained on MP* significantly improve formation energy prediction accuracy (e.g., 34% MAE reduction for MEGNET), directly addressing the challenge of data scarcity in complex functional materials.

## Links

- Paper: [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md)
- Task: [task page](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- Dataset: [HOIP Dataset](../datasets/HOIP_Dataset.md)
- Dataset URL: https://doi.org/10.1038/sdata.2017.152

## Task Context

Generating universal atomic embeddings that serve as transferable, task-agnostic atomic fingerprints to improve the accuracy of machine learning models predicting crystal properties—including formation energy, bandgap, total energy, and total magnetization—across diverse material systems and data-scarce domains such as hybrid organic-inorganic perovskites.

## Metadata

- Dataset use ID: `dataset_use_c9f9564247e0`
- Original dataset title: Hybrid Organic-Inorganic Perovskite (HOIP) dataset
- Tags: atomic embedding, crystal property prediction, transfer learning
