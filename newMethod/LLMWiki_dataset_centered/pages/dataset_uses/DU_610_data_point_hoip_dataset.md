# Dataset Use: 610-data-point HOIP dataset

- DatasetUse ID: `DU_610_data_point_hoip_dataset`
- Dataset: 610-data-point HOIP dataset (`D_610_data_point_hoip_dataset`)
- Papers: P036
- Usage records: 9

## Usage roles

- training
- label_source
- candidate_pool
- test

## Purposes

- primary dataset used for model training and evaluation after cleaning and conflict resolution
- partitioned into training and test sets for model development and evaluation
- source of experimental band gap labels resolved from literature reports
- source of elemental descriptors for feature engineering and physical feature pool construction
- used to perform correlation filtering and GBRT-based feature importance ranking for subfeature selection
- training set (85% of 610 data points) used to train the GBRT-P model
- test set (15% of 610 data points) used to evaluate GBRT-P model performance
- training set used to train the GASR model to discover mathematical formulas mapping physical features to band gap
- test set used to evaluate RMSE and complexity of 260 GASR-generated formulas

## Used fields

- composition
- experimental band gap value
- 7 physical features

## Construction methods

- selection of ABX3-structured HOIPs from PSC database; resolution of conflicting band gap reports via averaging (if Δ < 0.2 eV) or model selection (if Δ > 0.2 eV)
- random split
- conflict resolution via averaging or model selection based on experimental error tolerance
- extraction of elemental characteristics (e.g., electronegativity, ionic radius) from composition to construct nine base descriptors
- feature importance evaluation using GBRT algorithm on subsets of features
- random split of hoip_610_dataset
- feature engineering applied to hoip_610_dataset to extract 7 selected physical features

## Filter conditions

- ABX3 structure (A = Cs, FA, or MA; B = Pb or Sn; X = Br, Cl, or I)
- band gap conflict resolution rule
- same composition with differing band gap reports

## Sample counts

- 610

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

0.95

## Usage records

### UR_P036_01_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: data collection and cleaning (`data_acquisition`, `S_P036_01`)
- Usage role: training
- Purpose: primary dataset used for model training and evaluation after cleaning and conflict resolution
- Used fields: composition, experimental band gap value
- Filter conditions: ABX3 structure (A = Cs, FA, or MA; B = Pb or Sn; X = Br, Cl, or I), band gap conflict resolution rule
- Construction method: selection of ABX3-structured HOIPs from PSC database; resolution of conflicting band gap reports via averaging (if Δ < 0.2 eV) or model selection (if Δ > 0.2 eV)
- Sample count: 610
- Confidence: 1.0

Evidence:
- P036, PDF page 3, METHODS: "To ensure the quantity and accuracy of the data, two principles were used in the data collection and cleaning process. First, we selected compounds with a three-dimensional structure of ABX3 (A-site = Cs, FA, or MA; B-site = Pb or Sn; X-site = Br, Cl, or I). Second, for data with the same composition but different band gaps, we chose the average value when the difference between the maximum value and the minimum value is less than 0.2 eV. When it is greater than 0.2 eV, we chose the model because the experimental error is about 0.1−0.2 eV when using different instruments. All data points were collated from the PSC database built by Jacobsson et al.16 Eventually, the total data set consists of 610 data points with known band gap values."

### UR_P036_02_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: data splitting and distribution validation (`data_preparation`, `S_P036_02`)
- Usage role: training
- Purpose: partitioned into training and test sets for model development and evaluation
- Used fields: composition, experimental band gap value
- Filter conditions: Not stated
- Construction method: random split
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P036, PDF page 3, METHODS: "Then, we randomly divided 15% of the data set as the test set to evaluate the generalization capability for all ML models, and the remaining 85% as the training set to train all ML models."

### UR_P036_03_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: band gap labeling (`label_generation`, `S_P036_03`)
- Usage role: label_source
- Purpose: source of experimental band gap labels resolved from literature reports
- Used fields: experimental band gap value
- Filter conditions: same composition with differing band gap reports
- Construction method: conflict resolution via averaging or model selection based on experimental error tolerance
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P036, PDF page 3, METHODS: "Second, for data with the same composition but different band gaps, we chose the average value when the difference between the maximum value and the minimum value is less than 0.2 eV. When it is greater than 0.2 eV, we chose the model because the experimental error is about 0.1−0.2 eV when using different instruments."

### UR_P036_04_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: feature engineering and physical feature pool construction (`candidate_generation`, `S_P036_04`)
- Usage role: candidate_pool
- Purpose: source of elemental descriptors for feature engineering and physical feature pool construction
- Used fields: composition
- Filter conditions: Not stated
- Construction method: extraction of elemental characteristics (e.g., electronegativity, ionic radius) from composition to construct nine base descriptors
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P036, PDF page 3, METHODS: "In this work, we chose nine element characteristics as descriptors in the initial feature pool based on a priori knowledge, including Pauling’s electronegativity (χ), μ, τ, IR, electron affinity (EA), dipole polarizability (DP), atomic radius (AR), and the number of electrons on d and f orbitals."

