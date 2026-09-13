# Dataset Use: OpenKIM IP Repository

- DatasetUse ID: `DU_openkim_ip_repository`
- Dataset: OpenKIM IP Repository (`D_openkim_ip_repository`)
- Papers: P014
- Usage records: 8

## Usage roles

- source
- screening
- training
- candidate_pool
- validation

## Purposes

- Source of 178 interatomic potentials and precomputed small-scale indicator properties for data acquisition.
- Screening IPs for numerical instabilities and anomalous crystal response by analyzing MD simulation outputs and crystal response behavior.
- Filtering unreliable or missing small-scale indicator properties from the 163 × 62 property table.
- Providing the 163 × 35 dataset of small-scale indicator properties for k-nearest neighbors imputation to create a complete training set.
- Serving as the base pool for developing four new vacancy-related indicator properties via new Open-KIM test drivers.
- Providing the 153 × 39 candidate indicator properties for repeated k-fold cross-validation to select top-performing predictor combinations.
- Training the multi-linear regression model on the three selected predictors: {111} surface energy, lattice constant, and vacancy migration energy.
- Enabling leave-one-out cross-validation to estimate prediction error by fitting 153 regression models, each trained on 152 IPs and validated on the left-out IP.

## Used fields

- interatomic potential (IP)
- material species
- plastic flow strength
- small-scale indicator properties (62 initially considered)
- MD simulation output
- crystal response behavior
- small-scale indicator properties
- {111} surface energy
- lattice constant
- vacancy migration energy

## Construction methods

- k-nearest neighbors imputation
- development of new Open-KIM property calculations (KIM test drivers)

## Filter conditions

- numerical instabilities
- crystal rotation
- phase transformations
- amorphous phase formation
- voids
- missing values
- out-of-bounds values
- unreliable values

## Sample counts

- 153
- 163
- 178

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P014_01_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: collecting MD strength data and small-scale indicator properties from OpenKIM (`data_acquisition`, `S_P014_01`)
- Usage role: source
- Purpose: Source of 178 interatomic potentials and precomputed small-scale indicator properties for data acquisition.
- Used fields: interatomic potential (IP), material species, plastic flow strength, small-scale indicator properties (62 initially considered)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 178
- Confidence: 1.0

Evidence:
- P014, PDF page 1: "Here we explore covariance between predictions of metal plasticity, from 178 large-scale (~108 atoms) molecular dynamics (MD) simulations, and a variety of indicator properties computed at small-scales (≤102 atoms). All simulations use the same 178 IPs."
- P014, PDF page 2, Results and discussion: "The IPs used are available in the OpenKIM repository at https://openkim.org4 along with their predictions for a range of material properties computed using robust and vetted computational protocols."

### UR_P014_02_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: excluding IPs with numerical instabilities or anomalous crystal response (`candidate_screening`, `S_P014_02`)
- Usage role: screening
- Purpose: Screening IPs for numerical instabilities and anomalous crystal response by analyzing MD simulation outputs and crystal response behavior.
- Used fields: interatomic potential (IP), MD simulation output, crystal response behavior
- Filter conditions: numerical instabilities, crystal rotation, phase transformations, amorphous phase formation, voids
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P014, PDF page 2, Results and discussion: "MD simulations using one particular IP could not be completed due to numerical instabilities encountered irrespective of the integration time step. Another 14 IPs were excluded after subsequent analyzes revealed anomalies or irregularities in crystal response to straining, such as crystal rotation, phase transformations, and formation of amorphous phases, or voids..."

### UR_P014_03_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: excluding unreliable or missing small-scale indicator properties (`candidate_screening`, `S_P014_03`)
- Usage role: screening
- Purpose: Filtering unreliable or missing small-scale indicator properties from the 163 × 62 property table.
- Used fields: small-scale indicator properties
- Filter conditions: missing values, out-of-bounds values, unreliable values
- Construction method: Not stated
- Sample count: 163
- Confidence: 1.0

Evidence:
- P014, PDF page 2, Results and discussion: "At the same time, inspection of small-scale indicator properties of the remaining163IPs,precomputedintheOpenKIMrepository,revealedsome missing or out-of-bounds values deemed unreliable. Out of 62 initially considered indicators, 27 properties contained numerous missing or unreliable values and were excluded from our study altogether."

### UR_P014_04_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: imputing missing or unreasonable small-scale property values (`data_preparation`, `S_P014_04`)
- Usage role: training
- Purpose: Providing the 163 × 35 dataset of small-scale indicator properties for k-nearest neighbors imputation to create a complete training set.
- Used fields: small-scale indicator properties
- Filter conditions: Not stated
- Construction method: k-nearest neighbors imputation
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P014, PDF page 3: "Here we use data imputation to replace missing and unreasonable indicator values withinferredvalues,basedonak-nearestneighbors approach (see SI for details)."

