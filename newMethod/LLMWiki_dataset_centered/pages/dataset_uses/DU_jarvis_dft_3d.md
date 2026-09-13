# Dataset Use: JARVIS-DFT 3D

- DatasetUse ID: `DU_jarvis_dft_3d`
- Dataset: JARVIS-DFT 3D (`D_jarvis_dft_3d`)
- Papers: P001, P010, P022, P024, P028
- Usage records: 11

## Usage roles

- source
- test
- training

## Purposes

- retrieving benchmark dataset for evaluation
- evaluating model performance on crystal property prediction tasks
- acquisition of crystal structure datasets with DFT-simulated material properties
- training the CrystalFramer model from scratch using mean absolute loss function with Adam optimizer for 2000 epochs
- evaluation of CrystalFramer performance on crystal property prediction tasks
- Acquire crystal structure data with DFT-calculated properties for training and evaluation
- Evaluate the trained model's performance on predicting material properties
- Target dataset for fine-tuning and feature extraction-based transfer learning.
- Holdout test set for evaluating TL and scratch models.
- reference benchmark dataset for AI, ES, FF, and QC methods
- training set for AI models / validation set for AI models / test set for AI models

## Used fields

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

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 5572
- 44578
- 55723
- 75993

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P001_01_jarvis_dft_3d

- Paper: `P001` — BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION
- Task: Crystal Property Prediction (`T_P001_01`)
- Stage: Retrieving datasets from official websites (`data_acquisition`, `S_P001_01`)
- Usage role: source
- Purpose: retrieving benchmark dataset for evaluation
- Used fields: formation energy, band gap, bulk modulus, shear modulus, total energy, energy above the hull
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 75993
- Confidence: 1.0

Evidence:
- P001, PDF page 8, EXPERIMENTS: "• JARVIS-DFT (dft_3d): This dataset contains 75,993 entries, each annotated with formation energy, band gap (calculated using either the OptB88vDW functional, denoted as OPT, or the TBMBJ functional, denoted as MBJ), bulk modulus, shear modulus, total energy (calculated using the OptB88vDW functional), and energy above the hull (Ehull ) (Choudhary et al., 2020)."

### UR_P001_04_jarvis_dft_3d

- Paper: `P001` — BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION
- Task: Crystal Property Prediction (`T_P001_01`)
- Stage: Evaluating on Materials Project, JARVIS-DFT, and Matbench (`model_evaluation`, `S_P001_04`)
- Usage role: test
- Purpose: evaluating model performance on crystal property prediction tasks
- Used fields: formation energy, band gap, bulk modulus, shear modulus, total energy, energy above the hull
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 75993
- Confidence: 1.0

Evidence:
- P001, PDF page 1, ABSTRACT: "Extensive experiments are conducted on Materials Project, JARVIS-DFT, and MatBench, demonstrating that the proposed model achieves state-of-the-art performance."
- P001, PDF page 8, EXPERIMENTS: "• JARVIS-DFT (dft_3d): This dataset contains 75,993 entries, each annotated with formation energy, band gap (calculated using either the OptB88vDW functional, denoted as OPT, or the TBMBJ functional, denoted as MBJ), bulk modulus, shear modulus, total energy (calculated using the OptB88vDW functional), and energy above the hull (Ehull ) (Choudhary et al., 2020)."

### UR_P010_01_jarvis_dft_3d

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: acquisition of crystal structure datasets (`data_acquisition`, `S_P010_01`)
- Usage role: source
- Purpose: acquisition of crystal structure datasets with DFT-simulated material properties
- Used fields: formation_energy_peratom, optb88vdw_total_energy, optb88vdw_bandgap, mbj_bandgap, ehull
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 55723
- Confidence: 1.0

Evidence:
- P010, PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."

