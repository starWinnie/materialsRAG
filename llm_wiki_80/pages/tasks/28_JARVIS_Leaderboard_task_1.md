# 28_JARVIS_Leaderboard - Task 1

## Task Description

Benchmarking and systematically comparing the performance of diverse materials design methods—including artificial intelligence models, electronic structure calculations, force-field approaches, quantum computation algorithms, and experimental protocols—across multiple data modalities (atomic structures, spectra, images, text) and material properties (e.g., formation energy, bandgap, bulk modulus, CO₂ adsorption), to enable reproducible, transparent, and unbiased evaluation of method accuracy, robustness, and generalizability.

## Metadata

- Task ID: `task_933637998dc2`
- Source paper: [28 JARVIS Leaderboard](../papers/28_JARVIS_Leaderboard.md)
- Tags: benchmarking, method validation, reproducibility, performance comparison, materials design evaluation

## Supporting Datasets

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/28_JARVIS_Leaderboard_JARVIS-DFT_dataset_use_339beba1dea4.md)
- Original title in paper: JARVIS-DFT
- Link: https://jarvis.nist.gov/jarvisdft/

A high-throughput density functional theory (DFT) database containing computed properties for over 80,000 inorganic materials, including formation energies, bandgaps, elastic moduli, phonon spectra, and more. In this paper, JARVIS-DFT serves as the primary reference dataset for AI-based property prediction benchmarks (e.g., formation energy per atom, exfoliation energy) and as a source of ground-truth computational data for force-field and quantum computation benchmarking; its pre-split train/validation/test sets enable standardized model training and evaluation in the AI category.

### [JARVIS Database](../datasets/JARVIS_Database.md)

- Usage page: [usage note](../dataset_uses/28_JARVIS_Leaderboard_JARVIS_Database_dataset_use_25fa570bba6f.md)
- Original title in paper: JARVIS-Tools datasets
- Link: https://pages.nist.gov/jarvis/databases/

A collection of integrated, versioned datasets hosted via JARVIS-Tools and backed up on Figshare, encompassing atomic structures (3D, 2D, amorphous), spectra (XRD, DOS, Eliashberg), STEM/STM images, text (arXiv corpus), and interatomic potentials. These datasets support multi-modal benchmarking across all leaderboard categories: e.g., STEM images for AI image classification, XRD spectra for spectral prediction, and arXiv text for text classification/generation tasks — each linked to specific json.zip benchmark files with DOIs and metadata.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/28_JARVIS_Leaderboard_Materials_Project_dataset_use_2739e157a7e2.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A publicly available DFT-derived database of thermodynamic and structural properties for over 140,000 inorganic compounds, used in this paper as one of several external atomic-structure datasets for AI benchmarking (e.g., formation energy prediction). It provides complementary coverage to JARVIS-DFT and supports cross-dataset analysis to assess model generalizability and avoid bias from single-source data distributions.

### [QM9](../datasets/QM9.md)

- Usage page: [usage note](../dataset_uses/28_JARVIS_Leaderboard_QM9_dataset_use_9e8a2ff97b8e.md)
- Original title in paper: QM9
- Link: https://doi.org/10.6084/m9.figshare.978961

A quantum chemistry dataset containing DFT-computed properties (e.g., energies, dipole moments, vibrational frequencies) for 134,000 small organic molecules. In this paper, it is explicitly listed as an input dataset for AI models targeting molecular-level property prediction, supporting benchmarks in the AI category—particularly for spectroscopic or energetic property tasks where molecular structure is the primary input.

### [Experimental round-robin CO₂ adsorption data for ZSM-5 zeolite](../datasets/Experimental_round-robin_CO₂_adsorption_data_for_ZSM-5_zeolite.md)

- Usage page: [usage note](../dataset_uses/28_JARVIS_Leaderboard_Experimental_round-robin_CO₂_adsorption_data_for_ZSM-5_zeolite_datas.md)
- Original title in paper: Experimental round-robin CO₂ adsorption data for ZSM-5 zeolite
- Link: https://doi.org/10.1007/s10450-018-9952-0

Inter-laboratory experimental measurements of high-pressure CO₂ adsorption isotherms on ammonium ZSM-5 zeolite, generated via a coordinated round-robin study across multiple labs. This dataset serves as the experimental reference benchmark for the EXP category, enabling direct comparison of computational predictions (e.g., from RASPA simulations) and validating reproducibility across experimental setups — fulfilling the paper’s goal of integrating experimental benchmarking into the leaderboard framework.