### UR_P036_05_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: feature selection via correlation filtering and importance ranking (`candidate_screening`, `S_P036_05`)
- Usage role: training
- Purpose: used to perform correlation filtering and GBRT-based feature importance ranking for subfeature selection
- Used fields: composition, experimental band gap value
- Filter conditions: Not stated
- Construction method: feature importance evaluation using GBRT algorithm on subsets of features
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P036, PDF page 4, METHODS: "To further remove the redundant feature to avoid dimensional disasters, we then used the GBRT algorithm to evaluate the accuracy of the model using different subfeatures, the subfeatures selected each time are in a decreasing order of feature importance, and the RMSEs of training and test sets are used as the evaluation metric ... we chose the top 7 features in ranked feature importance as input variables"

### UR_P036_06_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: GBRT-P model training (`model_training`, `S_P036_06`)
- Usage role: training
- Purpose: training set (85% of 610 data points) used to train the GBRT-P model
- Used fields: composition, experimental band gap value
- Filter conditions: Not stated
- Construction method: random split of hoip_610_dataset
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P036, PDF page 3, METHODS: "Then, we randomly divided 15% of the data set as the test set to evaluate the generalization capability for all ML models, and the remaining 85% as the training set to train all ML models."

### UR_P036_07_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: GBRT-P model evaluation (`model_evaluation`, `S_P036_07`)
- Usage role: test
- Purpose: test set (15% of 610 data points) used to evaluate GBRT-P model performance
- Used fields: composition, experimental band gap value
- Filter conditions: Not stated
- Construction method: random split of hoip_610_dataset
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P036, PDF page 3, METHODS: "Then, we randomly divided 15% of the data set as the test set to evaluate the generalization capability for all ML models, and the remaining 85% as the training set to train all ML models."

### UR_P036_09_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: GASR model training (`model_training`, `S_P036_09`)
- Usage role: training
- Purpose: training set used to train the GASR model to discover mathematical formulas mapping physical features to band gap
- Used fields: 7 physical features, experimental band gap value
- Filter conditions: Not stated
- Construction method: feature engineering applied to hoip_610_dataset to extract 7 selected physical features
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P036, PDF page 5, METHODS: "To explicitly obtain the mapping between physical features and the band gap, we used the GASR algorithm to develop mathematical formulas between 7 features and band gaps."

### UR_P036_10_610_data_point_hoip_dataset

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: GASR formula evaluation (`model_evaluation`, `S_P036_10`)
- Usage role: test
- Purpose: test set used to evaluate RMSE and complexity of 260 GASR-generated formulas
- Used fields: 7 physical features, experimental band gap value
- Filter conditions: Not stated
- Construction method: feature engineering applied to hoip_610_dataset to extract 7 selected physical features
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P036, PDF page 7, RESULTS AND DISCUSSION: "Table 2 gives the mathematical formulas with the lowest RMSE of test at each complexity among the 260 formulas generated by the GASR algorithm, the best of which is eq 2, with an RMSE of test set for 0.084 eV and complexity of 3"

## Aggregated evidence

- , PDF page 3, METHODS: "To ensure the quantity and accuracy of the data, two principles were used in the data collection and cleaning process. First, we selected compounds with a three-dimensional structure of ABX3 (A-site = Cs, FA, or MA; B-site = Pb or Sn; X-site = Br, Cl, or I). Second, for data with the same composition but different band gaps, we chose the average value when the difference between the maximum value and the minimum value is less than 0.2 eV. When it is greater than 0.2 eV, we chose the model because the experimental error is about 0.1−0.2 eV when using different instruments. All data points were collated from the PSC database built by Jacobsson et al.16 Eventually, the total data set consists of 610 data points with known band gap values."
- , PDF page 3, METHODS: "Then, we randomly divided 15% of the data set as the test set to evaluate the generalization capability for all ML models, and the remaining 85% as the training set to train all ML models."
- , PDF page 3, METHODS: "Second, for data with the same composition but different band gaps, we chose the average value when the difference between the maximum value and the minimum value is less than 0.2 eV. When it is greater than 0.2 eV, we chose the model because the experimental error is about 0.1−0.2 eV when using different instruments."
- , PDF page 3, METHODS: "In this work, we chose nine element characteristics as descriptors in the initial feature pool based on a priori knowledge, including Pauling’s electronegativity (χ), μ, τ, IR, electron affinity (EA), dipole polarizability (DP), atomic radius (AR), and the number of electrons on d and f orbitals."
- , PDF page 4, METHODS: "To further remove the redundant feature to avoid dimensional disasters, we then used the GBRT algorithm to evaluate the accuracy of the model using different subfeatures, the subfeatures selected each time are in a decreasing order of feature importance, and the RMSEs of training and test sets are used as the evaluation metric ... we chose the top 7 features in ranked feature importance as input variables"
- , PDF page 3, METHODS: "Then, we randomly divided 15% of the data set as the test set to evaluate the generalization capability for all ML models, and the remaining 85% as the training set to train all ML models."
- , PDF page 3, METHODS: "Then, we randomly divided 15% of the data set as the test set to evaluate the generalization capability for all ML models, and the remaining 85% as the training set to train all ML models."
- , PDF page 5, METHODS: "To explicitly obtain the mapping between physical features and the band gap, we used the GASR algorithm to develop mathematical formulas between 7 features and band gaps."
- , PDF page 7, RESULTS AND DISCUSSION: "Table 2 gives the mathematical formulas with the lowest RMSE of test at each complexity among the 260 formulas generated by the GASR algorithm, the best of which is eq 2, with an RMSE of test set for 0.084 eV and complexity of 3"
