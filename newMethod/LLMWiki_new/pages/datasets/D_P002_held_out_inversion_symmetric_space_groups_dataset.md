# Dataset: held-out inversion-symmetric space groups dataset

- Dataset ID: `D_P002_held_out_inversion_symmetric_space_groups_dataset`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- held-out inversion-symmetric space groups dataset
- held-out dataset of inversion-symmetric space groups
- dataset of held-out inversion groups

## Observed material scopes

- crystalline solids

## Observed research tasks

- developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group

## Observed research stages

- model_evaluation

## Observed properties

- total energy
- shear modulus

## Observed fields

- space group identifier
- crystal structure

## Usage evidence

- P002 (A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP): screening in performing zero-shot generalization evaluation — Evaluate the ability of the CFT model to generalize to space groups not seen during training.

## Dataset evidence

- P002, PDF page 9, 5.4 ZERO-SHOT GENERALIZATION TO UNSEEN SPACE GROUPS: "We test this hypothesis in a zero-shot setting by holding out all space groups containing inversion symmetry from the training set."
- P002, PDF page 9, 5.4 ZERO-SHOT GENERALIZATION TO UNSEEN SPACE GROUPS: "For each held-out inversion group G ∈Ginv, we compute the group-wise MAE under the zero-shot and all-data training regimes, denoted MAEzero-shot G and MAEall-data G."
