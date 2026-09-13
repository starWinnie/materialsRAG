# 99_Siamese foundation models for crystal structure prediction - Task 1

## Task Description

Predicting the stable 3D crystal structure (lattice vectors and atomic fractional coordinates) of a material solely from its chemical composition, without any prior structural information — a task known as Crystal Structure Prediction (CSP). The model must generate thermodynamically stable structures that match experimental references in geometry and energy, especially for complex, large-unit-cell, or previously uncharacterized materials such as high-temperature superconductors.

## Metadata

- Task ID: `task_f51228e4b019`
- Source paper: [99 Siamese foundation models for crystal structure prediction](../papers/99_Siamese_foundation_models_for_crystal_structure_prediction.md)
- Tags: crystal structure prediction, generative modeling, materials discovery

## Supporting Datasets

### [CrysDB](../datasets/CrysDB.md)

- Usage page: [usage note](../dataset_uses/99_Siamese_foundation_models_for_crystal_structure_prediction_CrysDB_dataset_use_170a23fc4.md)
- Original title in paper: CrysDB
- Link: https://doi.org/10.6084/m9.figshare.31440697

A large-scale pretraining dataset comprising ~940K crystal structures (919,258 after deduplication), sourced from the Materials Project (MP) and Open Quantum Materials Database (OQMD). It includes both stable (Ehull ≤ 0.08 eV/atom) and unstable (0.08 < Ehull ≤ 1.0 eV/atom) crystals with 3–30 atoms per unit cell, annotated with energy above hull (Ehull). CrysDB is used to pretrain DAO-G (in a two-stage pipeline) and DAO-P, enabling learning of broad structural distributions and facilitating dataset relaxation and energy-guided sampling for CSP.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/99_Siamese_foundation_models_for_crystal_structure_prediction_MP-20_dataset_use_a8407fc18e.md)
- Original title in paper: MP-20
- Link: https://next-gen.materialsproject.org

A benchmark dataset derived from the Materials Project, containing 45,231 crystal structures limited to ≤20 atoms per unit cell. It is used for fine-tuning and evaluating DAO-G’s CSP performance via Match Rate (MR) and RMSE against ground-truth structures; the dataset is explicitly excluded from CrysDB during deduplication to prevent data leakage and ensure rigorous out-of-distribution evaluation.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/99_Siamese_foundation_models_for_crystal_structure_prediction_MPTS-52_dataset_use_919f1b8e.md)
- Original title in paper: MPTS-52
- Link: https://next-gen.materialsproject.org

A more challenging CSP benchmark from the Materials Project, containing 40,476 crystal structures with up to 52 atoms per unit cell — capturing greater structural complexity than MP-20. It serves as a downstream fine-tuning and evaluation set for DAO-G, with strict deduplication against CrysDB to avoid contamination, enabling assessment of generalization to larger, more diverse systems.

### [SuperCon3D](../datasets/SuperCon3D.md)

- Usage page: [usage note](../dataset_uses/99_Siamese_foundation_models_for_crystal_structure_prediction_SuperCon3D_dataset_use_efff2.md)
- Original title in paper: SuperCon3D
- Link: https://doi.org/10.48505/nims.3739

A curated 3D structural subset of the SuperCon database, containing 1,017 ordered superconductors with experimentally determined crystal structures and critical temperatures (Tc). It is used to fine-tune DAO-G for superconductor-specific structure generation and to fine-tune DAO-P (with and without augmentation) for Tc prediction — validating CSP capability on real-world, high-complexity superconducting materials unseen during pretraining.
