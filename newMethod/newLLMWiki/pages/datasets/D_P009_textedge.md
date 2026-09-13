# Dataset: TextEdge

- Dataset ID: `D_P009_textedge`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- TextEdge
- benchmark dataset
- curated dataset

## Observed material scopes

- crystalline materials

## Observed research tasks

- predicting the properties of crystalline materials

## Observed research stages

- data_preparation
- model_training
- model_evaluation

## Observed properties

- band gap
- formation energy per atom
- energy above hull
- crystal volume
- energy per atom
- Is-gap-direct

## Observed fields

- crystal text description
- ID
- structural information
- structure text description

## Usage evidence

- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): source in generating crystal text descriptions using Robocrystallographer — Generate crystal text descriptions using Robocrystallographer
- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): training in fine-tuning T5 encoder for property prediction — Train LLM-Prop model on preprocessed text descriptions to predict crystal properties / Validate LLM-Prop model during training
- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): test in evaluating performance against baselines — Evaluate LLM-Prop's performance against baselines on held-out test set

## Dataset evidence

- P009, PDF page 1: "In this paper, we develop and make public a benchmark dataset (TextEdge) that contains crystal text descriptions with their properties."
- P009, PDF page 2, Results: "We release to the public the curated dataset we used as a benchmark, called TextEdge, to accelerate natural language processing (NLP) for materials science research."
- P009, PDF page 11, Data availability: "The benchmark dataset collected in this work and the checkpoints of the LLM-Prop model for the three properties studied can be accessed at https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG?ths=true."
