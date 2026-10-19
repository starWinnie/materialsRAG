# Dataset: JARVIS-DFT

- Dataset ID: `D_jarvis_dft`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Joint Automated Repository for Various Integrated Simulations
- JARVIS
- JARVIS dataset
- JARVIS-DFT
- Joint Automated Repository for Various Integrated Simulations (JARVIS)
- JARVIS-density functional theory (DFT)
- JARVIS-DFT database

## Observed material scopes

- inorganic compounds
- crystals
- crystal structures
- crystalline materials
- inorganic crystalline solids
- solid-state materials
- metals
- semiconductors
- insulators
- 3D bulk materials
- 2D layered materials
- multicomponent systems up to senary compounds
- materials with up to 6 components, 201 space groups, 7 crystal systems

## Observed research tasks

- Predicting thermodynamic stability of inorganic compounds
- Generate universal atomic embeddings (UAEs) for crystal property prediction
- Accurate piezoelectric tensor prediction
- crystal property prediction
- Crystal material property prediction
- Probing out-of-distribution generalization in machine learning for materials
- Predicting solid-state material properties
- generation of natural language-material narratives
- benchmarking machine learning force fields (MLFFs)
- fast screening and mapping energy landscape for multicomponent systems

## Observed research stages

- data_acquisition
- label_generation
- model_evaluation
- model_training
- candidate_screening
- data_preparation
- computational_validation

## Observed properties

- formation energy
- decomposition energy (ΔHd)
- bandgap
- bandgaps
- formation energies
- energy above hull
- total energy
- Bandgap(OPT)
- Ehull
- Bandgap(MBJ)
- Bulk Moduli(Kv)
- Shear Moduli(Gv)
- band gap
- bulk modulus
- bandgap (MBJ)
- bandgap (OPT)
- shear modulus (Gv)
- bulk modulus (Kv)
- SLME (%)
- spillage
- van der Waals correction with optimized Becke88 functional (OptB88vdW) bandgaps
- dielectric constants
- Tran-Blaha modified Becke Johnson potential (MBJ) bandgaps
- shear modulus
- magnetic moment
- DFPT-based maximum piezoelectric coefficients
- Boltztrap-based Seebeck coefficient
- power factor
- electric field gradient
- exfoliation energies
- energy above convex hull
- solar-cell efficiency (SLME)
- topological spin-orbit spillage
- effective masses
- convex hull stability
- metal/non-metal classification
- magnetic/non-magnetic classification
- formation energy per atom
- density
- space group symbol
- crystal system
- total magnetization
- oxide type
- ehull
- SLME
- relaxed structural data (primitive lattice vectors, volume)
- elastic properties (bulk modulus, elastic tensor)
- phonon band structure
- vacancy calculations
- surfaces
- band gap (calculated with vdW-DF-optB88)
- space group
- atomic number
- chemical formula type
- Wyckoff site
- dimensionality
- exfoliation energy
- OPT bandgap
- MBJ bandgap
- static refractive index (OPT and MBJ)
- static dielectric constants

## Observed fields

- chemical formula
- ΔHd
- stability label
- CIF files
- atomic species
- atomic coordinates
- formation energy
- bandgap
- crystal structure
- formation_energy
- energy_above_hull
- total_energy
- property labels
- band gap
- bulk modulus
- crystal structure (A, P, L)
- atom features
- fractional coordinates
- lattice matrix
- target property values
- structure
- formation_energy_per_atom
- bandgap_optb88vdw
- bandgap_mbj
- dielectric_constant_optb88vdw
- dielectric_constant_mbj
- dielectric_constant_dfpt
- bulk_modulus
- shear_modulus
- magnetic_moment
- piezoelectric_max_coefficient
- seebeck_coefficient
- power_factor
- electric_field_gradient
- exfoliation_energy
- slme
- spin_orbit_spillage
- effective_mass_electron
- effective_mass_hole
- is_metal
- is_magnetic
- formation energy per atom
- energy above hull
- density
- space group symbol
- crystal system
- total magnetization
- oxide type
- bandgap (OPT)
- bandgap (MBJ)
- total energy
- shear modulus
- ehull
- spillage
- primitive lattice vectors
- volume
- elastic tensor
- phonon band structure
- vacancy formation energy
- surface energy
- space group
- atomic number
- Wyckoff site
- dimensionality
- exfoliation energy
- OPT bandgap
- MBJ bandgap
- OPT-nx
- OPT-ny
- OPT-nz
- MBJ-nx
- MBJ-ny
- MBJ-nz
- static dielectric constants

