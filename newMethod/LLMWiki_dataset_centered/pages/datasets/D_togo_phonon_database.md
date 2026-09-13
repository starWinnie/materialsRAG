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

- complex crystalline materials
- materials with >40 atoms per unit cell

## Observed research tasks

- phonon spectra and bandstructure prediction

## Observed research stages

- data_acquisition
- data_preparation
- model_evaluation
- computational_validation

## Observed properties

- phonon dispersion along highly symmetric paths
- Γ-phonon spectra

## Observed fields

- POSCAR
- FORCE_SET
- phonopy.config files
- phonon dispersion (cm⁻¹)

## Usage evidence

- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): source in acquisition of ab initio phonon data — Source of phonon dispersion data for complex materials with large unit cells
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): screening in phonon data preparation and splitting — Complex-material test set for evaluating generalizability on large-unit-cell systems
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): computational_validation in evaluation of phonon prediction accuracy — Validation set for assessing performance on complex materials beyond training domain
- P027 (Virtual Node Graph Neural Network for Full Phonon Prediction): computational_validation in validation on alloy systems and complex materials — Validation on alloy systems and high-entropy alloys using phonon data derived from Togo database or analogous DFPT/VCA methods

## Dataset evidence

- P027, PDF page 9, Methods: "We also got phonon dispersion of complex (more number of atoms per unit cell) materials from Atsushi Togo’s phonon database31."
- P027, PDF page 13, unknown: "Another set of data for testing the model was taken from the Phonon database by Dr. Atsuhi Togo at Kyoto University (“Togo Database” for short)?, which contains the phonons of more complex materials, but meanwhile contain more phonons with imaginary phonon energies."
- P027, PDF page 8, unknown: "http://phonondb.mtl.kyoto-u.ac.jp/"
