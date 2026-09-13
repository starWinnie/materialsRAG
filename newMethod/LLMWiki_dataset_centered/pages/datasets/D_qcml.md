# Dataset: QCML

- Dataset ID: `D_qcml`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- QCML
- QCML database

## Observed material scopes

- molecules
- ionic systems
- metallic systems

## Observed research tasks

- molecular dynamics simulation using machine learning force fields

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation

## Observed properties

- atomic forces
- energy
- spin and charge states

## Observed fields

- 3D atomic positions
- atomic numbers
- spin and charge states
- pairwise distances and displacement vectors

## Usage evidence

- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): source in acquisition of QCML dataset — Acquisition of a large-scale quantum chemistry reference dataset spanning the periodic table, including out-of-equilibrium structures and different spin and charge states.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): training in data splitting and augmentation — Create train/validation/test splits ensuring conformational integrity and apply random rotations and reflections to learn approximate O(3)-equivariance.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): training in supervised pretraining on QCML — Supervised pretraining on the QCML dataset to predict atomic forces directly.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): test in benchmark evaluation on force prediction accuracy — Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the QCML evaluation set.

## Dataset evidence

- P032, PDF page 3, We examine the effects of forgoing almost all commonly: "We modify an edge transformer (ET)43,44 with MD-specific embedding layers and train on the new QCML database.45 QCML ranges across the periodic table, including out-of-equilibrium structures and different spin and charge states, and includes properties for a subset of ∼30 × 106 entries calculated with density functional theory accuracy at the PBE0 level46,47 (including dispersion corrections48,49)."
- P032, PDF page 5, Pretraining performance: "We create an approximate 90%/5%/5% split from QCML. As QCML contains multiple conformations for each structure sampled along its normal modes, we ensure that all conformations of a structure are assigned to the same split."
- P032, PDF page 5, Pretraining performance: "We perform supervised pretraining on the new QCML dataset.45"
- P032, PDF page 5, Pretraining performance: "In Table I, we present the mean absolute error (MAE) of force predictions for MD-ET, SpookyNet,70 and PaiNN21 on the QCML evaluation set at the end of pretraining."