## Usage evidence

- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): source in Collecting DFT-computed thermodynamic stability data from public databases — Acquire labeled training and test data for compound stability
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): label_source in Assigning stability labels based on DFT-derived decomposition energy thresholds — Assign stability labels based on DFT-derived decomposition energy thresholds
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): benchmark in Benchmarking predictive performance across multiple metrics and datasets — Benchmark predictive performance across multiple metrics
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): source in Acquire crystal structure datasets — Source dataset for acquiring crystal structure and property data for training and evaluation
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): test in Evaluate ct-UAE transfer performance on back-end models — Evaluating ct-UAE transfer performance on back-end models (CGCNN) for formation energy and bandgap prediction
- P007 (Accurate piezoelectric tensor prediction with equivariant attention tensor graph neural network): source in Data acquisition from computational databases — To acquire piezoelectric tensor data for bulk crystals
- P011 (A Denoising Pre-training Framework for Accelerating Novel Material Discovery): training in fine-tuning for property prediction — Fine-tune the pre-trained model on downstream crystal property prediction tasks.
- P011 (A Denoising Pre-training Framework for Accelerating Novel Material Discovery): test in evaluation of property prediction accuracy — Evaluate the accuracy of crystal property prediction using Mean Absolute Error (MAE).
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): source in Use of benchmark crystal datasets — Acquire crystal structure and property data for training and evaluation
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): training in Training PDDFormer architecture — Train the PDDFormer neural network to map crystal graphs to property values
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): test in Quantitative evaluation on benchmark tasks — Assess predictive accuracy of trained models using mean absolute error (MAE) on held-out test sets
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): benchmark in Ablation studies on (W/U)PDD contribution — Isolate and quantify the impact of WPDD/UPDD integration on model performance via ablation studies
- P016 (Probing out-of-distribution generalization in machine learning for materials): source in Selection of ab initio-derived materials databases — Selection of ab initio-derived materials database for OOD evaluation
- P016 (Probing out-of-distribution generalization in machine learning for materials): training in Preprocessing and splitting for OOD tasks — Constructing OOD tasks via leave-one-X-out splitting based on chemistry or structural symmetry criteria
- P016 (Probing out-of-distribution generalization in machine learning for materials): training in Training representative ML models on each OOD task — Training ML models (RF, XGB, ALIGNN, GMP, LLM-Prop) on OOD training splits
- P016 (Probing out-of-distribution generalization in machine learning for materials): test in Evaluating OOD performance with MAE and R2 — Evaluating OOD performance of trained models using MAE and R2 metrics
- P016 (Probing out-of-distribution generalization in machine learning for materials): computational_validation in Inspecting materials representations via UMAP and kernel density estimation — Inspecting materials representations via UMAP and kernel density estimation to distinguish statistically OOD from representationally OOD test data
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in using three widely-used crystal benchmarks — evaluate the expressiveness of iComFormer and eComFormer models
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): test in evaluating downstream property prediction performance — evaluating downstream property prediction performance
- P046 (Atomistic Line Graph Neural Network for Improved Materials Property Predictions): source in Acquiring JARVIS-DFT and Materials Project datasets — Acquire precomputed DFT-calculated material property data for training and evaluation.
- P046 (Atomistic Line Graph Neural Network for Improved Materials Property Predictions): label_source in Using DFT-computed property values as labels — Provide ground-truth property values (formation energy, band gaps, dielectric constants, moduli, magnetic moment, etc.) as regression or classification targets.
- P046 (Atomistic Line Graph Neural Network for Improved Materials Property Predictions): training in Training ALIGNN models with MSE and NLL loss — Train ALIGNN models using regression and classification objectives. / Validate ALIGNN models during training. / Evaluate final model performance on held-out test set.
- P046 (Atomistic Line Graph Neural Network for Improved Materials Property Predictions): test in Evaluating model performance using MAE and ROC AUC — Evaluate final model performance on held-out test set.
- P051 (1.5 million materials narratives generated by chatbots): source in Dataset Collection — To acquire raw material data with computed properties for narrative generation.
- P057 (Latent Diffusion Pretraining for Crystal Property Prediction): training in fine-tuning for property prediction — fine-tune pretrained encoder with lightweight property predictor using limited labeled data
- P057 (Latent Diffusion Pretraining for Crystal Property Prediction): test in downstream property prediction evaluation — evaluate fine-tuned model performance on crystal property prediction tasks using MAE on test sets
- P059 (CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties): source in acquiring initial structures and reference data — acquire initial atomic structures and ground-truth reference data for benchmarking
- P064 (Machine learning with force-field inspired descriptors for materials: fast screening and mapping energy landscape): source in collect training data from JARVIS-DFT database — Acquire DFT-computed property data for bulk and 2D materials to train ML models

