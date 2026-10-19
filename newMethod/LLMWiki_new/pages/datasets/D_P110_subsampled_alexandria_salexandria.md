# Dataset: subsampled Alexandria (sAlexandria)

- Dataset ID: `D_P110_subsampled_alexandria_salexandria`
- Dataset type: `derived_subset`
- Source dataset: `D_alexandria`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- subsampled Alexandria (sAlexandria)
- sAlexandria
- sAlex
- subsampled Alexandria

## Observed material scopes

- inorganic bulk materials

## Observed research tasks

- training Machine Learning Interatomic Potentials (MLIPs) for inorganic materials

## Observed research stages

- model_training

## Observed properties

- energy
- forces
- cell stress

## Observed fields

- energy
- forces
- cell stress
- atomic positions
- unit cell

## Usage evidence

- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): training in pretraining and fine-tuning of EquiformerV2 and eSEN models on OMat24 and related datasets — to fine-tune pretrained models on domain-specific data while preventing data leakage to the WBM test set

## Dataset evidence

- P110, PDF page 11, 4.3 OMat24 MLIP training strategies: "Since similar structures exist in the Alexandria and the WBM dataset used for testing, we subsampled the Alexandria dataset for training to ensure there was no leakage between the training and testing datasets. The new subset of Alexandria (sAlexandria) was created by removing all trajectories in which any structure matched a structure in the WBM initial and relaxed structures using structure prototype labels35. Next, we reduced the size of the Alexandria dataset by removing all structures with energies > 0 eV, forces norm > 50 eV/Å, and stress > 80 GPa. Finally, we only sampled structures in the remaining trajectories that had a energy difference greater than 10 meV/atom. The resulting datasets used for training and validation had 10 million and 500 thousand structures respectively."
- P110, PDF page 13, Data Availability: "Data Availability The OMat24 and subsampled Alexandria (sAlex) datasets, as well as the reference compounds and fitted MP2020-style Compatiblity corrections are available for download via Hugging Face75."
