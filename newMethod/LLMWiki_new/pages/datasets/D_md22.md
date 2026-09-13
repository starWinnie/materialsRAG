# Dataset: MD22

- Dataset ID: `D_md22`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MD22
- MD22 data set

## Observed material scopes

- organic molecules
- buckyball catcher

## Observed research tasks

- training machine-learned interatomic potentials (MLIPs)

## Observed research stages

- data_acquisition
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
- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): training in fine-tuning foundation models — to demonstrate the application of PIWSL to the fine-tuning of foundation models using a sparse data set

## Dataset evidence

- P034, PDF page 5, 5.1. Models and Data Sets: "the MD22 data set containing larger molecules (Chmiela et al., 2023)"
- P034, PDF page 15, C.3. Description of the Data Sets: "The MD22 data set (Chmiela et al., 2023) includes seven larger organic molecules, such as a small peptide and a double-walled nanotube, whose size ranges from 42 to 370 atoms. The data set consists of MD trajectories sampled at temperatures between 400 and 500 K. The ML model requires learning the total energies and atomic forces for each molecule. The energies and forces are calculated at the PBE+MBD level of theory."
