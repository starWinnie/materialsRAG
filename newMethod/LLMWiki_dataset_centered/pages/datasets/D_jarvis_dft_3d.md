# Dataset: JARVIS-DFT 3D

- Dataset ID: `D_jarvis_dft_3d`
- Dataset type: `public_subset`
- Source dataset: `D_jarvis_dft`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- JARVIS-DFT
- dft_3d
- JARVIS-DFT-3D-2021
- JARVIS-DFT 3D 2021
- JARVIS
- dft_3d_2021
- JARVIS-DFT (3D 2021)
- JARVIS-3D
- JARVIS 3D
- JARVIS-3D dataset
- JARVIS-DFT 3D
- JARVIS-3D database

## Observed material scopes

- crystals
- crystal structures
- 3D materials
- inorganic materials
- computational materials
- materials

## Observed research tasks

- Crystal Property Prediction
- crystal structure modeling for SE(3)-invariant property prediction
- Predicting physical properties of materials from their crystal structures
- materials property prediction
- benchmarking of materials design methods

## Observed research stages

- data_acquisition
- model_evaluation
- model_training
- data_preparation

## Observed properties

- formation energy
- band gap
- bulk modulus
- shear modulus
- total energy
- energy above the hull
- bandgap (OPT)
- bandgap (MBJ)
- energy above hull (E hull)
- bandgap
- energy above hull
- dielectric constant
- piezoelectric tensor
- elastic tensor components
- Poisson ratio
- electron effective mass
- optical properties
- vibrational properties
- electronic properties
- forces
- Voigt bulk modulus
- exfoliation energy

## Observed fields

- formation energy
- band gap
- bulk modulus
- shear modulus
- total energy
- energy above the hull
- formation_energy_peratom
- optb88vdw_total_energy
- optb88vdw_bandgap
- mbj_bandgap
- ehull
- crystal structures
- DFT-calculated properties
- structure files (POSCAR)
- id
- structure
- bandgap
- bulk_modulus
- forces
- voigt_bulk_modulus
- exfoliation_energy

## Usage evidence

- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): source in Retrieving datasets from official websites — retrieving benchmark dataset for evaluation
- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): test in Evaluating on Materials Project, JARVIS-DFT, and Matbench — evaluating model performance on crystal property prediction tasks
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): source in acquisition of crystal structure datasets — acquisition of crystal structure datasets with DFT-simulated material properties
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): training in training of CrystalFramer architecture — training the CrystalFramer model from scratch using mean absolute loss function with Adam optimizer for 2000 epochs
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): test in evaluation on crystal property prediction tasks — evaluation of CrystalFramer performance on crystal property prediction tasks
- P022 (CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING): source in Using Materials Project and JARVIS-DFT datasets — Acquire crystal structure data with DFT-calculated properties for training and evaluation
- P022 (CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING): test in Evaluating model performance with mean absolute errors — Evaluate the trained model's performance on predicting material properties
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): training in acquisition of diverse materials datasets — Target dataset for fine-tuning and feature extraction-based transfer learning.
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): test in evaluation of TL and scratch models on holdout test sets — Holdout test set for evaluating TL and scratch models.
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): source in populating reference benchmark datasets — reference benchmark dataset for AI, ES, FF, and QC methods
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): training in generating benchmark datasets with defined data splits — training set for AI models / validation set for AI models / test set for AI models

## Dataset evidence

- P001, PDF page 8, EXPERIMENTS: "• JARVIS-DFT (dft_3d): This dataset contains 75,993 entries, each annotated with formation energy, band gap (calculated using either the OptB88vDW functional, denoted as OPT, or the TBMBJ functional, denoted as MBJ), bulk modulus, shear modulus, total energy (calculated using the OptB88vDW functional), and energy above the hull (Ehull ) (Choudhary et al., 2020). We also evaluate the baselines on the JARVIS-DFT-3D-2021 dataset (55,723 entries), which serves as an important supplementary benchmark."
- P010, PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- P010, PDF page 17, C DATASET SPECIFICATIONS: "The JARVIS-DFT 3D 2021 is a collection of 55,723 materials provided by Choudhary et al. (2020) and is accessible as dft_3d_2021 via jarvis-tools (or as dft_3d in older versions). These materials are annotated with various simulated properties using two DFT calculation methods, OptB88vdW (OPT) and TBmBJ (MBJ). Following recent studies (Yan et al., 2022; 2024; Lin et al., 2023; Taniai et al., 2024), we use formation energy (formation_energy_peratom), total energy (optb88vdw_total_energy), bandgap (optb88vdw_bandgap and mbj_bandgap), and energy above hull or E hull (ehull) as regression targets."
- P022, PDF page 7, EXPERIMENTS: "JARVIS-DFT (3D 2021) is a collection of 55,723 materials by Choudhary et al. (2020). Following Yan et al. (2022), we perform regression tasks of formation energy, total energy, bandgap, and energy above hull (E hull)."
- P024, PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."
- P024, PDF page 4, Poison: "JARVIS-3D database Here, we demonstrate the performance of TL models on different target materials properties in the JARVIS-3D dataset."
- P024, PDF page 9, DATA AVAILABILITY: "DATA AVAILABILITY The datasets used in this paper are publicly available from the corresponding websites- ... JARVIS5 from https://jarvis.nist.gov"
- P028, PDF page 3: "Fig. 1 | Leaderboard snapshot with an example output for AI-based formation energy per atom model on the JARVIS-DFT (dft_3d) dataset."
- P028, PDF page 3: "AI-SinglePropertyPrediction-formation_energy_peratom-dft_3d-test-mae.csv.zip"
- P028, PDF page 4, Results and discussion: "AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test"
- P028, PDF page 5: "JARVIS-DFT-3D dataset"
- P028, PDF page 9: "formation-energy-per atom model using AI for JARVIS-DFT 3D dataset with 5572 materials in the test set"
- P028, PDF page 6: "12 AI models (each AI model had a well-deﬁned 80:10:10 split for training, validation and testing respectively from the JARVIS-3D database)"
