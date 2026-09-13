# Dataset: OpenKIM IP Repository

- Dataset ID: `D_openkim_ip_repository`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- OpenKIM IP Repository
- OpenKIM repository

## Observed material scopes

- FCC metals

## Observed research tasks

- predicting plastic flow strength from small-scale indicator properties

## Observed research stages

- data_acquisition
- candidate_screening
- data_preparation
- candidate_generation
- model_training
- model_evaluation

## Observed properties

- plastic flow strength
- elastic constants
- surface energies
- vacancy formation energy
- vacancy migration barrier
- vacancy formation volume
- unstable stacking fault energy
- intrinsic stacking fault energy
- cohesive energy
- lattice constant
- thermal expansion coefficient

## Observed fields

- interatomic potential (IP)
- material species
- property value
- computational protocol
- uncertainty flag

## Usage evidence

- P014 (Cross-scale covariance for material property prediction): source in collecting MD strength data and small-scale indicator properties from OpenKIM — Source of 178 interatomic potentials and precomputed small-scale indicator properties for data acquisition.
- P014 (Cross-scale covariance for material property prediction): screening in excluding IPs with numerical instabilities or anomalous crystal response — Screening IPs for numerical instabilities and anomalous crystal response by analyzing MD simulation outputs and crystal response behavior.
- P014 (Cross-scale covariance for material property prediction): screening in excluding unreliable or missing small-scale indicator properties — Filtering unreliable or missing small-scale indicator properties from the 163 × 62 property table.
- P014 (Cross-scale covariance for material property prediction): training in imputing missing or unreasonable small-scale property values — Providing the 163 × 35 dataset of small-scale indicator properties for k-nearest neighbors imputation to create a complete training set.
- P014 (Cross-scale covariance for material property prediction): candidate_pool in developing new vacancy-related indicator properties — Serving as the base pool for developing four new vacancy-related indicator properties via new Open-KIM test drivers.
- P014 (Cross-scale covariance for material property prediction): training in selecting top-performing predictor combinations via k-fold cross-validation — Providing the 153 × 39 candidate indicator properties for repeated k-fold cross-validation to select top-performing predictor combinations.
- P014 (Cross-scale covariance for material property prediction): training in fitting multi-linear regression model on selected predictors — Training the multi-linear regression model on the three selected predictors: {111} surface energy, lattice constant, and vacancy migration energy.
- P014 (Cross-scale covariance for material property prediction): validation in estimating prediction error using leave-one-out cross-validation — Enabling leave-one-out cross-validation to estimate prediction error by fitting 153 regression models, each trained on 152 IPs and validated on the left-out IP.

## Dataset evidence

- P014, PDF page 2, Results and discussion: "The IPs used are available in the OpenKIM repository at https://openkim.org4 along with their predictions for a range of material properties computed using robust and vetted computational protocols."
- P014, PDF page 6, Methods: "OpenKIM4,17 (Open Knowledgebase of Interatomic Models) is a multi-faceted cyberinfrastructure project founded in 2009. All content on OpenKIM is publicly available at https://openkim.org. The components of OpenKIM enabling the present work are the IP repository, the KIM API, and the automatic property testing framework."
