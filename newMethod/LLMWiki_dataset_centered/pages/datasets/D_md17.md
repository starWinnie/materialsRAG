# Dataset: MD17

- Dataset ID: `D_md17`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MD17
- MD17-10k
- MD17@CCSD(T)

## Observed material scopes

- molecules

## Observed research tasks

- molecular dynamics simulation using machine learning force fields

## Observed research stages

- model_training
- model_evaluation

## Observed properties

- atomic forces
- energy
- trajectory

## Observed fields

- 3D atomic positions
- atomic numbers

## Usage evidence

- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): training in fine-tuning on downstream datasets — Fine-tuning the pretrained MD-ET model on specific molecular systems.
- P032 (How simple can you go? An off-the-shelf transformer approach to molecular dynamics): test in benchmark evaluation on force prediction accuracy — Assess the mean absolute error (MAE) of predicted atomic forces against ground truth on the MD17 dataset.

## Dataset evidence

- P032, PDF page 5, Pretraining performance: "We also report results for training the model directly on MD17. Since there is some overlap with the pretraining set, fine-tuning results for ethanol (marked with a ∗) have only limited significance."
- P032, PDF page 5, MD17-10k: "The MD17 dataset15 consists of MD trajectories for small organic molecules and has been proposed as a benchmark by Fu et al.74 Models are evaluated not only for their prediction accuracy (MAE) but also for their simulation stability and faithfulness."
- P032, PDF page 5, MD17-10k: "Table II compares MD-ET with several state-of-the-art models. In addition to fine-tuning ET-MD for 2000 steps, which we see as the default way to use a large-scale pretrained model, we also report results for training the model directly on MD17."
