# Dataset Use: Materials Project DFT-computed band gap dataset

- DatasetUse ID: `DU_materials_project_dft_computed_band_gap_dataset`
- Dataset: Materials Project DFT-computed band gap dataset (`D_materials_project_dft_computed_band_gap_dataset`)
- Papers: P037
- Usage records: 1

## Usage roles

- pretraining

## Purposes

- pretraining dataset for CrabNet model

## Used fields

- chemical formula
- band gap

## Construction methods

- None stated

## Filter conditions

- excluded entries equivalent to those in experimental Eg dataset

## Sample counts

- None stated

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P037_01_materials_project_dft_computed_band_gap_dataset

- Paper: `P037` — Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials
- Task: accelerating the discovery of new transparent conducting materials (TCMs) (`T_P037_01`)
- Stage: creating and validating unique experimental databases (`data_acquisition`, `S_P037_01`)
- Usage role: pretraining
- Purpose: pretraining dataset for CrabNet model
- Used fields: chemical formula, band gap
- Filter conditions: excluded entries equivalent to those in experimental Eg dataset
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P037, PDF page 9, Identification of metals and non-metals: "In our study, to enhance the accuracy of band gap identification, and thus minimizing the number of false negatives (in our definition, metals that are wrongly predicted as semiconductors or insulators), we have utilized a transfer learning approach. This involved pre-training CrabNet on an extensive dataset sourced from the Materials Project,3 encompassing all entries with chemical formulas and associated band gap information. At the time of data retrieval, 153 224 material entries with their corresponding band gaps were present in the Materials Project v2023.11.1 database. From this initial dataset, we filtered out chemical formulas that were deemed equivalent in our experimental band gap dataset, encompassing 4767 material entries. We have used the reduced chemical formula as criterion to establish equivalent entries, as atomic proportions are utilized when creating inputs to ML models. To ensure a fair evaluation we have discarded all such entries, ending up with a pretraining dataset consisting of 149 714 data points."

## Aggregated evidence

- , PDF page 9, Identification of metals and non-metals: "In our study, to enhance the accuracy of band gap identification, and thus minimizing the number of false negatives (in our definition, metals that are wrongly predicted as semiconductors or insulators), we have utilized a transfer learning approach. This involved pre-training CrabNet on an extensive dataset sourced from the Materials Project,3 encompassing all entries with chemical formulas and associated band gap information. At the time of data retrieval, 153 224 material entries with their corresponding band gaps were present in the Materials Project v2023.11.1 database. From this initial dataset, we filtered out chemical formulas that were deemed equivalent in our experimental band gap dataset, encompassing 4767 material entries. We have used the reduced chemical formula as criterion to establish equivalent entries, as atomic proportions are utilized when creating inputs to ML models. To ensure a fair evaluation we have discarded all such entries, ending up with a pretraining dataset consisting of 149 714 data points."
