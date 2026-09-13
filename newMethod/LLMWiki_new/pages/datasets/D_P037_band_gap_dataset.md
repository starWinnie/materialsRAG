# Dataset: band gap dataset

- Dataset ID: `D_P037_band_gap_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_zhuo_et_al_2018_experimental_band_gap_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- band gap dataset

## Observed material scopes

- transparent conducting materials (TCMs)
- oxides
- doped semiconductors
- metal oxides

## Observed research tasks

- accelerating the discovery of new transparent conducting materials (TCMs)

## Observed research stages

- data_preparation
- model_training
- model_evaluation

## Observed properties

- band gap

## Observed fields

- chemical formula
- band gap

## Usage evidence

- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): label_source in preprocessing and expert validation of experimental datasets — expert validation and expansion of the band gap dataset
- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): training in training state-of-the-art ML models on stoichiometry alone — training Random Forest and CrabNet models for band gap prediction
- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): validation in assessing model performance via K-fold, LOCO-CV, and leave-one-TCM-family-out — evaluation of trained models using K-fold, LOCO-CV, and leave-one-TCM-family-out schemes

## Dataset evidence

- P037, PDF page 4, 3.2 Band gap dataset: "The initial band gap data was sourced from a well-known experimental dataset proposed by ref. 22. The original dataset comprises 6354 material entries with experimental band gap measurements determined from optical and transport measurements."
- P037, PDF page 4, 3.2 Band gap dataset: "These preprocessing steps resulted in a final dataset comprising 4767 material entries..."
