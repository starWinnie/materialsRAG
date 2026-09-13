# Dataset: Togo phonon database

- Dataset ID: `D_togo_phonon_database`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Togo phonon database
- Atsushi Togo’s phonon database
- Phonon database by Dr. Atsuhi Togo at Kyoto University
- Togo Database

## Observed material scopes

- crystalline inorganic materials
- complex materials

## Observed research tasks

- Full Phonon Prediction

## Observed research stages

- data_acquisition
- data_preparation
- model_evaluation

## Observed properties

- phonon dispersion

## Observed fields

- POSCAR
- FORCE_SET
- phonopy.config files

## Usage evidence

- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): source in Phonon data acquisition from ab initio databases — Acquire phonon dispersion of complex materials
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): candidate_pool in Phonon data preparation and splitting — Select complex materials for additional test set
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): benchmark in Evaluating phonon prediction accuracy — Evaluate model performance on test set of complex materials

## Dataset evidence

- P027, PDF page 9, Methods: "We also got phonon dispersion of complex (more number of atoms per unit cell) materials from Atsushi Togo’s phonon database31."
- P027, PDF page 13, I DATA PREPARATION: "Another set of data for testing the model was taken from the Phonon database by Dr. Atsuhi Togo at Kyoto University (“Togo Database” for short)?, which contains the phonons of more complex materials, but meanwhile contain more phonons with imaginary phonon energies."
