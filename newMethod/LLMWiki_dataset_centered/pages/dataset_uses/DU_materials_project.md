# Dataset Use: Materials Project

- DatasetUse ID: `DU_materials_project`
- Dataset: Materials Project (`D_materials_project`)
- Papers: P001, P002, P004, P005, P008, P009, P010, P011, P012, P013, P016, P017, P021, P022, P023, P024, P025, P026, P027, P028, P038
- Usage records: 46

## Usage roles

- source
- test
- training
- validation
- experimental_validation
- label_source
- computational_validation
- benchmark
- candidate_pool

## Purposes

- retrieving benchmark dataset for evaluation
- evaluating model performance on crystal property prediction tasks
- To acquire crystal structure data and associated material properties for training and evaluation.
- To train the complete Crystal Fourier Transformer (CFT) architecture on the Materials Project dataset to predict material properties.
- To assess CFT's competitive performance against state-of-the-art graph neural networks on standard material property prediction tasks.
- To isolate and quantify the contribution of the pretraining step to the final model performance.
- To empirically validate the core hypothesis that the adaptive architecture can generalize to materials from space groups it has never seen during training.
- Acquisition of large-scale, diverse DFT-computed data including energies, forces, stresses, and magnetic moments for model training.
- Training diverse ML models—including universal interatomic potentials and energy-only predictors—on MP training data to predict relaxed energies or hull distances.
- Acquire large-scale DFT-computed thermodynamic stability data for inorganic compounds
- Derive binary stability labels via convex hull analysis using formation energies
- Train base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR)
- Benchmark ECSG against state-of-the-art models using multiple metrics
- Construct convex hull for DFT validation of candidate compounds
- Acquire initial theoretical dataset of semiconductor candidates via API.
- acquire raw crystal structural data and associated properties
- generate crystal text descriptions using Robocrystallographer
- obtain property labels for training and evaluation
- acquisition of crystal structure datasets with DFT-simulated material properties
- training the CrystalFramer model using mean absolute loss function with Adam optimizer
- evaluation of CrystalFramer performance on crystal property prediction tasks
- Fine-tuning the pre-trained model on labeled crystal property prediction tasks.
- Evaluating model performance on crystal property prediction using MAE.
- Source of crystal structures for constructing multi-edge crystal graphs with WPDD/UPDD representations
- Training WPDDFormer and UPDDFormer models on property prediction tasks
- Evaluating predictive accuracy of WPDDFormer/UPDDFormer on multiple material property tasks
- Ablation study on (W/U)PDD contribution using testing MAE as evaluation metric
- Continuity and completeness validation using EMD on perturbed crystal structures
- Acquire computational data for training and testing
- To obtain diverse, large-scale, precomputed materials property data for robust OOD evaluation.
- solid materials property prediction benchmark
- acquire crystal structure data and corresponding property labels for training and evaluation
- evaluate the performance of the trained models on held-out test sets using standard metrics
- Acquire crystal structure data with DFT-calculated properties for training and evaluation
- Train the Crystalformer model to predict material properties from crystal structures
- Evaluate the trained model's performance on predicting material properties
- pre-training via crystal structure reconstruction using unlabeled crystal graph data
- Source dataset for pre-training ALIGNN model on formation energy to learn transferable structural representations.
- Training the source model (ALIGNN) on formation energy of Materials Project to learn transferable structural representations.
- Train and validate ChargE3Net on inorganic materials across the periodic table
- Input for MD-HIT-composition redundancy reduction algorithm
- Input for MD-HIT-structure redundancy reduction algorithm
- Raw material data acquisition and initial filtering for downstream redundancy control
- Input material pool for generating Γ-phonon predictions using the trained MVN model
- reference benchmark dataset for AI methods
- Source of bulk oxide materials for slab generation.

## Used fields

- formation energy
- band gap
- metal/non-metal classification
- bulk modulus
- shear modulus
- Young's modulus
- atomic numbers
- fractional coordinates
- lattice vectors
- space group identifier
- energies
- forces
- stresses
- magnetic moments
- chemical formula
- decomposition energy (ΔHd)
- stability labels
- total energy data
- Ehull
- Eg
- Natoms
- Nelements
- structure
- crystal structure (CIF)
- property values
- CIF files
- formation energy per atom
- energy above hull
- crystal volume
- energy per atom
- Is-gap-direct
- e_form
- gap_pbe
- bulk_modulus
- shear_modulus
- crystal structure
- bulk moduli
- shear moduli
- formation_energy
- bandgap_OPT
- total_energy
- e_above_hull
- material compositions
- crystal structures
- tabulated physical and chemical descriptors
- material composition
- crystal structure (A, P, L)
- DFT-calculated properties
- crystal structure (A, F, L)
- structure files (POSCAR)
- formation energy labels
- atomic species
- atomic positions
- charge density grid points
- compositions
- band gaps
- atomic coordinates
- unit cell vectors
- space group
- id
- bandgap
- elastic_tensor
- thermal_conductivity
- dielectric_tensor
- bandstructure
- bulk_formula
- final_structure

## Construction methods

- convex hull analysis
- Robocrystallographer applied to CIF files

## Filter conditions

- space groups containing inversion symmetry
- exclude noble gas and radioactive elements
- Compounds with a ΔHd below 0 meV/atom were considered stable
- formation energies larger than 5 eV/atom removed
- excluded mp-101974 (HeSiO2)
- eliminated formulas with over 50 atoms
- unit cells < 100 atoms
- excludes slabs > 200 atoms

## Sample counts

- 4239
- 6331
- 60000
- 69239
- 85014
- 86741
- 106171
- 122959
- 125619
- 146323
- 154718

## Availability

- Dataset: public
- Recommendable: true

## Confidence

0.95

