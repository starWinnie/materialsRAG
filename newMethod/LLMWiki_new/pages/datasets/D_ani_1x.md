# Dataset: ANI-1x

- Dataset ID: `D_ani_1x`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- ANI-1x
- ANI-1x data set

## Observed material scopes

- organic molecules

## Observed research tasks

- training machine-learned interatomic potentials (MLIPs)

## Observed research stages

- data_acquisition
- model_training
- model_evaluation

## Observed properties

- total energies
- atomic forces

## Observed fields

- atomic configurations
- atom positions
- atom types
- reference energies
- reference atomic forces

## Usage evidence

- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): training in generating training data sets — to generate training data sets that sufficiently cover configurational (atom positions) and compositional (atom types) spaces
- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): training in training MLIPs with PIWSL loss — to train MLIPs with PIWSL loss
- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): test in benchmarking models trained with PIWSL — to benchmark models trained with PIWSL

## Dataset evidence

- P034, PDF page 5, 5.1. Models and Data Sets: "ANI-1x as a heterogeneous molecular data set (Smith et al., 2020)"
- P034, PDF page 15, C.3. Description of the Data Sets: "The ANI-1x data set is a heterogeneous molecular data set and includes 63,865 organic molecules (with chemical elements H, C, N, and O) whose size ranges from 4 to 64 atoms (Smith et al., 2020). The ML model requires learning total energies and atomic forces for various molecules and their conformations. Total energies and atomic forces are obtained through DFT calculations."
