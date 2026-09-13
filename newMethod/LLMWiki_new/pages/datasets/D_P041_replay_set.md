# Dataset: Replay set

- Dataset ID: `D_P041_replay_set`
- Dataset type: `derived_subset`
- Source dataset: `D_mptrj_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Replay set
- Replay dataset

## Observed material scopes

- most elements in the periodic table

## Observed research tasks

- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- data_acquisition
- model_training

## Observed properties

- potential energy
- atomic forces

## Observed fields

- atomic positions
- cell parameters
- energies
- forces

## Usage evidence

- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): candidate_pool in constructing the Replay set by random sampling from the pretrained dataset — obtain a representative subset of the pretrained dataset to mitigate catastrophic forgetting during fine-tuning
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): training in fine-tuning SevenNet-0 using reEWC method — refine the pretrained MLIP parameters using the hybrid reEWC strategy

## Dataset evidence

- P041, PDF page 4, Fine-tuning MLIPs on LPSC dataset: "On the other hand, to construct the Replay set for both Replay and reEWC, we randomly sample 10% of the MPtrj dataset."
