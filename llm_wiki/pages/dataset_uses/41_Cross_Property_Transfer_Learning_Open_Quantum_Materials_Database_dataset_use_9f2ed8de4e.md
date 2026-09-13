# 41_Cross_Property_Transfer_Learning - Open Quantum Materials Database

## Dataset Use

A computational materials database containing 341,443 unique compositions with DFT-calculated properties including formation energy, bandgap, stability, energy per atom, volume, and magnetic moment (as of May 2018). It is used to construct the source dataset (OQMD-JARVIS, size 321,140 after deduplication and overlap removal) for pre-training ElemNet-based source models; these models serve as the foundation for cross-property transfer learning to predict target properties on smaller datasets.

## Links

- Paper: [41 Cross Property Transfer Learning](../papers/41_Cross_Property_Transfer_Learning.md)
- Task: [task page](../tasks/41_Cross_Property_Transfer_Learning_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: http://oqmd.org

## Task Context

Predicting diverse materials properties (e.g., band gap, exfoliation energy, dielectric constants, thermoelectric coefficients) for compositions in small target datasets by leveraging knowledge transferred from deep learning models pre-trained on large source datasets of *different* — often unrelated — materials properties, using only elemental fractions as input.

## Metadata

- Dataset use ID: `dataset_use_9f2ed8de4eab`
- Original dataset title: Open Quantum Materials Database (OQMD)
- Tags: materials property prediction, cross-property transfer learning, small-data modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
