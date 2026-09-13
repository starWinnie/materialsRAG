# Dataset Use: xxMD

- DatasetUse ID: `DU_xxmd`
- Dataset: xxMD (`D_xxmd`)
- Papers: P032
- Usage records: 2

## Usage roles

- training
- test

## Purposes

- Fine-tuning the pretrained MD-ET model on specific molecular systems.
- Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the xxMD dataset.

## Used fields

- 3D atomic positions
- atomic numbers
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

### UR_P032_04_xxmd

- Paper: `P032` — How simple can you go? An off-the-shelf transformer approach to molecular dynamics
- Task: molecular dynamics simulation using machine learning force fields (`T_P032_01`)
- Stage: fine-tuning on downstream datasets (`model_training`, `S_P032_04`)
- Usage role: training
- Purpose: Fine-tuning the pretrained MD-ET model on specific molecular systems.
- Used fields: 3D atomic positions, atomic numbers, atomic forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P032, PDF page 7, xxMD: "The xxMD dataset by Pengmei et al.68 goes beyond the MD17 dataset by incorporating nonadiabatic MD trajectories specifically designed to capture chemical reactions, including geometries sampled from the PES of reactive intermediates, transition states, and products."

### UR_P032_05_xxmd

- Paper: `P032` — How simple can you go? An off-the-shelf transformer approach to molecular dynamics
- Task: molecular dynamics simulation using machine learning force fields (`T_P032_01`)
- Stage: benchmark evaluation on force prediction accuracy (`model_evaluation`, `S_P032_05`)
- Usage role: test
- Purpose: Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the xxMD dataset.
- Used fields: atomic forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P032, PDF page 7, xxMD: "Table V shows the MAE score on xxMD."

## Aggregated evidence

- , PDF page 7, xxMD: "The xxMD dataset by Pengmei et al.68 goes beyond the MD17 dataset by incorporating nonadiabatic MD trajectories specifically designed to capture chemical reactions, including geometries sampled from the PES of reactive intermediates, transition states, and products."
- , PDF page 7, xxMD: "Table V shows the MAE score on xxMD."
