# 24_Structure_Aware_Transfer_Learning - Task 1

## Task Description

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Task ID: `task_25b6baf65d50`
- Source paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Tags: materials property prediction, transfer learning, structure-aware modeling

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Materials_Project_dataset_use_adb846e44575.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org/

A large-scale DFT-computed database containing ~140,000 inorganic crystalline materials with relaxed crystal structures (POSCAR files) and computed properties including formation energy, bandgap, elastic tensors, and more. In this paper, it serves as the *source dataset*: its formation energy labels and 3D crystal structures are used to pre-train the ALIGNN source model for transfer learning across diverse target properties and material classes.

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_JARVIS-DFT_dataset_use_0ee7894cdd6e.md)
- Original title in paper: JARVIS-3D
- Link: https://jarvis.nist.gov

A DFT-computed database of ~55,000 3D crystalline materials with atomic structures and 46 distinct properties (e.g., bulk modulus, dielectric tensor, piezoelectric coefficients, bandgap). It is used as a *target dataset* for evaluating transfer learning performance — specifically, its formation energy, bandgap, and other solid-state properties are predicted using models fine-tuned or feature-extracted from the MP-pretrained ALIGNN model.

### [JARVIS-2D](../datasets/JARVIS-2D.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_JARVIS-2D_dataset_use_a1488a358518.md)
- Original title in paper: JARVIS-2D
- Link: https://jarvis.nist.gov

A DFT-computed database of ~1,000–2,000 2D layered materials (e.g., graphene, TMDs) with atomic structures and 32 properties including exfoliation energy, dielectric response, and electronic band structure metrics. It serves as a *target dataset* to test cross-dimensionality transfer learning: the MP-pretrained ALIGNN model is applied to predict properties of 2D materials, enabling evaluation of structural generalization beyond the 3D training domain.

### [Harvard Organic Photovoltaic Dataset (HOPV)](../datasets/Harvard_Organic_Photovoltaic_Dataset_HOPV.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Harvard_Organic_Photovoltaic_Dataset_HOPV_dataset_use.md)
- Original title in paper: Harvard Organic Photovoltaic Dataset (HOPV)
- Link: https://ndownloader.figshare.com/files/28814184

A quantum-chemical dataset of 1,000+ organic molecules with SMILES strings and DFT-computed properties (24 total), including HOMO/LUMO energies, bandgaps, and photovoltaic metrics (e.g., scharber PCE, Jsc, Voc) under multiple functionals (B3LYP, PBE0, etc.). It functions as a *target dataset* for cross-material-class transfer learning — testing whether structure-aware features learned from inorganic crystals (MP) generalize to molecular systems for predicting organic electronic properties.

### [Flla](../datasets/Flla.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Flla_dataset_use_9e5287aec96f.md)
- Original title in paper: Flla
- Link: https://github.com/hackingmaterials/automatminer

A DFT-computed dataset of ~3,900 inorganic compounds with formation energy, hull energy, and atomic relaxation data. Used as a *target dataset* to assess transfer learning robustness across independently computed DFT databases with different computational settings; its properties (e.g., DeltaE, Ehull) are predicted using the MP-pretrained ALIGNN model.

### [Dielectric Constant (DC) Database](../datasets/Dielectric_Constant_DC_Database.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Dielectric_Constant_DC_Database_dataset_use_ad047471e.md)
- Original title in paper: Dielectric Constant (DC) Database
- Link: https://github.com/hackingmaterials/automatminer

A DFT-computed dataset of ~1,000 inorganic materials with dielectric properties (static/dynamic dielectric tensors, refractive index, polarizability) and structural information. Serves as a *target dataset* for predicting low-data-count dielectric properties (e.g., volume, bandgap, N, poly-electric susceptibility) using transfer learning from MP, enabling validation on physically distinct property types.

### [Piezoelectric Tensor (PT) Database](../datasets/Piezoelectric_Tensor_PT_Database.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Piezoelectric_Tensor_PT_Database_dataset_use_73b1a9ad.md)
- Original title in paper: Piezoelectric Tensor (PT) Database
- Link: https://github.com/hackingmaterials/automatminer

A DFT-computed dataset of ~940 non-centrosymmetric crystals with piezoelectric tensors, volumes, and related structural descriptors. Used as a *target dataset* to evaluate transfer learning on highly anisotropic, symmetry-sensitive properties (e.g., Eij piezoelectric coefficients, volume) where data scarcity limits conventional modeling — predictions rely on features transferred from the MP source model.

### [Experimental Formation Energy (EFE)](../datasets/Experimental_Formation_Energy_EFE.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Experimental_Formation_Energy_EFE_dataset_use_c418be3.md)
- Original title in paper: Experimental Formation Energy (EFE)
- Link: https://github.com/hackingmaterials/automatminer

An experimental dataset of 605 intermetallic compounds with measured formation enthalpies (DeltaE) derived from calorimetry. Functions as a *target dataset* to validate transfer learning on real-world experimental data — the MP-pretrained ALIGNN model is adapted to predict experimental formation energies, bridging computation-to-experiment gaps.

### [Kingsbury Experimental Formation Energy (KEFE)](../datasets/Kingsbury_Experimental_Formation_Energy_KEFE.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Kingsbury_Experimental_Formation_Energy_KEFE_dataset_.md)
- Original title in paper: Kingsbury Experimental Formation Energy (KEFE)
- Link: https://github.com/hackingmaterials/automatminer

An experimental dataset of 1,557 inorganic compounds with measured formation enthalpies, curated from literature sources. Used as a *target dataset* to further test transfer learning on experimental thermodynamics data — its DeltaE values are predicted using fine-tuning or feature extraction from the MP source model, demonstrating generalization beyond DFT artifacts.

### [Kingsbury Experimental Bandgap (KEB)](../datasets/Kingsbury_Experimental_Bandgap_KEB.md)

- Usage page: [usage note](../dataset_uses/24_Structure_Aware_Transfer_Learning_Kingsbury_Experimental_Bandgap_KEB_dataset_use_91e22e.md)
- Original title in paper: Kingsbury Experimental Bandgap (KEB)
- Link: https://github.com/hackingmaterials/automatminer

An experimental dataset of 2,432 inorganic semiconductors and insulators with measured optical bandgaps. Serves as a *target dataset* for experimental electronic property prediction — the MP-pretrained ALIGNN model is transferred to predict experimental bandgaps, assessing robustness against measurement noise and methodology differences.
