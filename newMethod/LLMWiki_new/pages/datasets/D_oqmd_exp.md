# Dataset: OQMD-EXP

- Dataset ID: `D_oqmd_exp`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- OQMD-EXP
- OQMD-EXP dataset

## Observed material scopes

- crystalline materials
- crystal structures

## Observed research tasks

- crystal property prediction

## Observed research stages

- model_evaluation

## Observed properties

- formation energy

## Observed fields

- experimental formation energy
- formation energy

## Usage evidence

- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): test in evaluating downstream property prediction performance — evaluating downstream property prediction performance using experimental data
- P057 (Latent Diffusion Pretraining for Crystal Property Prediction): experimental_validation in downstream property prediction evaluation — evaluate CrysLDNet’s ability to mitigate DFT error bias using experimental data

## Dataset evidence

- P023, PDF page 6, Experimental Settings: "to investigate how our model helps to mitigate the DFT error, we also take a small dataset OQMD-EXP (Kirklin et al. 2015), containing 1,500 available experimental data of formation energy."
- P114, PDF page 5, 4.1. Datasets for Pretraining and Downstream Tasks: "Finally, to evaluate CrysLDNet’s ability to mitigate DFT error bias using experimental data (Section 4.6), we use the OQMD-EXP dataset (Kirklin et al., 2015), which contains ∼1,500 crystal materials with experimentally measured formation energies."
