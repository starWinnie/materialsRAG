# Dataset: SPICE

- Dataset ID: `D_spice`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- SPICE

## Observed material scopes

- molecules

## Observed research tasks

- molecular dynamics simulation using machine learning force fields

## Observed research stages

- model_training
- model_evaluation

## Observed properties

- atomic forces

## Observed fields

- 3D atomic positions
- atomic numbers

## Usage evidence

- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): training in fine-tuning on downstream datasets — Fine-tuning the pretrained MD-ET model on specific molecular systems.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): test in benchmark evaluation on force prediction accuracy — Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the SPICE dataset.

## Dataset evidence

- P032, PDF page 7, SPICE: "All previously evaluated datasets contain conformers of a single, relatively small structure (∼10-20 atoms). The SPICE dataset contains several subsets with conformers of multiple structures with a size of up to 96 atoms.69"
