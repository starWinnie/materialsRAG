# Dataset: Validated experimental band gap dataset

- Dataset ID: `D_validated_experimental_band_gap_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_zhuo_et_al_experimental_band_gap_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Validated experimental band gap dataset
- band gap dataset (4767 material entries)
- validated band gap dataset (4767 entries)

## Observed material scopes

- transparent conducting materials (TCMs)
- semiconductors

## Observed research tasks

- accelerating the discovery of new transparent conducting materials (TCMs)

## Observed research stages

- data_preparation

## Observed properties

- band gap

## Observed fields

- chemical formula
- band gap

## Usage evidence

- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): training in preprocessing raw conductivity and band gap data — training dataset for ML models predicting band gap

## Dataset evidence

- P037, PDF page 3, Introduction: "To enable a ML approach, we have created and validated two experimental datasets of room-temperature conductivity and band gap measurements, to be used as foundation for training SOTA ML models for the discovery of new TCMs."
- P037, PDF page 4, Band gap dataset: "Preprocessing steps were applied to the raw data. Specifically, we excluded groups of duplicated formulas with band gap measurements having a standard deviation greater than 0.1 eV."
- P037, PDF page 4, Band gap dataset: "These preprocessing steps resulted in a final dataset comprising 4767 material entries, with a mean ̄x of 1.04 (eV), a median ~x of 0.00 (eV), and an interquartile range spanning from 0.00 to 1.93 eV."
