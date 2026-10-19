# Dataset: multi-temperature non-crystalline database

- Dataset ID: `D_P105_multi_temperature_non_crystalline_database`
- Dataset type: `derived_subset`
- Source dataset: `D_P105_5000k_non_crystalline_database`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- multi-temperature non-crystalline database

## Observed material scopes

- non-crystalline inorganic materials
- amorphous materials
- liquid
- supercooled liquid
- glass

## Observed research tasks

- predict Li-ion diffusivity in non-crystalline materials

## Observed research stages

- label_generation
- model_training
- model_evaluation
- computational_validation

## Observed properties

- Li-ion diffusivity
- activation energy (Ea) for Li diffusion
- radial distribution functions (RDFs)

## Observed fields

- composition
- temperature
- structure
- RDFs

## Usage evidence

- P048 (The ab initio non-crystalline structure database: empowering machine learning to decode diffusivity): label_source in calculate Li-ion diffusivity and activation energy from AIMD trajectories — Calculate Li-ion diffusivity (D_Li) and activation energy (Ea) from AIMD simulation trajectories.
- P048 (The ab initio non-crystalline structure database: empowering machine learning to decode diffusivity): training in train machine learning models (RF, XGBoost, SISSO) on diffusivity data — Train machine learning models (RF, XGBoost, SISSO) to predict Li-ion diffusivity and activation energy. / Validate machine learning models during training using cross-validation.
- P048 (The ab initio non-crystalline structure database: empowering machine learning to decode diffusivity): test in evaluate ML model performance using parity plots and error metrics — Evaluate final ML model performance using parity plots and error metrics.
- P048 (The ab initio non-crystalline structure database: empowering machine learning to decode diffusivity): computational_validation in validate universal ML potentials (M3GNet) for structure generation — Validate universal ML potentials (M3GNet) by comparing RDFs and structure features against AIMD-calculated references.

## Dataset evidence

- P105, PDF page 9, Methods: "The last snapshot structure from the 5000K run is used as the input structure for MPMorph workflow at 1000K, 1500K, 2000K, and 2500K to generate the multi-temperature non-crystalline database."
