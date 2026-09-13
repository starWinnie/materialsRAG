# Dataset: Materials Project (2018.6.1)

- Dataset ID: `D_materials_project_2018_6_1`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Materials Project (2018.6.1)
- MP
- MP44
- MP dataset

## Observed material scopes

- crystals

## Observed research tasks

- Generate universal atomic embeddings (UAEs) for crystal property prediction

## Observed research stages

- data_acquisition
- model_evaluation
- candidate_screening
- computational_validation

## Observed properties

- formation energy
- bandgap
- total energy
- total magnetization

## Observed fields

- CIF files
- atomic species
- atomic coordinates
- PBE bandgap
- formation energy

## Usage evidence

- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): source in Acquire crystal structure datasets — Source dataset for acquiring crystal structure and property data for training and evaluation
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): test in Evaluate ct-UAE transfer performance on back-end models — Evaluating ct-UAE transfer performance on back-end models (CGCNN, MEGNET, ALIGNN) for formation energy and bandgap prediction
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): computational_validation in Screen optimal clustering configuration for interpretability — Computational validation of ct-UAE interpretability via clustering analysis on oxide compounds
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): label_source in Validate ct-UAE physical interpretability via reverse prediction — Providing elemental properties (atomic radius, boiling temperature, etc.) for reverse prediction to validate physical interpretability of ct-UAEs

## Dataset evidence

- P006, PDF page 2: "To examine the atomic embeddings tensors obtained from different models, we used MP and MP* dataset for formation energy (Ef) and PBE bandgap (Eg), which are key properties for evaluating their chemical stabilities and electronic performances. MP stands for the 2018.6.1 version for MP44 dataset, which contains 69,239 materials with properties."
