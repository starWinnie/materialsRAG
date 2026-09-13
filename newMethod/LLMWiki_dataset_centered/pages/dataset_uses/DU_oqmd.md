# Dataset Use: Open Quantum Materials Database (OQMD)

- DatasetUse ID: `DU_oqmd`
- Dataset: Open Quantum Materials Database (OQMD) (`D_oqmd`)
- Papers: P005, P010, P016, P023, P028, P035
- Usage records: 10

## Usage roles

- source
- training
- test

## Purposes

- Acquire large-scale DFT-computed thermodynamic stability data for inorganic compounds
- Train base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR)
- Benchmark ECSG against state-of-the-art models using multiple metrics
- acquisition of crystal structure datasets with DFT-simulated material properties
- training the CrystalFramer model using mean absolute loss function with Adam optimizer for 200 epochs with larger batch size
- evaluation of CrystalFramer performance on crystal property prediction tasks
- To obtain diverse, large-scale, precomputed materials property data for robust OOD evaluation.
- pre-training via crystal structure reconstruction using unlabeled crystal graph data
- reference benchmark dataset for ES methods
- Provide DFT formation energies for cross-validation and baseline comparison against MC3D and experimental data.

## Used fields

- chemical formula
- formation energy
- decomposition energy (ΔHd)
- stability labels
- _oqmd_delta_e
- _oqmd_band_gap
- _oqmd_stability
- crystal structure
- band gap
- bulk modulus
- crystal structure (A, F, L)
- id
- structure
- formation_energy
- bandgap
- elastic_tensor

## Construction methods

- None stated

## Filter conditions

- formation energies larger than 5 eV/atom removed

## Sample counts

- 81763
- 654108
- 817636

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P005_01_oqmd

- Paper: `P005` — Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration
- Task: Predicting thermodynamic stability of inorganic compounds (`T_P005_01`)
- Stage: Collecting DFT-computed stability data from public materials databases (`data_acquisition`, `S_P005_01`)
- Usage role: source
- Purpose: Acquire large-scale DFT-computed thermodynamic stability data for inorganic compounds
- Used fields: chemical formula, formation energy, decomposition energy (ΔHd)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."

### UR_P005_04_oqmd

- Paper: `P005` — Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration
- Task: Predicting thermodynamic stability of inorganic compounds (`T_P005_01`)
- Stage: Training base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR) via stacked generalization (`model_training`, `S_P005_04`)
- Usage role: training
- Purpose: Train base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR)
- Used fields: chemical formula, stability labels
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P005, PDF page 4, Performance benchmarking against existing models: "In addition to the MP database, we further trained the ECSG model and other existing models on the OQMD20 and JARVIS50 databases to conduct a more detailed comparison of their performance, as shown in Supplementary Tables 5 and 6."

### UR_P005_05_oqmd

- Paper: `P005` — Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration
- Task: Predicting thermodynamic stability of inorganic compounds (`T_P005_01`)
- Stage: Benchmarking ECSG against state-of-the-art models using multiple metrics (`model_evaluation`, `S_P005_05`)
- Usage role: test
- Purpose: Benchmark ECSG against state-of-the-art models using multiple metrics
- Used fields: chemical formula, stability labels
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P005, PDF page 4, Performance benchmarking against existing models: "In addition to the MP database, we further trained the ECSG model and other existing models on the OQMD20 and JARVIS50 databases to conduct a more detailed comparison of their performance, as shown in Supplementary Tables 5 and 6."

### UR_P010_01_oqmd

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: acquisition of crystal structure datasets (`data_acquisition`, `S_P010_01`)
- Usage role: source
- Purpose: acquisition of crystal structure datasets with DFT-simulated material properties
- Used fields: _oqmd_delta_e, _oqmd_band_gap, _oqmd_stability
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 817636
- Confidence: 1.0

Evidence:
- P010, PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."

### UR_P010_02_oqmd

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: training of CrystalFramer architecture (`model_training`, `S_P010_02`)
- Usage role: training
- Purpose: training the CrystalFramer model using mean absolute loss function with Adam optimizer for 200 epochs with larger batch size
- Used fields: _oqmd_delta_e, _oqmd_band_gap, _oqmd_stability
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 654108
- Confidence: 1.0

Evidence:
- P010, PDF page 8, Datasets.: "Unlike these studies, we also use the much larger-scale OQMD dataset to assess scalability."
- P010, PDF page 17, D TRAINING SETTINGS: "For the OQMD dataset, which was not used by the baseline method, we use similar settings with a larger batch size of 1024 materials and fewer epochs of 200."
- P010, PDF page 9, Table 3: Property prediction results on the OQMD dataset.: "Form. energy (eV/atom) Bandgap (eV) E hull (eV/atom) Method 654108 / 81763 / 81763 653388 / 81673 / 81673 654108 / 81763 / 81763"

### UR_P010_03_oqmd

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: evaluation on crystal property prediction tasks (`model_evaluation`, `S_P010_03`)
- Usage role: test
- Purpose: evaluation of CrystalFramer performance on crystal property prediction tasks
- Used fields: _oqmd_delta_e, _oqmd_band_gap, _oqmd_stability
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 81763
- Confidence: 1.0

Evidence:
- P010, PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "It is important to note that the current state-of-the-art, ComFormer, uses finely-tuned hyperparameters (e.g., learning rate, loss function, number of layers, graph structure) for each individual task, whereas we simply adjust the number of epochs and batch size for each dataset."
- P010, PDF page 9, Table 3: Property prediction results on the OQMD dataset.: "Form. energy (eV/atom) Bandgap (eV) E hull (eV/atom) Method 654108 / 81763 / 81763 653388 / 81673 / 81673 654108 / 81763 / 81763"

