# Dataset Use: HOIP dataset

- DatasetUse ID: `DU_hoip_dataset`
- Dataset: HOIP dataset (`D_hoip_dataset`)
- Papers: P015
- Usage records: 6

## Usage roles

- source
- training
- test
- benchmark
- candidate_pool

## Purposes

- Acquisition of computational perovskite property data for training and evaluation.
- Descriptor generation (MPNN embedding) and episodic partitioning for extrapolative training.
- Training MNNs via extrapolative episodic training (E2T) using episodes with extrapolative relationships.
- Evaluation of extrapolative prediction performance on unseen perovskite compositions (HOIP-GeF and HOIP-PbI).
- Ablation study to investigate hyperparameter sensitivity (|S_train|, |S_infer|, λ) for E2T performance.
- Fine-tuning pretrained E2T models on target-domain perovskite subsets (HOIP-GeF and HOIP-PbI) with limited samples.

## Used fields

- bandgap
- organic cation
- inorganic cation
- inorganic anion
- crystal structure
- cation/anion composition
- anion/cation composition
- Ge+F
- Pb+I

## Construction methods

- Calculated using density functional theory.

## Filter conditions

- 11 of 12 anion–cation combinations used for training; one combination (e.g., Ge+F or Pb+I) held out for test
- episodes constructed from 11 anion–cation combinations; (x,y) sampled from one combination, S sampled from remaining ten
- compounds containing both Ge and F excluded from training; compounds containing both Pb and I excluded from training
- HOIP-GeF or HOIP-PbI data used for fine-tuning (10–40 samples); half reserved for evaluation

## Sample counts

- 1345

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P015_01_hoip_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: acquisition of polymer and perovskite datasets (`data_acquisition`, `S_P015_01`)
- Usage role: source
- Purpose: Acquisition of computational perovskite property data for training and evaluation.
- Used fields: bandgap, organic cation, inorganic cation, inorganic anion
- Filter conditions: Not stated
- Construction method: Calculated using density functional theory.
- Sample count: 1345
- Confidence: 1.0

Evidence:
- P015, PDF page 10, Methods: "The HOIP dataset40,41 contains 1345 perovskite compounds and their properties, including bandgaps, dielectric constants, and relative energies, calculated using the density functional theory."

### UR_P015_02_hoip_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: descriptor generation and dataset partitioning (`data_preparation`, `S_P015_02`)
- Usage role: training
- Purpose: Descriptor generation (MPNN embedding) and episodic partitioning for extrapolative training.
- Used fields: crystal structure, cation/anion composition
- Filter conditions: 11 of 12 anion–cation combinations used for training; one combination (e.g., Ge+F or Pb+I) held out for test
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 10, Methods: "We classiﬁed the HOIP dataset into 12 categories (or domains) based on a combination of four inorganic anions and three cations. Data from 11 of the 12 categories were included in the training dataset D... In each step of E2T, a training instance at (x, y) was sampled from a randomly selected combination among the 11 anion–cation combinations, whereas the support set S with a size of m = 50 was sampled from the remaining ten combinations of anions and cations, resulting in the inclusion of only extrapolative episodes."

### UR_P015_03_hoip_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: training MNNs via extrapolative episodic training (E2T) (`model_training`, `S_P015_03`)
- Usage role: training
- Purpose: Training MNNs via extrapolative episodic training (E2T) using episodes with extrapolative relationships.
- Used fields: crystal structure, bandgap, anion/cation composition
- Filter conditions: episodes constructed from 11 anion–cation combinations; (x,y) sampled from one combination, S sampled from remaining ten
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 10, Methods: "In each step of E2T, a training instance at (x, y) was sampled from a randomly selected combination among the 11 anion–cation combinations, whereas the support set S with a size of m = 50 was sampled from the remaining ten combinations of anions and cations, resulting in the inclusion of only extrapolative episodes."

