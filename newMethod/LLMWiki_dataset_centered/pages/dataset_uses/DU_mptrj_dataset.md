# Dataset Use: MPtrj dataset

- DatasetUse ID: `DU_mptrj_dataset`
- Dataset: MPtrj dataset (`D_mptrj_dataset`)
- Papers: P004, P006, P039
- Usage records: 4

## Usage roles

- training
- computational_validation
- source

## Purposes

- Training universal interatomic potential (UIP) models (EquiformerV2+DeNS, ORB, SevenNet, MACE, CHGNet) on energies, forces, and stresses.
- to investigate the suitability of ct-UAE on energy-conserving interatomic potential (IAP) models
- Train a foundation model for all the periodic table elements up to Pu
- Train the foundation equivariant neural network potential

## Used fields

- energies
- forces
- stresses
- force
- stress
- energy
- atomic coordinates
- atomic types

## Construction methods

- curated subset from v.2021.11.10 MP release with anomalous examples cleaned and redundant frames subsampled

## Filter conditions

- excluded Yb-containing data due to transferability issues

## Sample counts

- None stated

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P004_03_mptrj_dataset

- Paper: `P004` — A framework to evaluate machine learning crystal stability predictions
- Task: ML-guided materials discovery (`T_P004_01`)
- Stage: Training of ML models on MP data (`model_training`, `S_P004_03`)
- Usage role: training
- Purpose: Training universal interatomic potential (UIP) models (EquiformerV2+DeNS, ORB, SevenNet, MACE, CHGNet) on energies, forces, and stresses.
- Used fields: energies, forces, stresses
- Filter conditions: Not stated
- Construction method: curated subset from v.2021.11.10 MP release with anomalous examples cleaned and redundant frames subsampled
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P004, PDF page 8, Article: "The final dataset we highlight, with which several of the UIP models have been trained, is the MPtrj dataset23. This dataset was curated from the earlier v.2021.11.10 MP release. The MPtrj dataset is a proper subset of the allowed training data but several potentially anomalous examples from within MP were cleaned out of the dataset before the frames were subsampled to remove redundant frames."

### UR_P006_03_mptrj_dataset

- Paper: `P006` — Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning
- Task: universal atomic embeddings (UAEs) (`T_P006_01`)
- Stage: evaluating transferability of ct-UAEs across databases and tasks (`model_evaluation`, `S_P006_03`)
- Usage role: computational_validation
- Purpose: to investigate the suitability of ct-UAE on energy-conserving interatomic potential (IAP) models
- Used fields: force, stress, energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P006, PDF page 4: "Additionally, we also investigated the suitability of ct-UAE on energy-conserving interatomic potential (IAP) models, which are trained based on the MPtrj dataset50."

### UR_P039_01_mptrj_dataset

- Paper: `P039` — A foundation machine learning potential with polarizable long-range interactions for materials modelling
- Task: Develop a foundation machine learning interatomic potential with explicit polarizable long-range interactions (`T_P039_01`)
- Stage: Acquire training datasets including diverse charge-state systems and periodic table elements (`data_acquisition`, `S_P039_01`)
- Usage role: source
- Purpose: Train a foundation model for all the periodic table elements up to Pu
- Used fields: atomic coordinates, atomic types, energies, forces, stresses
- Filter conditions: excluded Yb-containing data due to transferability issues
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P039, PDF page 4, Foundation model benchmark: "We trained a foundation model for all the periodic table elements up to Pu using the MPtrj dataset16 following our framework (our model), as described in the Methods section."
- P039, PDF page 9, Methods: "To train the foundation equivariance neural network potential, we used the MPtrj dataset16 sourced from Materials Projects48 as the training dataset. All configurations were calculated using DFT with the PBE82/PBE + U83 exchange-correlation functional and pseudopotential basis."

### UR_P039_02_mptrj_dataset

- Paper: `P039` — A foundation machine learning potential with polarizable long-range interactions for materials modelling
- Task: Develop a foundation machine learning interatomic potential with explicit polarizable long-range interactions (`T_P039_01`)
- Stage: Prepare dataset configurations with DFT-calculated energies, forces, and stresses (`data_preparation`, `S_P039_02`)
- Usage role: training
- Purpose: Train the foundation equivariant neural network potential
- Used fields: atomic coordinates, atomic types, energies, forces, stresses
- Filter conditions: excluded Yb-containing data due to transferability issues
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P039, PDF page 9, Methods: "To train the foundation equivariance neural network potential, we used the MPtrj dataset16 sourced from Materials Projects48 as the training dataset. All configurations were calculated using DFT with the PBE82/PBE + U83 exchange-correlation functional and pseudopotential basis."

## Aggregated evidence

- , PDF page 8, Article: "The final dataset we highlight, with which several of the UIP models have been trained, is the MPtrj dataset23. This dataset was curated from the earlier v.2021.11.10 MP release. The MPtrj dataset is a proper subset of the allowed training data but several potentially anomalous examples from within MP were cleaned out of the dataset before the frames were subsampled to remove redundant frames."
- , PDF page 4: "Additionally, we also investigated the suitability of ct-UAE on energy-conserving interatomic potential (IAP) models, which are trained based on the MPtrj dataset50."
- , PDF page 4, Foundation model benchmark: "We trained a foundation model for all the periodic table elements up to Pu using the MPtrj dataset16 following our framework (our model), as described in the Methods section."
- , PDF page 9, Methods: "To train the foundation equivariance neural network potential, we used the MPtrj dataset16 sourced from Materials Projects48 as the training dataset. All configurations were calculated using DFT with the PBE82/PBE + U83 exchange-correlation functional and pseudopotential basis."
- , PDF page 9, Methods: "To train the foundation equivariance neural network potential, we used the MPtrj dataset16 sourced from Materials Projects48 as the training dataset. All configurations were calculated using DFT with the PBE82/PBE + U83 exchange-correlation functional and pseudopotential basis."
