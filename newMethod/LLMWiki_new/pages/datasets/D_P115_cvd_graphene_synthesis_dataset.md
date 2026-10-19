# Dataset: CVD graphene synthesis dataset

- Dataset ID: `D_P115_cvd_graphene_synthesis_dataset`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- CVD graphene synthesis dataset
- CVD graphene dataset
- graphene CVD growth dataset

## Observed material scopes

- graphene

## Observed research tasks

- graphene layer number classification

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation

## Observed properties

- number of graphene layers
- pressure
- temperature
- growth time
- substrate
- precursor flow rates

## Observed fields

- CVD method
- Pressure (mbar)
- Temperature (°C)
- Growth time (min)
- Substrate
- No. of layers
- CH4 flow rate
- C2H4 flow rate
- C2H2 flow rate
- H2 flow rate

## Usage evidence

- P058 (Leveraging large language models to address data scarcity in machine learning for graphene synthesis): source in manual curation of CVD graphene literature data — Manual curation of CVD graphene literature data to collect a small dataset for CVD graphene synthesis
- P058 (Leveraging large language models to address data scarcity in machine learning for graphene synthesis): training in imputation of missing attributes — Imputation of missing attributes using statistical and LLM-based methods
- P058 (Leveraging large language models to address data scarcity in machine learning for graphene synthesis): training in feature engineering of substrate attribute — Feature engineering of substrate attribute using LLM text embeddings
- P058 (Leveraging large language models to address data scarcity in machine learning for graphene synthesis): training in discretization of feature space — Discretization of feature space for continuous attributes
- P058 (Leveraging large language models to address data scarcity in machine learning for graphene synthesis): training in training SVM classifier on processed data — Training SVM classifier on imputed, feature-engineered, and discretized data
- P058 (Leveraging large language models to address data scarcity in machine learning for graphene synthesis): test in evaluation of classification performance — Evaluation of SVM classifier performance using accuracy, AUROC, and cross-validation scores

## Dataset evidence

- P115, PDF page 2, Methodology: "Experimental CVD graphene literature is used to manually extract 164 data entries [39,71–78], each consisting of ten attributes."
- P115, PDF page 2, Methodology: "The dataset contains missing values for pressure, growth time, number of layers, and nearly all precursor flow rates."
- P115, PDF page 2, Methodology: "The CVD synthesis parameters reported for each data entry are presented in the supplementary file, graphene_growth_conditions_layers.csv."
- P115, PDF page 1, Introduction: "Dataset link: https://github.com/kadkhodaei-research-group/GScarceLLM.git"
