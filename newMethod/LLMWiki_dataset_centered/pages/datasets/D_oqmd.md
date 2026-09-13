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
- Open Quantum Materials Database (OQMD) v1.5
- OQMD v1.5

## Observed material scopes

- inorganic compounds
- crystals
- crystalline solids
- crystalline materials
- inorganic materials
- three-dimensional inorganic crystal structures

## Observed research tasks

- Predicting thermodynamic stability of inorganic compounds
- crystal structure modeling for SE(3)-invariant property prediction
- probing out-of-distribution generalization in machine learning for materials
- crystal property prediction
- benchmarking of materials design methods
- Correcting DFT formation energies towards experimental accuracy

## Observed research stages

- data_acquisition
- model_training
- model_evaluation

## Observed properties

- formation energy
- decomposition energy (ΔHd)
- bandgap
- energy above hull
- band gap
- bulk modulus
- elastic properties

## Observed fields

- chemical formula
- thermodynamic properties
- formation energy
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
- ICSD ID

## Usage evidence

- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): source in Collecting DFT-computed stability data from public materials databases — Acquire large-scale DFT-computed thermodynamic stability data for inorganic compounds
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): training in Training base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR) via stacked generalization — Train base-level models (ECCNN, Magpie, Roost) and meta-level model (MLR)
- P005 (Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration): test in Benchmarking ECSG against state-of-the-art models using multiple metrics — Benchmark ECSG against state-of-the-art models using multiple metrics
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): source in acquisition of crystal structure datasets — acquisition of crystal structure datasets with DFT-simulated material properties
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): training in training of CrystalFramer architecture — training the CrystalFramer model using mean absolute loss function with Adam optimizer for 200 epochs with larger batch size
- P010 (RETHINKING THE ROLE OF FRAMES FOR SE(3)-INVARIANT CRYSTAL STRUCTURE MODELING): test in evaluation on crystal property prediction tasks — evaluation of CrystalFramer performance on crystal property prediction tasks
- P016 (Probing out-of-distribution generalization in machine learning for materials): source in selection of ab initio-derived materials databases — To obtain diverse, large-scale, precomputed materials property data for robust OOD evaluation.
- P023 (A Diffusion-Based Pre-training Framework for Crystal Property Prediction): source in collecting unlabeled crystal structure data for pre-training — pre-training via crystal structure reconstruction using unlabeled crystal graph data
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): source in populating reference benchmark datasets — reference benchmark dataset for ES methods
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): source in Acquiring DFT formation energy datasets — Provide DFT formation energies for cross-validation and baseline comparison against MC3D and experimental data.

## Dataset evidence

- P005, PDF page 11, Methods: "In this work, we compared the performance of various models in predicting the stability of inorganic compounds on three large DFT-computed datasets, MP, OQMD, and JARVIS."
- P010, PDF page 8, Datasets.: "We use three datasets: JARVIS (55,723 materials), MP (69,239 materials), and OQMD (817,636 materials), using snapshots available through a Python package (jarvis-tools). These datasets provide several material properties, such as formation energy and bandgap, simulated by DFT calculations."
- P010, PDF page 17, C DATASET SPECIFICATIONS: "The Open Quantum Materials Database (OQMD) is another online public materials database by Kirklin et al. (2015). We specifically use its snapshot provided as oqmd_3d_no_cfid in jarvis-tools, which contains 817,636 materials with three DFT-calculated properties: formation energy (_oqmd_delta_e), bandgap (_oqmd_band_gap), and energy above hull (_oqmd_stability). We use these properties as regression targets. We release our data splits along with our code."
- P016, PDF page 2, Results: "Three ab initio-derived materials databases have been selected for this evaluation: Joint Automated Repository for Various Integrated Simulations (JARVIS), Materials Project (MP), and the Open Quantum Materials Database (OQMD)."
- P016, PDF page 8, Methods: "We use the snapshots of the JARVIS, Materials Project, and OMQD databases used in our previous study47, available on Zenodo at https://zenodo.org/records/8200972. The snapshots correspond the JARVIS 2022.12.12 version, the Materials Project 2021.11.10 version, and the OQMD v1.6 version (published in November 2023), and they have been preprocessed to remove materials with formation energies larger than 5 eV/atom."
- P023, PDF page 6, Experimental Settings: "We collect 800K untagged crystal graph data from two popular materials databases, Materials Project (MP) (Jain et al. 2013) and OQMD (Saal et al. 2013), to pre-train the CrysDiff model."
- P028, PDF page 7: "PBE87 data from Open Quantum Materials Database (OQMD)88,89"
- P035, PDF page 10, METHODS: "In addition to the comparison with experimental data, the MC3D formation energies are compared against the established high-throughput databases Materials Project [7, 8] and Open Quantum Materials Database [10]. We query the OQMD v1.5 (locally hosted) and MP v2023.11.1, and match structures by their ICSD ID."
