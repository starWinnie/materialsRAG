# 06_Transformer_Atomic_Embeddings - MC3D dataset

## Dataset Use

A dataset containing 3D crystal structures and associated total energies (E); used to assess ct-UAE performance on a distinct property (total energy) and in a different materials domain. Applied to enhance CGCNN, MEGNET, and ALIGNN models, yielding MAE reductions (e.g., 3.9% for CGCNN), confirming the task-supporting role of ct-UAEs in broadening applicability beyond formation energy and bandgap to other fundamental crystal properties.

## Links

- Paper: [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md)
- Task: [task page](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- Dataset: [MC3D dataset](../datasets/MC3D_dataset.md)
- Dataset URL: https://github.com/usnistgov/jarvis/tree/master/jarvis/core

## Task Context

Generating universal atomic embeddings that serve as transferable, task-agnostic atomic fingerprints to improve the accuracy of machine learning models predicting crystal properties—including formation energy, bandgap, total energy, and total magnetization—across diverse material systems and data-scarce domains such as hybrid organic-inorganic perovskites.

## Metadata

- Dataset use ID: `dataset_use_86b751f702ce`
- Original dataset title: MC3D dataset
- Tags: atomic embedding, crystal property prediction, transfer learning
