# 89_Generative deep learning for predicting ultrahigh lattice thermal conductivity materials - Task 1

## Task Description

Predicting ultrahigh lattice thermal conductivity (κL) materials—specifically, identifying novel crystalline carbon polymorphs with κL exceeding 800 W m⁻¹ K⁻¹ at room temperature—while ensuring thermodynamic stability through energy-optimized structures and accurate phonon-based thermal property prediction.

## Metadata

- Task ID: `task_d57eb460fca2`
- Source paper: [89 Generative deep learning for predicting ultrahigh lattice thermal conductivity materials](../papers/89_Generative_deep_learning_for_predicting_ultrahigh_lattice_thermal_conductivity_material.md)
- Tags: lattice thermal conductivity prediction, crystal structure generation, ultrahigh-κL material screening

## Supporting Datasets

### [Pickard's Carbon Allotrope Dataset (AIRSS-generated)](../datasets/Pickard_s_Carbon_Allotrope_Dataset_AIRSS-generated.md)

- Usage page: [usage note](../dataset_uses/89_Generative_deep_learning_for_predicting_ultrahigh_lattice_thermal_conductivity_material.md)
- Original title in paper: Pickard's Carbon Allotrope Dataset (AIRSS-generated)
- Link: https://doi.org/10.24435/MATERIALSCLOUD:2020.0026/V1

A dataset of 101,529 carbon periodic structures generated via ab initio random structure searching (AIRSS) at 10 GPa, containing unit cells with 6–24 atoms, all residing at local energy minima (i.e., locally stable). This dataset serves as the training source for the CDVAE generative model and provides the initial candidate pool for ultrahigh-κL screening; the authors use the lowest-energy 10% (randomly split 60/20/20) to train the model and subsequently generate 100,000 new candidates.

### [GAP-2020 (Carbon subset)](../datasets/GAP-2020_Carbon_subset.md)

- Usage page: [usage note](../dataset_uses/89_Generative_deep_learning_for_predicting_ultrahigh_lattice_thermal_conductivity_material.md)
- Original title in paper: GAP-2020 (Carbon subset)
- Link: https://doi.org/10.1063/5.0007721

A curated subset of the GAP-2020 database containing diverse carbon configurations—including RSS crystalline, bulk crystalline, SACADA crystals, diamond, graphite, nanotubes, fullerenes, and amorphous forms—filtered to include only structures with energy < −4.5 eV/atom and force magnitudes < 30 eV/Å (5,445 total configurations). It is used to pre-train the Allegro ML interatomic potential and initialize the active learning pipeline for high-fidelity stability and κL prediction.

### [Samara Carbon Allotrope Database (SACADA)](../datasets/Samara_Carbon_Allotrope_Database_SACADA.md)

- Usage page: [usage note](../dataset_uses/89_Generative_deep_learning_for_predicting_ultrahigh_lattice_thermal_conductivity_material.md)
- Original title in paper: Samara Carbon Allotrope Database (SACADA)
- Link: https://sacada.org/

A public repository of experimentally and computationally reported carbon allotropes, integrated into the GAP-2020 training set. It provides structurally diverse, validated carbon crystal references (e.g., known polymorphs beyond diamond) that enrich the pre-training data for the Allegro potential, enabling robust generalization across sp/sp²/sp³ bonding environments during structural optimization and κL evaluation.
