# Dataset Use: OQMD-EXP

- DatasetUse ID: `DU_oqmd_exp`
- Dataset: OQMD-EXP (`D_oqmd_exp`)
- Papers: P023
- Usage records: 1

## Usage roles

- training

## Purposes

- mitigating DFT error by fine-tuning with experimental formation energy data

## Used fields

- crystal structure (A, F, L)
- experimental formation energy values

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 1500

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P023_02_oqmd_exp

- Paper: `P023` — A Diffusion-Based Pre-training Framework for Crystal Property Prediction
- Task: crystal property prediction (`T_P023_01`)
- Stage: collecting labeled crystal property data for fine-tuning and evaluation (`data_acquisition`, `S_P023_02`)
- Usage role: training
- Purpose: mitigating DFT error by fine-tuning with experimental formation energy data
- Used fields: crystal structure (A, F, L), experimental formation energy values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 1500
- Confidence: 1.0

Evidence:
- P023, PDF page 6, Experimental Settings: "Therefore, to investigate how our model helps to mitigate the DFT error, we also take a small dataset OQMD-EXP (Kirklin et al. 2015), containing 1,500 available experimental data of formation energy."

## Aggregated evidence

- , PDF page 6, Experimental Settings: "Therefore, to investigate how our model helps to mitigate the DFT error, we also take a small dataset OQMD-EXP (Kirklin et al. 2015), containing 1,500 available experimental data of formation energy."
