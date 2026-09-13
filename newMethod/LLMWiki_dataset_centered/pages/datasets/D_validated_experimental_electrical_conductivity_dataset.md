# Dataset: Validated experimental electrical conductivity dataset

- Dataset ID: `D_validated_experimental_electrical_conductivity_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_mpds_electrical_conductivity_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Validated experimental electrical conductivity dataset
- electrical conductivity dataset (8231 material entries)
- validated conductivity dataset (8231 entries)

## Observed material scopes

- transparent conducting materials (TCMs)
- semiconductors

## Observed research tasks

- accelerating the discovery of new transparent conducting materials (TCMs)

## Observed research stages

- data_preparation

## Observed properties

- electrical conductivity

## Observed fields

- chemical formula
- conductivity
- temperature

## Usage evidence

- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): training in preprocessing raw conductivity and band gap data — training dataset for ML models predicting electrical conductivity

## Dataset evidence

- P037, PDF page 3, Introduction: "To enable a ML approach, we have created and validated two experimental datasets of room-temperature conductivity and band gap measurements, to be used as foundation for training SOTA ML models for the discovery of new TCMs."
- P037, PDF page 3, Electrical conductivity dataset: "At this stage, we performed a meticulous validation, which involved a line-by-line review of the obtained data by domain experts, referring back to the original literature on suspicious entries, to ensure the accuracy of the reported conductivity measurements, alongside the correctness of the corresponding chemical formulas."
- P037, PDF page 3, Electrical conductivity dataset: "We end up with a final, validated database comprising 8231 material entries, with a mean ̄x of 1.09 (log10 (S cm−1)), a median ~x of 2.44 (log10 (S cm−1)) and an interquartile range (50% of data; materials from the 25th to the 75th percentile of log10(s)) spanning from −0.18 to 3.60 (log10 (S cm−1))."
