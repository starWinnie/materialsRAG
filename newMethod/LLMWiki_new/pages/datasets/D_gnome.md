# Dataset: GNoME

- Dataset ID: `D_gnome`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- GNoME
- GNoME materials
- GNoME dataset
- GNoME-based ab-initio configurations

## Observed material scopes

- inorganic materials
- crystals
- crystal structures

## Observed research tasks

- electron density prediction
- crystal property prediction
- crystal structure generation

## Observed research stages

- data_acquisition
- model_evaluation

## Observed properties

- electron charge density
- structures
- crystal structure
- formation energy
- stability
- ab-initio configurations

## Observed fields

- atomic species
- atomic positions
- charge density grid
- CIF files
- ab-initio data

## Usage evidence

- P025 (Higher-order equivariant neural networks for charge density prediction in materials): test in collecting DFT-computed charge density data — Evaluate generalization capabilities of ChargE3Net on out-of-distribution materials
- P057 (Latent Diffusion Pretraining for Crystal Property Prediction): pretraining in pretraining data acquisition — acquire large-scale unlabeled crystal structures for pretraining
- P102 (Foundational Large Language Models for Materials Research): label_source in quantitative assessment of crystal generation — Provide ground truth materials for computing coverage metrics (COV-R and COV-P) to measure similarity between ensembles of generated materials and ground truth materials in the test set.

## Dataset evidence

- P025, PDF page 2, Results: "We demonstrate the application of MP-trained ChargE3Net to initialize DFT calculations, resulting in a median of 26.7% reduction in SCF steps on unseen MP data and 28.6% on novel GNoME materials50."
- P114, PDF page 5, 4.1. Datasets for Pretraining and Downstream Tasks: "For pretraining, we follow prior work (Shen et al., 2025a) and use 380,740 crystal structures filtered from the recent GNoME dataset (Merchant et al., 2023)."
- P311, PDF page 11, Methods: "These files were aggregated from three major sources: the Materials Project [55], GNoME-based ab-initio configurations [56], and the American mineralogist crystal structure database (AMCSD) [57]."