## Usage records

### UR_P001_01_materials_project

- Paper: `P001` — BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION
- Task: Crystal Property Prediction (`T_P001_01`)
- Stage: Retrieving datasets from official websites (`data_acquisition`, `S_P001_01`)
- Usage role: source
- Purpose: retrieving benchmark dataset for evaluation
- Used fields: formation energy, band gap, metal/non-metal classification, bulk modulus, shear modulus, Young's modulus
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 122959
- Confidence: 1.0

Evidence:
- P001, PDF page 8, EXPERIMENTS: "• Materials Project (MP) Database: We use stable structures retrieved from the Materials Project (Jain et al., 2020), comprising 122,959 entries with annotated formation energy, band gap, and metal/non-metal classification labels. Additionally, 9,473 of these entries include mechanical properties such as bulk modulus, shear modulus and Young’s modulus."

### UR_P001_04_materials_project

- Paper: `P001` — BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION
- Task: Crystal Property Prediction (`T_P001_01`)
- Stage: Evaluating on Materials Project, JARVIS-DFT, and Matbench (`model_evaluation`, `S_P001_04`)
- Usage role: test
- Purpose: evaluating model performance on crystal property prediction tasks
- Used fields: formation energy, band gap, metal/non-metal classification, bulk modulus, shear modulus, Young's modulus
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 122959
- Confidence: 1.0

Evidence:
- P001, PDF page 1, ABSTRACT: "Extensive experiments are conducted on Materials Project, JARVIS-DFT, and MatBench, demonstrating that the proposed model achieves state-of-the-art performance."
- P001, PDF page 8, EXPERIMENTS: "• Materials Project (MP) Database: We use stable structures retrieved from the Materials Project (Jain et al., 2020), comprising 122,959 entries with annotated formation energy, band gap, and metal/non-metal classification labels. Additionally, 9,473 of these entries include mechanical properties such as bulk modulus, shear modulus and Young’s modulus."

### UR_P002_01_materials_project

- Paper: `P002` — A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP
- Task: developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group (`T_P002_01`)
- Stage: using data from the Materials Project (`data_acquisition`, `S_P002_01`)
- Usage role: source
- Purpose: To acquire crystal structure data and associated material properties for training and evaluation.
- Used fields: atomic numbers, fractional coordinates, lattice vectors, space group identifier
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P002, PDF page 7, EXPERIMENTAL SETUP: "For our primary benchmark experiments, we use data from the Materials Project, one of the largest databases of computational material properties (Jain et al., 2013)."

### UR_P002_06_materials_project

- Paper: `P002` — A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP
- Task: developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group (`T_P002_01`)
- Stage: training the full Crystal Fourier Transformer (CFT) for material property prediction (`model_training`, `S_P002_06`)
- Usage role: training
- Purpose: To train the complete Crystal Fourier Transformer (CFT) architecture on the Materials Project dataset to predict material properties.
- Used fields: atomic numbers, fractional coordinates, lattice vectors, space group identifier
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P002, PDF page 8, MATERIAL PROPERTY PREDICTION: "Having validated our encoding module, we now evaluate the full CFT architecture on the task of predicting material properties from the Materials Project dataset."

### UR_P002_07_materials_project

- Paper: `P002` — A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP
- Task: developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group (`T_P002_01`)
- Stage: evaluating CFT's performance on material property prediction benchmarks (`model_evaluation`, `S_P002_07`)
- Usage role: test
- Purpose: To assess CFT's competitive performance against state-of-the-art graph neural networks on standard material property prediction tasks.
- Used fields: atomic numbers, fractional coordinates, lattice vectors, space group identifier
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P002, PDF page 8, MATERIAL PROPERTY PREDICTION: "Table 1 shows the test MAE for CFT and baseline models. Our CFT model achieves competitive performance across all four properties and outperforms all baselines on Total Energy and Shear Moduli prediction."

### UR_P002_08_materials_project

- Paper: `P002` — A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP
- Task: developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group (`T_P002_01`)
- Stage: comparing CFT with and without pretraining of positional encodings (`ablation_study`, `S_P002_08`)
- Usage role: validation
- Purpose: To isolate and quantify the contribution of the pretraining step to the final model performance.
- Used fields: atomic numbers, fractional coordinates, lattice vectors, space group identifier
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P002, PDF page 19, WHY PRETRAIN?: "Table 3 shows that pretraining the positional encodings improves property prediction performance across the board, in comparison to end-to-end training with random initialization of the positional encodings."

### UR_P002_09_materials_project

- Paper: `P002` — A SINGLE ARCHITECTURE FOR REPRESENTING INVARIANCE UNDER ANY SPACE GROUP
- Task: developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group (`T_P002_01`)
- Stage: performing zero-shot generalization to unseen space groups (`experimental_validation`, `S_P002_09`)
- Usage role: experimental_validation
- Purpose: To empirically validate the core hypothesis that the adaptive architecture can generalize to materials from space groups it has never seen during training.
- Used fields: atomic numbers, fractional coordinates, lattice vectors, space group identifier
- Filter conditions: space groups containing inversion symmetry
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P002, PDF page 9, ZERO-SHOT GENERALIZATION TO UNSEEN SPACE GROUPS: "The core hypothesis behind our adaptive architecture is that, by explicitly parameterizing the group constraints, CFT can generalize to materials from previously unseen space groups. We test this hypothesis in a zero-shot setting by holding out all space groups containing inversion symmetry from the training set."

### UR_P004_01_materials_project

