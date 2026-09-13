# Dataset: TextEdge

- Dataset ID: `D_P009_textedge`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project_database_as_of_november_1_2022`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- TextEdge
- benchmark dataset (TextEdge)

## Observed material scopes

- crystalline materials
- crystals

## Observed research tasks

- predicting the properties of crystalline materials using large language models

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
- property labels

## Usage evidence

- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): training in fine-tuning T5 encoder with linear prediction head — Fine-tune T5 encoder with linear prediction head on preprocessed text inputs to regress/classify crystal properties.
- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): test in evaluating performance on test set across six properties — Evaluate predictive accuracy of LLM-Prop against baselines using MAE (regression) and AUC (classification).

## Dataset evidence

- P009, PDF page 1: "In this paper, we develop and make public a benchmark dataset (TextEdge) that contains crystal text descriptions with their properties."
- P009, PDF page 4, Data collection and analysis: "We generated the crystal text descriptions using Robocrystallographer41, a tool that generates a deterministic human readable text description of a structure given its CIF file."
