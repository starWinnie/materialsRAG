# Dataset: Kingsbury Experimental Formation Energy

- Dataset ID: `D_kingsbury_experimental_formation_energy`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Kingsbury Experimental Formation Energy
- Kingsbury Experimental Formation Energy (KEFE)
- KEFE

## Observed material scopes

- 3D materials
- inorganic materials
- experimental materials

## Observed research tasks

- materials property prediction

## Observed research stages

- data_acquisition
- model_evaluation

## Observed properties

- formation energy

## Observed fields

- structure files (POSCAR)

## Usage evidence

- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): training in acquisition of diverse materials datasets — Target dataset for fine-tuning and feature extraction-based transfer learning.
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): test in evaluation of TL and scratch models on holdout test sets — Holdout test set for evaluating TL and scratch models.

## Dataset evidence

- P024, PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."
- P024, PDF page 7, Dataset: "Table 6. The table shows the test MAE of the SC model, proposed TL model and % error change for each of the target materials properties for prediction task of ‘Experimental Data’. Dataset Property Data Size Base MAE of SC Model MAE of Proposed TL Model % Error Change KEFE Deltae (eVatom−1) 1557 0.9375 0.1109 0.0608 -45.18"
- P024, PDF page 9, DATA AVAILABILITY: "DATA AVAILABILITY The datasets used in this paper are publicly available from the corresponding websites- ... Flla44, Dielectric Constant45, Piezoelectric Tensor46, Experimental Formation Energy47, Kingsbury Experimental Formation Energy48, Kingsbury Experimental Bandgap49 from AutoMatminer63 (https://github.com/hackingmaterials/automatminer)"
