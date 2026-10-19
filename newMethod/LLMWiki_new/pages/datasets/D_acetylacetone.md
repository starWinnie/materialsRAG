# Dataset: acetylacetone

- Dataset ID: `D_acetylacetone`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- acetylacetone
- AcAc
- acetylacetone dataset

## Observed material scopes

- reactive molecules
- small organic molecules

## Observed research tasks

- Creating fast and accurate force fields

## Observed research stages

- data_acquisition
- model_training
- model_evaluation

## Observed properties

- potential energy
- forces

## Observed fields

- atomic positions
- chemical elements
- DFT-computed energies and forces

## Usage evidence

- P054 (MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields): training in Using DFT-computed energies and forces — Acquire ab initio training data for force field development
- P054 (MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields): training in Training MACE models — Train the MACE architecture on acquired datasets to learn interatomic potentials
- P054 (MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields): test in Evaluating accuracy and computational cost on benchmarks — Assess model performance in terms of accuracy (energy/force errors), extrapolation, and computational efficiency

## Dataset evidence

- P111, PDF page 16, A.2.3 Acetylacetone Dataset: "The acetylacetone dataset contains trajectories of a small reactive molecule sampled at different temperature. The task is to train on snapshot sampled at 300K and test on independent test sets sampled at 300K and 600K."
- P111, PDF page 9, 5.3.3 AcAc: Flexibility and Reactivity: "A similar benchmark dataset assessing a model’s extrapolation capabilities to higher temperatures, bond breaking, and bond torsions of the acetylacetone molecule was proposed in [3]."
