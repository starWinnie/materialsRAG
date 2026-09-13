# Dataset Use: synthetic orbit distance dataset

- DatasetUse ID: `DU_synthetic_orbit_distance_dataset`
- Dataset: synthetic orbit distance dataset (`D_synthetic_orbit_distance_dataset`)
- Papers: P002
- Usage records: 2

## Usage roles

- candidate_pool
- training

## Purposes

- To generate a controlled synthetic dataset for validating the geometric fidelity of the G-invariant encoding module.
- To train the symmetry-adapted encoding module to produce embeddings where the Euclidean distance corresponds to the true orbit distance.

## Used fields

- atomic position pair
- space group
- lattice vectors
- ground-truth orbit distances

## Construction methods

- constructing synthetic dataset containing 100,000 samples for each of the 230 space groups

## Filter conditions

- None stated

## Sample counts

- 100000

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P002_02_synthetic_orbit_distance_dataset

- Paper: `P002` — A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP
- Task: developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group (`T_P002_01`)
- Stage: constructing synthetic dataset for orbit distance validation (`data_preparation`, `S_P002_02`)
- Usage role: candidate_pool
- Purpose: To generate a controlled synthetic dataset for validating the geometric fidelity of the G-invariant encoding module.
- Used fields: atomic position pair, space group, lattice vectors
- Filter conditions: Not stated
- Construction method: constructing synthetic dataset containing 100,000 samples for each of the 230 space groups
- Sample count: 100000
- Confidence: 1.0

Evidence:
- P002, PDF page 8, SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "We construct a synthetic dataset containing 100,000 samples for each of the 230 space groups. Each sample consists of a pair of random atomic positions as fractional coordinates in [0, 1)3, a space group, and randomly generated lattice vectors that satisfy the constraints of the Bravais lattice for the group."

### UR_P002_05_synthetic_orbit_distance_dataset

- Paper: `P002` — A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP
- Task: developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group (`T_P002_01`)
- Stage: pretraining the G-invariant positional encoding module (`model_training`, `S_P002_05`)
- Usage role: training
- Purpose: To train the symmetry-adapted encoding module to produce embeddings where the Euclidean distance corresponds to the true orbit distance.
- Used fields: atomic position pair, space group, lattice vectors, ground-truth orbit distances
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P002, PDF page 8, SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "We first validate this capability in a controlled, self-supervised setting before applying the model to downstream tasks. The goal is to train the encoder to produce positional encodings where the Euclidean distance between embeddings directly corresponds to the true orbit distance dG(x1, x2) between atoms."
- P002, PDF page 8, SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "The model is trained to minimize the Mean Squared Error (MSE) between the L2 distance of the output embeddings and the ground-truth orbit distance."

## Aggregated evidence

- , PDF page 8, SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "We construct a synthetic dataset containing 100,000 samples for each of the 230 space groups. Each sample consists of a pair of random atomic positions as fractional coordinates in [0, 1)3, a space group, and randomly generated lattice vectors that satisfy the constraints of the Bravais lattice for the group."
- , PDF page 8, SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "We first validate this capability in a controlled, self-supervised setting before applying the model to downstream tasks. The goal is to train the encoder to produce positional encodings where the Euclidean distance between embeddings directly corresponds to the true orbit distance dG(x1, x2) between atoms."
- , PDF page 8, SYMMETRY-ADAPTED ENCODINGS CAPTURE ORBIT DISTANCE: "The model is trained to minimize the Mean Squared Error (MSE) between the L2 distance of the output embeddings and the ground-truth orbit distance."
