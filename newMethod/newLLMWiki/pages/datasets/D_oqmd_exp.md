# Dataset: OQMD-EXP

- Dataset ID: `D_oqmd_exp`
- Dataset type: `public_subset`
- Source dataset: `D_oqmd`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- OQMD-EXP

## Observed material scopes

- crystalline materials

## Observed research tasks

- crystal property prediction

## Observed research stages

- data_acquisition
- model_evaluation

## Observed properties

- formation energy

## Observed fields

- crystal structure (A, F, L)
- experimental formation energy values

## Usage evidence

- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): training in collecting labeled crystal property data — fine-tuning for crystal property prediction to mitigate DFT error using experimental formation energy data
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): test in downstream task evaluation — downstream task evaluation on formation energy using MAE

## Dataset evidence

- P023, PDF page 6, Experimental Settings: "Therefore, to investigate how our model helps to mitigate the DFT error, we also take a small dataset OQMD-EXP (Kirklin et al. 2015), containing 1,500 available experimental data of formation energy."
