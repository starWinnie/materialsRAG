# Dataset: LPSC fine-tuning dataset

- Dataset ID: `D_P041_lpsc_fine_tuning_dataset`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- LPSC fine-tuning dataset
- fine-tuning dataset
- fine-tuning set

## Observed material scopes

- Li6PS5Cl (LPSC)

## Observed research tasks

- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- data_acquisition
- model_training
- model_evaluation

## Observed properties

- potential energy
- atomic forces

## Observed fields

- atomic positions
- cell parameters
- energies
- forces

## Usage evidence

- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): training in constructing the fine-tuning dataset from AIMD trajectories of LPSC — generate training data capturing diverse Li-ion hopping events and high-energy configurations for LPSC
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): training in fine-tuning SevenNet-0 using reEWC method — refine the pretrained MLIP parameters using the hybrid reEWC strategy
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): validation in evaluating forgetting prevention and learning performance on sMPtrj and fine-tuning validation sets — assess target system learning (loss on LPSC validation set)

## Dataset evidence

- P041, PDF page 4, Fine-tuning MLIPs on LPSC dataset: "The fine-tuning dataset is constructed from MD trajectories of an LPSC unit cell (52atoms) obtained from 100 ps simulations conducted at 600 and 1000 K. At each temperature, 500 structures are uniformly sampled at 200 fs intervals, resulting in a total of 1000 structures. These structures are then randomly split into training and validation datasets at a 9:1 ratio."
