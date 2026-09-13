# Dataset: synthetic orbit distance dataset

- Dataset ID: `D_synthetic_orbit_distance_dataset`
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
- crystals

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

- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): candidate_pool in constructing synthetic dataset for orbit distance validation — To generate a controlled synthetic dataset for validating the geometric fidelity of the G-invariant encoding module.
- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): training in pretraining the G-invariant positional encoding module — To train the symmetry-adapted encoding module to produce embeddings where the Euclidean distance corresponds to the true orbit distance.

## Dataset evidence

- P002, PDF page 8, SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "We construct a synthetic dataset containing 100,000 samples for each of the 230 space groups. Each sample consists of a pair of random atomic positions as fractional coordinates in [0, 1)3, a space group, and randomly generated lattice vectors that satisfy the constraints of the Bravais lattice for the group."