### UR_P010_02_jarvis_dft_3d

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: training of CrystalFramer architecture (`model_training`, `S_P010_02`)
- Usage role: training
- Purpose: training the CrystalFramer model from scratch using mean absolute loss function with Adam optimizer for 2000 epochs
- Used fields: formation_energy_peratom, optb88vdw_total_energy, optb88vdw_bandgap, mbj_bandgap, ehull
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 44578
- Confidence: 1.0

Evidence:
- P010, PDF page 8, Training settings.: "Specifically, for the JARVIS dataset, we train our model from scratch by optimizing the mean absolute loss function using Adam (Kingma & Ba, 2015) for a total of 2000 epochs, while enabling the frames from the beginning."
- P010, PDF page 17, C DATASET SPECIFICATIONS: "The JARVIS-DFT 3D 2021 is a collection of 55,723 materials provided by Choudhary et al. (2020) and is accessible as dft_3d_2021 via jarvis-tools (or as dft_3d in older versions). These materials are annotated with various simulated properties using two DFT calculation methods, OptB88vdW (OPT) and TBmBJ (MBJ). Following recent studies (Yan et al., 2022; 2024; Lin et al., 2023; Taniai et al., 2024), we use formation energy (formation_energy_peratom), total energy (optb88vdw_total_energy), bandgap (optb88vdw_bandgap and mbj_bandgap), and energy above hull or E hull (ehull) as regression targets."
- P010, PDF page 9, Table 1: Property prediction results on the JARVIS dataset.: "Form. energy Total energy Bandgap (OPT) Bandgap (MBJ) E hull 44578 / 5572 / 5572 44578 / 5572 / 5572 44578 / 5572 / 5572 14537 / 1817 / 1817 44296 / 5537 / 5537"

### UR_P010_03_jarvis_dft_3d

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: evaluation on crystal property prediction tasks (`model_evaluation`, `S_P010_03`)
- Usage role: test
- Purpose: evaluation of CrystalFramer performance on crystal property prediction tasks
- Used fields: formation_energy_peratom, optb88vdw_total_energy, optb88vdw_bandgap, mbj_bandgap, ehull
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 5572
- Confidence: 1.0

Evidence:
- P010, PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "Tables 1 and 2 extensively compare the mean absolute errors of the proposed and existing methods for the JARVIS (5 tasks) and MP (4 tasks) datasets."
- P010, PDF page 9, Table 1: Property prediction results on the JARVIS dataset.: "Form. energy Total energy Bandgap (OPT) Bandgap (MBJ) E hull 44578 / 5572 / 5572 44578 / 5572 / 5572 44578 / 5572 / 5572 14537 / 1817 / 1817 44296 / 5537 / 5537"

### UR_P022_01_jarvis_dft_3d

- Paper: `P022` — CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING
- Task: Predicting physical properties of materials from their crystal structures (`T_P022_01`)
- Stage: Using Materials Project and JARVIS-DFT datasets (`data_acquisition`, `S_P022_01`)
- Usage role: source
- Purpose: Acquire crystal structure data with DFT-calculated properties for training and evaluation
- Used fields: crystal structures, DFT-calculated properties
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 55723
- Confidence: 1.0

Evidence:
- P022, PDF page 7, EXPERIMENTS: "JARVIS-DFT (3D 2021) is a collection of 55,723 materials by Choudhary et al. (2020). Following Yan et al. (2022), we perform regression tasks of formation energy, total energy, bandgap, and energy above hull (E hull)."

### UR_P022_04_jarvis_dft_3d

- Paper: `P022` — CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING
- Task: Predicting physical properties of materials from their crystal structures (`T_P022_01`)
- Stage: Evaluating model performance with mean absolute errors (`model_evaluation`, `S_P022_04`)
- Usage role: test
- Purpose: Evaluate the trained model's performance on predicting material properties
- Used fields: crystal structures, DFT-calculated properties
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 5572
- Confidence: 1.0

