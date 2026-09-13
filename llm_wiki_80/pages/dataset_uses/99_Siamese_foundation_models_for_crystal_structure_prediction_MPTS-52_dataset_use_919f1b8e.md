# 99_Siamese foundation models for crystal structure prediction - MPTS-52

## Dataset Use

A more challenging CSP benchmark from the Materials Project, containing 40,476 crystal structures with up to 52 atoms per unit cell — capturing greater structural complexity than MP-20. It serves as a downstream fine-tuning and evaluation set for DAO-G, with strict deduplication against CrysDB to avoid contamination, enabling assessment of generalization to larger, more diverse systems.

## Links

- Paper: [99 Siamese foundation models for crystal structure prediction](../papers/99_Siamese_foundation_models_for_crystal_structure_prediction.md)
- Task: [task page](../tasks/99_Siamese_foundation_models_for_crystal_structure_prediction_task_1.md)
- Dataset: [MPTS-52](../datasets/MPTS-52.md)
- Dataset URL: https://next-gen.materialsproject.org

## Task Context

Predicting the stable 3D crystal structure (lattice vectors and atomic fractional coordinates) of a material solely from its chemical composition, without any prior structural information — a task known as Crystal Structure Prediction (CSP). The model must generate thermodynamically stable structures that match experimental references in geometry and energy, especially for complex, large-unit-cell, or previously uncharacterized materials such as high-temperature superconductors.

## Metadata

- Dataset use ID: `dataset_use_919f1b8e6d37`
- Original dataset title: MPTS-52
- Tags: crystal structure prediction, generative modeling, materials discovery
