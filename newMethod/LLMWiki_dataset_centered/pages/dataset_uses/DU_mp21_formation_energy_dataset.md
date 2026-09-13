# Dataset Use: MP21 Formation Energy Dataset

- DatasetUse ID: `DU_mp21_formation_energy_dataset`
- Dataset: MP21 Formation Energy Dataset (`D_mp21_formation_energy_dataset`)
- Papers: P013
- Usage records: 3

## Usage roles

- benchmark
- pretraining
- training

## Purposes

- Benchmark CrysCo's performance on formation energy prediction
- Pretrain CrysCoT models on formation energy for transfer learning to data-scarce properties
- Train CrysCo for ablation study on number of EGAT layers using formation energy prediction task

## Used fields

- material compositions
- crystal structures

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 126785

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P013_04_mp21_formation_energy_dataset

- Paper: `P013` — Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions
- Task: materials property prediction (`T_P013_01`)
- Stage: transfer learning for data-scarce properties (`model_training`, `S_P013_04`)
- Usage role: pretraining
- Purpose: Pretrain CrysCoT models on formation energy for transfer learning to data-scarce properties
- Used fields: material compositions, crystal structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 126785
- Confidence: 1.0

Evidence:
- P013, PDF page 6, unknown: "We ﬁrst trained parent models on primary properties (Eg, Ef, and EHull), with dataset sizes ranging from 126,728 to 126,785 entries from MP21."

### UR_P013_05_mp21_formation_energy_dataset

- Paper: `P013` — Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions
- Task: materials property prediction (`T_P013_01`)
- Stage: benchmarking CrysCo's performance (`model_evaluation`, `S_P013_05`)
- Usage role: benchmark
- Purpose: Benchmark CrysCo's performance on formation energy prediction
- Used fields: material compositions, crystal structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 126785
- Confidence: 1.0

Evidence:
- P013, PDF page 4, unknown: "Table 1 | The eight datasets derived from the MP21 database and used in the present study Dataset name	Source	Material property	# Crystal structures Mp_eform (Ef)	MP21	Formation energy per atom (eV/atoms)	126,785"

### UR_P013_06_mp21_formation_energy_dataset

- Paper: `P013` — Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions
- Task: materials property prediction (`T_P013_01`)
- Stage: ablation study on number of EGAT layers (`ablation_study`, `S_P013_06`)
- Usage role: training
- Purpose: Train CrysCo for ablation study on number of EGAT layers using formation energy prediction task
- Used fields: material compositions, crystal structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P013, PDF page 5, unknown: "In order to determine the optimal balance between the accuracy and computational efﬁciency of CrysCo, we carried out an ablation study by changing the number of EGAT layers on the formation energy (Ef) prediction task."

## Aggregated evidence

- , PDF page 4, unknown: "Table 1 | The eight datasets derived from the MP21 database and used in the present study Dataset name	Source	Material property	# Crystal structures Mp_eform (Ef)	MP21	Formation energy per atom (eV/atoms)	126,785"
- , PDF page 6, unknown: "We ﬁrst trained parent models on primary properties (Eg, Ef, and EHull), with dataset sizes ranging from 126,728 to 126,785 entries from MP21."
- , PDF page 5, unknown: "In order to determine the optimal balance between the accuracy and computational efﬁciency of CrysCo, we carried out an ablation study by changing the number of EGAT layers on the formation energy (Ef) prediction task."
