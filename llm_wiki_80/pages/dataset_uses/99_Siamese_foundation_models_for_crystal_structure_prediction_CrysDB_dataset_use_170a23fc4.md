# 99_Siamese foundation models for crystal structure prediction - CrysDB

## Dataset Use

A large-scale pretraining dataset comprising ~940K crystal structures (919,258 after deduplication), sourced from the Materials Project (MP) and Open Quantum Materials Database (OQMD). It includes both stable (Ehull ≤ 0.08 eV/atom) and unstable (0.08 < Ehull ≤ 1.0 eV/atom) crystals with 3–30 atoms per unit cell, annotated with energy above hull (Ehull). CrysDB is used to pretrain DAO-G (in a two-stage pipeline) and DAO-P, enabling learning of broad structural distributions and facilitating dataset relaxation and energy-guided sampling for CSP.

## Links

- Paper: [99 Siamese foundation models for crystal structure prediction](../papers/99_Siamese_foundation_models_for_crystal_structure_prediction.md)
- Task: [task page](../tasks/99_Siamese_foundation_models_for_crystal_structure_prediction_task_1.md)
- Dataset: [CrysDB](../datasets/CrysDB.md)
- Dataset URL: https://doi.org/10.6084/m9.figshare.31440697

## Task Context

Predicting the stable 3D crystal structure (lattice vectors and atomic fractional coordinates) of a material solely from its chemical composition, without any prior structural information — a task known as Crystal Structure Prediction (CSP). The model must generate thermodynamically stable structures that match experimental references in geometry and energy, especially for complex, large-unit-cell, or previously uncharacterized materials such as high-temperature superconductors.

## Metadata

- Dataset use ID: `dataset_use_170a23fc4556`
- Original dataset title: CrysDB
- Tags: crystal structure prediction, generative modeling, materials discovery
