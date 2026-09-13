# Dataset: MPtrj dataset

- Dataset ID: `D_mptrj_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MPtrj dataset
- MPtrj

## Observed material scopes

- inorganic crystals
- crystals
- elements across the periodic table up to Pu

## Observed research tasks

- ML-guided materials discovery
- universal atomic embeddings (UAEs)
- Develop a foundation machine learning interatomic potential with explicit polarizable long-range interactions

## Observed research stages

- model_training
- model_evaluation
- data_acquisition
- data_preparation

## Observed properties

- energies
- forces
- stresses
- force
- stress
- energy
- total potential energy

## Observed fields

- energies
- forces
- stresses
- force
- stress
- energy
- atomic coordinates
- atomic types

## Usage evidence

- P004 (A framework to evaluate machine learning crystal stability predictions): training in Training of ML models on MP data — Training universal interatomic potential (UIP) models (EquiformerV2+DeNS, ORB, SevenNet, MACE, CHGNet) on energies, forces, and stresses.
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): computational_validation in evaluating transferability of ct-UAEs across databases and tasks — to investigate the suitability of ct-UAE on energy-conserving interatomic potential (IAP) models
- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): source in Acquire training datasets including diverse charge-state systems and periodic table elements — Train a foundation model for all the periodic table elements up to Pu
- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): training in Prepare dataset configurations with DFT-calculated energies, forces, and stresses — Train the foundation equivariant neural network potential

## Dataset evidence

- P004, PDF page 8, Article: "The final dataset we highlight, with which several of the UIP models have been trained, is the MPtrj dataset23. This dataset was curated from the earlier v.2021.11.10 MP release. The MPtrj dataset is a proper subset of the allowed training data but several potentially anomalous examples from within MP were cleaned out of the dataset before the frames were subsampled to remove redundant frames."
- P004, PDF page 8, Article: "Here we take the pre-trained ‘eqV2 S DeNS’40 trained on the MPtrj dataset."
- P006, PDF page 4: "Additionally, we also investigated the suitability of ct-UAE on energy-conserving interatomic potential (IAP) models, which are trained based on the MPtrj dataset50."
- P039, PDF page 4, Foundation model benchmark: "We trained a foundation model for all the periodic table elements up to Pu using the MPtrj dataset16 following our framework (our model), as described in the Methods section."
- P039, PDF page 9, Methods: "To train the foundation equivariance neural network potential, we used the MPtrj dataset16 sourced from Materials Projects48 as the training dataset. All configurations were calculated using DFT with the PBE82/PBE + U83 exchange-correlation functional and pseudopotential basis."
- P039, PDF page 10, Data availability: "The MPtrj dataset is also publicly available from the reference94 through https://doi.org/10.6084/m9.figshare.23713842."
