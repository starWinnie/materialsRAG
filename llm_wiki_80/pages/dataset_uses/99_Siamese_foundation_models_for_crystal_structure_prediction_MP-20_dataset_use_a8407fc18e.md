# 99_Siamese foundation models for crystal structure prediction - MP-20

## Dataset Use

A benchmark dataset derived from the Materials Project, containing 45,231 crystal structures limited to ≤20 atoms per unit cell. It is used for fine-tuning and evaluating DAO-G’s CSP performance via Match Rate (MR) and RMSE against ground-truth structures; the dataset is explicitly excluded from CrysDB during deduplication to prevent data leakage and ensure rigorous out-of-distribution evaluation.

## Links

- Paper: [99 Siamese foundation models for crystal structure prediction](../papers/99_Siamese_foundation_models_for_crystal_structure_prediction.md)
- Task: [task page](../tasks/99_Siamese_foundation_models_for_crystal_structure_prediction_task_1.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://next-gen.materialsproject.org

## Task Context

Predicting the stable 3D crystal structure (lattice vectors and atomic fractional coordinates) of a material solely from its chemical composition, without any prior structural information — a task known as Crystal Structure Prediction (CSP). The model must generate thermodynamically stable structures that match experimental references in geometry and energy, especially for complex, large-unit-cell, or previously uncharacterized materials such as high-temperature superconductors.

## Metadata

- Dataset use ID: `dataset_use_a8407fc18e3d`
- Original dataset title: MP-20
- Tags: crystal structure prediction, generative modeling, materials discovery
