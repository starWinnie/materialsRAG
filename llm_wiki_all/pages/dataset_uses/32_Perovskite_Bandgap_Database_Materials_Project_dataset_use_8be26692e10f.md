# 32_Perovskite_Bandgap_Database - Materials Project

## Dataset Use

A public repository of computed materials properties, including ~69,640 DFT (PBE)-calculated bandgaps for crystals, used to pre-train foundational models (MEGNet, MatGL) before fine-tuning on perovskite-specific data. In this paper, it served as the source of pre-trained weights for transfer learning, enabling improved generalization for perovskite bandgap prediction despite domain shift.

## Links

- Paper: [32 Perovskite Bandgap Database](../papers/32_Perovskite_Bandgap_Database.md)
- Task: [task page](../tasks/32_Perovskite_Bandgap_Database_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the bandgaps of mixed ABX3 perovskites (where A = Cs, FA, or MA; B = Pb or Sn; X = Br, Cl, or I) with continuously varying compositions to enable thermodynamic modeling and prediction of light-induced halide segregation behavior under illumination.

## Metadata

- Dataset use ID: `dataset_use_8be26692e10f`
- Original dataset title: Materials Project database
- Tags: bandgap prediction, halide segregation prediction, perovskite property modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
