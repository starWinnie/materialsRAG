# 25_ChargE3Net - GNoME materials dataset (subset)

## Dataset Use

A curated subset of 1,924 novel inorganic materials published by Google’s GNoME project, selected to include structures with ≥5 unique elemental species — intentionally out-of-distribution relative to the Materials Project training set. It contains DFT-computed charge densities generated using consistent VASP settings (k-point density, energy cutoff, PAW potentials). This dataset was used to test ChargE3Net’s generalization capability for charge density prediction on previously unseen chemical spaces — directly supporting the task of robust cross-dataset transfer for DFT acceleration beyond the training domain.

## Links

- Paper: [25 ChargE3Net](../papers/25_ChargE3Net_paper_a54c14466f4e.md)
- Task: [task page](../tasks/25_ChargE3Net_task_1_task_16fde01f7b15.md)
- Dataset: [GNoME materials dataset (subset)](../datasets/GNoME_materials_dataset_subset_dataset_c17327be4ec0.md)
- Dataset URL: https://doi.org/10.1038/s41586-023-06735-9

## Task Context

Predicting the 3D electron charge density distribution of atomic systems (molecules and crystalline materials) from atomic species identities and Cartesian coordinates, to serve as an accurate initialization for self-consistent density functional theory (DFT) calculations and enable non-self-consistent property prediction.

## Metadata

- Dataset use ID: `dataset_use_eb7d715612ea`
- Original dataset title: GNoME materials dataset (subset)
- Tags: charge density prediction, DFT initialization, electron density modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Candidate Space Construction
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
