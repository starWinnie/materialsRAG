# 41_Cross_Property_Transfer_Learning - JARVIS Database

## Dataset Use

A computational materials database comprising 28,171 unique compounds with up to 36 DFT-computed properties (as of July 2020), including band gap, exfoliation energy, dielectric constants, thermoelectric coefficients, elastic moduli, and Seebeck coefficients. After preprocessing (removing duplicates by retaining only the most stable structure per composition and excluding overlaps with OQMD), it serves as the target dataset for 39 distinct materials property prediction tasks, enabling evaluation of cross-property transfer learning performance.

## Links

- Paper: [41 Cross Property Transfer Learning](../papers/41_Cross_Property_Transfer_Learning.md)
- Task: [task page](../tasks/41_Cross_Property_Transfer_Learning_task_1.md)
- Dataset: [JARVIS Database](../datasets/JARVIS_Database.md)
- Dataset URL: https://jarvis.nist.gov

## Task Context

Predicting diverse materials properties (e.g., band gap, exfoliation energy, dielectric constants, thermoelectric coefficients) for compositions in small target datasets by leveraging knowledge transferred from deep learning models pre-trained on large source datasets of *different* — often unrelated — materials properties, using only elemental fractions as input.

## Metadata

- Dataset use ID: `dataset_use_4b96eaf50f0b`
- Original dataset title: Joint Automated Repository for Various Integrated Simulations (JARVIS)
- Tags: materials property prediction, cross-property transfer learning, small-data modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
