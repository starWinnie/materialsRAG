# Dataset Use: JARVIS-DFT 2D

- DatasetUse ID: `DU_jarvis_dft_2d`
- Dataset: JARVIS-DFT 2D (`D_jarvis_dft_2d`)
- Papers: P024, P028
- Usage records: 4

## Usage roles

- training
- test
- source

## Purposes

- Target dataset for fine-tuning and feature extraction-based transfer learning.
- Holdout test set for evaluating TL and scratch models.
- reference benchmark dataset for 2D exfoliation energy predictions
- test set for 2D exfoliation energy predictions

## Used fields

- structure files (POSCAR)
- id
- structure
- exfoliation_energy

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- None stated

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P024_01_jarvis_dft_2d

- Paper: `P024` — Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets
- Task: materials property prediction (`T_P024_01`)
- Stage: acquisition of diverse materials datasets (`data_acquisition`, `S_P024_01`)
- Usage role: training
- Purpose: Target dataset for fine-tuning and feature extraction-based transfer learning.
- Used fields: structure files (POSCAR)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P024, PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."

### UR_P024_05_jarvis_dft_2d

- Paper: `P024` — Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets
- Task: materials property prediction (`T_P024_01`)
- Stage: evaluation of TL and scratch models on holdout test sets (`model_evaluation`, `S_P024_05`)
- Usage role: test
- Purpose: Holdout test set for evaluating TL and scratch models.
- Used fields: structure files (POSCAR)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P024, PDF page 2, RESULTS: "The target datasets are randomly split with a ﬁxed random seed into training, validation, and holdout test sets in the ratio of 80:10:10."

### UR_P028_01_jarvis_dft_2d

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: populating reference benchmark datasets (`data_acquisition`, `S_P028_01`)
- Usage role: source
- Purpose: reference benchmark dataset for 2D exfoliation energy predictions
- Used fields: id, structure, exfoliation_energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 4, Results and discussion: "for 2D exfoliation energies in JARVIS-DFT dataset"

### UR_P028_02_jarvis_dft_2d

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: generating benchmark datasets with defined data splits (`data_preparation`, `S_P028_02`)
- Usage role: test
- Purpose: test set for 2D exfoliation energy predictions
- Used fields: id, structure, exfoliation_energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 4, Results and discussion: "AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test"

## Aggregated evidence

- , PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."
- , PDF page 2, RESULTS: "The target datasets are randomly split with a ﬁxed random seed into training, validation, and holdout test sets in the ratio of 80:10:10."
- , PDF page 4, Results and discussion: "for 2D exfoliation energies in JARVIS-DFT dataset"
- , PDF page 4, Results and discussion: "AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test"
