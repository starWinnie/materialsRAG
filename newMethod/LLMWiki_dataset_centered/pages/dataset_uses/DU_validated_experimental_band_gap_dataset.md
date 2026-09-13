# Dataset Use: Validated experimental band gap dataset

- DatasetUse ID: `DU_validated_experimental_band_gap_dataset`
- Dataset: Validated experimental band gap dataset (`D_validated_experimental_band_gap_dataset`)
- Papers: P037
- Usage records: 1

## Usage roles

- training

## Purposes

- training dataset for ML models predicting band gap

## Used fields

- chemical formula
- band gap

## Construction methods

- preprocessing and expert validation of Zhuo et al. band gap data

## Filter conditions

- excluded groups of duplicated formulas with std > 0.1 eV
- excluded noble gases and pure elements
- excluded entries outside 4 std from mean

## Sample counts

- 4767

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P037_02_validated_experimental_band_gap_dataset

- Paper: `P037` — Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials
- Task: accelerating the discovery of new transparent conducting materials (TCMs) (`T_P037_01`)
- Stage: preprocessing raw conductivity and band gap data (`data_preparation`, `S_P037_02`)
- Usage role: training
- Purpose: training dataset for ML models predicting band gap
- Used fields: chemical formula, band gap
- Filter conditions: excluded groups of duplicated formulas with std > 0.1 eV, excluded noble gases and pure elements, excluded entries outside 4 std from mean
- Construction method: preprocessing and expert validation of Zhuo et al. band gap data
- Sample count: 4767
- Confidence: 1.0

Evidence:
- P037, PDF page 4, Band gap dataset: "These preprocessing steps resulted in a final dataset comprising 4767 material entries, with a mean ̄x of 1.04 (eV), a median ~x of 0.00 (eV), and an interquartile range spanning from 0.00 to 1.93 eV."

## Aggregated evidence

- , PDF page 4, Band gap dataset: "These preprocessing steps resulted in a final dataset comprising 4767 material entries, with a mean ̄x of 1.04 (eV), a median ~x of 0.00 (eV), and an interquartile range spanning from 0.00 to 1.93 eV."
