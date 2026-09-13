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

- crystals
- inorganic compounds
- bulk crystals
- crystal materials
- crystalline materials
- crystalline solids
- inorganic materials

## Observed research tasks

- Crystal Property Prediction
- Predicting thermodynamic stability of inorganic compounds
- Generating universal atomic embeddings (UAEs) for crystal property prediction
- Accurate piezoelectric tensor prediction
- Crystal material property prediction
- Probing out-of-distribution generalization in machine learning for materials
- crystal tensor property prediction

## Observed research stages

- data_acquisition
- model_evaluation
- computational_validation
- model_training

## Observed properties

- formation energy
- band gap
- bulk modulus
- shear modulus
- total energy
- energy above the hull
- decomposition energy (ΔHd)
- bandgap
- piezoelectric tensor (eijk)
- bandgaps
- formation energies
- energy above hull
- bulk moduli
- shear moduli
- Bandgap(OPT)
- Ehull
- Bandgap(MBJ)
- Bulk Moduli(Kv)
- Shear Moduli(Gv)
- dielectric tensor
- piezoelectric tensor
- elastic tensor
- SLME
- spillage

## Observed fields

- structure
- formation energy
- band gap
- bulk modulus
- shear modulus
- total energy
- energy above the hull
- chemical formula
- thermodynamic stability
- ΔHd
- formation energy (Ef)
- bandgap (Eg)
- crystal structure
- piezoelectric tensor
- bulk moduli
- shear moduli
- energy above hull
- crystal structure M = (A, P, L)
- tensor property values
- crystal structure (A, P, L)
- property labels
- crystal structure (A, F, L)
- target property values

## Usage evidence

- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): source in Retrieving crystal datasets — retrieve crystal structure and property data for benchmarking
- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): test in Evaluating model performance on benchmark datasets — evaluate model performance on crystal property prediction tasks
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): source in Collecting thermodynamic stability data from DFT-computed databases — Acquire labeled stability data for training and evaluation
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): test in Benchmarking model performance using multiple metrics — Benchmarking model performance using multiple metrics
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): computational_validation in Validating predictions via first-principles DFT calculations — Validating predictions via first-principles DFT calculations
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): source in Collecting crystal structure datasets — Data acquisition for formation energy and bandgap evaluation
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): benchmark in Evaluating ct-UAE transfer performance on property prediction — Evaluating ct-UAE transfer performance on formation energy and bandgap prediction
- P007 (Accurate piezoelectric tensor prediction with equivariant attention tensor graph neural network): source in Data acquisition from computational databases — To acquire piezoelectric tensor data for bulk crystals
- P011 (A Denoising Pre-training Framework for Accelerating Novel Material Discovery): training in fine-tuning on downstream property prediction tasks — Fine-tune the pre-trained model on labeled crystal property prediction tasks.
- P011 (A Denoising Pre-training Framework for Accelerating Novel Material Discovery): test in evaluation of property prediction performance — Evaluate the accuracy of crystal property prediction using MAE.
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): source in Acquisition of crystal structure datasets — Acquisition of benchmark crystal structure dataset with known properties
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): training in Training PDDFormer models (WPDDFormer/UPDDFormer) — Training PDDFormer models on crystal graphs with ground-truth property labels
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): test in Evaluation on benchmark property prediction tasks — Evaluation of trained models on held-out test set using MAE metric
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): computational_validation in Continuity and completeness validation using EMD and theoretical proof — Continuity and completeness validation using EMD and theoretical proof
- P016 (Probing out-of-distribution generalization in machine learning for materials): source in Selection of ab initio-derived materials databases — Acquisition of large, diverse, and preprocessed materials dataset for robust OOD evaluation.
- P020 (A Space Group Symmetry Informed Network for O(3) Equivariant Crystal Tensor Prediction): source in curating a dataset — source database for curating the crystal tensor property dataset
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in using three widely-used crystal benchmarks — acquire crystal structure data and corresponding property labels for training and evaluation
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in evaluating ComFormer variants on crystal benchmarks — assess the predictive accuracy of the trained models on various crystal property prediction tasks
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): training in collecting labeled crystal property data — fine-tuning for crystal property prediction and evaluation on nine properties
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): test in downstream task evaluation — downstream task evaluation on nine properties using MAE

## Dataset evidence

- P001, PDF page 8, Datasets: "• JARVIS-DFT (dft_3d): This dataset contains 75,993 entries, each annotated with formation energy, band gap (calculated using either the OptB88vDW functional, denoted as OPT, or the TBMBJ functional, denoted as MBJ), bulk modulus, shear modulus, total energy (calculated using the OptB88vDW functional), and energy above the hull (Ehull ) (Choudhary et al., 2020). We also evaluate the baselines on the JARVIS-DFT-3D-2021 dataset (55,723 entries), which serves as an important supplementary benchmark."
- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- P005, PDF page 11, Methods: "The same data processing method was applied to the OQMD and JARVIS databases, and datasets in unknown spaces."
- P006, PDF page 4: "The ability and transferability of the universal atomic embedding are further tested on different databases and tasks. Each is cut into 8:1:1 for training, validation, and testing. Details on the dataset can be found in Supplementary 2A. As for the Jarvis dataset49, the result is shown in Table 1."
- P007, PDF page 7, Data availability: "The two-dimensional materials used in this study were obtained from the C2DB database (https://c2db.fysik.dtu.dk/), while the bulk material data were sourced from the Materials Project and the JARVIS database (https://jarvis.nist.gov/login?next=/jarvisdft/)."
- P011, PDF page 3, Crystal Datasets: "The benchmark for crystal property prediction is well established. There are two standard benchmark datasets, JARVIS and Materials Project (Choudhary et al. 2020; Chen et al. 2019), to evaluate the performance of our model."
- P011, PDF page 4, Experimental Setup: "The JARVIS dataset contains 55,722 materials with critical crystal properties for functional material design, including bandgaps, formation energies, energy above hull, total energy and so on."
- P012, PDF page 1, Abstract: "Comprehensive evaluation results show that WPDDFormer achieves state-of-the-art predictive accuracy across tasks on benchmark datasets such as the Materials Project and JARVIS-DFT."
- P012, PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."
- P012, PDF page 7, 5.1 Experimental Results: "The quantitative results for JARVIS [Choudhary et al., 2020] are shown in Table 1. WPDDformer achieves the best performance across all tasks."
- P016, PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- P016, PDF page 8, Methods: "We use the snapshots of the JARVIS, Materials Project, and OMQD databases used in our previous study, available on Zenodo at https://zenodo.org/records/8200972. The snapshots correspond the JARVIS 2022.12.12 version, the Materials Project 2021.11.10 version, and the OQMD v1.6 version (published in November 2023), and they have been preprocessed to remove materials with formation energies larger than 5 eV/atom."
- P020, PDF page 7, Dataset: "In our research, a dataset is curated specifically focusing on crystal tensor properties, including dielectric, piezoelectric, and elastic tensors, sourced from the JARVIS-DFT database (Choudhary et al., 2020)."
- P021, PDF page 8, 5 EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."
- P023, PDF page 6, Experimental Settings: "Further, to evaluate the fine-tuning performance of CrysDiff compared with other crystal property predictors, we select the 2021.8.18 version of JARVIS-DFT (Choudhary et al. 2020), another popular materials database, for the downstream property prediction task. JARVIS-DFT consists of 55,722 materials with 19 properties, like formation energy, bandgap, total energy, bulk modulus, etc., which depend significantly on crystal structures and atom features."
