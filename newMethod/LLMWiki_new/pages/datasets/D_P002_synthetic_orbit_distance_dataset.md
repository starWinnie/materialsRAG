# Dataset: synthetic orbit distance dataset

- Dataset ID: `D_P002_synthetic_orbit_distance_dataset`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- synthetic orbit distance dataset
- synthetic dataset

## Observed material scopes

- crystalline solids

## Observed research tasks

- developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group

## Observed research stages

- data_preparation
- model_training

## Observed properties

- orbit distance

## Observed fields

- atomic position pair
- space group
- lattice vectors

## Usage evidence

- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): training in constructing synthetic dataset for orbit distance validation — Validate the geometric fidelity of the G-invariant encoding module by training it to produce embeddings where Euclidean distance corresponds to orbit distance.
- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): training in pretraining the G-invariant encoding module — Train the positional encoding module to produce embeddings where Euclidean distance corresponds to orbit distance.

## Dataset evidence

- P002, PDF page 8, 5.2 SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "We construct a synthetic dataset containing 100,000 samples for each of the 230 space groups. Each sample consists of a pair of random atomic positions as fractional coordinates in [0, 1)3, a space group, and randomly generated lattice vectors that satisfy the constraints of the Bravais lattice for the group."
