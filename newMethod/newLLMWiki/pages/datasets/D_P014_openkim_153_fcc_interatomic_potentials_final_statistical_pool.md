# Dataset: OpenKIM 153 FCC Interatomic Potentials (final statistical pool)

- Dataset ID: `D_P014_openkim_153_fcc_interatomic_potentials_final_statistical_pool`
- Dataset type: `derived_subset`
- Source dataset: `D_P014_openkim_163_fcc_interatomic_potentials_screened`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- OpenKIM 153 FCC Interatomic Potentials (final statistical pool)
- 153 IPs
- 153 IP models
- statistical pool of 153 IP models

## Observed material scopes

- FCC metals

## Observed research tasks

- predicting plastic flow strength from small-scale indicator properties

## Observed research stages

- candidate_generation
- model_training
- model_evaluation

## Observed properties

- plastic flow strength (MD)
- small-scale indicator properties

## Observed fields

- IP identifier
- metal species
- plastic flow strength
- C44
- rVFPE
- uSFE
- iSFE
- SE 111 FCC
- lattice constant
- vacancy migration energy
- relaxed vacancy formation energy
- unrelaxed vacancy formation energy
- vacancy formation volume

## Usage evidence

- P014 (Cross-scale covariance for material property prediction): candidate_pool in developing new vacancy-related indicator properties — Serve as basis for developing new vacancy-related indicator properties
- P014 (Cross-scale covariance for material property prediction): training in training multi-linear regression models on indicator properties — Train multi-linear regression models relating plastic flow strength to small-scale indicator properties
- P014 (Cross-scale covariance for material property prediction): validation in evaluating regression model performance with cross-validation — Evaluate regression model performance using leave-one-out cross-validation

## Dataset evidence

- P014, PDF page 4, unknown: "Of the 16 models that were identified as SF jammed, six had been previously excluded from the statistical pool based on other considerations. Outliers or not, we excluded all SF jammed IPs from further statistical analyses on the grounds that they exhibit a plastic response qualitatively different from the rest of the remaining IP models, thus paring our statistical pool down to 153 IP models (see SI for details)."
