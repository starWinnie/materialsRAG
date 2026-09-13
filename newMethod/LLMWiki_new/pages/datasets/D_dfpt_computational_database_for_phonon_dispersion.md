# Dataset: DFPT computational database for phonon dispersion

- Dataset ID: `D_dfpt_computational_database_for_phonon_dispersion`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- DFPT computational database for phonon dispersion
- ab initio DFPT computational database for phonon dispersion in harmonic model
- DFPT database
- Main Database
- data set containing full phonon bands of 1521 semiconducting inorganic materials
- density functional perturbation theory (DFPT)

## Observed material scopes

- crystalline inorganic materials
- semiconducting inorganic materials

## Observed research tasks

- phonon spectra and bandstructure prediction

## Observed research stages

- data_acquisition
- data_preparation
- model_evaluation

## Observed properties

- phonon dispersion along highly symmetric paths
- second-order derivatives of energies with respect to atomic perturbations
- Γ-point phonon energies
- high-symmetry k-point phonon energies

## Observed fields

- material structures (primitive structure from Materials Project)
- phonon dispersion
- second-order energy derivatives

## Usage evidence

- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): source in acquisition of ab initio phonon data — acquisition of ab initio phonon dispersion data via DFPT calculations
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): training in preprocessing of crystal structures and phonon data — training data for phonon prediction models / testing data for phonon prediction models
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): test in evaluation of phonon prediction accuracy — evaluation of test accuracy through loss distribution and correlation plots

## Dataset evidence

- P027, PDF page 9, Methods: "We trained all of our models against an ab initio DFPT computational database for phonon dispersion in harmonic model25."
- P027, PDF page 9, Methods: "The data set contains material structures (the same as the primitive structure obtained from the Material Project12), second-order derivatives of energies with respect to atomic perturbations for regular points inside the irreducible zone, and phonon dispersion along highly symmetric paths of 1,521 crystalline inorganic materials."
- P027, PDF page 12, I DATA PREPARATION: "The data set containing full phonon bands of 1521 semiconducting inorganic materials are calculated from density functional perturbation theory (DFPT)?, which is the main dataset for training (“Main Database” for short)."
