# Dataset: QCML

- Dataset ID: `D_qcml`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- QCML

## Observed material scopes

- molecules
- ionic systems
- metallic systems

## Observed research tasks

- molecular dynamics simulation using a neural network force field

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- candidate_screening

## Observed properties

- atomic forces
- total energy
- spin and charge states

## Observed fields

- 3D atomic positions
- atomic numbers
- spin and charge states
- pairwise distances and displacement vectors

## Usage evidence

- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): source in acquisition of QCML dataset — Acquisition of large-scale quantum chemistry reference dataset spanning the periodic table, including out-of-equilibrium structures and different spin and charge states.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): training in dataset splitting and augmentation — Partition QCML into train/validation/test splits while preserving conformational grouping, and apply random rotations and reflections to enable learning of approximate O(3)-equivariance.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): training in supervised pretraining of MD-ET on QCML — Supervised pretraining of MD-ET to predict atomic forces directly using mean absolute error loss.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): benchmark in benchmark evaluation on standard MD datasets — Benchmark evaluation of pretrained MD-ET's zero-shot and few-shot performance measuring force MAE.

## Dataset evidence

- P032, PDF page 3, We examine the effects of forgoing almost all commonly: "QCML ranges across the periodic table, including out-of-equilibrium structures and different spin and charge states, and includes properties for a subset of ∼30 × 10⁶ entries calculated with density functional theory accuracy at the PBE0 level46,47 (including dispersion corrections48,49)."
