# Dataset: JARVIS-DFT

- Dataset ID: `D_jarvis_dft`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- JARVIS-DFT
- dft_3d
- Joint Automated Repository for Various Integrated Simulations
- JARVIS
- JARVIS dataset
- JARVIS database
- Joint Automated Repository for Various Integrated Simulations (JARVIS)
- JARVIS-DFT database
- 2021.8.18 version of JARVIS-DFT

## Observed material scopes

- inorganic compounds
- crystals
- crystal structures
- crystalline materials
- inorganic crystalline solids
- bulk crystals
- crystal materials
- crystalline solids
- inorganic materials

## Observed research tasks

- Predicting thermodynamic stability of inorganic compounds
- Generate universal atomic embeddings (UAEs) for crystal property prediction
- Accurate piezoelectric tensor prediction
- crystal property prediction
- Crystal material property prediction
- Probing out-of-distribution generalization in machine learning for materials
- crystal tensor property prediction

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
- energy above the hull
- piezoelectric tensor (eijk)
- dielectric tensor
- piezoelectric tensor
- elastic tensor


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

## Dataset evidence

- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- P005, PDF page 11, Methods: "The same data processing method was applied to the OQMD and JARVIS databases, and datasets in unknown spaces."
- P005, PDF page 2, Results: "In our experiments, the proposed model yields an AUC of 0.988 in predicting compound stability within the Joint Automated Repository for Various Integrated Simulations (JARVIS) database."
- P006, PDF page 4: "The ability and transferability of the universal atomic embedding are further tested on different databases and tasks. Each is cut into 8:1:1 for training, validation, and testing. Details on the dataset can be found in Supplementary 2A. As for the Jarvis dataset49, the result is shown in Table 1."
- P007, PDF page 7, Data availability: "The two-dimensional materials used in this study were obtained from the C2DB database (https://c2db.fysik.dtu.dk/), while the bulk material data were sourced from the Materials Project and the JARVIS database (https://jarvis.nist.gov/login?next=/jarvisdft/)."
- P011, PDF page 3, Method: "The benchmark for crystal property prediction is well established. There are two standard benchmark datasets, JARVIS and Materials Project (Choudhary et al. 2020; Chen et al. 2019), to evaluate the performance of our model."
- P011, PDF page 4, Experiments: "The JARVIS dataset contains 55,722 materials with critical crystal properties for functional material design, including bandgaps, formation energies, energy above hull, total energy and so on."
- P012, PDF page 1, Abstract: "Comprehensive evaluation results show that WPDDFormer achieves state-of-the-art predictive accuracy across tasks on benchmark datasets such as the Materials Project and JARVIS-DFT."
- P012, PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."
- P012, PDF page 7, 5.1 Experimental Results: "The quantitative results for JARVIS [Choudhary et al., 2020] are shown in Table 1."
- P016, PDF page 2, Evaluation setup: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS)29,30, Materials Project (MP)31, and the Open Quantum Materials Database (OQMD)32."
- P016, PDF page 8, Methods: "We use the snapshots of the JARVIS, Materials Project, and OMQD databases used in our previous study47, available on Zenodo at https://zenodo.org/records/8200972. The snapshots correspond the JARVIS 2022.12.12 version, the Materials Project 2021.11.10 version, and the OQMD v1.6 version (published in November 2023), and they have been preprocessed to remove materials with formation energies larger than 5 eV/atom."
- P021, PDF page 8, 5 EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."
- P023, PDF page 6, Experimental Settings: "we select the 2021.8.18 version of JARVIS-DFT (Choudhary et al. 2020), another popular materials database, for the downstream property prediction task. JARVIS-DFT consists of 55,722 materials with 19 properties, like formation energy, bandgap, total energy, bulk modulus, etc., which depend significantly on crystal structures and atom features."
