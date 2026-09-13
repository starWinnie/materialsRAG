# 11_DPF - JARVIS Dataset

## Dataset Use

A publicly available benchmark dataset containing 55,722 experimentally and computationally derived crystal structures, each annotated with multiple material properties including formation energy, band gap (OPT and MBJ), total energy, energy above hull (Ehull), bulk modulus, and shear modulus. Used as a primary downstream evaluation benchmark to fine-tune and validate the pre-trained models’ performance on crystal property prediction tasks, with MAE as the evaluation metric.

## Links

- Paper: [11 DPF](../papers/11_DPF_paper_7100e5964f9d.md)
- Task: [task page](../tasks/11_DPF_task_1_task_9126e9e26415.md)
- Dataset: [JARVIS dataset](../datasets/JARVIS_dataset_dataset_22e101c9fff4.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting key physical and electronic properties of crystalline materials—including formation energy, band gap (both OPT and MBJ variants), total energy, energy above hull (Ehull), bulk modulus, and shear modulus—using deep learning models trained on limited labeled data by first pre-training on large-scale unlabeled crystal structures via denoising reconstruction tasks.

## Metadata

- Dataset use ID: `dataset_use_3b0d2afbcbdb`
- Original dataset title: JARVIS Dataset
- Tags: crystal property prediction, pre-training, denoising reconstruction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
