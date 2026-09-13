# 99_Siamese foundation models for crystal structure prediction - SuperCon3D

## Dataset Use

A curated 3D structural subset of the SuperCon database, containing 1,017 ordered superconductors with experimentally determined crystal structures and critical temperatures (Tc). It is used to fine-tune DAO-G for superconductor-specific structure generation and to fine-tune DAO-P (with and without augmentation) for Tc prediction — validating CSP capability on real-world, high-complexity superconducting materials unseen during pretraining.

## Links

- Paper: [99 Siamese foundation models for crystal structure prediction](../papers/99_Siamese_foundation_models_for_crystal_structure_prediction.md)
- Task: [task page](../tasks/99_Siamese_foundation_models_for_crystal_structure_prediction_task_1.md)
- Dataset: [SuperCon3D](../datasets/SuperCon3D.md)
- Dataset URL: https://doi.org/10.48505/nims.3739

## Task Context

Predicting the stable 3D crystal structure (lattice vectors and atomic fractional coordinates) of a material solely from its chemical composition, without any prior structural information — a task known as Crystal Structure Prediction (CSP). The model must generate thermodynamically stable structures that match experimental references in geometry and energy, especially for complex, large-unit-cell, or previously uncharacterized materials such as high-temperature superconductors.

## Metadata

- Dataset use ID: `dataset_use_efff2da8b6c3`
- Original dataset title: SuperCon3D
- Tags: crystal structure prediction, generative modeling, materials discovery
