# 47_Data-driven discovery of 2D materials by deep generative models - Task 1

## Task Description

Discovering new two-dimensional (2D) materials with high thermodynamic stability (energy above convex hull ΔHhull < 0.3 eV/atom) and structural/chemical novelty beyond known crystal prototypes, by generating candidate atomic structures de novo using deep generative modeling and systematic lattice decoration.

## Metadata

- Task ID: `task_d6641e402970`
- Source paper: [47 Data-driven discovery of 2D materials by deep generative models](../papers/47_Data-driven_discovery_of_2D_materials_by_deep_generative_models.md)
- Tags: materials discovery, 2D materials generation, thermodynamic stability prediction

## Supporting Datasets

### [C2DB](../datasets/C2DB.md)

- Usage page: [usage note](../dataset_uses/47_Data-driven_discovery_of_2D_materials_by_deep_generative_models_C2DB_dataset_use_2f8382.md)
- Original title in paper: Computational 2D Materials Database (C2DB)
- Link: https://cmr.fysik.dtu.dk/c2db/c2db.html

A publicly available computational database containing DFT-relaxed atomic structures and properties of over 4000 experimentally known and predicted 2D materials; in this paper, it provides the 2615 stable 2D materials (ΔHhull < 0.3 eV/atom) used as training data for the CDVAE and as seed structures for lattice decoration, and later hosts all 11630 newly predicted relaxed structures (8599 with ΔHhull < 0.3 eV/atom, 2004 within 50 meV of the convex hull) for community access and validation.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/47_Data-driven_discovery_of_2D_materials_by_deep_generative_models_Open_Quantum_Materials_.md)
- Original title in paper: Open Quantum Materials Database (OQMD)
- Link: https://oqmd.org/

A reference database of 9590 elementary, binary, and ternary bulk crystals lying within 20 meV of the convex hull, used to construct the thermodynamic convex hull for computing ΔHhull of generated 2D materials; its structures were re-evaluated with GPAW (without re-optimization) to ensure consistent energy referencing with the C2DB 2D materials during stability assessment.
