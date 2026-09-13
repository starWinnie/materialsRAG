# Dataset Use: MP* dataset

- DatasetUse ID: `DU_mp_dataset`
- Dataset: MP* dataset (`D_mp_dataset`)
- Papers: P006
- Usage records: 1

## Usage roles

- pretraining

## Purposes

- to pre-train the CrystalTransformer model on the expanded MP* dataset focusing on bandgap energy Eg and formation energy Ef predictive tasks

## Used fields

- formation energy (Ef)
- PBE bandgap (Eg)

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 134243

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P006_01_mp_dataset

- Paper: `P006` — Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning
- Task: universal atomic embeddings (UAEs) (`T_P006_01`)
- Stage: pre-training CrystalTransformer on MP* dataset (`model_training`, `S_P006_01`)
- Usage role: pretraining
- Purpose: to pre-train the CrystalTransformer model on the expanded MP* dataset focusing on bandgap energy Eg and formation energy Ef predictive tasks
- Used fields: formation energy (Ef), PBE bandgap (Eg)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 134243
- Confidence: 1.0

Evidence:
- P006, PDF page 3: "Front-end models as CrystalTransformer, CGCNN, ALIGNN, and MEGNET are ﬁrst pre-trained on the expanded MP* dataset, focusing on the bandgap energy Eg and formation energy Ef predictive tasks."
- P006, PDF page 2: "MP* denotes the 2023.6.23 version, which contains 134,243 materials."

## Aggregated evidence

- , PDF page 3: "Front-end models as CrystalTransformer, CGCNN, ALIGNN, and MEGNET are ﬁrst pre-trained on the expanded MP* dataset, focusing on the bandgap energy Eg and formation energy Ef predictive tasks."
- , PDF page 2: "MP* denotes the 2023.6.23 version, which contains 134,243 materials."
