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
- OMQD

## Observed material scopes

- inorganic compounds
- crystals
- crystalline solids
- inorganic materials
- crystalline materials

## Observed research tasks

- Predicting thermodynamic stability of inorganic compounds
- crystal property prediction
- Probing out-of-distribution generalization in machine learning for materials

## Observed research stages

- data_acquisition
- model_evaluation
- computational_validation
- data_preparation
- model_training

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
- thermodynamic stability
- ΔHd
- formation energy
- bandgap
- energy above hull
- crystal structure
- band gap
- bulk modulus
- crystal structure (A, F, L)

## Usage evidence

- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): source in Collecting thermodynamic stability data from DFT-computed databases — Acquire labeled stability data for training and evaluation
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): test in Benchmarking model performance using multiple metrics — Benchmarking model performance using multiple metrics
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): computational_validation in Validating predictions via first-principles DFT calculations — Validating predictions via first-principles DFT calculations
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): source in using datasets derived from JARVIS, Materials Project (MP), and Open Quantum Materials Database (OQMD) — acquire crystal structure data and corresponding DFT-simulated properties
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): training in using consistent data splits and preprocessing — prepare data using standardized splits and preprocessing for fair comparison
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): training in training CrystalFramer with dynamic frames — train the CrystalFramer architecture with dynamic frame construction
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): benchmark in comparing mean absolute errors on crystal property prediction tasks — evaluate performance against baselines using mean absolute error metrics
- P016 (Probing out-of-distribution generalization in machine learning for materials): source in Selection of ab initio-derived materials databases — Acquisition of large, diverse, and preprocessed materials dataset for robust OOD evaluation.
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): source in collecting unlabeled crystal structure data — pre-training via crystal structure reconstruction using unlabeled crystal graph data

## Dataset evidence

- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- P005, PDF page 11, Methods: "The same data processing method was applied to the OQMD and JARVIS databases, and datasets in unknown spaces."
- P010, PDF page 8, CRYSTAL PROPERTY PREDICTION: "Datasets. We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- P010, PDF page 17, C DATASET SPECIFICATIONS: "The Open Quantum Materials Database (OQMD) is another online public materials database by Kirklin et al. (2015). We specifically use its snapshot provided as oqmd_3d_no_cfid in jarvis-tools, which contains 817,636 materials with three DFT-calculated properties: formation energy (_oqmd_delta_e), bandgap (_oqmd_band_gap), and energy above hull (_oqmd_stability). We use these properties as regression targets. We release our data splits along with our code."
- P016, PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- P016, PDF page 8, Methods: "We use the snapshots of the JARVIS, Materials Project, and OMQD databases used in our previous study, available on Zenodo at https://zenodo.org/records/8200972. The snapshots correspond the JARVIS 2022.12.12 version, the Materials Project 2021.11.10 version, and the OQMD v1.6 version (published in November 2023), and they have been preprocessed to remove materials with formation energies larger than 5 eV/atom."
- P023, PDF page 6, Experimental Settings: "We collect 800K untagged crystal graph data from two popular materials databases, Materials Project (MP) (Jain et al. 2013) and OQMD (Saal et al. 2013), to pre-train the CrysDiff model."
