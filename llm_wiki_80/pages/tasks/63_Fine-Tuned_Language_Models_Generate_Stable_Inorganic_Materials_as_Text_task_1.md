# 63_Fine-Tuned Language Models Generate Stable Inorganic Materials as Text - Task 1

## Task Description

Generating stable inorganic crystalline materials as text-encoded 3D atomic structures, where stability is defined by low energy above hull (Ehull < 0.1 eV/atom), and the generated structures must satisfy physical constraints including non-overlapping atomic radii and net neutral charge.

## Metadata

- Task ID: `task_eb2b09890f75`
- Source paper: [63 Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](../papers/63_Fine-Tuned_Language_Models_Generate_Stable_Inorganic_Materials_as_Text.md)
- Tags: materials generation, crystal structure prediction, stability prediction, text-to-structure generation

## Supporting Datasets

### [Materials Project MP-20](../datasets/Materials_Project_MP-20.md)

- Usage page: [usage note](../dataset_uses/63_Fine-Tuned_Language_Models_Generate_Stable_Inorganic_Materials_as_Text_Materials_Projec.md)
- Original title in paper: Materials Project MP-20
- Link: https://materialsproject.org/

A curated dataset of 45,231 experimentally and computationally validated stable inorganic crystalline materials from the Materials Project database, each containing full crystallographic information (lattice parameters, fractional atomic coordinates, space group, composition) and computed DFT-derived properties including energy above hull (Ehull), band gap, and formation energy. It is used in this paper to train fine-tuned LLaMA-2 models for unconditional generation and to construct the ground-truth convex energy hull for evaluating the predicted stability (Ehull) of generated samples.

### [Extended Materials Project Dataset](../datasets/Extended_Materials_Project_Dataset.md)

- Usage page: [usage note](../dataset_uses/63_Fine-Tuned_Language_Models_Generate_Stable_Inorganic_Materials_as_Text_Extended_Materia.md)
- Original title in paper: Extended Materials Project Dataset
- Link: https://materialsproject.org/

An expanded collection of ~120,000–127,609 inorganic crystal structures drawn from the Materials Project (as of April 2023), filtered to exclude crystals with more than 30 atoms per unit cell. This dataset includes additional property annotations beyond MP-20 — such as space group number, band gap, Ehull, and chemical formula — and is used specifically to train the fine-tuned LLaMA-2 models for text-conditional generation (e.g., conditioning on composition or space group) and structural infilling tasks.
