# Dataset Use: MD17

- DatasetUse ID: `DU_md17`
- Dataset: MD17 (`D_md17`)
- Papers: P032
- Usage records: 2

## Usage roles

- training
- test

## Purposes

- Fine-tuning the pretrained MD-ET model on specific molecular systems.
- Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the MD17 dataset.

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

### UR_P032_04_md17

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
- P032, PDF page 3, We examine the effects of forgoing almost all commonly: "For downstream task evaluation, we fine-tune the model for a small number of steps only."
- P032, PDF page 5, Pretraining performance: "We also report results for training the model directly on MD17. Since there is some overlap with the pretraining set, fine-tuning results for ethanol (marked with a ∗) have only limited significance."

### UR_P032_05_md17

- Paper: `P032` — How simple can you go? An off-the-shelf transformer approach to molecular dynamics
- Task: molecular dynamics simulation using machine learning force fields (`T_P032_01`)
- Stage: benchmark evaluation on force prediction accuracy (`model_evaluation`, `S_P032_05`)
- Usage role: test
- Purpose: Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the MD17 dataset.
- Used fields: atomic forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P032, PDF page 5, MD17-10k: "The MD17 dataset15 consists of MD trajectories for small organic molecules and has been proposed as a benchmark by Fu et al.74 Models are evaluated not only for their prediction accuracy (MAE) but also for their simulation stability and faithfulness."

## Aggregated evidence

- , PDF page 3, We examine the effects of forgoing almost all commonly: "For downstream task evaluation, we fine-tune the model for a small number of steps only."
- , PDF page 5, Pretraining performance: "We also report results for training the model directly on MD17. Since there is some overlap with the pretraining set, fine-tuning results for ethanol (marked with a ∗) have only limited significance."
- , PDF page 5, MD17-10k: "The MD17 dataset15 consists of MD trajectories for small organic molecules and has been proposed as a benchmark by Fu et al.74 Models are evaluated not only for their prediction accuracy (MAE) but also for their simulation stability and faithfulness."
