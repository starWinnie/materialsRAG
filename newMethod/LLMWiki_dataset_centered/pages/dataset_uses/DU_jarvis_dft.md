# Dataset Use: JARVIS-DFT

- DatasetUse ID: `DU_jarvis_dft`
- Dataset: JARVIS-DFT (`D_jarvis_dft`)
- Papers: P005, P006, P011, P012, P016, P020, P021, P023
- Usage records: 19

## Usage roles

- source
- training
- test
- computational_validation
- validation
- benchmark
- screening

## Purposes

- Acquire large-scale DFT-computed thermodynamic stability data for inorganic compounds
- Train base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR)
- Benchmark ECSG against state-of-the-art models using multiple metrics
- to test the ability and transferability of ct-UAEs on different databases and tasks
- Fine-tuning the pre-trained model on labeled crystal property prediction tasks.
- Evaluating model performance on crystal property prediction using MAE.
- Source of crystal structures for constructing multi-edge crystal graphs with WPDD/UPDD representations
- Training WPDDFormer and UPDDFormer models on property prediction tasks
- Evaluating predictive accuracy of WPDDFormer/UPDDFormer on multiple material property tasks
- Ablation study on (W/U)PDD contribution using testing MAE as evaluation metric
- Continuity and completeness validation using EMD on perturbed crystal structures
- To obtain diverse, large-scale, precomputed materials property data for robust OOD evaluation.
- source dielectric, piezoelectric, and elastic tensors for curating the crystal tensor property dataset
- acquire crystal structure data and corresponding property labels for training and evaluation
- evaluate the performance of the trained models on held-out test sets using standard metrics
- demonstrate the importance of geometric completeness and specific architectural components by systematically removing them
- fine-tuning and evaluation of crystal property prediction on nine target properties
- downstream task evaluation on nine crystal properties using MAE
- ablation study on key design components for Formation Energy and Bandgap (MBJ)

## Used fields

- chemical formula
- formation energy
- decomposition energy (ΔHd)
- stability labels
- formation energy (Ef)
- bandgap (Eg)
- crystal structure
- bandgap
- energy above hull
- total energy
- bandgap(MBJ)
- bandgap(OPT)
- formation_energy
- bandgap_OPT
- bandgap_MBJ
- bulk_moduli_Kv
- shear_moduli_Gv
- e_above_hull
- band gap
- bulk modulus
- crystal structure M = (A, P, L)
- tensor property values
- crystal structure (A, P, L)
- Etotal
- Ehull
- crystal structure (A, F, L)
- target property values

## Construction methods

- None stated

## Filter conditions

- formation energies larger than 5 eV/atom removed

## Sample counts

- 55722

## Availability

- Dataset: public
- Recommendable: true

## Confidence

0.95

## Usage records

### UR_P005_01_jarvis_dft

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

### UR_P005_04_jarvis_dft

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

### UR_P005_05_jarvis_dft

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

### UR_P006_03_jarvis_dft

- Paper: `P006` — Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning
- Task: universal atomic embeddings (UAEs) (`T_P006_01`)
- Stage: evaluating transferability of ct-UAEs across databases and tasks (`model_evaluation`, `S_P006_03`)
- Usage role: computational_validation
- Purpose: to test the ability and transferability of ct-UAEs on different databases and tasks
- Used fields: formation energy (Ef), bandgap (Eg)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P006, PDF page 4: "The ability and transferability of the universal atomic embedding are further tested on different databases and tasks. Each is cut into 8:1:1 for training, validation, and testing. Details on the dataset can be found in Supplementary 2A. As for the Jarvis dataset49, the result is shown in Table 1. The CT-CGCNN model demonstrates an improvement in predicting both formation energy Ef and bandgap energy Eg."

### UR_P011_04_jarvis_dft

- Paper: `P011` — A Denoising Pre-training Framework for Accelerating Novel Material Discovery
- Task: crystal property prediction (`T_P011_01`)
- Stage: fine-tuning on downstream property prediction (`model_training`, `S_P011_04`)
- Usage role: training
- Purpose: Fine-tuning the pre-trained model on labeled crystal property prediction tasks.
- Used fields: crystal structure, formation energy, bandgap, energy above hull, total energy, bandgap(MBJ)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 55722
- Confidence: 1.0

Evidence:
- P011, PDF page 4, Experimental Setup: "The JARVIS dataset contains 55,722 materials with critical crystal properties for functional material design, including bandgaps, formation energies, energy above hull, total energy and so on."

### UR_P011_05_jarvis_dft

