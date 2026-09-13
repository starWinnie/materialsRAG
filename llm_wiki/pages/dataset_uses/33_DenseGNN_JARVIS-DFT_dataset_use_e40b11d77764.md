# 33_DenseGNN - JARVIS-DFT

## Dataset Use

A dataset of ~67,000 inorganic crystal structures with DFT-calculated properties (e.g., formation energy, band gap, dielectric, piezoelectric, exfoliation energy) computed using OptB88vdW and TBmBJ functionals; used to train and evaluate DenseGNN for crystal property prediction, particularly on formation energy and bandgap tasks, with an 80:10:10 train/validation/test split.

## Links

- Paper: [33 DenseGNN](../papers/33_DenseGNN.md)
- Task: [task page](../tasks/33_DenseGNN_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting material properties—including formation energy, band gap, bulk modulus, phonon frequencies, dielectric constant, and perovskite formation energy—for crystals, molecules, and catalytic materials using graph neural networks, with emphasis on achieving high accuracy on both large-scale computational datasets and small experimental datasets while maintaining scalability and training efficiency.

## Metadata

- Dataset use ID: `dataset_use_e40b11d77764`
- Original dataset title: JARVIS-DFT
- Tags: property prediction, materials informatics, graph neural network

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
