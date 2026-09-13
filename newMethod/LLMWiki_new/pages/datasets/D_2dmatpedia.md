# Dataset: 2DMatPedia

- Dataset ID: `D_2dmatpedia`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- 2DMatPedia
- 2DMatPedia database

## Observed material scopes

- two-dimensional materials

## Observed research tasks

- Predicting thermodynamic stability of inorganic compounds
- Accurate piezoelectric tensor prediction

## Observed research stages

- data_acquisition
- model_evaluation
- candidate_generation

## Observed properties

- thermodynamic stability
- bandgap
- crystal structure

## Observed fields

- composition
- stability
- bandgap
- crystal structure

## Usage evidence

- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): test in Collecting DFT-computed thermodynamic stability data from public databases — Benchmark predictive performance on two-dimensional materials
- P007 (Accurate piezoelectric tensor prediction with equivariant attention tensor graph neural network): candidate_pool in High-throughput screening of candidate materials — To screen candidate 2D piezoelectric materials using trained EATGNN

## Dataset evidence

- P005, PDF page 9, unknown: "Then, we tested the trained model on the 2Dmatpedia database, which contains 4743 materials."
- P005, PDF page 9, unknown: "After verifying the stability using labels from 2dMatpedia, 313 of them were found to meet the stability requirements."
- P007, PDF page 6, unknown: "In order to discover new potential high-performance piezoelectric materials, we use our model on both 3D and 2D materials in the Materials Project and 2DMatPedia database36, respectively. Our selection criteria are 1) out of the training datasets, 2) inversion asymmetry, 3) Egap > 0.1 eV, and 4) Nuc < 30 atoms."
