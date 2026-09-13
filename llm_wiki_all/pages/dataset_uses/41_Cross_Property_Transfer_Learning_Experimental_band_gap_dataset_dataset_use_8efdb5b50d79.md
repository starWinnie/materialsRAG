# 41_Cross_Property_Transfer_Learning - Experimental band gap dataset

## Dataset Use

An experimental dataset of 4,920 material entries containing measured band gap values (in eV), sourced from the AutoMatminer repository. It serves as a second experimental small-target dataset to validate the cross-property transfer learning framework, assessing whether source models trained on computational formation energy or band gap can enhance prediction of experimentally measured band gaps — particularly challenging due to known DFT band gap underestimation.

## Links

- Paper: [41 Cross Property Transfer Learning](../papers/41_Cross_Property_Transfer_Learning.md)
- Task: [task page](../tasks/41_Cross_Property_Transfer_Learning_task_1.md)
- Dataset: [Experimental band gap dataset](../datasets/Experimental_band_gap_dataset.md)
- Dataset URL: https://github.com/hackingmaterials/automatminer

## Task Context

Predicting diverse materials properties (e.g., band gap, exfoliation energy, dielectric constants, thermoelectric coefficients) for compositions in small target datasets by leveraging knowledge transferred from deep learning models pre-trained on large source datasets of *different* — often unrelated — materials properties, using only elemental fractions as input.

## Metadata

- Dataset use ID: `dataset_use_8efdb5b50d79`
- Original dataset title: Experimental band gap dataset
- Tags: materials property prediction, cross-property transfer learning, small-data modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
