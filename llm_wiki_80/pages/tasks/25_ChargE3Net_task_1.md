# 25_ChargE3Net - Task 1

## Task Description

Predicting the 3D electron charge density distribution of atomic systems (molecules and crystalline materials) from atomic species identities and Cartesian coordinates, to serve as an accurate initialization for self-consistent density functional theory (DFT) calculations and enable non-self-consistent property prediction.

## Metadata

- Task ID: `task_16fde01f7b15`
- Source paper: [25 ChargE3Net](../papers/25_ChargE3Net.md)
- Tags: charge density prediction, DFT initialization, electron density modeling

## Supporting Datasets

### [Materials Project (MP) charge density dataset](../datasets/Materials_Project_MP_charge_density_dataset.md)

- Usage page: [usage note](../dataset_uses/25_ChargE3Net_Materials_Project_MP_charge_density_dataset_dataset_use_173b4b3d221e.md)
- Original title in paper: Materials Project (MP) charge density dataset
- Link: https://api.materialsproject.org

A large-scale, publicly available dataset containing DFT-computed electron charge densities on 3D grids for 108,683 inorganic crystalline materials, covering diverse compositions, crystal systems, and space groups across the periodic table. It was used to train and evaluate ChargE3Net for generalizable, high-fidelity charge density prediction — specifically to support the task of initializing DFT calculations and reducing self-consistent field (SCF) iterations on unseen bulk materials.

### [QM9 charge density dataset](../datasets/QM9_charge_density_dataset.md)

- Usage page: [usage note](../dataset_uses/25_ChargE3Net_QM9_charge_density_dataset_dataset_use_91e9b63fe83d.md)
- Original title in paper: QM9 charge density dataset
- Link: https://doi.org/10.11583/DTU.16794500.v1

A dataset of VASP-calculated electron charge densities for 133,845 small organic molecules (with training/validation/test splits of 123,835/50/10,000), derived from the original QM9 molecular database. It contains grid-based charge density values computed at consistent resolution and boundary conditions, and was used to benchmark ChargE3Net’s accuracy on small, isolated molecules — supporting the core task of learning equivariant representations for charge density prediction under molecular symmetry constraints.

### [NMC (Nickel Manganese Cobalt) battery cathode dataset](../datasets/NMC_Nickel_Manganese_Cobalt_battery_cathode_dataset.md)

- Usage page: [usage note](../dataset_uses/25_ChargE3Net_NMC_Nickel_Manganese_Cobalt_battery_cathode_dataset_dataset_use_8f147f1ffe05.md)
- Original title in paper: NMC (Nickel Manganese Cobalt) battery cathode dataset
- Link: https://doi.org/10.11583/DTU.16837721.v1

A dataset of VASP-computed charge densities for 2,000 nickel-manganese-cobalt oxide structures with varying lithium content, sampled from battery cathode material space. It includes training/validation/test splits of 1,450/50/500 and provides charge density grids for crystalline solids with periodic boundary conditions. This dataset was used to evaluate ChargE3Net’s performance on a chemically focused, technologically relevant class of materials — supporting the task of predicting charge densities for transition-metal oxide systems where angular electron correlations are critical.

### [GNoME materials dataset (subset)](../datasets/GNoME_materials_dataset_subset.md)

- Usage page: [usage note](../dataset_uses/25_ChargE3Net_GNoME_materials_dataset_subset_dataset_use_eb7d715612ea.md)
- Original title in paper: GNoME materials dataset (subset)
- Link: https://doi.org/10.1038/s41586-023-06735-9

A curated subset of 1,924 novel inorganic materials published by Google’s GNoME project, selected to include structures with ≥5 unique elemental species — intentionally out-of-distribution relative to the Materials Project training set. It contains DFT-computed charge densities generated using consistent VASP settings (k-point density, energy cutoff, PAW potentials). This dataset was used to test ChargE3Net’s generalization capability for charge density prediction on previously unseen chemical spaces — directly supporting the task of robust cross-dataset transfer for DFT acceleration beyond the training domain.
