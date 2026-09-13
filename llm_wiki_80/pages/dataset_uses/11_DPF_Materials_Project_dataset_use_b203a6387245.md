# 11_DPF - Materials Project

## Dataset Use

A large-scale computational materials database aggregating DFT-calculated properties for over 100,000 inorganic crystals. The subset used in this paper includes 69,239 structures labeled with formation energy and band gap, and 5,451 structures labeled with bulk modulus and shear modulus. Serves as the second major downstream benchmark for fine-tuning and evaluating the denoising-pre-trained models across diverse crystal property prediction tasks under consistent experimental protocols.

## Links

- Paper: [11 DPF](../papers/11_DPF.md)
- Task: [task page](../tasks/11_DPF_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting key physical and electronic properties of crystalline materials—including formation energy, band gap (both OPT and MBJ variants), total energy, energy above hull (Ehull), bulk modulus, and shear modulus—using deep learning models trained on limited labeled data by first pre-training on large-scale unlabeled crystal structures via denoising reconstruction tasks.

## Metadata

- Dataset use ID: `dataset_use_b203a6387245`
- Original dataset title: Materials Project Dataset
- Tags: crystal property prediction, pre-training, denoising reconstruction
