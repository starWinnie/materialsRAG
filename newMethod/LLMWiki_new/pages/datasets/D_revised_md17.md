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
- MD17

## Observed material scopes

- organic molecules
- aspirin
- small organic molecules

## Observed research tasks

- training machine-learned interatomic potentials (MLIPs)
- Creating fast and accurate force fields

## Observed research stages

- data_acquisition
- model_training
- experimental_validation
- model_evaluation

## Observed properties

- total energies
- atomic forces
- potential energy
- forces

## Observed fields

- atomic configurations
- atom positions
- atom types
- reference energies
- reference atomic forces
- atomic positions
- chemical elements
- DFT-computed energies and forces

## Usage evidence

- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): training in generating training data sets — to generate training data sets that sufficiently cover configurational (atom positions) and compositional (atom types) spaces
- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): training in training MLIPs with PIWSL loss — to train MLIPs with PIWSL loss
- P034 (Physics-Informed Weakly Supervised Learning for Interatomic Potentials): experimental_validation in evaluating robustness during MD simulations — to evaluate robustness during MD simulations of the MLIP models trained with and without PIWSL
- P054 (MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields): training in Using DFT-computed energies and forces — Acquire ab initio training data for force field development
- P054 (MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields): training in Training MACE models — Train the MACE architecture on acquired datasets to learn interatomic potentials
- P054 (MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields): test in Evaluating accuracy and computational cost on benchmarks — Assess model performance in terms of accuracy (energy/force errors), extrapolation, and computational efficiency

## Dataset evidence

- P034, PDF page 5, 5.1. Models and Data Sets: "the revised MD17 (rMD17) data set containing small molecules with sampled configurational spaces for each (Chmiela et al., 2017; 2018; Christensen & von Lilienfeld, 2020)"
- P034, PDF page 15, C.3. Description of the Data Sets: "The rMD17 data set includes ten small organic molecules, including 100,000 configurations obtained by running MD simulations for each (Christensen & von Lilienfeld, 2020). The ML model requires learning the total energies and atomic forces for each molecule. In this revised version of the MD17 data set, the molecules are taken from the original MD17 data set (Chmiela et al., 2017; 2018). However, the energies and forces are recalculated at the PBE/def2-SVP level of theory using very tight SCF convergence and a very dense DFT integration grid."
- P111, PDF page 15, A.2.1 rMD17 Dataset: "The revised MD17 (rMD17) dataset contains five train test splits of 10 different small organic molecules [11]. Each of the splits contains 1000 configurations for each molecule sampled randomly from a long Ab initio molecular dynamics simulation carried out at 500 K computed with DFT."
- P111, PDF page 7, 5.3.1 rMD17: Molecular Dynamics Trajectory: "The revised MD17 (rMD17) dataset contains train test splits randomly selected from a long molecular dynamics trajectory of ten small organic molecules [11]. For each molecule, the splits consist of 1000 training and test configurations."
