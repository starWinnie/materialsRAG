# Dataset: HOIP experimental band gap dataset

- Dataset ID: `D_P036_hoip_experimental_band_gap_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_psc_database`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- HOIP experimental band gap dataset
- total data set
- data set consisting of HOIPs’ experimental band gaps
- 610 data points with known band gap values

## Observed material scopes

- hybrid organic−inorganic perovskites (HOIPs)
- ABX3 (A = Cs, formamidinium (FA), or methylammonium (MA); B = Pb or Sn; X = Br, Cl, or I)

## Observed research tasks

- predicting the experimental band gap values of HOIPs

## Observed research stages

- data_acquisition
- data_preparation
- candidate_generation
- candidate_screening
- experimental_validation

## Observed properties

- experimental band gap

## Observed fields

- composition
- experimental band gap

## Usage evidence

- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): training in data collection and cleaning — primary dataset used for ML model training and evaluation
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): training in data partitioning — to train all ML models / to evaluate the generalization capability for all ML models
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): candidate_pool in composition screening — to define the feature space for virtual composition screening
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): screening in selection of validation candidates — to identify compositions not present in original dataset for experimental synthesis
- P036 (Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning): computational_validation in experimental verification — to computationally validate predictions before experimental synthesis / to compare predicted band gaps against experimentally measured band gaps

## Dataset evidence

- P036, PDF page 3, METHODS: "Eventually, the total data set consists of 610 data points with known band gap values."
