# Dataset Use: TextEdge

- DatasetUse ID: `DU_textedge`
- Dataset: TextEdge (`D_textedge`)
- Papers: P009
- Usage records: 2

## Usage roles

- training
- test

## Purposes

- fine-tune T5 encoder on preprocessed text and property labels
- evaluate prediction performance on test set using MAE and AUC

## Used fields

- crystal text description
- band gap
- formation energy per atom
- energy above hull
- crystal volume
- energy per atom
- Is-gap-direct

## Construction methods

- derived from Materials Project via Robocrystallographer text generation and preprocessing

## Filter conditions

- None stated

## Sample counts

- 10000

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P009_05_textedge

- Paper: `P009` — LLM-Prop: predicting the properties of crystalline materials using large language models
- Task: predicting the properties of crystalline materials (`T_P009_01`)
- Stage: fine-tuning T5 encoder on preprocessed text and property labels (`model_training`, `S_P009_05`)
- Usage role: training
- Purpose: fine-tune T5 encoder on preprocessed text and property labels
- Used fields: crystal text description, band gap, formation energy per atom, energy above hull, crystal volume, energy per atom, Is-gap-direct
- Filter conditions: Not stated
- Construction method: derived from Materials Project via Robocrystallographer text generation and preprocessing
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P009, PDF page 4, Data collection and analysis: "The data originally contained 145,825 crystals structure-description pairs which we randomly split into 125,825 samples for the training set, 10,000 samples for the validation set and 10,000 samples for the test set."
- P009, PDF page 4, Data collection and analysis: "The data originally contained 145,825 crystals structure-description pairs which we randomly split into 125,825 samples for the training set, 10,000 samples for the validation set and 10,000 samples for the test set."

### UR_P009_06_textedge

- Paper: `P009` — LLM-Prop: predicting the properties of crystalline materials using large language models
- Task: predicting the properties of crystalline materials (`T_P009_01`)
- Stage: evaluating prediction performance on test set using MAE and AUC (`model_evaluation`, `S_P009_06`)
- Usage role: test
- Purpose: evaluate prediction performance on test set using MAE and AUC
- Used fields: crystal text description, band gap, formation energy per atom, energy above hull, crystal volume, energy per atom, Is-gap-direct
- Filter conditions: Not stated
- Construction method: derived from Materials Project via Robocrystallographer text generation and preprocessing
- Sample count: 10000
- Confidence: 1.0

Evidence:
- P009, PDF page 4, Data collection and analysis: "The data originally contained 145,825 crystals structure-description pairs which we randomly split into 125,825 samples for the training set, 10,000 samples for the validation set and 10,000 samples for the test set."

## Aggregated evidence

- , PDF page 4, Data collection and analysis: "The data originally contained 145,825 crystals structure-description pairs which we randomly split into 125,825 samples for the training set, 10,000 samples for the validation set and 10,000 samples for the test set."
- , PDF page 4, Data collection and analysis: "The data originally contained 145,825 crystals structure-description pairs which we randomly split into 125,825 samples for the training set, 10,000 samples for the validation set and 10,000 samples for the test set."
- , PDF page 4, Data collection and analysis: "The data originally contained 145,825 crystals structure-description pairs which we randomly split into 125,825 samples for the training set, 10,000 samples for the validation set and 10,000 samples for the test set."
