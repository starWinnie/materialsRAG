# 32_Perovskite_Bandgap_Database - Task 1

## Task Description

Predicting the bandgaps of mixed ABX3 perovskites (where A = Cs, FA, or MA; B = Pb or Sn; X = Br, Cl, or I) with continuously varying compositions to enable thermodynamic modeling and prediction of light-induced halide segregation behavior under illumination.

## Metadata

- Task ID: `task_c76fa5389271`
- Source paper: [32 Perovskite Bandgap Database](../papers/32_Perovskite_Bandgap_Database.md)
- Tags: bandgap prediction, halide segregation prediction, perovskite property modeling

## Supporting Datasets

### [Perovskite Solar Cell (PSC) Database](../datasets/Perovskite_Solar_Cell_PSC_Database.md)

- Usage page: [usage note](../dataset_uses/32_Perovskite_Bandgap_Database_Perovskite_Solar_Cell_PSC_Database_dataset_use_6dd03c0b02af.md)
- Original title in paper: Perovskite Solar Cell (PSC) Database
- Link: https://doi.org/10.1038/s41560-022-01002-7

A publicly available experimental database established by Jacobsson et al., containing experimentally measured bandgap values for various perovskite solar cell materials. In this paper, it contributed to the experimental bandgap dataset (645 total entries after curation), used to fine-tune machine learning models and validate predictions of mixed-halide perovskite bandgaps.

### [Liu et al. experimental bandgap dataset](../datasets/Liu_et_al._experimental_bandgap_dataset.md)

- Usage page: [usage note](../dataset_uses/32_Perovskite_Bandgap_Database_Liu_et_al._experimental_bandgap_dataset_dataset_use_1239455.md)
- Original title in paper: Liu et al. experimental bandgap dataset
- Link: https://doi.org/10.1016/j.orgel.2022.106426

A curated collection of 227 experimentally reported bandgap values for ABX3 perovskites, sourced from literature and used in this work to augment the experimental training set. After deduplication and averaging of repeated compositions, it formed part of the 645-entry experimental bandgap dataset used to train and evaluate the Atomsets-MLP model for accurate bandgap prediction.

### [Yang et al. experimental bandgap dataset](../datasets/Yang_et_al._experimental_bandgap_dataset.md)

- Usage page: [usage note](../dataset_uses/32_Perovskite_Bandgap_Database_Yang_et_al._experimental_bandgap_dataset_dataset_use_6f9015.md)
- Original title in paper: Yang et al. experimental bandgap dataset
- Link: https://doi.org/10.1021/acsami.3c04027

A set of 610 experimentally measured bandgaps for hybrid perovskites, collected from published studies and integrated into the authors’ unified experimental bandgap dataset (645 entries after filtering). It provided compositional diversity and experimental ground truth for transfer learning and model validation targeting bandgap prediction of mixed-cation/mixed-anion perovskites.

### [DFT-calculated bandgap dataset (PBE functional)](../datasets/DFT-calculated_bandgap_dataset_PBE_functional.md)

- Usage page: [usage note](../dataset_uses/32_Perovskite_Bandgap_Database_DFT-calculated_bandgap_dataset_PBE_functional_dataset_use_8.md)
- Original title in paper: DFT-calculated bandgap dataset (PBE functional)
- Link: None

A custom computational dataset comprising 108 DFT-calculated bandgaps for mixed halide perovskites (e.g., FAPb(I1-xBrx)3, MAPb(I1-xBrx)3, CsPb(I1-xBrx)3, and multi-cation variants), generated using VASP with the PBE functional and structural models built via Pymatgen. This dataset was combined with experimental data to train transfer-learned models (e.g., Fine-Tuned MEGNet, Atomsets-MLP) to bridge accuracy gaps between DFT and experiment.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/32_Perovskite_Bandgap_Database_Materials_Project_dataset_use_8be26692e10f.md)
- Original title in paper: Materials Project database
- Link: https://materialsproject.org

A public repository of computed materials properties, including ~69,640 DFT (PBE)-calculated bandgaps for crystals, used to pre-train foundational models (MEGNet, MatGL) before fine-tuning on perovskite-specific data. In this paper, it served as the source of pre-trained weights for transfer learning, enabling improved generalization for perovskite bandgap prediction despite domain shift.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->
