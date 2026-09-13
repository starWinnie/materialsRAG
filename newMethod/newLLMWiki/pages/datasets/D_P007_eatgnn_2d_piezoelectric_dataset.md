# Dataset: EATGNN 2D piezoelectric dataset

- Dataset ID: `D_P007_eatgnn_2d_piezoelectric_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_computational_2d_materials_database`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- EATGNN 2D piezoelectric dataset
- 1350 data points

## Observed material scopes

- two-dimensional materials

## Observed research tasks

- Accurate piezoelectric tensor prediction

## Observed research stages

- data_preparation
- model_evaluation

## Observed properties

- piezoelectric tensor (eijk)

## Observed fields

- crystal structure
- piezoelectric tensor

## Usage evidence

- P007 (Accurate piezoelectric tensor prediction with equivariant attention tensor graph neural network): training in Data resampling and symmetry correction — To train EATGNN model on cleaned, symmetry-compliant 2D piezoelectric data
- P007 (Accurate piezoelectric tensor prediction with equivariant attention tensor graph neural network): test in Evaluation using MAE and RMSE on test sets — To evaluate EATGNN performance on held-out 2D test set

## Dataset evidence

- P007, PDF page 5, unknown: "The piezoelectric tensor data of 2D materials was obtained from the C2DB database33,34, comprising a total of 1382 data points, after analyzing and removing some extreme outliers to prevent the model from learning an inaccurate data distribution, 1350 data points were retained and randomly split into training and test sets with 9:1 ratio."
