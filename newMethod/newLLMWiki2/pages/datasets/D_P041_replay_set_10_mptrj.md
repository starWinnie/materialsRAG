# Dataset: Replay set (10% MPtrj)

- Dataset ID: `D_P041_replay_set_10_mptrj`
- Dataset type: `derived_subset`
- Source dataset: `D_mptrj`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Replay set (10% MPtrj)
- Replay set
- 10% of the MPtrj dataset
- Replay set for both Replay and reEWC

## Observed material scopes

- diverse inorganic crystals
- most elements in the periodic table

## Observed research tasks

- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- data_acquisition
- data_preparation
- model_training

## Observed properties

- energy
- force
- stress

## Observed fields

- atomic configurations
- DFT energies
- forces
- stresses

## Usage evidence

- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): candidate_pool in constructing the Replay set by sampling from the pretrained MPtrj dataset — constructing the Replay set by sampling from the pretrained MPtrj dataset
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): training in preprocessing datasets for fine-tuning — preprocessing datasets for fine-tuning
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): training in fine-tuning SevenNet-0 using reEWC loss function — fine-tuning SevenNet-0 using reEWC loss function

## Dataset evidence

- P041, PDF page 4, Fine-tuning MLIPs on LPSC dataset: "On the other hand, to construct the Replay set for both Replay and reEWC, we randomly sample 10% of the MPtrj dataset."
