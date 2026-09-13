# Dataset: DFPT phonon database for semiconducting inorganic materials

- Dataset ID: `D_dfpt_phonon_database_for_semiconducting_inorganic_materials`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- DFPT phonon database for semiconducting inorganic materials
- ab initio DFPT computational database for phonon dispersion in harmonic model
- Main Database
- DFPT database
- density functional perturbation theory (DFPT) phonon database

## Observed material scopes

- semiconducting inorganic materials
- crystalline materials

## Observed research tasks

- phonon spectra and bandstructure prediction

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation

## Observed properties

- phonon dispersion along highly symmetric paths
- second-order derivatives of energies with respect to atomic perturbations
- Γ-phonon spectra

## Observed fields

- material structures (primitive structure from Materials Project)
- phonon dispersion (cm⁻¹)
- wave vectors (fractional reciprocal unit)

## Usage evidence

- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): source in acquisition of ab initio phonon data — Source of high-quality ab initio phonon dispersion data for training and validation
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): training in phonon data preparation and splitting — Training set for VGNN models (VVN, MVN, k-MVN) / Test set for VGNN models (VVN, MVN, k-MVN)
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): training in training of VGNN models (VVN, MVN, k-MVN) — Training data for optimizing neural network parameters via MSE loss minimization
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): test in evaluation of phonon prediction accuracy — Test set for evaluating prediction accuracy via loss distribution and correlation plots

## Dataset evidence

- P027, PDF page 9, Methods: "We trained all of our models against an ab initio DFPT computational database for phonon dispersion in harmonic model25."
- P027, PDF page 9, Methods: "The data set contains material structures (the same as the primitive structure obtained from the Material Project12), second-order derivatives of energies with respect to atomic perturbations for regular points inside the irreducible zone, and phonon dispersion along highly symmetric paths of 1,521 crystalline inorganic materials."
- P027, PDF page 12, I DATA PREPARATION: "The data set containing full phonon bands of 1521 semiconducting inorganic materials are calculated from density functional perturbation theory (DFPT)?, which is the main dataset for training (“Main Database” for short)."
