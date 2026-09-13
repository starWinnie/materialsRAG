# Dataset Use: RadonPy polymer dataset

- DatasetUse ID: `DU_radonpy_polymer_dataset`
- Dataset: RadonPy polymer dataset (`D_radonpy_polymer_dataset`)
- Papers: P015
- Usage records: 5

## Usage roles

- source
- training
- test
- candidate_pool

## Purposes

- Acquisition of computational polymer property data for training and evaluation.
- Descriptor generation (Morgan fingerprint) and episodic partitioning for extrapolative training.
- Training MNNs via extrapolative episodic training (E2T) using episodes with extrapolative relationships.
- Evaluation of extrapolative prediction performance on unseen polymer classes.
- Fine-tuning pretrained E2T models on target-domain polymer classes with limited samples.

## Used fields

- Cp
- refractive index
- polymer class
- repeating unit structure

## Construction methods

- Generated using RadonPy via all-atom MD simulations; ~70,000 hypothetical polymers generated with N-gram-based polymer structure generator and classified into 20 classes using PolyInfo rules.

## Filter conditions

- 19 of 20 polymer classes used for training; remaining class held out for test
- episodes constructed from 19 polymer classes; (x,y) sampled from one class, S sampled from others
- one held-out polymer class (e.g., p13–p14–p18) used for testing
- target polymer class data used for fine-tuning (20–500 samples); half reserved for evaluation

## Sample counts

- 69480

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P015_01_radonpy_polymer_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: acquisition of polymer and perovskite datasets (`data_acquisition`, `S_P015_01`)
- Usage role: source
- Purpose: Acquisition of computational polymer property data for training and evaluation.
- Used fields: Cp, refractive index, polymer class, repeating unit structure
- Filter conditions: Not stated
- Construction method: Generated using RadonPy via all-atom MD simulations; ~70,000 hypothetical polymers generated with N-gram-based polymer structure generator and classified into 20 classes using PolyInfo rules.
- Sample count: 69480
- Confidence: 1.0

Evidence:
- P015, PDF page 8, Methods: "In the polymer-property prediction experiments, 69,480 samples of Cp and 68,700 samples of the refractive index were used for the amorphous homopolymers. The data were generated using RadonPy36, which is a Python tool to construct a workflow for fully automated calculations of various polymeric properties using all-atom MD simulations."

### UR_P015_02_radonpy_polymer_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: descriptor generation and dataset partitioning (`data_preparation`, `S_P015_02`)
- Usage role: training
- Purpose: Descriptor generation (Morgan fingerprint) and episodic partitioning for extrapolative training.
- Used fields: repeating unit structure, polymer class
- Filter conditions: 19 of 20 polymer classes used for training; remaining class held out for test
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 9, Methods: "Data of 19 of 20 polymer classes were used for training, whereas the remaining class was used for testing... In each step of E2T, a training instance on (x, y) was sampled from a randomly selected polymer class, whereas the support set S of size m=30 was sampled entirely from the 19 polymer classes, including interpolative and extrapolative episodes."

### UR_P015_03_radonpy_polymer_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: training MNNs via extrapolative episodic training (E2T) (`model_training`, `S_P015_03`)
- Usage role: training
- Purpose: Training MNNs via extrapolative episodic training (E2T) using episodes with extrapolative relationships.
- Used fields: repeating unit structure, Cp, refractive index, polymer class
- Filter conditions: episodes constructed from 19 polymer classes; (x,y) sampled from one class, S sampled from others
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 9, Methods: "In each step of E2T, a training instance on (x, y) was sampled from a randomly selected polymer class, whereas the support set S of size m=30 was sampled entirely from the 19 polymer classes, including interpolative and extrapolative episodes."

### UR_P015_04_radonpy_polymer_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: evaluation of extrapolative prediction performance (`model_evaluation`, `S_P015_04`)
- Usage role: test
- Purpose: Evaluation of extrapolative prediction performance on unseen polymer classes.
- Used fields: Cp, refractive index, polymer class
- Filter conditions: one held-out polymer class (e.g., p13–p14–p18) used for testing
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 3, Experimental results: "To evaluate the prediction performance for an unseen polymer class, the following process was implemented: (1) a model was trained using randomly selected samples from 19 of the 20 polymer classes and (2) its generalizability was assessed using data from the remaining polymer class."

### UR_P015_06_radonpy_polymer_dataset

- Paper: `P015` — Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training
- Task: extrapolative prediction of material properties (`T_P015_01`)
- Stage: fine-tuning for downstream extrapolative domains (`candidate_screening`, `S_P015_06`)
- Usage role: candidate_pool
- Purpose: Fine-tuning pretrained E2T models on target-domain polymer classes with limited samples.
- Used fields: Cp, refractive index, polymer class
- Filter conditions: target polymer class data used for fine-tuning (20–500 samples); half reserved for evaluation
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P015, PDF page 6, Fine-tuning to extrapolative domains: "Fine-tuning was performed on the RadonPy dataset. In this experiment, a pretrained E2T model with a source data size of 38,000 was fine-tuned on data from the target domain corresponding to a particular polymer class."

## Aggregated evidence

- , PDF page 8, Methods: "In the polymer-property prediction experiments, 69,480 samples of Cp and 68,700 samples of the refractive index were used for the amorphous homopolymers. The data were generated using RadonPy36, which is a Python tool to construct a workflow for fully automated calculations of various polymeric properties using all-atom MD simulations."
- , PDF page 9, Methods: "Data of 19 of 20 polymer classes were used for training, whereas the remaining class was used for testing... In each step of E2T, a training instance on (x, y) was sampled from a randomly selected polymer class, whereas the support set S of size m=30 was sampled entirely from the 19 polymer classes, including interpolative and extrapolative episodes."
- , PDF page 9, Methods: "In each step of E2T, a training instance on (x, y) was sampled from a randomly selected polymer class, whereas the support set S of size m=30 was sampled entirely from the 19 polymer classes, including interpolative and extrapolative episodes."
- , PDF page 3, Experimental results: "To evaluate the prediction performance for an unseen polymer class, the following process was implemented: (1) a model was trained using randomly selected samples from 19 of the 20 polymer classes and (2) its generalizability was assessed using data from the remaining polymer class."
- , PDF page 6, Fine-tuning to extrapolative domains: "Fine-tuning was performed on the RadonPy dataset. In this experiment, a pretrained E2T model with a source data size of 38,000 was fine-tuned on data from the target domain corresponding to a particular polymer class."
