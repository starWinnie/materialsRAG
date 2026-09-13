# Dataset Use: QCML

- DatasetUse ID: `DU_qcml`
- Dataset: QCML (`D_qcml`)
- Papers: P032
- Usage records: 4

## Usage roles

- source
- training
- test

## Purposes

- Acquisition of a large-scale quantum chemistry reference dataset spanning the periodic table, including out-of-equilibrium structures and different spin and charge states.
- Create train/validation/test splits ensuring conformational integrity and apply random rotations and reflections to learn approximate O(3)-equivariance.
- Supervised pretraining on the QCML dataset to predict atomic forces directly.
- Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the QCML evaluation set.

## Used fields

- 3D atomic positions
- atomic numbers
- spin and charge states
- pairwise distances and displacement vectors
- atomic forces

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- None stated

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P032_01_qcml

- Paper: `P032` — How simple can you go? An off-the-shelf transformer approach to molecular dynamics
- Task: molecular dynamics simulation using machine learning force fields (`T_P032_01`)
- Stage: acquisition of QCML dataset (`data_acquisition`, `S_P032_01`)
- Usage role: source
- Purpose: Acquisition of a large-scale quantum chemistry reference dataset spanning the periodic table, including out-of-equilibrium structures and different spin and charge states.
- Used fields: 3D atomic positions, atomic numbers, spin and charge states, pairwise distances and displacement vectors
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P032, PDF page 3, We examine the effects of forgoing almost all commonly: "We modify an edge transformer (ET)43,44 with MD-specific embedding layers and train on the new QCML database.45 QCML ranges across the periodic table, including out-of-equilibrium structures and different spin and charge states, and includes properties for a subset of ∼30 × 106 entries calculated with density functional theory accuracy at the PBE0 level46,47 (including dispersion corrections48,49)."

### UR_P032_02_qcml

- Paper: `P032` — How simple can you go? An off-the-shelf transformer approach to molecular dynamics
- Task: molecular dynamics simulation using machine learning force fields (`T_P032_01`)
- Stage: data splitting and augmentation (`data_preparation`, `S_P032_02`)
- Usage role: training
- Purpose: Create train/validation/test splits ensuring conformational integrity and apply random rotations and reflections to learn approximate O(3)-equivariance.
- Used fields: 3D atomic positions, atomic numbers, spin and charge states
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P032, PDF page 5, Pretraining performance: "We create an approximate 90%/5%/5% split from QCML. As QCML contains multiple conformations for each structure sampled along its normal modes, we ensure that all conformations of a structure are assigned to the same split. To learn approximate equivariance, we use data augmentation: during pretraining, we duplicate each batch once and apply random rotations and reflections to both copies to form an augmented batch."

### UR_P032_03_qcml

- Paper: `P032` — How simple can you go? An off-the-shelf transformer approach to molecular dynamics
- Task: molecular dynamics simulation using machine learning force fields (`T_P032_01`)
- Stage: supervised pretraining on QCML (`model_training`, `S_P032_03`)
- Usage role: training
- Purpose: Supervised pretraining on the QCML dataset to predict atomic forces directly.
- Used fields: atomic forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P032, PDF page 3, We examine the effects of forgoing almost all commonly: "Instead of predicting a combined loss50 of energies and forces or calculating forces as the negative gradient of the predicted energy with respect to positions, we predict forces directly."
- P032, PDF page 5, Pretraining performance: "We perform supervised pretraining on the new QCML dataset.45"

### UR_P032_05_qcml

- Paper: `P032` — How simple can you go? An off-the-shelf transformer approach to molecular dynamics
- Task: molecular dynamics simulation using machine learning force fields (`T_P032_01`)
- Stage: benchmark evaluation on force prediction accuracy (`model_evaluation`, `S_P032_05`)
- Usage role: test
- Purpose: Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the QCML evaluation set.
- Used fields: atomic forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P032, PDF page 5, Pretraining performance: "In Table I, we present the mean absolute error (MAE) of force predictions for MD-ET, SpookyNet,70 and PaiNN21 on the QCML evaluation set at the end of pretraining."

## Aggregated evidence

- , PDF page 3, We examine the effects of forgoing almost all commonly: "We modify an edge transformer (ET)43,44 with MD-specific embedding layers and train on the new QCML database.45 QCML ranges across the periodic table, including out-of-equilibrium structures and different spin and charge states, and includes properties for a subset of ∼30 × 106 entries calculated with density functional theory accuracy at the PBE0 level46,47 (including dispersion corrections48,49)."
- , PDF page 5, Pretraining performance: "We create an approximate 90%/5%/5% split from QCML. As QCML contains multiple conformations for each structure sampled along its normal modes, we ensure that all conformations of a structure are assigned to the same split. To learn approximate equivariance, we use data augmentation: during pretraining, we duplicate each batch once and apply random rotations and reflections to both copies to form an augmented batch."
- , PDF page 3, We examine the effects of forgoing almost all commonly: "Instead of predicting a combined loss50 of energies and forces or calculating forces as the negative gradient of the predicted energy with respect to positions, we predict forces directly."
- , PDF page 5, Pretraining performance: "We perform supervised pretraining on the new QCML dataset.45"
- , PDF page 5, Pretraining performance: "In Table I, we present the mean absolute error (MAE) of force predictions for MD-ET, SpookyNet,70 and PaiNN21 on the QCML evaluation set at the end of pretraining."
