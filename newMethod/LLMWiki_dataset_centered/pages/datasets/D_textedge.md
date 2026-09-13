# Dataset: TextEdge

- Dataset ID: `D_textedge`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- TextEdge
- benchmark dataset
- curated dataset
- benchmark text data

## Observed material scopes

- crystalline materials

## Observed research tasks

- predicting the properties of crystalline materials

## Observed research stages

- model_training
- model_evaluation

## Observed properties

- band gap
- formation energy per atom
- energy above hull
- unit cell volume
- energy per atom
- whether the band gap is direct or indirect

## Observed fields

- crystal text description
- crystal ID
- structural information
- property values

## Usage evidence

- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): training in fine-tuning T5 encoder on preprocessed text and property labels — fine-tune T5 encoder on preprocessed text and property labels
- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): test in evaluating prediction performance on test set using MAE and AUC — evaluate prediction performance on test set using MAE and AUC

## Dataset evidence

- P009, PDF page 1: "In this paper, we develop and make public a benchmark dataset (TextEdge) that contains crystal text descriptions with their properties."
- P009, PDF page 2, Results: "Finally, we release to the public the curated dataset we used as a benchmark, called TextEdge, to accelerate natural language processing (NLP) for materials science research."
- P009, PDF page 4, Data collection and analysis: "We focus on six crystal properties that include both regression and classification tasks and are diverse enough to evaluate the capabilities of any property predictor. We collect the data of band gap, formation energy per atom (FEPA), energy above hull (Ehull), crystal volume, energy per atom (EPA), and an indicator of whether the band gap is direct or indirect (Is-gap-direct)."
- P009, PDF page 4, Data collection and analysis: "The data originally contained 145,825 crystals structure-description pairs which we randomly split into 125,825 samples for the training set, 10,000 samples for the validation set and 10,000 samples for the test set."
