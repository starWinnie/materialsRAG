# Dataset: Materials Project DFT-computed band gap dataset

- Dataset ID: `D_materials_project_dft_computed_band_gap_dataset`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Materials Project DFT-computed band gap dataset
- Materials Project
- Materials Project v2023.11.1 database

## Observed material scopes

- transparent conducting materials (TCMs)
- semiconductors

## Observed research tasks

- accelerating the discovery of new transparent conducting materials (TCMs)

## Observed research stages

- data_acquisition

## Observed properties

- band gap

## Observed fields

- chemical formula
- band gap

## Usage evidence

- P037 (Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials): pretraining in creating and validating unique experimental databases — pretraining dataset for CrabNet model

## Dataset evidence

- P037, PDF page 7, Results: "CrabNet undergoes pretraining on a dataset of DFT-computed band gaps sourced from the Materials Project.3"
- P037, PDF page 9, Identification of metals and non-metals: "In our study, to enhance the accuracy of band gap identification, and thus minimizing the number of false negatives (in our definition, metals that are wrongly predicted as semiconductors or insulators), we have utilized a transfer learning approach. This involved pre-training CrabNet on an extensive dataset sourced from the Materials Project,3 encompassing all entries with chemical formulas and associated band gap information. At the time of data retrieval, 153 224 material entries with their corresponding band gaps were present in the Materials Project v2023.11.1 database."
- P037, PDF page 14, Data availability: "Additional band gap data used for pre-training CrabNet were obtained from the Materials Project (version 2023.11.1), accessible via their API at https://materialsproject.org."