Evidence:
- P022, PDF page 7, EXPERIMENTS: "Tables 1 and 2 summarize the mean absolute errors (MAEs) for totally nine regression tasks of the Materials Project and JARVIS-DFT datasets, comparing our method with eight existing methods"
- P022, PDF page 8, Method: "Form. energy Total energy Bandgap (OPT) Bandgap (MBJ) E hull 44578 / 5572 / 5572 44578 / 5572 / 5572 44578 / 5572 / 5572 14537 / 1817 / 1817 44296 / 5537 / 5537"

### UR_P024_01_jarvis_dft_3d

- Paper: `P024` — Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets
- Task: materials property prediction (`T_P024_01`)
- Stage: acquisition of diverse materials datasets (`data_acquisition`, `S_P024_01`)
- Usage role: training
- Purpose: Target dataset for fine-tuning and feature extraction-based transfer learning.
- Used fields: structure files (POSCAR)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P024, PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."

### UR_P024_05_jarvis_dft_3d

- Paper: `P024` — Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets
- Task: materials property prediction (`T_P024_01`)
- Stage: evaluation of TL and scratch models on holdout test sets (`model_evaluation`, `S_P024_05`)
- Usage role: test
- Purpose: Holdout test set for evaluating TL and scratch models.
- Used fields: structure files (POSCAR)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P024, PDF page 2, RESULTS: "The target datasets are randomly split with a ﬁxed random seed into training, validation, and holdout test sets in the ratio of 80:10:10."

### UR_P028_01_jarvis_dft_3d

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: populating reference benchmark datasets (`data_acquisition`, `S_P028_01`)
- Usage role: source
- Purpose: reference benchmark dataset for AI, ES, FF, and QC methods
- Used fields: id, structure, formation_energy_peratom, bandgap, bulk_modulus, forces, voigt_bulk_modulus, exfoliation_energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 3: "Fig. 1 | Leaderboard snapshot with an example output for AI-based formation energy per atom model on the JARVIS-DFT (dft_3d) dataset."

### UR_P028_02_jarvis_dft_3d

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: generating benchmark datasets with defined data splits (`data_preparation`, `S_P028_02`)
- Usage role: training
- Purpose: training set for AI models / validation set for AI models / test set for AI models
- Used fields: id, structure, formation_energy_peratom
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 6: "12 AI models (each AI model had a well-deﬁned 80:10:10 split for training, validation and testing respectively from the JARVIS-3D database)"
- P028, PDF page 6: "12 AI models (each AI model had a well-deﬁned 80:10:10 split for training, validation and testing respectively from the JARVIS-3D database)"
- P028, PDF page 9: "formation-energy-per atom model using AI for JARVIS-DFT 3D dataset with 5572 materials in the test set"

## Aggregated evidence

