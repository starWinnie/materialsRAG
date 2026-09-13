# Dataset: Materials Project database (as of November 1, 2022)

- Dataset ID: `D_materials_project_database_as_of_november_1_2022`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Materials Project database (as of November 1, 2022)
- Materials Project database
- Materials Project

## Observed material scopes

- crystalline materials
- crystals

## Observed research tasks

- predicting the properties of crystalline materials using large language models

## Observed research stages

- data_acquisition
- data_preparation
- label_generation

## Observed properties

- band gap
- formation energy per atom
- energy above hull
- unit cell volume
- energy per atom
- whether the band gap is direct or indirect

## Observed fields

- crystal structure (CIF)
- property labels

## Usage evidence

- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): source in collecting dataset from Materials Project database — Acquire crystal structure-description pairs and associated property labels.
- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): source in generating crystal text descriptions using Robocrystallographer — Generate crystal text descriptions using Robocrystallographer.
- P009 (LLM-Prop: predicting the properties of crystalline materials using large language models): label_source in obtaining property labels from Materials Project — Extract ground-truth numerical and categorical property values for training and evaluation.

## Dataset evidence

- P009, PDF page 4, Data collection and analysis: "We collected the dataset used in this work from the Materials Project database40 using the Materials Project free API as of November 1, 2022. We focus on six crystal properties that include both regression and classification tasks and are diverse enough to evaluate the capabilities of any property predictor. We collect the data of band gap, formation energy per atom (FEPA), energy above hull (Ehull), crystal volume, energy per atom (EPA), and an indicator of whether the band gap is direct or indirect (Is-gap-direct)."
