# Dataset: JARVIS-DFT 2D

- Dataset ID: `D_jarvis_dft_2d`
- Dataset type: `public_subset`
- Source dataset: `D_jarvis_dft`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- JARVIS-2D
- JARVIS 2D
- Joint Automated Repository for Various Integrated Simulations (JARVIS) 2D
- JARVIS-DFT 2D
- dft_2d

## Observed material scopes

- 2D materials
- inorganic materials
- computational materials
- perfect and defect materials

## Observed research tasks

- materials property prediction
- benchmarking of materials design methods

## Observed research stages

- data_acquisition
- model_training
- candidate_generation

## Observed properties

- formation energy
- band gap
- dielectric constant
- exfoliation energy
- SLME
- Meps
- PMDi
- MaxM
- MinM
- MaxIrM
- MinIrM
- PMEij
- Poisson ratio
- ShearGV
- BulkKV
- ETC
- NSB
- PSB
- PPF
- NPF
- Deltae
- Ehull
- Encut
- Magoszi
- Magout
- Epsx
- Epsy
- Epsz
- KLU
- BgOptb
- BgMbj
- Spillage

## Observed fields

- structure files (POSCAR)
- property labels
- atomic structures
- identifier (id)

## Usage evidence

- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): candidate_pool in acquisition of diverse materials datasets — acquisition of diverse materials datasets for use as target dataset in transfer learning
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): training in transfer learning via fine-tuning on target datasets — transfer learning via fine-tuning on target datasets
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): candidate_pool in feature extraction from pre-trained ALIGNN for target compounds — feature extraction from pre-trained ALIGNN for target compounds
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): source in populate dataset from json.zip — populate benchmark dataset for 2D exfoliation energies

## Dataset evidence

- P024, PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."
- P024, PDF page 5, JARVIS-2D database: "Table 4 presents the prediction accuracy of the best SC and best TL model on the test set for each of the 34 target properties in JARVIS-2D database."
- P024, PDF page 9, DATA AVAILABILITY: "The datasets used in this paper are publicly available from the corresponding websites- ... JARVIS5 from https://jarvis.nist.gov"
- P028, PDF page 4, Results and discussion: "A user can populate the reference dataset (with well-deﬁned data splits) used for a speciﬁc benchmark (e.g., for 2D exfoliation energies in JARVIS-DFT dataset using an AI method: “AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test”)."
