# Dataset Use: Validated experimental electrical conductivity dataset

- DatasetUse ID: `DU_validated_experimental_electrical_conductivity_dataset`
- Dataset: Validated experimental electrical conductivity dataset (`D_validated_experimental_electrical_conductivity_dataset`)
- Papers: P037
- Usage records: 1

## Usage roles

- training

## Purposes

- training dataset for ML models predicting electrical conductivity

## Used fields

- chemical formula
- conductivity

## Construction methods

- preprocessing and expert validation of MPDS and UCSB conductivity data

## Filter conditions

- excluded pure elements and noble gases
- selected only room temperature (298 ± 5 K)
- discarded duplicated formulas with std > 10 S cm−1
- excluded entries outside 4 std from mean

## Sample counts

- 8231

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P037_02_validated_experimental_electrical_conductivity_dataset

- Paper: `P037` — Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials
- Task: accelerating the discovery of new transparent conducting materials (TCMs) (`T_P037_01`)
- Stage: preprocessing raw conductivity and band gap data (`data_preparation`, `S_P037_02`)
- Usage role: training
- Purpose: training dataset for ML models predicting electrical conductivity
- Used fields: chemical formula, conductivity
- Filter conditions: excluded pure elements and noble gases, selected only room temperature (298 ± 5 K), discarded duplicated formulas with std > 10 S cm−1, excluded entries outside 4 std from mean
- Construction method: preprocessing and expert validation of MPDS and UCSB conductivity data
- Sample count: 8231
- Confidence: 1.0

Evidence:
- P037, PDF page 3, Electrical conductivity dataset: "We end up with a final, validated database comprising 8231 material entries, with a mean ̄x of 1.09 (log10 (S cm−1)), a median ~x of 2.44 (log10 (S cm−1)) and an interquartile range (50% of data; materials from the 25th to the 75th percentile of log10(s)) spanning from −0.18 to 3.60 (log10 (S cm−1))."

## Aggregated evidence

- , PDF page 3, Electrical conductivity dataset: "We end up with a final, validated database comprising 8231 material entries, with a mean ̄x of 1.09 (log10 (S cm−1)), a median ~x of 2.44 (log10 (S cm−1)) and an interquartile range (50% of data; materials from the 25th to the 75th percentile of log10(s)) spanning from −0.18 to 3.60 (log10 (S cm−1))."
