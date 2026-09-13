# Dataset: MP21 Formation Energy Dataset

- Dataset ID: `D_mp21_formation_energy_dataset`
- Dataset type: `public_subset`
- Source dataset: `D_materials_project`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MP21 Formation Energy Dataset
- Mp_eform (Ef)
- Mp_eform

## Observed material scopes

- inorganic materials

## Observed research tasks

- materials property prediction

## Observed research stages

- model_evaluation
- model_training

## Observed properties

- formation energy per atom (eV/atoms)

## Observed fields

- material compositions
- crystal structures

## Usage evidence

- P013 (Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions): benchmark in benchmarking against state-of-the-art models on 8 property datasets — benchmark CrysCo's performance on formation energy prediction
- P013 (Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions): training in training hybrid CrysCo model with EGAT and transformer architectures — train the hybrid model on primary properties (formation energy)
- P013 (Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions): pretraining in transfer learning for data-scarce properties — pre-train model on formation energy for transfer learning to data-scarce properties

## Dataset evidence

- P013, PDF page 4: "Table 1 | The eight datasets derived from the MP21 database and used in the present study Dataset name	Source	Material property	# Crystal structures Mp_eform (Ef)	MP21	Formation energy per atom (eV/atoms)	126,785"
