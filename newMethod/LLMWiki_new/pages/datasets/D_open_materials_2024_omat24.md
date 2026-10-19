# Dataset: Open Materials 2024 (OMat24)

- Dataset ID: `D_open_materials_2024_omat24`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Open Materials 2024 (OMat24)
- OMat24
- Open Materials 2024 (OMat24) dataset

## Observed material scopes

- inorganic bulk materials

## Observed research tasks

- training Machine Learning Interatomic Potentials (MLIPs) for inorganic materials

## Observed research stages

- data_acquisition
- data_preparation
- label_generation
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

- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): candidate_pool in generation of diverse non-equilibrium structures via Boltzmann sampling, AIMD, and rattled relaxations — to generate diverse non-equilibrium structures via Boltzmann sampling, AIMD, and rattled relaxations
- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): training in creation of explicit training, validation and test splits — to create explicit training, validation and test splits ensuring consistent training and evaluation by the community
- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): label_source in DFT calculation of energy, forces and cell stress labels — to generate ground-truth labels for MLIP training using DFT calculations
- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): pretraining in pretraining and fine-tuning of EquiformerV2 and eSEN models on OMat24 and related datasets — to pretrain EquiformerV2 and eSEN models before fine-tuning

## Dataset evidence

- P110, PDF page 2, Results: "We introduce the Open Materials 2024 (OMat24) dataset (Figure 1) to improve the generalization of MLIPs across a wide range of materials and to reduce systematic softening."
- P110, PDF page 2, 2.1 The OMat24 dataset: "The OMat24 dataset includes a total of 118 million structures labeled with energy, forces and cell stress."
- P110, PDF page 1, Introduction: "Dataset: https://huggingface.co/datasets/fairchem/OMAT24, Creative Commons 4.0 License"