- Paper: `P011` — A Denoising Pre-training Framework for Accelerating Novel Material Discovery
- Task: crystal property prediction (`T_P011_01`)
- Stage: evaluating property prediction accuracy (`model_evaluation`, `S_P011_05`)
- Usage role: test
- Purpose: Evaluating model performance on crystal property prediction using MAE.
- Used fields: crystal structure, formation energy, bandgap(OPT), total energy, energy above hull, bandgap(MBJ)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P011, PDF page 3, Method: "Table 1: The experimental results in terms of MAE on JARVIS dataset."

### UR_P012_01_jarvis_dft

- Paper: `P012` — PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction
- Task: Crystal material property prediction (`T_P012_01`)
- Stage: Crystal graph construction with WPDD/UPDD (`data_preparation`, `S_P012_01`)
- Usage role: source
- Purpose: Source of crystal structures for constructing multi-edge crystal graphs with WPDD/UPDD representations
- Used fields: crystal structure
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P012, PDF page 4, 4.3 Crystal Graph Construction: "By introducing PDD, we constructed a general complete and continuous multi-edge crystal graph. In the graph, node features are xi. An edge is established from node j to node i when the Euclidean distance |ej′i|2 between a duplicate of j and i satisfies |ej′i|2 = |pj + k′1l1 + k′2l2 + k′3l3 −pi|2 ≤r, where r ∈R is the cutoff radius. Next, we construct a PDD row for each atom. Since directly representing PDD as edge features is impractical, we retain its matrix form and incorporate it into the construction of the multi-edge crystal graph to reflect the global information of the crystal structure. Therefore, we represent the constructed crystal graph as G = (X, XI, E, PDD)."

### UR_P012_02_jarvis_dft

- Paper: `P012` — PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction
- Task: Crystal material property prediction (`T_P012_01`)
- Stage: Training PDDFormer (WPDDFormer/UPDDFormer) (`model_training`, `S_P012_02`)
- Usage role: training
- Purpose: Training WPDDFormer and UPDDFormer models on property prediction tasks
- Used fields: crystal structure, formation_energy, bandgap_OPT, bandgap_MBJ, bulk_moduli_Kv, shear_moduli_Gv
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P012, PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."

### UR_P012_03_jarvis_dft

- Paper: `P012` — PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction
- Task: Crystal material property prediction (`T_P012_01`)
- Stage: Evaluation on benchmark property prediction tasks (`model_evaluation`, `S_P012_03`)
- Usage role: test
- Purpose: Evaluating predictive accuracy of WPDDFormer/UPDDFormer on multiple material property tasks
- Used fields: crystal structure, formation_energy, bandgap_OPT, bandgap_MBJ, bulk_moduli_Kv, shear_moduli_Gv
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P012, PDF page 7, 5.1 Experimental Results: "The quantitative results for JARVIS [Choudhary et al., 2020] are shown in Table 1."

### UR_P012_04_jarvis_dft

- Paper: `P012` — PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction
- Task: Crystal material property prediction (`T_P012_01`)
- Stage: Ablation study on (W/U)PDD contribution (`ablation_study`, `S_P012_04`)
- Usage role: validation
- Purpose: Ablation study on (W/U)PDD contribution using testing MAE as evaluation metric
- Used fields: crystal structure, e_above_hull, bandgap_OPT
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P012, PDF page 7, 5.2 Ablation Studies: "In this section, we demonstrate the impact of introducing (W/U)PDD on the representation learning of crystal materials through ablation studies. Specifically, we conducted experiments on the MP and JARVIS datasets, using testing mean absolute error (MAE) as the quantitative evaluation metric, comparing the results for Band Gap and Ehull tasks, as shown in Table 4."

### UR_P012_05_jarvis_dft

- Paper: `P012` — PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction
- Task: Crystal material property prediction (`T_P012_01`)
- Stage: Continuity and completeness validation using EMD (`computational_validation`, `S_P012_05`)
- Usage role: computational_validation
- Purpose: Continuity and completeness validation using EMD on perturbed crystal structures
- Used fields: crystal structure
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P012, PDF page 2, Introduction: "Finally, we employ the Earth Mover’s Distance (EMD) [Rubner et al., 2000] to assess the continuity of crystal graphs, demonstrating that WPDD crystal graphs constructed using only Euclidean distances maintain continuity and general completeness under slight atomic position perturbations, providing a more accurate depiction of actual crystal structures."

### UR_P016_01_jarvis_dft

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
- P016, PDF page 2, Results: "Table 1 | In-distribution performance for the formation energy prediction ... JARVIS ... Models are arranged in the ascending order of MAEs of the MP dataset from left to right. Best performance is highlighted in bold. TheMP, JARVIS,andOQMD datasets contain146k, 76k,and 1M entries, respectively."

### UR_P020_01_jarvis_dft

