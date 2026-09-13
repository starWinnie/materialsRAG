# CrysDB

## Metadata

- Dataset ID: `dataset_6f5369c60377`
- Aliases: CrysDB
- Links: https://doi.org/10.6084/m9.figshare.31440697
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A large-scale pretraining dataset comprising ~940K crystal structures (919,258 after deduplication), sourced from the Materials Project (MP) and Open Quantum Materials Database (OQMD). It includes both stable (Ehull ≤ 0.08 eV/atom) and unstable (0.08 < Ehull ≤ 1.0 eV/atom) crystals with 3–30 atoms per unit cell, annotated with energy above hull (Ehull). CrysDB is used to pretrain DAO-G (in a two-stage pipeline) and DAO-P, enabling learning of broad structural distributions and facilitating dataset relaxation and energy-guided sampling for CSP.

## Uses

- [99_Siamese foundation models for crystal structure prediction](../dataset_uses/99_Siamese_foundation_models_for_crystal_structure_prediction_CrysDB_dataset_use_170a23fc4.md): [99 Siamese foundation models for crystal structure prediction](../papers/99_Siamese_foundation_models_for_crystal_structure_prediction.md), [task](../tasks/99_Siamese_foundation_models_for_crystal_structure_prediction_task_1.md)
