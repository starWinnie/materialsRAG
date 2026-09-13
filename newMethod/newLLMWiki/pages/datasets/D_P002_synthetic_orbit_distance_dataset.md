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
- crystals

## Observed research tasks

- developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group

## Observed research stages

- data_preparation
- label_generation
- model_training

## Observed properties

- orbit distance

## Observed fields

- atomic positions
- space group
- lattice vectors

## Usage evidence

- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): candidate_pool in constructing synthetic dataset for orbit distance validation — Generate synthetic crystal pairs with ground-truth orbit distances to pretrain and validate the symmetry-adapted encoding module.
- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): label_source in computing orbit distance as ground truth — Calculate the orbit distance dG(x1, x2) = minϕ1,ϕ2∈G ||ϕ1(x1) − ϕ2(x2)||2 for each pair of atomic positions in the synthetic dataset.
- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): training in pretraining the symmetry-adapted positional encoding module — Train the G-invariant encoding module to produce embeddings where Euclidean distance matches the ground-truth orbit distance.

## Dataset evidence

- P002, PDF page 8, 5.2 SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "We construct a synthetic dataset containing 100,000 samples for each of the 230 space groups. Each sample consists of a pair of random atomic positions as fractional coordinates in [0, 1)3, a space group, and randomly generated lattice vectors that satisfy the constraints of the Bravais lattice for the group."
