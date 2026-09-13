# Dataset: TiO2

- Dataset ID: `D_tio2`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- TiO2
- TiO2 data set

## Observed material scopes

- inorganic materials
- bulk materials
- transition-metal oxide

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

- P034, PDF page 5, 5.1. Models and Data Sets: "TiO2 as a data set for inorganic materials (Artrith & Urban, 2016)"
- P034, PDF page 15, C.3. Description of the Data Sets: "TiO2 dataset includes 7815 bulk structures of several TiO2 phases whose reference energies and forces are obtained through DFT calculations (Artrith & Urban, 2016). The number of atoms in a single configuration ranges from 6 to 95."