### UR_P015_04_hoip_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: evaluation of extrapolative prediction performance (`model_evaluation`, `S_P015_04`)
- Usage role: test
- Purpose: Evaluation of extrapolative prediction performance on unseen perovskite compositions (HOIP-GeF and HOIP-PbI).
- Used fields: bandgap, Ge+F, Pb+I
- Filter conditions: compounds containing both Ge and F excluded from training; compounds containing both Pb and I excluded from training
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 5, unknown: "We performed numerical experiments using the same setting as that employed by Na et al.42,43. The HOIP dataset was divided into 12 groups... For creating a training episode, we excluded all samples with Ge and F or with Pb and I and randomly selected 50 instances of (x, y) from one group while drawing S of size 50 from the 10 remaining groups."

### UR_P015_05_hoip_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: hyperparameter sensitivity analysis for E2T (`ablation_study`, `S_P015_05`)
- Usage role: benchmark
- Purpose: Ablation study to investigate hyperparameter sensitivity (|S_train|, |S_infer|, λ) for E2T performance.
- Used fields: bandgap, anion/cation composition
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 6, Methods: "We conducted an ablation study using the HOIP dataset to investigate the influence of the training and inference support sizes, ∣Strain∣ and ∣Sinfer∣, and the smoothing parameter λ for the ridge regressor head on the E2T performance."

### UR_P015_06_hoip_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: fine-tuning for downstream extrapolative domains (`candidate_screening`, `S_P015_06`)
- Usage role: candidate_pool
- Purpose: Fine-tuning pretrained E2T models on target-domain perovskite subsets (HOIP-GeF and HOIP-PbI) with limited samples.
- Used fields: bandgap, Ge+F, Pb+I
- Filter conditions: HOIP-GeF or HOIP-PbI data used for fine-tuning (10–40 samples); half reserved for evaluation
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 11, Fine-tuning experiments: "An MNN pretrained by E2T with a source data size of 1248 (HOIP-GeF) or 1228 (HOIP-PbI) was fine-tuned on data, including data from the target domain. Half of the target dataset was reserved for performance evaluation, whereas 10–40 samples from the remaining data were used for fine-tuning."

## Aggregated evidence

- , PDF page 10, Methods: "The HOIP dataset40,41 contains 1345 perovskite compounds and their properties, including bandgaps, dielectric constants, and relative energies, calculated using the density functional theory."
- , PDF page 10, Methods: "We classiﬁed the HOIP dataset into 12 categories (or domains) based on a combination of four inorganic anions and three cations. Data from 11 of the 12 categories were included in the training dataset D... In each step of E2T, a training instance at (x, y) was sampled from a randomly selected combination among the 11 anion–cation combinations, whereas the support set S with a size of m = 50 was sampled from the remaining ten combinations of anions and cations, resulting in the inclusion of only extrapolative episodes."
- , PDF page 10, Methods: "In each step of E2T, a training instance at (x, y) was sampled from a randomly selected combination among the 11 anion–cation combinations, whereas the support set S with a size of m = 50 was sampled from the remaining ten combinations of anions and cations, resulting in the inclusion of only extrapolative episodes."
- , PDF page 5, unknown: "We performed numerical experiments using the same setting as that employed by Na et al.42,43. The HOIP dataset was divided into 12 groups... For creating a training episode, we excluded all samples with Ge and F or with Pb and I and randomly selected 50 instances of (x, y) from one group while drawing S of size 50 from the 10 remaining groups."
- , PDF page 6, Methods: "We conducted an ablation study using the HOIP dataset to investigate the influence of the training and inference support sizes, ∣Strain∣ and ∣Sinfer∣, and the smoothing parameter λ for the ridge regressor head on the E2T performance."
- , PDF page 11, Fine-tuning experiments: "An MNN pretrained by E2T with a source data size of 1248 (HOIP-GeF) or 1228 (HOIP-PbI) was fine-tuned on data, including data from the target domain. Half of the target dataset was reserved for performance evaluation, whereas 10–40 samples from the remaining data were used for fine-tuning."
