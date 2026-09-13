# Dataset: Experimental ABX3-type perovskite bandgap dataset

- Dataset ID: `D_P033_experimental_abx3_type_perovskite_bandgap_dataset`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Experimental ABX3-type perovskite bandgap dataset
- 227 sets of experimental bandgap data of perovskites
- 227 data points of experimental values
- experimental data derived from experimental reports

## Observed material scopes

- ABX3-type perovskites

## Observed research tasks

- bandgap prediction of ABX3-type perovskites

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation
- computational_validation
- experimental_validation
- candidate_screening

## Observed properties

- bandgap

## Observed fields

- chemical composition
- bandgap

## Usage evidence

- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): source in search and collection of experimental bandgap data — Source of experimental bandgap data for building the perovskite database
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): training in database establishment and cleaning — Training dataset after cleaning and splitting / Test dataset after cleaning and splitting
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): training in training of bandgap prediction models — Training input for multiple ML models (LR, KNN, SVR, RF, MLP, Xgboost)
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): test in evaluation of bandgap prediction models — Test input for evaluating model performance (RMSE, r)
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): computational_validation in validation against DFT calculations — Reference for comparison between ML predictions and DFT calculations on new compositions
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): experimental_validation in experimental validation of ML predictions — Reference for experimental validation of ML prediction on synthesized Cs0.05(FA0.85MA0.15)0.95Pb(I0.85Br0.15)3
- P033 (Study on bandgap predications of ABX3-type perovskites by machine learning): screening in screening of chemical composition effects using SHAP — Input for SHAP-based feature importance analysis to identify key chemical components influencing bandgap

## Dataset evidence

- P033, PDF page 1, A B S T R A C T: "The present work adopts machine learning (ML) to predict bandgaps of perovskites, where we collect 227 sets of experimental bandgap data of perovskites from the latest 1254 publications, to establish and identify 4 models from 24 kinds of ML models."
- P033, PDF page 2, Build model: "In our work, the use of the experimental data derived from experimental reports (227 data points of experimental values collected from 1254 published papers) ensures that our BPMs is more realistic."
