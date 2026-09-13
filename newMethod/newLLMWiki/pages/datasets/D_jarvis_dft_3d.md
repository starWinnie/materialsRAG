# Dataset: JARVIS-DFT 3D

- Dataset ID: `D_jarvis_dft_3d`
- Dataset type: `public_subset`
- Source dataset: `D_jarvis_dft`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- JARVIS-DFT 3D 2021
- JARVIS
- dft_3d_2021
- dft_3d
- JARVIS-DFT (3D 2021)
- JARVIS-3D
- JARVIS 3D
- Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D
- JARVIS-DFT 3D
- JARVIS-DFT

## Observed material scopes

- crystals
- crystal structures
- 3D materials
- inorganic materials
- computational materials
- perfect and defect materials

## Observed research tasks

- crystal property prediction
- Predicting physical properties of materials from their crystal structures
- materials property prediction
- benchmarking of materials design methods

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation
- candidate_generation

## Observed properties

- formation_energy_peratom
- optb88vdw_total_energy
- optb88vdw_bandgap
- mbj_bandgap
- ehull
- formation energy
- total energy
- bandgap
- energy above hull
- band gap
- elastic tensor components
- dielectric constant
- piezoelectric tensor
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
- Encut
- Magoszi
- Magout
- Epsx
- Epsy
- Epsz
- KLU
- BgOptb
- BgMbj
- AvgME
- AvgMH
- Spillage
- Exfoli
- bulk modulus
- Voigt bulk modulus
- forces
- electron bandstructures
- dielectric functions
- solar cell efficiencies
- superconducting transition temperatures
- heat capacity
- hMOF data

## Observed fields

- formation energy
- total energy
- bandgap (OPT)
- bandgap (MBJ)
- E hull
- crystal structure
- bandgap
- energy above hull
- structure files (POSCAR)
- property labels
- atomic structures
- identifier (id)

## Usage evidence

- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): source in using datasets derived from JARVIS, Materials Project (MP), and Open Quantum Materials Database (OQMD) — acquire crystal structure data and corresponding DFT-simulated properties
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): training in using consistent data splits and preprocessing — prepare data using standardized splits and preprocessing for fair comparison
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): training in training CrystalFramer with dynamic frames — train the CrystalFramer architecture with dynamic frame construction
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): benchmark in comparing mean absolute errors on crystal property prediction tasks — evaluate performance against baselines using mean absolute error metrics
- P022 (CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING): source in Using Materials Project and JARVIS-DFT datasets — Acquire crystal structure data with DFT-calculated properties for training and evaluation
- P022 (CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING): test in Evaluating model performance on regression tasks — Evaluate the trained model's performance on predicting various material properties
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): candidate_pool in acquisition of diverse materials datasets — acquisition of diverse materials datasets for use as target dataset in transfer learning
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): training in transfer learning via fine-tuning on target datasets — transfer learning via fine-tuning on target datasets
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): candidate_pool in feature extraction from pre-trained ALIGNN for target compounds — feature extraction from pre-trained ALIGNN for target compounds
- P024 (Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets): training in training of target model on extracted features — training of target model on extracted features
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): source in populate dataset from json.zip — populate benchmark dataset with well-defined data splits

## Dataset evidence

- P010, PDF page 8, CRYSTAL PROPERTY PREDICTION: "Datasets. We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- P010, PDF page 17, C DATASET SPECIFICATIONS: "The JARVIS-DFT 3D 2021 is a collection of 55,723 materials provided by Choudhary et al. (2020) and is accessible as dft_3d_2021 via jarvis-tools (or as dft_3d in older versions). These materials are annotated with various simulated properties using two DFT calculation methods, OptB88vdW (OPT) and TBmBJ (MBJ). Following recent studies (Yan et al., 2022; 2024; Lin et al., 2023; Taniai et al., 2024), we use formation energy (formation_energy_peratom), total energy (optb88vdw_total_energy), bandgap (optb88vdw_bandgap and mbj_bandgap), and energy above hull or E hull (ehull) as regression targets."
- P022, PDF page 7, EXPERIMENTS: "JARVIS-DFT (3D 2021) is a collection of 55,723 materials by Choudhary et al. (2020). Following Yan et al. (2022), we perform regression tasks of formation energy, total energy, bandgap, and energy above hull (E hull). For bandgap, the dataset provides property values obtained by DFT calculation methods using the OptB88vdW functional (OPT) or the Tran-Blaha modified Becke-Johnson potential (MBJ)."
- P024, PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."
- P024, PDF page 4, JARVIS-3D database: "Table 2 presents the prediction accuracy of the best SC and best TL model on the test set for each of the 48 target properties."
- P024, PDF page 9, DATA AVAILABILITY: "The datasets used in this paper are publicly available from the corresponding websites- ... JARVIS5 from https://jarvis.nist.gov"
- P028, PDF page 3: "The jarvis_populate_data.py scripts generate a benchmark dataset."
- P028, PDF page 4, Results and discussion: "A user can populate the reference dataset (with well-deﬁned data splits) used for a speciﬁc benchmark (e.g., for 2D exfoliation energies in JARVIS-DFT dataset using an AI method: “AI-SinglePropertyPrediction-exfoliation_energy-dft_3d-test”)."
- P028, PDF page 6: "Fig. 6(a) we see the comparison of 12 AI models (each AI model had a well-deﬁned 80:10:10 split for training, validation and testing respectively from the JARVIS-3D database)"
- P028, PDF page 9: "Fig. 9(a), we ﬁnd that formation energy is one of the easiest quantities to train AI models [...] for JARVIS-DFT 3D dataset with 5572 materials in the test set"