### UR_P016_01_oqmd

- Paper: `P016` — Probing out-of-distribution generalization in machine learning for materials
- Task: probing out-of-distribution generalization in machine learning for materials (`T_P016_01`)
- Stage: selection of ab initio-derived materials databases (`data_acquisition`, `S_P016_01`)
- Usage role: source
- Purpose: To obtain diverse, large-scale, precomputed materials property data for robust OOD evaluation.
- Used fields: chemical formula, crystal structure, formation energy, band gap, bulk modulus
- Filter conditions: formation energies larger than 5 eV/atom removed
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P016, PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- P016, PDF page 2, Results: "Table 1 | In-distribution performance for the formation energy prediction ... OQMD ... Models are arranged in the ascending order of MAEs of the MP dataset from left to right. Best performance is highlighted in bold. TheMP, JARVIS,andOQMD datasets contain146k, 76k,and 1M entries, respectively."

### UR_P023_01_oqmd

- Paper: `P023` — A Diffusion-Based Pre-training Framework for Crystal Property Prediction
- Task: crystal property prediction (`T_P023_01`)
- Stage: collecting unlabeled crystal structure data for pre-training (`data_acquisition`, `S_P023_01`)
- Usage role: source
- Purpose: pre-training via crystal structure reconstruction using unlabeled crystal graph data
- Used fields: crystal structure (A, F, L)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P023, PDF page 6, Experimental Settings: "We collect 800K untagged crystal graph data from two popular materials databases, Materials Project (MP) (Jain et al. 2013) and OQMD (Saal et al. 2013), to pre-train the CrysDiff model."

### UR_P028_01_oqmd

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: populating reference benchmark datasets (`data_acquisition`, `S_P028_01`)
- Usage role: source
- Purpose: reference benchmark dataset for ES methods
- Used fields: id, structure, formation_energy, bandgap, elastic_tensor
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 7: "PBE87 data from Open Quantum Materials Database (OQMD)88,89"

### UR_P035_02_oqmd

- Paper: `P035` — Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning
- Task: Correcting DFT formation energies towards experimental accuracy (`T_P035_01`)
- Stage: Acquiring DFT formation energy datasets (`data_acquisition`, `S_P035_02`)
- Usage role: source
- Purpose: Provide DFT formation energies for cross-validation and baseline comparison against MC3D and experimental data.
- Used fields: formation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P035, PDF page 10, METHODS: "In addition to the comparison with experimental data, the MC3D formation energies are compared against the established high-throughput databases Materials Project [7, 8] and Open Quantum Materials Database [10]. We query the OQMD v1.5 (locally hosted) and MP v2023.11.1, and match structures by their ICSD ID."

## Aggregated evidence

- , PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- , PDF page 4, Performance benchmarking against existing models: "In addition to the MP database, we further trained the ECSG model and other existing models on the OQMD20 and JARVIS50 databases to conduct a more detailed comparison of their performance, as shown in Supplementary Tables 5 and 6."
- , PDF page 4, Performance benchmarking against existing models: "In addition to the MP database, we further trained the ECSG model and other existing models on the OQMD20 and JARVIS50 databases to conduct a more detailed comparison of their performance, as shown in Supplementary Tables 5 and 6."
- , PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- , PDF page 8, Datasets.: "Unlike these studies, we also use the much larger-scale OQMD dataset to assess scalability."
- , PDF page 17, D TRAINING SETTINGS: "For the OQMD dataset, which was not used by the baseline method, we use similar settings with a larger batch size of 1024 materials and fewer epochs of 200."
- , PDF page 9, Table 3: Property prediction results on the OQMD dataset.: "Form. energy (eV/atom) Bandgap (eV) E hull (eV/atom) Method 654108 / 81763 / 81763 653388 / 81673 / 81673 654108 / 81763 / 81763"
- , PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "It is important to note that the current state-of-the-art, ComFormer, uses finely-tuned hyperparameters (e.g., learning rate, loss function, number of layers, graph structure) for each individual task, whereas we simply adjust the number of epochs and batch size for each dataset."
- , PDF page 9, Table 3: Property prediction results on the OQMD dataset.: "Form. energy (eV/atom) Bandgap (eV) E hull (eV/atom) Method 654108 / 81763 / 81763 653388 / 81673 / 81673 654108 / 81763 / 81763"
- , PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- , PDF page 2, Results: "Table 1 | In-distribution performance for the formation energy prediction ... OQMD ... Models are arranged in the ascending order of MAEs of the MP dataset from left to right. Best performance is highlighted in bold. TheMP, JARVIS,andOQMD datasets contain146k, 76k,and 1M entries, respectively."
- , PDF page 6, Experimental Settings: "We collect 800K untagged crystal graph data from two popular materials databases, Materials Project (MP) (Jain et al. 2013) and OQMD (Saal et al. 2013), to pre-train the CrysDiff model."
- , PDF page 7: "PBE87 data from Open Quantum Materials Database (OQMD)88,89"
- , PDF page 10, METHODS: "In addition to the comparison with experimental data, the MC3D formation energies are compared against the established high-throughput databases Materials Project [7, 8] and Open Quantum Materials Database [10]. We query the OQMD v1.5 (locally hosted) and MP v2023.11.1, and match structures by their ICSD ID."