- Paper: `P004` — A framework to evaluate machine learning crystal stability predictions
- Task: ML-guided materials discovery (`T_P004_01`)
- Stage: Acquisition of training data from Materials Project database (`data_acquisition`, `S_P004_01`)
- Usage role: source
- Purpose: Acquisition of large-scale, diverse DFT-computed data including energies, forces, stresses, and magnetic moments for model training.
- Used fields: energies, forces, stresses, magnetic moments
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P004, PDF page 7, Methods: "We recorded a snapshot of energies, forces, stresses and magnetic moments for all MP ionic steps on 15 March 2023 as the canonical training set for Matbench Discovery, and provide convenience functions through our Python package for easily feeding those data into future model submissions to our benchmark."

### UR_P004_03_materials_project

- Paper: `P004` — A framework to evaluate machine learning crystal stability predictions
- Task: ML-guided materials discovery (`T_P004_01`)
- Stage: Training of ML models on MP data (`model_training`, `S_P004_03`)
- Usage role: training
- Purpose: Training diverse ML models—including universal interatomic potentials and energy-only predictors—on MP training data to predict relaxed energies or hull distances.
- Used fields: energies, forces, stresses, magnetic moments
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P004, PDF page 7, Methods: "Our benchmark defines the training set as all data available from the v.2022.10.28 MP release. We recorded a snapshot of energies, forces, stresses and magnetic moments for all MP ionic steps on 15 March 2023 as the canonical training set for Matbench Discovery..."

### UR_P005_01_materials_project

- Paper: `P005` — Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration
- Task: Predicting thermodynamic stability of inorganic compounds (`T_P005_01`)
- Stage: Collecting DFT-computed stability data from public materials databases (`data_acquisition`, `S_P005_01`)
- Usage role: source
- Purpose: Acquire large-scale DFT-computed thermodynamic stability data for inorganic compounds
- Used fields: chemical formula, formation energy, decomposition energy (ΔHd)
- Filter conditions: exclude noble gas and radioactive elements
- Construction method: Not stated
- Sample count: 85014
- Confidence: 1.0

Evidence:
- P005, PDF page 11, Methods: "Before using these databases, data preprocessing was required. After excluding noble gas and radioactive elements, the MP database contained 85,014 compounds with information on thermodynamic properties such as formation energy."

### UR_P005_03_materials_project

- Paper: `P005` — Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration
- Task: Predicting thermodynamic stability of inorganic compounds (`T_P005_01`)
- Stage: Deriving stability labels from decomposition energy (ΔHd) via convex hull analysis (`label_generation`, `S_P005_03`)
- Usage role: label_source
- Purpose: Derive binary stability labels via convex hull analysis using formation energies
- Used fields: formation energy
- Filter conditions: Compounds with a ΔHd below 0 meV/atom were considered stable
- Construction method: convex hull analysis
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P005, PDF page 11, Methods: "Compounds with a ΔHd below 0 meV/atom were considered stable and are labeled accordingly."

### UR_P005_04_materials_project

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
- P005, PDF page 4, Performance benchmarking against existing models: "All models were trained using data sourced from the MP dataset, as detailed in the Methods section."

### UR_P005_05_materials_project

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
- P005, PDF page 4, Performance benchmarking against existing models: "In this section, we performed a comprehensive comparison between our proposed method and several state-of-the-art baselines... to validate the effectiveness of our proposed ECSG."

### UR_P005_08_materials_project

- Paper: `P005` — Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration
- Task: Predicting thermodynamic stability of inorganic compounds (`T_P005_01`)
- Stage: Validating predictions via first-principles DFT calculations (`computational_validation`, `S_P005_08`)
- Usage role: computational_validation
- Purpose: Construct convex hull for DFT validation of candidate compounds
- Used fields: total energy data
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P005, PDF page 13, First principles calculation: "To construct the convex hull for each set of elements comprising A-A′-B-B′-O, the total energy data of all compounds in the MP database was considered and extracted using the database API."

### UR_P008_01_materials_project

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: obtaining material dataset from Materials Project database (`data_acquisition`, `S_P008_01`)
- Usage role: source
- Purpose: Acquire initial theoretical dataset of semiconductor candidates via API.
- Used fields: Ehull, Eg, Natoms, Nelements, structure
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 154718
- Confidence: 1.0

Evidence:
- P008, PDF page 3, Preliminary high-throughput screening: "Initially, we start by acquiring all the materials from the MP database based on its API, resulting in a total of 1,54,718 entries saved in a JSON file as the Python dictionary object."

### UR_P009_01_materials_project

- Paper: `P009` — LLM-Prop: predicting the properties of crystalline materials using large language models
- Task: predicting the properties of crystalline materials (`T_P009_01`)
- Stage: collecting crystal structure-description pairs from Materials Project (`data_acquisition`, `S_P009_01`)
- Usage role: source
- Purpose: acquire raw crystal structural data and associated properties
- Used fields: crystal structure (CIF), property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P009, PDF page 4, Data collection and analysis: "We collected the dataset used in this work from the Materials Project database40 using the Materials Project free API as of November 1, 2022."

### UR_P009_02_materials_project

- Paper: `P009` — LLM-Prop: predicting the properties of crystalline materials using large language models
- Task: predicting the properties of crystalline materials (`T_P009_01`)
- Stage: generating crystal text descriptions using Robocrystallographer (`data_preparation`, `S_P009_02`)
- Usage role: source
- Purpose: generate crystal text descriptions using Robocrystallographer
- Used fields: CIF files
- Filter conditions: Not stated
- Construction method: Robocrystallographer applied to CIF files
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P009, PDF page 4, Data collection and analysis: "We generated the crystal text descriptions using Robocrystallographer41, a tool that generates a deterministic human readable text description of a structure given its CIF file."

### UR_P009_04_materials_project

