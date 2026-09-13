# Dataset: xxMD

- Dataset ID: `D_xxmd`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- xxMD

## Observed material scopes

- molecules

## Observed research tasks

- molecular dynamics simulation using machine learning force fields

## Observed research stages

- model_training
- model_evaluation

## Observed properties

- atomic forces
- trajectory

## Observed fields

- 3D atomic positions
- atomic numbers

## Usage evidence

- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): training in fine-tuning on downstream datasets — Fine-tuning the pretrained MD-ET model on specific molecular systems.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): test in benchmark evaluation on force prediction accuracy — Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the xxMD dataset.

## Dataset evidence

- P032, PDF page 7, xxMD: "The xxMD dataset by Pengmei et al.68 goes beyond the MD17 dataset by incorporating nonadiabatic MD trajectories specifically designed to capture chemical reactions, including geometries sampled from the PES of reactive intermediates, transition states, and products."
