# Dataset: Experimental ABX3-type perovskite bandgap dataset (227 samples)

- Dataset ID: `D_experimental_abx3_type_perovskite_bandgap_dataset_227_samples`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Experimental ABX3-type perovskite bandgap dataset (227 samples)
- 227 sets of experimental bandgap data of perovskites
- experimental bandgap data
- ABX3-type perovskites database
- BPM-ABX3-type perovskites

## Observed material scopes

- ABX3-type perovskites

## Observed research tasks

- bandgap prediction of ABX3-type perovskites

## Observed research stages

- data_acquisition
- data_preparation
- candidate_generation
- experimental_validation
- label_generation

## Observed properties

- bandgap

## Observed fields

- chemical composition
- bandgap

## Usage evidence

- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): source in collection of experimental bandgap data — Source of experimental bandgap measurements for constructing the primary perovskite database
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): training in database establishment and cleaning — Training dataset after cleaning (204 samples) for initial BPM development / Test dataset (23 samples) for evaluating initial BPM performance
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): candidate_pool in generation of 24 candidate bandgap prediction models — Base pool from which four specialized subsets (ABX3, all-inorganic, hybrid, tin-free) were derived for candidate model generation
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): experimental_validation in validation via synthesis and optical measurement of new perovskite — Reference experimental bandgap for validating prediction on newly synthesized Cs0.05(FA0.85MA0.15)0.95Pb(I0.85Br0.15)3
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): label_source in SHAP-based interpretation of feature contributions to bandgap — Source of bandgap labels for SHAP-based interpretation of feature contributions

## Dataset evidence

- P033, PDF page 1, ABSTRACT: "we collect 227 sets of experimental bandgap data of perovskites from the latest 1254 publications"
- P033, PDF page 2, Build model: "The first step is to search articles by using the keyword “perovskite bandgap” in the web of science according to relevance, and then download them in ACS, nature, science, wiley, Elsevier and other."