- Paper: `P009` — LLM-Prop: predicting the properties of crystalline materials using large language models
- Task: predicting the properties of crystalline materials (`T_P009_01`)
- Stage: obtaining property labels from Materials Project database (`label_generation`, `S_P009_04`)
- Usage role: label_source
- Purpose: obtain property labels for training and evaluation
- Used fields: band gap, formation energy per atom, energy above hull, crystal volume, energy per atom, Is-gap-direct
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P009, PDF page 4, Data collection and analysis: "We collect the data of band gap, formation energy per atom (FEPA), energy above hull (Ehull), crystal volume, energy per atom (EPA), and an indicator of whether the band gap is direct or indirect (Is-gap-direct)."

### UR_P010_01_materials_project

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: acquisition of crystal structure datasets (`data_acquisition`, `S_P010_01`)
- Usage role: source
- Purpose: acquisition of crystal structure datasets with DFT-simulated material properties
- Used fields: e_form, gap_pbe, bulk_modulus, shear_modulus
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 69239
- Confidence: 1.0

Evidence:
- P010, PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."

### UR_P010_02_materials_project

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: training of CrystalFramer architecture (`model_training`, `S_P010_02`)
- Usage role: training
- Purpose: training the CrystalFramer model using mean absolute loss function with Adam optimizer
- Used fields: e_form, gap_pbe, bulk_modulus, shear_modulus
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 60000
- Confidence: 1.0

Evidence:
- P010, PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "Tables 1 and 2 extensively compare the mean absolute errors of the proposed and existing methods for the JARVIS (5 tasks) and MP (4 tasks) datasets."
- P010, PDF page 9, Table 2: Property prediction results on the MP dataset.: "Formation energy Bandgap Bulk modulus Shear modulus 60000 / 5000 / 4239 60000 / 5000 / 4239 4664 / 393 / 393 4664 / 392 / 393"

### UR_P010_03_materials_project

- Paper: `P010` — RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING
- Task: crystal structure modeling for SE(3)-invariant property prediction (`T_P010_01`)
- Stage: evaluation on crystal property prediction tasks (`model_evaluation`, `S_P010_03`)
- Usage role: test
- Purpose: evaluation of CrystalFramer performance on crystal property prediction tasks
- Used fields: e_form, gap_pbe, bulk_modulus, shear_modulus
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 4239
- Confidence: 1.0

Evidence:
- P010, PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "Tables 1 and 2 extensively compare the mean absolute errors of the proposed and existing methods for the JARVIS (5 tasks) and MP (4 tasks) datasets."
- P010, PDF page 9, Table 2: Property prediction results on the MP dataset.: "Formation energy Bandgap Bulk modulus Shear modulus 60000 / 5000 / 4239 60000 / 5000 / 4239 4664 / 393 / 393 4664 / 392 / 393"

### UR_P011_04_materials_project

- Paper: `P011` — A Denoising Pre-training Framework for Accelerating Novel Material Discovery
- Task: crystal property prediction (`T_P011_01`)
- Stage: fine-tuning on downstream property prediction (`model_training`, `S_P011_04`)
- Usage role: training
- Purpose: Fine-tuning the pre-trained model on labeled crystal property prediction tasks.
- Used fields: crystal structure, formation energy, band gap, bulk moduli, shear moduli
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 69239
- Confidence: 1.0

Evidence:
- P011, PDF page 4, Experimental Setup: "The Materials Project dataset aggregates several key crystal property datasets, including formation energy, band gap, bulk moduli, and shear moduli. Among them, 69,239 crystals are labeled with properties of formation energy and band gap, while only 5,451 crystal structures are labeled with the properties of bulk moduli and shear moduli."

### UR_P011_05_materials_project

- Paper: `P011` — A Denoising Pre-training Framework for Accelerating Novel Material Discovery
- Task: crystal property prediction (`T_P011_01`)
- Stage: evaluating property prediction accuracy (`model_evaluation`, `S_P011_05`)
- Usage role: test
- Purpose: Evaluating model performance on crystal property prediction using MAE.
- Used fields: crystal structure, formation energy, band gap, bulk moduli, shear moduli
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P011, PDF page 5, Experimental Results: "The experimental results on the Materials Project benchmark dataset are shown in Table. 4."

### UR_P012_01_materials_project

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

### UR_P012_02_materials_project

- Paper: `P012` — PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction
- Task: Crystal material property prediction (`T_P012_01`)
- Stage: Training PDDFormer (WPDDFormer/UPDDFormer) (`model_training`, `S_P012_02`)
- Usage role: training
- Purpose: Training WPDDFormer and UPDDFormer models on property prediction tasks
- Used fields: crystal structure, formation_energy, bandgap_OPT, total_energy, e_above_hull, bulk_modulus, shear_modulus
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P012, PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."

### UR_P012_03_materials_project

- Paper: `P012` — PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction
- Task: Crystal material property prediction (`T_P012_01`)
- Stage: Evaluation on benchmark property prediction tasks (`model_evaluation`, `S_P012_03`)
- Usage role: test
- Purpose: Evaluating predictive accuracy of WPDDFormer/UPDDFormer on multiple material property tasks
- Used fields: crystal structure, formation_energy, bandgap_OPT, total_energy, e_above_hull, bulk_modulus, shear_modulus
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P012, PDF page 7, 5.1 Experimental Results: "The Materials Project (MP) The experimental results on MP [Chen et al., 2019] are shown in Table 2."

### UR_P012_04_materials_project

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

### UR_P012_05_materials_project

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

### UR_P013_01_materials_project

- Paper: `P013` — Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions
- Task: materials property prediction (`T_P013_01`)
- Stage: using computational data from the MP21 public database (`data_acquisition`, `S_P013_01`)
- Usage role: source
- Purpose: Acquire computational data for training and testing
- Used fields: material compositions, crystal structures, tabulated physical and chemical descriptors
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P013, PDF page 2, unknown: "As training data, we used computational data from the MP21 public database4."

