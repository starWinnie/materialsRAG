# Dataset: 610-data-point HOIP dataset

- Dataset ID: `D_610_data_point_hoip_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_psc_database`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- 610-data-point HOIP dataset
- 610 data points
- 610-data-point dataset of HOIPs with known experimental band gaps
- total data set consists of 610 data points with known band gap values

## Observed material scopes

- hybrid organic−inorganic perovskites (HOIPs)
- ABX3 (A = Cs, FA, or MA; B = Pb or Sn; X = Br, Cl, or I)

## Observed research tasks

- predicting the experimental band gap values of HOIPs

## Observed research stages

- data_acquisition
- data_preparation
- label_generation
- candidate_generation
- candidate_screening
- model_training
- model_evaluation

## Observed properties

- experimental band gap

## Observed fields

- composition
- experimental band gap value

## Usage evidence

- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): training in data collection and cleaning — primary dataset used for model training and evaluation after cleaning and conflict resolution
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): training in data splitting and distribution validation — partitioned into training and test sets for model development and evaluation
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): label_source in band gap labeling — source of experimental band gap labels resolved from literature reports
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): candidate_pool in feature engineering and physical feature pool construction — source of elemental descriptors for feature engineering and physical feature pool construction
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): training in feature selection via correlation filtering and importance ranking — used to perform correlation filtering and GBRT-based feature importance ranking for subfeature selection
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): training in GBRT-P model training — training set (85% of 610 data points) used to train the GBRT-P model
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): test in GBRT-P model evaluation — test set (15% of 610 data points) used to evaluate GBRT-P model performance
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): training in GASR model training — training set used to train the GASR model to discover mathematical formulas mapping physical features to band gap
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): test in GASR formula evaluation — test set used to evaluate RMSE and complexity of 260 GASR-generated formulas

## Dataset evidence

- P036, PDF page 3, METHODS: "All data points were collated from the PSC database built by Jacobsson et al.16 Eventually, the total data set consists of 610 data points with known band gap values."
