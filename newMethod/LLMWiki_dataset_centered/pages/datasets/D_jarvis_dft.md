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
- JARVIS-DFT database
- 2021.8.18 version of JARVIS-DFT

## Observed material scopes

- inorganic compounds
- crystals
- crystal structures
- crystalline materials
- crystalline solids

## Observed research tasks

- Predicting thermodynamic stability of inorganic compounds
- universal atomic embeddings (UAEs)
- crystal property prediction
- Crystal material property prediction
- probing out-of-distribution generalization in machine learning for materials
- crystal tensor property prediction

## Observed research stages

- data_acquisition
- model_training
- model_evaluation
- data_preparation
- ablation_study
- computational_validation

## Observed properties

- formation energy
- decomposition energy (ΔHd)
- bandgap
- bandgaps
- formation energies
- energy above hull
- total energy
- band gap
- bulk moduli
- shear moduli
- bulk modulus
- dielectric tensor
- piezoelectric tensor
- elastic tensor
- Ehull
- bandgap (OPT)
- bandgap (MBJ)
- bulk modulus (Kv)
- shear modulus (Gv)
- SLME (%)
- spillage

## Observed fields

- chemical formula
- thermodynamic properties
- formation energy
- formation energy (Ef)
- bandgap (Eg)
- crystal structure
- properties
- crystal_structure
- formation_energy
- bandgap_OPT
- bandgap_MBJ
- bulk_moduli_Kv
- shear_moduli_Gv
- band gap
- bulk modulus
- crystal structure M = (A, P, L)
- tensor property values
- crystal structure (A, P, L)
- bandgap(OPT)
- bandgap(MBJ)
- Etotal
- Ehull
- crystal structure (A, F, L)
- target property values

## Usage evidence

- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): source in Collecting DFT-computed stability data from public materials databases — Acquire large-scale DFT-computed thermodynamic stability data for inorganic compounds
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): training in Training base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR) via stacked generalization — Train base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR)
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): test in Benchmarking ECSG against state-of-the-art models using multiple metrics — Benchmark ECSG against state-of-the-art models using multiple metrics
- P006 (Transformer-generated atomic embeddings to enhance prediction accuracy of crystal properties with machine learning): computational_validation in evaluating transferability of ct-UAEs across databases and tasks — to test the ability and transferability of ct-UAEs on different databases and tasks
- P011 (A Denoising Pre-training Framework for Accelerating Novel Material Discovery): training in fine-tuning on downstream property prediction — Fine-tuning the pre-trained model on labeled crystal property prediction tasks.
- P011 (A Denoising Pre-training Framework for Accelerating Novel Material Discovery): test in evaluating property prediction accuracy — Evaluating model performance on crystal property prediction using MAE.
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): source in Crystal graph construction with WPDD/UPDD — Source of crystal structures for constructing multi-edge crystal graphs with WPDD/UPDD representations
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): training in Training PDDFormer (WPDDFormer/UPDDFormer) — Training WPDDFormer and UPDDFormer models on property prediction tasks
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): test in Evaluation on benchmark property prediction tasks — Evaluating predictive accuracy of WPDDFormer/UPDDFormer on multiple material property tasks
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): validation in Ablation study on (W/U)PDD contribution — Ablation study on (W/U)PDD contribution using testing MAE as evaluation metric
- P012 (PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction): computational_validation in Continuity and completeness validation using EMD — Continuity and completeness validation using EMD on perturbed crystal structures
- P016 (Probing out-of-distribution generalization in machine learning for materials): source in selection of ab initio-derived materials databases — To obtain diverse, large-scale, precomputed materials property data for robust OOD evaluation.
- P020 (A Space Group Symmetry Informed Network for O(3) Equivariant Crystal Tensor Prediction): source in curating a dataset encompassing dielectric, piezoelectric, and elastic tensors — source dielectric, piezoelectric, and elastic tensors for curating the crystal tensor property dataset
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): source in using three widely-used crystal benchmarks — acquire crystal structure data and corresponding property labels for training and evaluation
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in evaluating predictive accuracy on crystal benchmarks — evaluate the performance of the trained models on held-out test sets using standard metrics
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): screening in ablation studies on geometric completeness and model components — demonstrate the importance of geometric completeness and specific architectural components by systematically removing them
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): training in collecting labeled crystal property data for fine-tuning and evaluation — fine-tuning and evaluation of crystal property prediction on nine target properties
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): test in downstream task evaluation on JARVIS-DFT — downstream task evaluation on nine crystal properties using MAE
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): benchmark in ablation study on key design components — ablation study on key design components for Formation Energy and Bandgap (MBJ)

## Dataset evidence

- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- P006, PDF page 4: "As for the Jarvis dataset49, the result is shown in Table 1. The CT-CGCNN model demonstrates an improvement in predicting both formation energy Ef and bandgap energy Eg."
- P011, PDF page 3, Crystal Datasets: "The benchmark for crystal property prediction is well established. There are two standard benchmark datasets, JARVIS and Materials Project (Choudhary et al. 2020; Chen et al. 2019), to evaluate the performance of our model."
- P011, PDF page 4, Experimental Setup: "The JARVIS dataset contains 55,722 materials with critical crystal properties for functional material design, including bandgaps, formation energies, energy above hull, total energy and so on."
- P012, PDF page 1, Abstract: "Comprehensive evaluation results show that WPDDFormer achieves state-of-the-art predictive accuracy across tasks on benchmark datasets such as the Materials Project and JARVIS-DFT."
- P012, PDF page 7, 5 Experiments: "We conducted experiments on two material benchmark datasets, namely the Materials Project [Chen et al., 2019] and Jarvis [Choudhary et al., 2020] datasets."
- P012, PDF page 7, 5.1 Experimental Results: "The quantitative results for JARVIS [Choudhary et al., 2020] are shown in Table 1."
- P016, PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- P016, PDF page 8, Methods: "We use the snapshots of the JARVIS, Materials Project, and OMQD databases used in our previous study47, available on Zenodo at https://zenodo.org/records/8200972. The snapshots correspond the JARVIS 2022.12.12 version, the Materials Project 2021.11.10 version, and the OQMD v1.6 version (published in November 2023), and they have been preprocessed to remove materials with formation energies larger than 5 eV/atom."
- P020, PDF page 7, 5.1. Curated Crystal Tensor Property Dataset: "In our research, a dataset is curated specifically focusing on crystal tensor properties, including dielectric, piezoelectric, and elastic tensors, sourced from the JARVIS-DFT database (Choudhary et al., 2020)."
- P021, PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."
- P023, PDF page 6, Experimental Settings: "Further, to evaluate the fine-tuning performance of CrysDiff compared with other crystal property predictors, we select the 2021.8.18 version of JARVIS-DFT (Choudhary et al. 2020), another popular materials database, for the downstream property prediction task. JARVIS-DFT consists of 55,722 materials with 19 properties, like formation energy, bandgap, total energy, bulk modulus, etc., which depend significantly on crystal structures and atom features."
- P023, PDF page 6, Total Energy: "Table 1: The prediction performance (MAE) of nine properties on the JARVIS-DFT dataset for the proposed CrysDiff model against existing train-from-scratch and pretrain-finetune models."