### UR_P016_01_materials_project

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
- P016, PDF page 2, Results: "Table 1 | In-distribution performance for the formation energy prediction ... MP ... Models are arranged in the ascending order of MAEs of the MP dataset from left to right. Best performance is highlighted in bold. TheMP, JARVIS,andOQMD datasets contain146k, 76k,and 1M entries, respectively."

### UR_P017_01_materials_project

- Paper: `P017` — Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules
- Task: Out-of-Distribution Property Prediction (`T_P017_01`)
- Stage: Dataset collection for solids and molecules (`data_acquisition`, `S_P017_01`)
- Usage role: source
- Purpose: solid materials property prediction benchmark
- Used fields: material composition, property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 6331
- Confidence: 1.0

Evidence:
- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "The datasets vary in size, ranging from approximately 300 to 14,000 samples."
- P017, PDF page 3, Table 1: "Elastic Anisotropy 6331"

### UR_P021_01_materials_project

- Paper: `P021` — COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION
- Task: crystal material property prediction (`T_P021_01`)
- Stage: using three widely-used crystal benchmarks (`data_acquisition`, `S_P021_01`)
- Usage role: source
- Purpose: acquire crystal structure data and corresponding property labels for training and evaluation
- Used fields: crystal structure (A, P, L), formation energy, band gap, bulk moduli, shear moduli
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P021, PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."

### UR_P021_04_materials_project

- Paper: `P021` — COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION
- Task: crystal material property prediction (`T_P021_01`)
- Stage: evaluating predictive accuracy on crystal benchmarks (`model_evaluation`, `S_P021_04`)
- Usage role: benchmark
- Purpose: evaluate the performance of the trained models on held-out test sets using standard metrics
- Used fields: formation energy, band gap, bulk moduli, shear moduli
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P021, PDF page 8, EXPERIMENTS: "For JARVIS and MP, we follow the experimental settings of Matformer (Yan et al., 2022) and PotNet (Lin et al., 2023), and use mean absolute error (MAE) as the evaluation metric."

### UR_P022_01_materials_project

- Paper: `P022` — CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING
- Task: Predicting physical properties of materials from their crystal structures (`T_P022_01`)
- Stage: Using Materials Project and JARVIS-DFT datasets (`data_acquisition`, `S_P022_01`)
- Usage role: source
- Purpose: Acquire crystal structure data with DFT-calculated properties for training and evaluation
- Used fields: crystal structures, DFT-calculated properties
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 69239
- Confidence: 1.0

Evidence:
- P022, PDF page 7, EXPERIMENTS: "Materials Project (MEGNet) is a collection of 69,239 materials from the Materials Project database retrieved by Chen et al. (2019). Following Yan et al. (2022), we perform regression tasks of formation energy, bandgap, bulk modulus, and shear modulus."

### UR_P022_03_materials_project

- Paper: `P022` — CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING
- Task: Predicting physical properties of materials from their crystal structures (`T_P022_01`)
- Stage: Training Crystalformer model with mean absolute error loss (`model_training`, `S_P022_03`)
- Usage role: training
- Purpose: Train the Crystalformer model to predict material properties from crystal structures
- Used fields: crystal structures, DFT-calculated properties
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P022, PDF page 7, EXPERIMENTS: "For each regression task in the Materials Project dataset, we train our model by optimizing the mean absolute error loss function via stochastic gradient descent (SGD) with a batch size of 128 materials for 500 epochs."

### UR_P022_04_materials_project

- Paper: `P022` — CRYSTALFORMER: INFINITELY CONNECTED ATTENTION FOR PERIODIC STRUCTURE ENCODING
- Task: Predicting physical properties of materials from their crystal structures (`T_P022_01`)
- Stage: Evaluating model performance with mean absolute errors (`model_evaluation`, `S_P022_04`)
- Usage role: test
- Purpose: Evaluate the trained model's performance on predicting material properties
- Used fields: crystal structures, DFT-calculated properties
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 4239
- Confidence: 1.0

Evidence:
- P022, PDF page 7, EXPERIMENTS: "Tables 1 and 2 summarize the mean absolute errors (MAEs) for totally nine regression tasks of the Materials Project and JARVIS-DFT datasets, comparing our method with eight existing methods"
- P022, PDF page 8, Method: "Formation energy Bandgap Bulk modulus Shear modulus 60000 / 5000 / 4239 60000 / 5000 / 4239 4664 / 393 / 393 4664 / 392 / 393"

### UR_P023_01_materials_project

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

### UR_P024_01_materials_project

- Paper: `P024` — Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets
- Task: materials property prediction (`T_P024_01`)
- Stage: acquisition of diverse materials datasets (`data_acquisition`, `S_P024_01`)
- Usage role: source
- Purpose: Source dataset for pre-training ALIGNN model on formation energy to learn transferable structural representations.
- Used fields: structure files (POSCAR), formation energy labels
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P024, PDF page 2, RESULTS: "A model trained on the formation energy of the MP dataset39 is used as the source model to perform ﬁne-tuning and feature extraction-based transfer learning as formation energy has shown to lead to meaningful representations from large source datasets36, which can then be applied during the model training on the smaller target datasets to improve their predictive performance."

### UR_P024_03_materials_project

- Paper: `P024` — Structure-aware graph neural network based deep transfer learning framework for enhanced predictive analytics on diverse materials datasets
- Task: materials property prediction (`T_P024_01`)
- Stage: training of source model (ALIGNN) on large dataset (`model_training`, `S_P024_03`)
- Usage role: training
- Purpose: Training the source model (ALIGNN) on formation energy of Materials Project to learn transferable structural representations.
- Used fields: structure files (POSCAR), formation energy labels
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P024, PDF page 2, RESULTS: "A model trained on the formation energy of the MP dataset39 is used as the source model to perform ﬁne-tuning and feature extraction-based transfer learning as formation energy has shown to lead to meaningful representations from large source datasets36, which can then be applied during the model training on the smaller target datasets to improve their predictive performance."

