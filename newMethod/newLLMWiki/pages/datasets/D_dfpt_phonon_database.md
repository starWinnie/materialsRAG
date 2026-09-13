# Dataset: DFPT phonon database

- Dataset ID: `D_dfpt_phonon_database`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- DFPT phonon database
- ab initio DFPT computational database
- DFPT database
- Main Database

## Observed material scopes

- crystalline inorganic materials

## Observed research tasks

- Full Phonon Prediction

## Observed research stages

- data_acquisition
- data_preparation
- model_evaluation

## Observed properties

- phonon dispersion along highly symmetric paths
- Γ-point phonon energies
- second-order derivatives of energies with respect to atomic perturbations

## Observed fields

- material structures (primitive structure from Materials Project)
- phonon dispersion
- second-order derivatives

## Usage evidence

- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): source in Phonon data acquisition from ab initio databases — Acquire high-quality phonon data for training and validation
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): training in Phonon data preparation and splitting — Train models on phonon dispersion along highly symmetric paths / Test models on phonon dispersion along highly symmetric paths
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): benchmark in Evaluating phonon prediction accuracy — Evaluate model performance on test set from same database as training

## Dataset evidence

- P027, PDF page 9, Methods: "We trained all of our models against an ab initio DFPT computational database for phonon dispersion in harmonic model25. The data set contains material structures (the same as the primitive structure obtained from the Material Project12), second-order derivatives of energies with respect to atomic perturbations for regular points inside the irreducible zone, and phonon dispersion along highly symmetric paths of 1,521 crystalline inorganic materials."
