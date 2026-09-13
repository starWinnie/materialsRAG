# Dataset: electrical conductivity dataset

- Dataset ID: `D_P037_electrical_conductivity_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_mpds_and_ucsb_datasets`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- electrical conductivity dataset

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

- electrical conductivity

## Observed fields

- chemical formula
- conductivity
- temperature

## Usage evidence

- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): label_source in preprocessing and expert validation of experimental datasets — expert validation and nonsense-detection strategies applied to the electrical conductivity dataset
- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): training in training state-of-the-art ML models on stoichiometry alone — training Random Forest and CrabNet models for electrical conductivity prediction
- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): validation in assessing model performance via K-fold, LOCO-CV, and leave-one-TCM-family-out — evaluation of trained models using K-fold, LOCO-CV, and leave-one-TCM-family-out schemes

## Dataset evidence

- P037, PDF page 3, 3.1 Electrical conductivity dataset: "The electrical conductivity dataset was constructed using two primary data sources. Initially, data on conductivity and resistivity, along with associated chemical formulas, were gathered from the Materials Platform for Data Science (MPDS),4 with 38 068 entries available as of December 2024. This source was supplemented with the UCSB dataset21 (1794 entries)..."
- P037, PDF page 3, 3.1 Electrical conductivity dataset: "We end up with a final, validated database comprising 8231 material entries..."