### UR_P014_05_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: developing new vacancy-related indicator properties (`candidate_generation`, `S_P014_05`)
- Usage role: candidate_pool
- Purpose: Serving as the base pool for developing four new vacancy-related indicator properties via new Open-KIM test drivers.
- Used fields: interatomic potential (IP), material species
- Filter conditions: Not stated
- Construction method: development of new Open-KIM property calculations (KIM test drivers)
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P014, PDF page 4: "Following this logic, we developed new Open- KIM property calculations (KIM test drivers) for computing the vacancy formation energy (both relaxed and unrelaxed), the vacancy migration barrier, and the vacancy formation volume"

### UR_P014_06_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: selecting top-performing predictor combinations via k-fold cross-validation (`candidate_screening`, `S_P014_06`)
- Usage role: training
- Purpose: Providing the 153 × 39 candidate indicator properties for repeated k-fold cross-validation to select top-performing predictor combinations.
- Used fields: small-scale indicator properties
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P014, PDF page 4: "To select the most informative indicators, we use repeated k-fold cross-validation15toevaluateall9919regressionmodelsbuiltonone,two,andthree out of 39 candidate indicators (39 choose 1 + 39 choose 2 + 39 choose 3)."

### UR_P014_07_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: fitting multi-linear regression model on selected predictors (`model_training`, `S_P014_07`)
- Usage role: training
- Purpose: Training the multi-linear regression model on the three selected predictors: {111} surface energy, lattice constant, and vacancy migration energy.
- Used fields: {111} surface energy, lattice constant, vacancy migration energy, plastic flow strength
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 153
- Confidence: 1.0

Evidence:
- P014, PDF page 5: "Figure 4b presents one of the best 3-variable regression models (see the ﬁgure caption for details), ﬁt the 153 samples remaining in the statistical pool with the adjusted goodness of ﬁt parameter r2 = 0.88."

### UR_P014_08_openkim_ip_repository

- Paper: `P014` — Cross-scale covariance for material property prediction
- Task: predicting plastic flow strength from small-scale indicator properties (`T_P014_01`)
- Stage: estimating prediction error using leave-one-out cross-validation (`model_evaluation`, `S_P014_08`)
- Usage role: validation
- Purpose: Enabling leave-one-out cross-validation to estimate prediction error by fitting 153 regression models, each trained on 152 IPs and validated on the left-out IP.
- Used fields: {111} surface energy, lattice constant, vacancy migration energy, plastic flow strength
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 153
- Confidence: 1.0

Evidence:
- P014, PDF page 5: "Here, we ﬁt 153 regression models on the same three predictors, leaving out one of the 153 IP samples from each model for validation. As an estimate of the prediction error by regression on DFT predictors, the average relative prediction error among 153 leave-one-out models is 15%."

## Aggregated evidence

- , PDF page 1: "Here we explore covariance between predictions of metal plasticity, from 178 large-scale (~108 atoms) molecular dynamics (MD) simulations, and a variety of indicator properties computed at small-scales (≤102 atoms). All simulations use the same 178 IPs."
- , PDF page 2, Results and discussion: "The IPs used are available in the OpenKIM repository at https://openkim.org4 along with their predictions for a range of material properties computed using robust and vetted computational protocols."
- , PDF page 2, Results and discussion: "MD simulations using one particular IP could not be completed due to numerical instabilities encountered irrespective of the integration time step. Another 14 IPs were excluded after subsequent analyzes revealed anomalies or irregularities in crystal response to straining, such as crystal rotation, phase transformations, and formation of amorphous phases, or voids..."
- , PDF page 2, Results and discussion: "At the same time, inspection of small-scale indicator properties of the remaining163IPs,precomputedintheOpenKIMrepository,revealedsome missing or out-of-bounds values deemed unreliable. Out of 62 initially considered indicators, 27 properties contained numerous missing or unreliable values and were excluded from our study altogether."
- , PDF page 3: "Here we use data imputation to replace missing and unreasonable indicator values withinferredvalues,basedonak-nearestneighbors approach (see SI for details)."
- , PDF page 4: "Following this logic, we developed new Open- KIM property calculations (KIM test drivers) for computing the vacancy formation energy (both relaxed and unrelaxed), the vacancy migration barrier, and the vacancy formation volume"
- , PDF page 4: "To select the most informative indicators, we use repeated k-fold cross-validation15toevaluateall9919regressionmodelsbuiltonone,two,andthree out of 39 candidate indicators (39 choose 1 + 39 choose 2 + 39 choose 3)."
- , PDF page 5: "Figure 4b presents one of the best 3-variable regression models (see the ﬁgure caption for details), ﬁt the 153 samples remaining in the statistical pool with the adjusted goodness of ﬁt parameter r2 = 0.88."
- , PDF page 5: "Here, we ﬁt 153 regression models on the same three predictors, leaving out one of the 153 IP samples from each model for validation. As an estimate of the prediction error by regression on DFT predictors, the average relative prediction error among 153 leave-one-out models is 15%."
