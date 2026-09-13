# 41_Cross_Property_Transfer_Learning - Experimental formation energy dataset

## Dataset Use

An experimental dataset of 1,643 material entries containing measured formation energies (in eV/atom), sourced from the qmpy thermodata repository. It is used as a real-world small-target dataset to evaluate cross-property transfer learning performance, specifically testing whether models pre-trained on computational formation energy (OQMD) can improve prediction accuracy on experimental formation energy data — a key demonstration of generalizability beyond computational domains.

## Links

- Paper: [41 Cross Property Transfer Learning](../papers/41_Cross_Property_Transfer_Learning.md)
- Task: [task page](../tasks/41_Cross_Property_Transfer_Learning_task_1.md)
- Dataset: [Experimental formation energy dataset](../datasets/Experimental_formation_energy_dataset.md)
- Dataset URL: https://github.com/wolverton-research-group/qmpy/blob/master/qmpy/data/thermodata/ssub.dat

## Task Context

Predicting diverse materials properties (e.g., band gap, exfoliation energy, dielectric constants, thermoelectric coefficients) for compositions in small target datasets by leveraging knowledge transferred from deep learning models pre-trained on large source datasets of *different* — often unrelated — materials properties, using only elemental fractions as input.

## Metadata

- Dataset use ID: `dataset_use_1213283c0071`
- Original dataset title: Experimental formation energy dataset
- Tags: materials property prediction, cross-property transfer learning, small-data modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
