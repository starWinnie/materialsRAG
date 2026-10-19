# Dataset: 3BPA

- Dataset ID: `D_3bpa`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- 3BPA
- 3-(benzyloxy)pyridin-2-amine

## Observed material scopes

- drug-like molecules

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

- P111, PDF page 15, A.2.2 3BPA Dataset: "The 3BPA dataset contains DFT train test splits of a flexible drug-like organic molecule sampled from different temperature molecular dynamics trajectories [33]."
- P111, PDF page 8, 5.3.2 3BPA: Extrapolation to Out-of-domain Data: "The 3BPA dataset introduced in [33] tests a model’s extrapolation capabilities. Its training set contains 500 geometries sampled from 300 K molecular dynamics simulation of the large and flexible drug-like molecule 3-(benzyloxy)pyridin-2-amine."