### UR_P025_01_materials_project

- Paper: `P025` — Higher-order equivariant neural networks for charge density prediction in materials
- Task: charge density prediction (`T_P025_01`)
- Stage: collecting DFT-computed charge density data (`data_acquisition`, `S_P025_01`)
- Usage role: training
- Purpose: Train and validate ChargE3Net on inorganic materials across the periodic table
- Used fields: atomic species, atomic positions, charge density grid points
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 106171
- Confidence: 1.0

Evidence:
- P025, PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- P025, PDF page 7, Datasets: "For theMPdata,wecollected122,689structuresandassociatedchargedensitiesfromapi.materialsproject.org49. Structures in the dataset that shared composition and space group were identiﬁed as duplicates and only the highest material_idstructurewasincluded,leaving108,683materials.Thedatawas split randomly into training, validation, and test splits with sizes 106,171,512,and2000respectively."

### UR_P026_01_materials_project

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: MD-HIT-composition redundancy reduction (`data_preparation`, `S_P026_01`)
- Usage role: source
- Purpose: Input for MD-HIT-composition redundancy reduction algorithm
- Used fields: compositions
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 86741
- Confidence: 1.0

Evidence:
- P026, PDF page 4, Datasets generation: "We downloaded 125,619 cif files with material structures from the Materials Project database, which includes 89,354 materials with unique compositions. In cases where compositions corresponded to multiple polymorphs, we adopted average material property values by default, with the exception of formation energy property, for which we used the minimum value. Additionally, we excluded mp-101974 (HeSiO2) due to issues with calculating Matscholar features. After eliminating formulas with over 50 atoms, we obtained a non-duplicate composition dataset with 86,741 samples..."

### UR_P026_02_materials_project

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: MD-HIT-structure redundancy reduction (`data_preparation`, `S_P026_02`)
- Usage role: source
- Purpose: Input for MD-HIT-structure redundancy reduction algorithm
- Used fields: CIF files
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 125619
- Confidence: 1.0

Evidence:
- P026, PDF page 4, Datasets generation: "We downloaded 125,619 cif files with material structures from the Materials Project database, which includes 89,354 materials with unique compositions."

### UR_P026_03_materials_project

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: download and curate Materials Project datasets (`data_acquisition`, `S_P026_03`)
- Usage role: source
- Purpose: Raw material data acquisition and initial filtering for downstream redundancy control
- Used fields: CIF files, compositions, formation energy per atom, band gaps
- Filter conditions: excluded mp-101974 (HeSiO2), eliminated formulas with over 50 atoms
- Construction method: Not stated
- Sample count: 125619
- Confidence: 1.0

Evidence:
- P026, PDF page 4, Datasets generation: "We downloaded 125,619 cif files with material structures from the Materials Project database, which includes 89,354 materials with unique compositions. In cases where compositions corresponded to multiple polymorphs, we adopted average material property values by default, with the exception of formation energy property, for which we used the minimum value. Additionally, we excluded mp-101974 (HeSiO2) due to issues with calculating Matscholar features. After eliminating formulas with over 50 atoms, we obtained a non-duplicate composition dataset with 86,741 samples..."

### UR_P027_06_materials_project

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: generation of Γ-phonon database for Materials Project (`candidate_generation`, `S_P027_06`)
- Usage role: candidate_pool
- Purpose: Input material pool for generating Γ-phonon predictions using the trained MVN model
- Used fields: atomic coordinates, unit cell vectors, atomic numbers, chemical formula, space group
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 146323
- Confidence: 1.0

Evidence:
- P027, PDF page 37, VII Γ-PHONON DATABASE: "here we present a new phonon database containing the phonon spectra for the entire 146,323 Materials in Materials Project (MP) as of 2022 computed by the MVN approach."

### UR_P028_01_materials_project

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: populating reference benchmark datasets (`data_acquisition`, `S_P028_01`)
- Usage role: source
- Purpose: reference benchmark dataset for AI methods
- Used fields: id, structure, formation_energy, bandgap, elastic_tensor, thermal_conductivity, dielectric_tensor, bandstructure
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 10, Methods: "DFT datasets such as JARVIS-DFT70,71, Materials Project (MP)65, Tight binding three-body dataset (TB3)72, Quantum-Machine 9 (QM9)139,140."

### UR_P038_01_materials_project

- Paper: `P038` — Rational design of nanoscale stabilized oxide catalysts for OER with OC22
- Task: Rational design of nanoscale stabilized oxide catalysts for OER (`T_P038_01`)
- Stage: Slab generation from Materials Project (`data_acquisition`, `S_P038_01`)
- Usage role: source
- Purpose: Source of bulk oxide materials for slab generation.
- Used fields: bulk_formula, final_structure
- Filter conditions: unit cells < 100 atoms, excludes slabs > 200 atoms
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P038, PDF page 2, 2.1 Slab generation: "The bulk materials used for slab construction in this study were obtained from the Materials Project."

## Aggregated evidence

