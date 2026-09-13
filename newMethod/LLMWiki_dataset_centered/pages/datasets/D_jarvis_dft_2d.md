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
- JARVIS-2D dataset
- JARVIS-DFT 2D
- dft_2d

## Observed material scopes

- 2D materials
- inorganic materials
- computational materials

## Observed research tasks

- materials property prediction
- benchmarking of materials design methods

## Observed research stages

- data_acquisition
- model_evaluation
- data_preparation

## Observed properties

- formation energy
- band gap
- exfoliation energy
- dielectric constant
- elastic tensor components
- optical properties

## Observed fields

- structure files (POSCAR)
- id
- structure
- exfoliation_energy

## Usage evidence

- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): training in acquisition of diverse materials datasets — Target dataset for fine-tuning and feature extraction-based transfer learning.
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): test in evaluation of TL and scratch models on holdout test sets — Holdout test set for evaluating TL and scratch models.
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): source in populating reference benchmark datasets — reference benchmark dataset for 2D exfoliation energy predictions
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): test in generating benchmark datasets with defined data splits — test set for 2D exfoliation energy predictions

## Dataset evidence

- P024, PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."
- P024, PDF page 4, Poison: "JARVIS-2D database In the previous sections, we used different DFT-computed datasets containing 3D materials to perform the model training using the proposed framework to improve the performance of the target model. However, there also exist a class of materials that exhibit plate-like 2D shapes whose physical and chemical properties may differ in nature from that of 3D materials. Hence, here we investigate the effect of using the same source model trained on 3D materials dataset with TL to build target models on datasets containing 2D materials."
- P024, PDF page 9, DATA AVAILABILITY: "DATA AVAILABILITY The datasets used in this paper are publicly available from the corresponding websites- ... JARVIS5 from https://jarvis.nist.gov"
- P028, PDF page 4, Results and discussion: "for 2D exfoliation energies in JARVIS-DFT dataset"