- , PDF page 8, EXPERIMENTS: "• JARVIS-DFT (dft_3d): This dataset contains 75,993 entries, each annotated with formation energy, band gap (calculated using either the OptB88vDW functional, denoted as OPT, or the TBMBJ functional, denoted as MBJ), bulk modulus, shear modulus, total energy (calculated using the OptB88vDW functional), and energy above the hull (Ehull ) (Choudhary et al., 2020)."
- , PDF page 1, ABSTRACT: "Extensive experiments are conducted on Materials Project, JARVIS-DFT, and MatBench, demonstrating that the proposed model achieves state-of-the-art performance."
- , PDF page 8, EXPERIMENTS: "• JARVIS-DFT (dft_3d): This dataset contains 75,993 entries, each annotated with formation energy, band gap (calculated using either the OptB88vDW functional, denoted as OPT, or the TBMBJ functional, denoted as MBJ), bulk modulus, shear modulus, total energy (calculated using the OptB88vDW functional), and energy above the hull (Ehull ) (Choudhary et al., 2020)."
- , PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- , PDF page 8, Training settings.: "Specifically, for the JARVIS dataset, we train our model from scratch by optimizing the mean absolute loss function using Adam (Kingma & Ba, 2015) for a total of 2000 epochs, while enabling the frames from the beginning."
- , PDF page 17, C DATASET SPECIFICATIONS: "The JARVIS-DFT 3D 2021 is a collection of 55,723 materials provided by Choudhary et al. (2020) and is accessible as dft_3d_2021 via jarvis-tools (or as dft_3d in older versions). These materials are annotated with various simulated properties using two DFT calculation methods, OptB88vdW (OPT) and TBmBJ (MBJ). Following recent studies (Yan et al., 2022; 2024; Lin et al., 2023; Taniai et al., 2024), we use formation energy (formation_energy_peratom), total energy (optb88vdw_total_energy), bandgap (optb88vdw_bandgap and mbj_bandgap), and energy above hull or E hull (ehull) as regression targets."
- , PDF page 9, Table 1: Property prediction results on the JARVIS dataset.: "Form. energy Total energy Bandgap (OPT) Bandgap (MBJ) E hull 44578 / 5572 / 5572 44578 / 5572 / 5572 44578 / 5572 / 5572 14537 / 1817 / 1817 44296 / 5537 / 5537"
- , PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "Tables 1 and 2 extensively compare the mean absolute errors of the proposed and existing methods for the JARVIS (5 tasks) and MP (4 tasks) datasets."
- , PDF page 9, Table 1: Property prediction results on the JARVIS dataset.: "Form. energy Total energy Bandgap (OPT) Bandgap (MBJ) E hull 44578 / 5572 / 5572 44578 / 5572 / 5572 44578 / 5572 / 5572 14537 / 1817 / 1817 44296 / 5537 / 5537"
- , PDF page 7, EXPERIMENTS: "JARVIS-DFT (3D 2021) is a collection of 55,723 materials by Choudhary et al. (2020). Following Yan et al. (2022), we perform regression tasks of formation energy, total energy, bandgap, and energy above hull (E hull)."
- , PDF page 7, EXPERIMENTS: "Tables 1 and 2 summarize the mean absolute errors (MAEs) for totally nine regression tasks of the Materials Project and JARVIS-DFT datasets, comparing our method with eight existing methods"
- , PDF page 8, Method: "Form. energy Total energy Bandgap (OPT) Bandgap (MBJ) E hull 44578 / 5572 / 5572 44578 / 5572 / 5572 44578 / 5572 / 5572 14537 / 1817 / 1817 44296 / 5537 / 5537"
- , PDF page 2, RESULTS: "We use nine datasets of DFT-computed and experimental properties in this work: Materials Project (MP)4, Joint Automated Repository for Various Integrated Simulations (JARVIS) 3D with 46 properties and 2D with 32 properties5, Flla44 with three properties, Dielectric Constant (DC)45 with five properties, Piezoelectric Tensor (PT)46 with two properties, Experimental Formation Energy (EFE)47 with one property, Kingsbury Experimental Formation Energy (KEFE)48 with one property, Kingsbury Experimental Bandgap (KEB)49 with one property, and Harvard Organic Photovoltaic Dataset (HOPV)50 with 24 properties."
- , PDF page 2, RESULTS: "The target datasets are randomly split with a ﬁxed random seed into training, validation, and holdout test sets in the ratio of 80:10:10."
- , PDF page 3: "Fig. 1 | Leaderboard snapshot with an example output for AI-based formation energy per atom model on the JARVIS-DFT (dft_3d) dataset."
- , PDF page 6: "12 AI models (each AI model had a well-deﬁned 80:10:10 split for training, validation and testing respectively from the JARVIS-3D database)"
- , PDF page 6: "12 AI models (each AI model had a well-deﬁned 80:10:10 split for training, validation and testing respectively from the JARVIS-3D database)"
- , PDF page 9: "formation-energy-per atom model using AI for JARVIS-DFT 3D dataset with 5572 materials in the test set"