- , PDF page 8, EXPERIMENTS: "• Materials Project (MP) Database: We use stable structures retrieved from the Materials Project (Jain et al., 2020), comprising 122,959 entries with annotated formation energy, band gap, and metal/non-metal classification labels. Additionally, 9,473 of these entries include mechanical properties such as bulk modulus, shear modulus and Young’s modulus."
- , PDF page 1, ABSTRACT: "Extensive experiments are conducted on Materials Project, JARVIS-DFT, and MatBench, demonstrating that the proposed model achieves state-of-the-art performance."
- , PDF page 8, EXPERIMENTS: "• Materials Project (MP) Database: We use stable structures retrieved from the Materials Project (Jain et al., 2020), comprising 122,959 entries with annotated formation energy, band gap, and metal/non-metal classification labels. Additionally, 9,473 of these entries include mechanical properties such as bulk modulus, shear modulus and Young’s modulus."
- , PDF page 7, EXPERIMENTAL SETUP: "For our primary benchmark experiments, we use data from the Materials Project, one of the largest databases of computational material properties (Jain et al., 2013)."
- , PDF page 8, MATERIAL PROPERTY PREDICTION: "Having validated our encoding module, we now evaluate the full CFT architecture on the task of predicting material properties from the Materials Project dataset."
- , PDF page 8, MATERIAL PROPERTY PREDICTION: "Table 1 shows the test MAE for CFT and baseline models. Our CFT model achieves competitive performance across all four properties and outperforms all baselines on Total Energy and Shear Moduli prediction."
- , PDF page 19, WHY PRETRAIN?: "Table 3 shows that pretraining the positional encodings improves property prediction performance across the board, in comparison to end-to-end training with random initialization of the positional encodings."
- , PDF page 9, ZERO-SHOT GENERALIZATION TO UNSEEN SPACE GROUPS: "The core hypothesis behind our adaptive architecture is that, by explicitly parameterizing the group constraints, CFT can generalize to materials from previously unseen space groups. We test this hypothesis in a zero-shot setting by holding out all space groups containing inversion symmetry from the training set."
- , PDF page 7, Methods: "We recorded a snapshot of energies, forces, stresses and magnetic moments for all MP ionic steps on 15 March 2023 as the canonical training set for Matbench Discovery, and provide convenience functions through our Python package for easily feeding those data into future model submissions to our benchmark."
- , PDF page 7, Methods: "Our benchmark defines the training set as all data available from the v.2022.10.28 MP release. We recorded a snapshot of energies, forces, stresses and magnetic moments for all MP ionic steps on 15 March 2023 as the canonical training set for Matbench Discovery..."
- , PDF page 11, Methods: "Before using these databases, data preprocessing was required. After excluding noble gas and radioactive elements, the MP database contained 85,014 compounds with information on thermodynamic properties such as formation energy."
- , PDF page 11, Methods: "Compounds with a ΔHd below 0 meV/atom were considered stable and are labeled accordingly."
- , PDF page 4, Performance benchmarking against existing models: "All models were trained using data sourced from the MP dataset, as detailed in the Methods section."
- , PDF page 4, Performance benchmarking against existing models: "In this section, we performed a comprehensive comparison between our proposed method and several state-of-the-art baselines... to validate the effectiveness of our proposed ECSG."
- , PDF page 13, First principles calculation: "To construct the convex hull for each set of elements comprising A-A′-B-B′-O, the total energy data of all compounds in the MP database was considered and extracted using the database API."
- , PDF page 3, Preliminary high-throughput screening: "Initially, we start by acquiring all the materials from the MP database based on its API, resulting in a total of 1,54,718 entries saved in a JSON file as the Python dictionary object."
- , PDF page 4, Data collection and analysis: "We collected the dataset used in this work from the Materials Project database40 using the Materials Project free API as of November 1, 2022."
- , PDF page 4, Data collection and analysis: "We generated the crystal text descriptions using Robocrystallographer41, a tool that generates a deterministic human readable text description of a structure given its CIF file."
- , PDF page 4, Data collection and analysis: "We collect the data of band gap, formation energy per atom (FEPA), energy above hull (Ehull), crystal volume, energy per atom (EPA), and an indicator of whether the band gap is direct or indirect (Is-gap-direct)."
- , PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- , PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "Tables 1 and 2 extensively compare the mean absolute errors of the proposed and existing methods for the JARVIS (5 tasks) and MP (4 tasks) datasets."
- , PDF page 9, Table 2: Property prediction results on the MP dataset.: "Formation energy Bandgap Bulk modulus Shear modulus 60000 / 5000 / 4239 60000 / 5000 / 4239 4664 / 393 / 393 4664 / 392 / 393"
- , PDF page 8, 5.1 CRYSTAL PROPERTY PREDICTION: "Tables 1 and 2 extensively compare the mean absolute errors of the proposed and existing methods for the JARVIS (5 tasks) and MP (4 tasks) datasets."
- , PDF page 9, Table 2: Property prediction results on the MP dataset.: "Formation energy Bandgap Bulk modulus Shear modulus 60000 / 5000 / 4239 60000 / 5000 / 4239 4664 / 393 / 393 4664 / 392 / 393"
- , PDF page 4, Experimental Setup: "The Materials Project dataset aggregates several key crystal property datasets, including formation energy, band gap, bulk moduli, and shear moduli. Among them, 69,239 crystals are labeled with properties of formation energy and band gap, while only 5,451 crystal structures are labeled with the properties of bulk moduli and shear moduli."
- , PDF page 5, Experimental Results: "The experimental results on the Materials Project benchmark dataset are shown in Table. 4."
- , PDF page 4, 4.3 Crystal Graph Construction: "By introducing PDD, we constructed a general complete and continuous multi-edge crystal graph. In the graph, node features are xi. An edge is established from node j to node i when the Euclidean distance |ej′i|2 between a duplicate of j and i satisfies |ej′i|2 = |pj + k′1l1 + k′2l2 + k′3l3 −pi|2 ≤r, where r ∈R is the cutoff radius. Next, we construct a PDD row for each atom. Since directly representing PDD as edge features is impractical, we retain its matrix form and incorporate it into the construction of the multi-edge crystal graph to reflect the global information of the crystal structure. Therefore, we represent the constructed crystal graph as G = (X, XI, E, PDD)."
- , PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."
- , PDF page 7, 5.1 Experimental Results: "The Materials Project (MP) The experimental results on MP [Chen et al., 2019] are shown in Table 2."
- , PDF page 7, 5.2 Ablation Studies: "In this section, we demonstrate the impact of introducing (W/U)PDD on the representation learning of crystal materials through ablation studies. Specifically, we conducted experiments on the MP and JARVIS datasets, using testing mean absolute error (MAE) as the quantitative evaluation metric, comparing the results for Band Gap and Ehull tasks, as shown in Table 4."
- , PDF page 2, Introduction: "Finally, we employ the Earth Mover’s Distance (EMD) [Rubner et al., 2000] to assess the continuity of crystal graphs, demonstrating that WPDD crystal graphs constructed using only Euclidean distances maintain continuity and general completeness under slight atomic position perturbations, providing a more accurate depiction of actual crystal structures."
- , PDF page 2, unknown: "As training data, we used computational data from the MP21 public database4."
- , PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- , PDF page 2, Results: "Table 1 | In-distribution performance for the formation energy prediction ... MP ... Models are arranged in the ascending order of MAEs of the MP dataset from left to right. Best performance is highlighted in bold. TheMP, JARVIS,andOQMD datasets contain146k, 76k,and 1M entries, respectively."
- , PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- , PDF page 2, Results: "The datasets vary in size, ranging from approximately 300 to 14,000 samples."
- , PDF page 3, Table 1: "Elastic Anisotropy 6331"
- , PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."
- , PDF page 8, EXPERIMENTS: "For JARVIS and MP, we follow the experimental settings of Matformer (Yan et al., 2022) and PotNet (Lin et al., 2023), and use mean absolute error (MAE) as the evaluation metric."
- , PDF page 7, EXPERIMENTS: "Materials Project (MEGNet) is a collection of 69,239 materials from the Materials Project database retrieved by Chen et al. (2019). Following Yan et al. (2022), we perform regression tasks of formation energy, bandgap, bulk modulus, and shear modulus."
- , PDF page 7, EXPERIMENTS: "For each regression task in the Materials Project dataset, we train our model by optimizing the mean absolute error loss function via stochastic gradient descent (SGD) with a batch size of 128 materials for 500 epochs."
- , PDF page 7, EXPERIMENTS: "Tables 1 and 2 summarize the mean absolute errors (MAEs) for totally nine regression tasks of the Materials Project and JARVIS-DFT datasets, comparing our method with eight existing methods"
- , PDF page 8, Method: "Formation energy Bandgap Bulk modulus Shear modulus 60000 / 5000 / 4239 60000 / 5000 / 4239 4664 / 393 / 393 4664 / 392 / 393"
- , PDF page 6, Experimental Settings: "We collect 800K untagged crystal graph data from two popular materials databases, Materials Project (MP) (Jain et al. 2013) and OQMD (Saal et al. 2013), to pre-train the CrysDiff model."
- , PDF page 2, RESULTS: "A model trained on the formation energy of the MP dataset39 is used as the source model to perform ﬁne-tuning and feature extraction-based transfer learning as formation energy has shown to lead to meaningful representations from large source datasets36, which can then be applied during the model training on the smaller target datasets to improve their predictive performance."
- , PDF page 2, RESULTS: "A model trained on the formation energy of the MP dataset39 is used as the source model to perform ﬁne-tuning and feature extraction-based transfer learning as formation energy has shown to lead to meaningful representations from large source datasets36, which can then be applied during the model training on the smaller target datasets to improve their predictive performance."
- , PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- , PDF page 7, Datasets: "For theMPdata,wecollected122,689structuresandassociatedchargedensitiesfromapi.materialsproject.org49. Structures in the dataset that shared composition and space group were identiﬁed as duplicates and only the highest material_idstructurewasincluded,leaving108,683materials.Thedatawas split randomly into training, validation, and test splits with sizes 106,171,512,and2000respectively."
- , PDF page 4, Datasets generation: "We downloaded 125,619 cif files with material structures from the Materials Project database, which includes 89,354 materials with unique compositions. In cases where compositions corresponded to multiple polymorphs, we adopted average material property values by default, with the exception of formation energy property, for which we used the minimum value. Additionally, we excluded mp-101974 (HeSiO2) due to issues with calculating Matscholar features. After eliminating formulas with over 50 atoms, we obtained a non-duplicate composition dataset with 86,741 samples..."
- , PDF page 4, Datasets generation: "We downloaded 125,619 cif files with material structures from the Materials Project database, which includes 89,354 materials with unique compositions."
- , PDF page 4, Datasets generation: "We downloaded 125,619 cif files with material structures from the Materials Project database, which includes 89,354 materials with unique compositions. In cases where compositions corresponded to multiple polymorphs, we adopted average material property values by default, with the exception of formation energy property, for which we used the minimum value. Additionally, we excluded mp-101974 (HeSiO2) due to issues with calculating Matscholar features. After eliminating formulas with over 50 atoms, we obtained a non-duplicate composition dataset with 86,741 samples..."
- , PDF page 37, VII Γ-PHONON DATABASE: "here we present a new phonon database containing the phonon spectra for the entire 146,323 Materials in Materials Project (MP) as of 2022 computed by the MVN approach."
- , PDF page 10, Methods: "DFT datasets such as JARVIS-DFT70,71, Materials Project (MP)65, Tight binding three-body dataset (TB3)72, Quantum-Machine 9 (QM9)139,140."
- , PDF page 2, 2.1 Slab generation: "The bulk materials used for slab construction in this study were obtained from the Materials Project."
