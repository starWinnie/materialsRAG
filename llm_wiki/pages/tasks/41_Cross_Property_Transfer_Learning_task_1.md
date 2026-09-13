# 41_Cross_Property_Transfer_Learning - Task 1

## Task Description

Predicting diverse materials properties (e.g., band gap, exfoliation energy, dielectric constants, thermoelectric coefficients) for compositions in small target datasets by leveraging knowledge transferred from deep learning models pre-trained on large source datasets of *different* — often unrelated — materials properties, using only elemental fractions as input.

## Metadata

- Task ID: `task_d690dacb05c5`
- Source paper: [41 Cross Property Transfer Learning](../papers/41_Cross_Property_Transfer_Learning.md)
- Tags: materials property prediction, cross-property transfer learning, small-data modeling

## Supporting Datasets

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/41_Cross_Property_Transfer_Learning_Open_Quantum_Materials_Database_dataset_use_9f2ed8de4e.md)
- Original title in paper: Open Quantum Materials Database (OQMD)
- Link: http://oqmd.org

A computational materials database containing 341,443 unique compositions with DFT-calculated properties including formation energy, bandgap, stability, energy per atom, volume, and magnetic moment (as of May 2018). It is used to construct the source dataset (OQMD-JARVIS, size 321,140 after deduplication and overlap removal) for pre-training ElemNet-based source models; these models serve as the foundation for cross-property transfer learning to predict target properties on smaller datasets.

### [JARVIS Database](../datasets/JARVIS_Database.md)

- Usage page: [usage note](../dataset_uses/41_Cross_Property_Transfer_Learning_JARVIS_Database_dataset_use_4b96eaf50f0b.md)
- Original title in paper: Joint Automated Repository for Various Integrated Simulations (JARVIS)
- Link: https://jarvis.nist.gov

A computational materials database comprising 28,171 unique compounds with up to 36 DFT-computed properties (as of July 2020), including band gap, exfoliation energy, dielectric constants, thermoelectric coefficients, elastic moduli, and Seebeck coefficients. After preprocessing (removing duplicates by retaining only the most stable structure per composition and excluding overlaps with OQMD), it serves as the target dataset for 39 distinct materials property prediction tasks, enabling evaluation of cross-property transfer learning performance.

### [Experimental formation energy dataset](../datasets/Experimental_formation_energy_dataset.md)

- Usage page: [usage note](../dataset_uses/41_Cross_Property_Transfer_Learning_Experimental_formation_energy_dataset_dataset_use_1213.md)
- Original title in paper: Experimental formation energy dataset
- Link: https://github.com/wolverton-research-group/qmpy/blob/master/qmpy/data/thermodata/ssub.dat

An experimental dataset of 1,643 material entries containing measured formation energies (in eV/atom), sourced from the qmpy thermodata repository. It is used as a real-world small-target dataset to evaluate cross-property transfer learning performance, specifically testing whether models pre-trained on computational formation energy (OQMD) can improve prediction accuracy on experimental formation energy data — a key demonstration of generalizability beyond computational domains.

### [Experimental band gap dataset](../datasets/Experimental_band_gap_dataset.md)

- Usage page: [usage note](../dataset_uses/41_Cross_Property_Transfer_Learning_Experimental_band_gap_dataset_dataset_use_8efdb5b50d79.md)
- Original title in paper: Experimental band gap dataset
- Link: https://github.com/hackingmaterials/automatminer

An experimental dataset of 4,920 material entries containing measured band gap values (in eV), sourced from the AutoMatminer repository. It serves as a second experimental small-target dataset to validate the cross-property transfer learning framework, assessing whether source models trained on computational formation energy or band gap can enhance prediction of experimentally measured band gaps — particularly challenging due to known DFT band gap underestimation.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
