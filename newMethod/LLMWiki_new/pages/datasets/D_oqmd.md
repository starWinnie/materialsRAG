# Dataset: Open Quantum Materials Database (OQMD)

- Dataset ID: `D_oqmd`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Open Quantum Materials Database
- OQMD
- oqmd_3d_no_cfid
- Open Quantum Materials Database (OQMD)
- OpenQuantumMaterials Database

## Observed material scopes

- inorganic compounds
- crystals
- inorganic crystalline solids
- inorganic crystalline materials
- crystal structures

## Observed research tasks

- Predicting thermodynamic stability of inorganic compounds
- crystal property prediction
- Probing out-of-distribution generalization in machine learning for materials

## Observed research stages

- data_acquisition
- label_generation
- model_evaluation
- data_preparation
- model_training
- computational_validation

## Observed properties

- formation energy
- decomposition energy (ΔHd)
- _oqmd_delta_e
- _oqmd_band_gap
- _oqmd_stability
- band gap
- bulk modulus

## Observed fields

- chemical formula
- ΔHd
- stability label
- _oqmd_delta_e
- _oqmd_band_gap
- _oqmd_stability
- crystal structure
- formation energy
- band gap
- bulk modulus

## Usage evidence

- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): source in Collecting DFT-computed thermodynamic stability data from public databases — Acquire labeled training and test data for compound stability
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): label_source in Assigning stability labels based on DFT-derived decomposition energy thresholds — Assign stability labels based on DFT-derived decomposition energy thresholds
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): benchmark in Benchmarking predictive performance across multiple metrics and datasets — Benchmark predictive performance across multiple metrics
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): source in using datasets derived from JARVIS, Materials Project (MP), and Open Quantum Materials Database (OQMD) — acquire crystal structure data and associated DFT-simulated properties
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): training in using consistent data splits and preprocessing — prepare data using standardized splits and preprocessing for fair comparison
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): benchmark in comparing mean absolute errors on crystal property prediction tasks — evaluate performance against baselines using mean absolute error metrics
- P016 (Probing out-of-distribution generalization in machine learning for materials): source in Selection of ab initio-derived materials databases — Selection of ab initio-derived materials database for OOD evaluation
- P016 (Probing out-of-distribution generalization in machine learning for materials): training in Preprocessing and splitting for OOD tasks — Constructing OOD tasks via leave-one-X-out splitting based on chemistry or structural symmetry criteria
- P016 (Probing out-of-distribution generalization in machine learning for materials): training in Training representative ML models on each OOD task — Training ML models (RF, XGB, ALIGNN, GMP, LLM-Prop) on OOD training splits
- P016 (Probing out-of-distribution generalization in machine learning for materials): test in Evaluating OOD performance with MAE and R2 — Evaluating OOD performance of trained models using MAE and R2 metrics
- P016 (Probing out-of-distribution generalization in machine learning for materials): computational_validation in Inspecting materials representations via UMAP and kernel density estimation — Inspecting materials representations via UMAP and kernel density estimation to distinguish statistically OOD from representationally OOD test data
- P016 (Probing out-of-distribution generalization in machine learning for materials): computational_validation in Analyzing learning curves for training time and training set size — Analyzing learning curves for training time and training set size to test neural scaling laws on representationally ID vs. OOD tasks

## Dataset evidence

- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- P005, PDF page 11, Methods: "The same data processing method was applied to the OQMD and JARVIS databases, and datasets in unknown spaces."
- P010, PDF page 8, CRYSTAL PROPERTY PREDICTION: "Datasets. We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- P010, PDF page 17, C DATASET SPECIFICATIONS: "The Open Quantum Materials Database (OQMD) is another online public materials database by Kirklin et al. (2015). We specifically use its snapshot provided as oqmd_3d_no_cfid in jarvis-tools, which contains 817,636 materials with three DFT-calculated properties: formation energy (_oqmd_delta_e), bandgap (_oqmd_band_gap), and energy above hull (_oqmd_stability). We use these properties as regression targets. We release our data splits along with our code."
- P016, PDF page 2, Evaluation setup: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS)29,30, Materials Project (MP)31, and the Open Quantum Materials Database (OQMD)32."
- P016, PDF page 8, Methods: "We use the snapshots of the JARVIS, Materials Project, and OMQD databases used in our previous study47, available on Zenodo at https://zenodo.org/records/8200972. The snapshots correspond the JARVIS 2022.12.12 version, the Materials Project 2021.11.10 version, and the OQMD v1.6 version (published in November 2023), and they have been preprocessed to remove materials with formation energies larger than 5 eV/atom."
- P026, PDF page 1: "Materials databases such as Materials Project and OpenQuantumMaterials Database (OQMD)11,12 are characterized by the existence of many redundant (highly similar) materials..."
- P035, PDF page 1, ABSTRACT: "We then compare against two other DFT databases, the Open Quantum Materials Database (OQMD) and the Materials Project (MP), as well as against experimental formation enthalpies."