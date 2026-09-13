# 25_ChargE3Net - QM9 charge density dataset

## Dataset Use

A dataset of VASP-calculated electron charge densities for 133,845 small organic molecules (with training/validation/test splits of 123,835/50/10,000), derived from the original QM9 molecular database. It contains grid-based charge density values computed at consistent resolution and boundary conditions, and was used to benchmark ChargE3Net’s accuracy on small, isolated molecules — supporting the core task of learning equivariant representations for charge density prediction under molecular symmetry constraints.

## Links

- Paper: [25 ChargE3Net](../papers/25_ChargE3Net_paper_a54c14466f4e.md)
- Task: [task page](../tasks/25_ChargE3Net_task_1_task_16fde01f7b15.md)
- Dataset: [QM9 charge density dataset](../datasets/QM9_charge_density_dataset_dataset_f281b31ea1d7.md)
- Dataset URL: https://doi.org/10.11583/DTU.16794500.v1

## Task Context

Predicting the 3D electron charge density distribution of atomic systems (molecules and crystalline materials) from atomic species identities and Cartesian coordinates, to serve as an accurate initialization for self-consistent density functional theory (DFT) calculations and enable non-self-consistent property prediction.

## Metadata

- Dataset use ID: `dataset_use_91e9b63fe83d`
- Original dataset title: QM9 charge density dataset
- Tags: charge density prediction, DFT initialization, electron density modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
