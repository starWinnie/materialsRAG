# 46_Novel inorganic crystal structures predicted using autonomous simulation agents - Task 1

## Task Description

Predicting the thermodynamic stability (i.e., energy above the convex hull) of hypothetical inorganic crystal structures to identify novel stable and metastable materials, specifically targeting structures within 1 meV/atom (ground states) and 200 meV/atom (metastable) of the convex hull for accelerated materials discovery.

## Metadata

- Task ID: `task_d2937fd62655`
- Source paper: [46 Novel inorganic crystal structures predicted using autonomous simulation agents](../papers/46_Novel_inorganic_crystal_structures_predicted_using_autonomous_simulation_agents.md)
- Tags: crystal structure prediction, phase stability prediction, thermodynamic stability screening

## Supporting Datasets

### [CAMD Dataset (2022)](../datasets/CAMD_Dataset_2022.md)

- Usage page: [usage note](../dataset_uses/46_Novel_inorganic_crystal_structures_predicted_using_autonomous_simulation_agents_CAMD_Da.md)
- Original title in paper: CAMD Dataset (2022)
- Link: https://doi.org/10.6084/m9.figshare.19601956.v1

A dataset of 96,640 DFT-computed inorganic crystal structures generated via the CAMD autonomous active-learning workflow, including pymatgen Structure objects, formation energies (eV/atom), energies above the convex hull (stability), space groups, chemical systems, reduced formulas, and 273 composition- and structure-derived features. It is used to train and validate machine learning models for predicting formation energy and phase stability, and to screen for thermodynamically stable/metastable candidates during active-learning campaigns.

### [OQMD-ICSD (Open Quantum Materials Database — Inorganic Crystal Structure Database subset)](../datasets/OQMD-ICSD_Open_Quantum_Materials_Database_-_Inorganic_Crystal_Structure_Database_subset.md)

- Usage page: [usage note](../dataset_uses/46_Novel_inorganic_crystal_structures_predicted_using_autonomous_simulation_agents_OQMD-IC.md)
- Original title in paper: OQMD-ICSD (Open Quantum Materials Database — Inorganic Crystal Structure Database subset)
- Link: https://oqmd.org/

A seed dataset of 34,463 experimentally derived crystal structures from the ICSD, integrated into the OQMD, used to initialize the CAMD active-learning agents and define the baseline convex hull against which the thermodynamic stability of newly predicted structures is measured. It provides ground-truth experimental reference structures and formation energies essential for computing energy-above-hull values and training initial ML models.
