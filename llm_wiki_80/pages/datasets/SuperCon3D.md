# SuperCon3D

## Metadata

- Dataset ID: `dataset_a1d68951db7c`
- Aliases: SuperCon3D
- Links: https://doi.org/10.48505/nims.3739, https://github.com/pincher-chen/SODNet
- Used by papers: 2
- Dataset usage records: 2

## Description Examples

- SuperCon3D is a newly constructed dataset containing 1,578 experimentally verified superconductors, each with both a 3D crystal structure (ordered or disordered, including substitutional, positional, and combined disorder types) and its experimentally measured superconducting transition temperature (Tc). It was built by matching 11,949 superconductors from the SuperCon database (with chemical formulas and Tc) against 208,425 entries from the ICSD database using chemical composition, space group, and lattice parameters; hydrogen-enriched superconductors were supplemented from literature. This dataset directly supports the Tc prediction task for training and evaluating SODNet and benchmarking other property predictors.
- A curated 3D structural subset of the SuperCon database, containing 1,017 ordered superconductors with experimentally determined crystal structures and critical temperatures (Tc). It is used to fine-tune DAO-G for superconductor-specific structure generation and to fine-tune DAO-P (with and without augmentation) for Tc prediction — validating CSP capability on real-world, high-complexity superconducting materials unseen during pretraining.

## Uses

- [31_Superconductivity_Ordered_Disordered](../dataset_uses/31_Superconductivity_Ordered_Disordered_SuperCon3D_dataset_use_1ec550fb8fdf.md): [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md), [task](../tasks/31_Superconductivity_Ordered_Disordered_task_1.md)
- [99_Siamese foundation models for crystal structure prediction](../dataset_uses/99_Siamese_foundation_models_for_crystal_structure_prediction_SuperCon3D_dataset_use_efff2.md): [99 Siamese foundation models for crystal structure prediction](../papers/99_Siamese_foundation_models_for_crystal_structure_prediction.md), [task](../tasks/99_Siamese_foundation_models_for_crystal_structure_prediction_task_1.md)
