# Dataset: revised MD17

- Dataset ID: `D_revised_md17`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- revised MD17
- rMD17
- rMD17 data set

## Observed material scopes

- organic molecules
- aspirin

## Observed research tasks

- training machine-learned interatomic potentials (MLIPs)

## Observed research stages

- model_training
- model_evaluation
- experimental_validation

## Observed properties

- total energies
- atomic forces

## Observed fields

- atomic configurations
- reference energies
- reference atomic forces

## Usage evidence

- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): training in training MLIPs with PIWSL loss — training MLIPs with PIWSL loss
- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): test in benchmarking models trained with PIWSL — benchmarking models trained with PIWSL
- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): experimental_validation in evaluating robustness during MD simulations — evaluating robustness during MD simulations

## Dataset evidence

- P034, PDF page 5, 5.1. Models and Data Sets: "the revised MD17 (rMD17) data set containing small molecules with sampled configurational spaces for each (Chmiela et al., 2017; 2018; Christensen & von Lilienfeld, 2020)"
- P034, PDF page 15, C.3. Description of the Data Sets: "The rMD17 data set includes ten small organic molecules, including 100,000 configurations obtained by running MD simulations for each (Christensen & von Lilienfeld, 2020). The ML model requires learning the total energies and atomic forces for each molecule. In this revised version of the MD17 data set, the molecules are taken from the original MD17 data set (Chmiela et al., 2017; 2018). However, the energies and forces are recalculated at the PBE/def2-SVP level of theory using very tight SCF convergence and a very dense DFT integration grid."