- Paper: `P020` — A Space Group Symmetry Informed Network for O(3) Equivariant Crystal Tensor Prediction
- Task: crystal tensor property prediction (`T_P020_01`)
- Stage: curating a dataset encompassing dielectric, piezoelectric, and elastic tensors (`data_acquisition`, `S_P020_01`)
- Usage role: source
- Purpose: source dielectric, piezoelectric, and elastic tensors for curating the crystal tensor property dataset
- Used fields: crystal structure M = (A, P, L), tensor property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P020, PDF page 7, 5.1. Curated Crystal Tensor Property Dataset: "In our research, a dataset is curated specifically focusing on crystal tensor properties, including dielectric, piezoelectric, and elastic tensors, sourced from the JARVIS-DFT database (Choudhary et al., 2020)."

### UR_P021_01_jarvis_dft

- Paper: `P021` — COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION
- Task: crystal material property prediction (`T_P021_01`)
- Stage: using three widely-used crystal benchmarks (`data_acquisition`, `S_P021_01`)
- Usage role: source
- Purpose: acquire crystal structure data and corresponding property labels for training and evaluation
- Used fields: crystal structure (A, P, L), formation energy, bandgap(OPT), bandgap(MBJ), Etotal, Ehull
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P021, PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."

### UR_P021_04_jarvis_dft

- Paper: `P021` — COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION
- Task: crystal material property prediction (`T_P021_01`)
- Stage: evaluating predictive accuracy on crystal benchmarks (`model_evaluation`, `S_P021_04`)
- Usage role: benchmark
- Purpose: evaluate the performance of the trained models on held-out test sets using standard metrics
- Used fields: formation energy, bandgap(OPT), bandgap(MBJ), Etotal, Ehull
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P021, PDF page 8, EXPERIMENTS: "For JARVIS and MP, we follow the experimental settings of Matformer (Yan et al., 2022) and PotNet (Lin et al., 2023), and use mean absolute error (MAE) as the evaluation metric."

### UR_P021_05_jarvis_dft

- Paper: `P021` — COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION
- Task: crystal material property prediction (`T_P021_01`)
- Stage: ablation studies on geometric completeness and model components (`ablation_study`, `S_P021_05`)
- Usage role: screening
- Purpose: demonstrate the importance of geometric completeness and specific architectural components by systematically removing them
- Used fields: formation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P021, PDF page 9, 5.2 ABLATION STUDIES: "In this section, we demonstrate the importance of geometric complete crystal graphs and Comformer components by conducting ablation studies on JARVIS formation energy task."

### UR_P023_02_jarvis_dft

- Paper: `P023` — A Diffusion-Based Pre-training Framework for Crystal Property Prediction
- Task: crystal property prediction (`T_P023_01`)
- Stage: collecting labeled crystal property data for fine-tuning and evaluation (`data_acquisition`, `S_P023_02`)
- Usage role: training
- Purpose: fine-tuning and evaluation of crystal property prediction on nine target properties
- Used fields: crystal structure (A, F, L), target property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 55722
- Confidence: 1.0

Evidence:
- P023, PDF page 6, Experimental Settings: "Further, to evaluate the fine-tuning performance of CrysDiff compared with other crystal property predictors, we select the 2021.8.18 version of JARVIS-DFT (Choudhary et al. 2020), another popular materials database, for the downstream property prediction task. JARVIS-DFT consists of 55,722 materials with 19 properties, like formation energy, bandgap, total energy, bulk modulus, etc., which depend significantly on crystal structures and atom features."

### UR_P023_05_jarvis_dft

- Paper: `P023` — A Diffusion-Based Pre-training Framework for Crystal Property Prediction
- Task: crystal property prediction (`T_P023_01`)
- Stage: downstream task evaluation on JARVIS-DFT (`model_evaluation`, `S_P023_05`)
- Usage role: test
- Purpose: downstream task evaluation on nine crystal properties using MAE
- Used fields: crystal structure (A, F, L), target property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P023, PDF page 6, Total Energy: "In Table 1, we report the MAE of different predicted crystal properties."
- P023, PDF page 6, Total Energy: "Table 1: The prediction performance (MAE) of nine properties on the JARVIS-DFT dataset for the proposed CrysDiff model against existing train-from-scratch and pretrain-finetune models."

### UR_P023_06_jarvis_dft

- Paper: `P023` — A Diffusion-Based Pre-training Framework for Crystal Property Prediction
- Task: crystal property prediction (`T_P023_01`)
- Stage: ablation study on key design components (`ablation_study`, `S_P023_06`)
- Usage role: benchmark
- Purpose: ablation study on key design components for Formation Energy and Bandgap (MBJ)
- Used fields: crystal structure (A, F, L), target property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P023, PDF page 7, Ablation Study: "Figure 5: The prediction performance (MAE) of two properties for CrysDiff variants on the JARVIS-DFT dataset."

## Aggregated evidence

- , PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- , PDF page 4, Performance benchmarking against existing models: "In addition to the MP database, we further trained the ECSG model and other existing models on the OQMD20 and JARVIS50 databases to conduct a more detailed comparison of their performance, as shown in Supplementary Tables 5 and 6."
- , PDF page 4, Performance benchmarking against existing models: "In addition to the MP database, we further trained the ECSG model and other existing models on the OQMD20 and JARVIS50 databases to conduct a more detailed comparison of their performance, as shown in Supplementary Tables 5 and 6."
- , PDF page 4: "The ability and transferability of the universal atomic embedding are further tested on different databases and tasks. Each is cut into 8:1:1 for training, validation, and testing. Details on the dataset can be found in Supplementary 2A. As for the Jarvis dataset49, the result is shown in Table 1. The CT-CGCNN model demonstrates an improvement in predicting both formation energy Ef and bandgap energy Eg."
- , PDF page 4, Experimental Setup: "The JARVIS dataset contains 55,722 materials with critical crystal properties for functional material design, including bandgaps, formation energies, energy above hull, total energy and so on."
- , PDF page 3, Method: "Table 1: The experimental results in terms of MAE on JARVIS dataset."
- , PDF page 4, 4.3 Crystal Graph Construction: "By introducing PDD, we constructed a general complete and continuous multi-edge crystal graph. In the graph, node features are xi. An edge is established from node j to node i when the Euclidean distance |ej′i|2 between a duplicate of j and i satisfies |ej′i|2 = |pj + k′1l1 + k′2l2 + k′3l3 −pi|2 ≤r, where r ∈R is the cutoff radius. Next, we construct a PDD row for each atom. Since directly representing PDD as edge features is impractical, we retain its matrix form and incorporate it into the construction of the multi-edge crystal graph to reflect the global information of the crystal structure. Therefore, we represent the constructed crystal graph as G = (X, XI, E, PDD)."
- , PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."
- , PDF page 7, 5.1 Experimental Results: "The quantitative results for JARVIS [Choudhary et al., 2020] are shown in Table 1."
- , PDF page 7, 5.2 Ablation Studies: "In this section, we demonstrate the impact of introducing (W/U)PDD on the representation learning of crystal materials through ablation studies. Specifically, we conducted experiments on the MP and JARVIS datasets, using testing mean absolute error (MAE) as the quantitative evaluation metric, comparing the results for Band Gap and Ehull tasks, as shown in Table 4."
- , PDF page 2, Introduction: "Finally, we employ the Earth Mover’s Distance (EMD) [Rubner et al., 2000] to assess the continuity of crystal graphs, demonstrating that WPDD crystal graphs constructed using only Euclidean distances maintain continuity and general completeness under slight atomic position perturbations, providing a more accurate depiction of actual crystal structures."
- , PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- , PDF page 2, Results: "Table 1 | In-distribution performance for the formation energy prediction ... JARVIS ... Models are arranged in the ascending order of MAEs of the MP dataset from left to right. Best performance is highlighted in bold. TheMP, JARVIS,andOQMD datasets contain146k, 76k,and 1M entries, respectively."
- , PDF page 7, 5.1. Curated Crystal Tensor Property Dataset: "In our research, a dataset is curated specifically focusing on crystal tensor properties, including dielectric, piezoelectric, and elastic tensors, sourced from the JARVIS-DFT database (Choudhary et al., 2020)."
- , PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."
- , PDF page 8, EXPERIMENTS: "For JARVIS and MP, we follow the experimental settings of Matformer (Yan et al., 2022) and PotNet (Lin et al., 2023), and use mean absolute error (MAE) as the evaluation metric."
- , PDF page 9, 5.2 ABLATION STUDIES: "In this section, we demonstrate the importance of geometric complete crystal graphs and Comformer components by conducting ablation studies on JARVIS formation energy task."
- , PDF page 6, Experimental Settings: "Further, to evaluate the fine-tuning performance of CrysDiff compared with other crystal property predictors, we select the 2021.8.18 version of JARVIS-DFT (Choudhary et al. 2020), another popular materials database, for the downstream property prediction task. JARVIS-DFT consists of 55,722 materials with 19 properties, like formation energy, bandgap, total energy, bulk modulus, etc., which depend significantly on crystal structures and atom features."
- , PDF page 6, Total Energy: "In Table 1, we report the MAE of different predicted crystal properties."
- , PDF page 6, Total Energy: "Table 1: The prediction performance (MAE) of nine properties on the JARVIS-DFT dataset for the proposed CrysDiff model against existing train-from-scratch and pretrain-finetune models."
- , PDF page 7, Ablation Study: "Figure 5: The prediction performance (MAE) of two properties for CrysDiff variants on the JARVIS-DFT dataset."
