# Dataset: Open Catalyst 2025

- Dataset ID: `D_open_catalyst_2025`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Open Catalyst 2025
- OC25
- Open Catalyst 2025 (OC25) dataset

## Observed material scopes

- catalyst surface
- solvent
- ion
- adsorbate molecule

## Observed research tasks

- CO dimerization on copper surfaces

## Observed research stages

- data_acquisition
- model_training
- computational_validation

## Observed properties

- total energy
- per-atom forces

## Observed fields

- energies
- forces

## Usage evidence

- P062 (Insights into CO dimerization at electrified Cu interfaces from large-scale machine learning simulations): source in OC25 dataset construction — Construct the largest dataset for solid–liquid interfaces comprising over 7 million DFT calculations sampling explicit solvent configurations across elements, solvents, ions, and non-equilibrium structures.
- P062 (Insights into CO dimerization at electrified Cu interfaces from large-scale machine learning simulations): training in Training eSEN-OC25 MLIP model — Train an energy-conserving graph neural network (eSEN-S) to enable near-DFT accuracy at reduced computational cost.
- P062 (Insights into CO dimerization at electrified Cu interfaces from large-scale machine learning simulations): computational_validation in DFT validation of MLIP-predicted configurations — Assess reliability of eSEN-OC25 predictions for large-cell CO dimerization simulations by computing DFT single-points on ∼100 configurations per state (initial, transition, final).

## Dataset evidence

- P119, PDF page 2, Results: "To bridge this gap, we introduce the Open Catalyst 2025 (OC25) dataset and models for solid-liquid interfaces, comprising over 7 million DFT calculations sampling more than one million explicit solvent configurations across a wide variety of elements, solvents, ions, and non-equilibrium structures."
- P119, PDF page 2, Results: "The OC25 dataset is constructed from a combination of DFT relaxations and AIMD simulations of catalyst, solvent, and ion structures. Structures consist of a catalyst surface, a solvent, and at least one adsorbate molecule."
- P119, PDF page 2, Results: "Overall, the OC25 dataset consists of 7,801,261 single-point calculations, spanning 1,511,270 unique systems and 88 unique elements (Figure 1)."