## Dataset evidence

- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- P005, PDF page 11, Methods: "The same data processing method was applied to the OQMD and JARVIS databases, and datasets in unknown spaces."
- P005, PDF page 2, Results: "In our experiments, the proposed model yields an AUC of 0.988 in predicting compound stability within the Joint Automated Repository for Various Integrated Simulations (JARVIS) database."
- P006, PDF page 4: "The ability and transferability of the universal atomic embedding are further tested on different databases and tasks. Each is cut into 8:1:1 for training, validation, and testing. Details on the dataset can be found in Supplementary 2A. As for the Jarvis dataset49, the result is shown in Table 1."
- P011, PDF page 3, Method: "The benchmark for crystal property prediction is well established. There are two standard benchmark datasets, JARVIS and Materials Project (Choudhary et al. 2020; Chen et al. 2019), to evaluate the performance of our model."
- P011, PDF page 4, Experiments: "The JARVIS dataset contains 55,722 materials with critical crystal properties for functional material design, including bandgaps, formation energies, energy above hull, total energy and so on."
- P012, PDF page 1, Abstract: "Comprehensive evaluation results show that WPDDFormer achieves state-of-the-art predictive accuracy across tasks on benchmark datasets such as the Materials Project and JARVIS-DFT."
- P012, PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."
- P012, PDF page 7, 5.1 Experimental Results: "The quantitative results for JARVIS [Choudhary et al., 2020] are shown in Table 1."
- P016, PDF page 2, Evaluation setup: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS)29,30, Materials Project (MP)31, and the Open Quantum Materials Database (OQMD)32."
- P016, PDF page 8, Methods: "We use the snapshots of the JARVIS, Materials Project, and OMQD databases used in our previous study47, available on Zenodo at https://zenodo.org/records/8200972. The snapshots correspond the JARVIS 2022.12.12 version, the Materials Project 2021.11.10 version, and the OQMD v1.6 version (published in November 2023), and they have been preprocessed to remove materials with formation energies larger than 5 eV/atom."
- P021, PDF page 8, 5 EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."
- P023, PDF page 6, Experimental Settings: "we select the 2021.8.18 version of JARVIS-DFT (Choudhary et al. 2020), another popular materials database, for the downstream property prediction task. JARVIS-DFT consists of 55,722 materials with 19 properties, like formation energy, bandgap, total energy, bulk modulus, etc., which depend significantly on crystal structures and atom features."
- P103, PDF page 1, unknown: "We train 44 models for predicting several solid-state material properties available in the JARVIS-DFT and materials-project databases."
- P103, PDF page 3, Results and discussion: "We train several crystalline material properties from JARVIS-density functional theory (DFT) 34-44 and materials project45 datasets."
- P103, PDF page 8, F. Model performance: "Similarly, we use 2021.5.16 version of JARVIS-DFT dataset, which consists of 48525 materials with several properties such as van der Waals correction with optimized Becke88 functional (OptB88vdW)48 bandgaps, formation energies, dielectric constants, Tran-Blaha modified Becke Johnson potential (MBJ)49 bandgaps and dielectric constants, bulk, shear modulus, magnetic moment, density functional perturbation theory (DFPT) based maximum piezoelectric coefficients, Boltztrap50 based Seebeck coefficient, power factor, maximum absolute value of electric field gradient."
- P103, PDF page 9, unknown: "Similarly, we train ALIGNN models on the JARVIS-DFT34-44 dataset which consists of data for 48525 materials. In addition to properties such as formation energies, and bandgaps it also consists several unique quantities such as solar-cell efficiency (spectroscopic limited maximum efficiency, SLME), topological spin-orbit spillage, dielectric constant with (єx (DFPT)) and without ionic contributions (єx (OPT, MBJ)), exfoliation energies for two-dimensional (2D), electric field gradients (EFG), Voigt bulk (Kv) and shear modulus (Gv), energy above convex hull (ehull), maximum piezoelectric stress (eij) and strain (dij) tensors, n-type and p-type Seebeck coefficient and power factors (PF), crystallographic averages of electron (me) and hole (mh) effective masses."
- P108, PDF page 1, ABSTRACT: "We have generated a dataset of 1,494,017 natural language-material paragraphs based on combined OQMD, Materials Project, JARVIS, COD and AFLOW2 databases"
- P108, PDF page 2, Methods: "1. Dataset Collection: We obtained material data from publicly available repositories, the joint automated repository for various integrated simulations (JARVIS)18."
- P114, PDF page 5, 4.1. Datasets for Pretraining and Downstream Tasks: "Further, for the downstream crystal property prediction task, we primarily use two benchmark (property-labeled) crystal datasets: Materials Project (MP-2018.6.1) (Chen et al., 2019) and JARVIS-DFT (Choudhary et al., 2020). Note that these are DFT benchmark datasets, where all properties are derived from DFT-based calculations. The JARVIS dataset is a widely used benchmark containing 55,722 crystal structures, and following prior studies, we focus on nine properties: formation energy, bandgap (OPT), bandgap (MBJ), total energy, bulk modulus, shear modulus, ehull, spillage, and SLME."
- P116, PDF page 2: "A majority of the reference data used to compare our uMLFF results to were obtained from the JARVIS-DFT database, which contains relaxed structural data (primitive lattice vectors, volume), elastic properties (bulk modulus, elastic tensor), phonon band structure,14,15 vacancy calculations45 and surfaces.46"
- P116, PDF page 2: "All of the DFT data in JARVIS was computed with the vdW-DF-optB8847 functional."
- P116, PDF page 3: "In addition, Table S1 and S2 give detailed information of the chemical composition, crystal structure and band gap for each material, where we see that the set contains 28 metals (zero band gap), 14 insulators (band gap above 3 eV) and 62 semiconductors (band gap between 0 and 3 eV)."
- P121, PDF page 1, ABSTRACT: "The training data consists of 24549 bulk and 616 monolayer materials taken from JARVIS-DFT database."
- P121, PDF page 5, III. TRAINING DATA AND ALGORITHM: "For model training, we use our publicly available JARVIS-DFT database [5] which (at the time of writing) consists of 24549 bulk and 616 monolayer 2D materials with 24549 formation energies, 22404 OptB88vdW (OPT) and 10499 TBmBJ (MBJ) bandgaps and static dielectric constants [28], 10954 bulk and shear modulus [29] and 616 exfoliation energies for 2D layered materials."
