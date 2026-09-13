# 63_Fine-Tuned Language Models Generate Stable Inorganic Materials as Text - Extended Materials Project Dataset

## Dataset Use

An expanded collection of ~120,000–127,609 inorganic crystal structures drawn from the Materials Project (as of April 2023), filtered to exclude crystals with more than 30 atoms per unit cell. This dataset includes additional property annotations beyond MP-20 — such as space group number, band gap, Ehull, and chemical formula — and is used specifically to train the fine-tuned LLaMA-2 models for text-conditional generation (e.g., conditioning on composition or space group) and structural infilling tasks.

## Links

- Paper: [63 Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](../papers/63_Fine-Tuned_Language_Models_Generate_Stable_Inorganic_Materials_as_Text.md)
- Task: [task page](../tasks/63_Fine-Tuned_Language_Models_Generate_Stable_Inorganic_Materials_as_Text_task_1.md)
- Dataset: [Extended Materials Project Dataset](../datasets/Extended_Materials_Project_Dataset.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Generating stable inorganic crystalline materials as text-encoded 3D atomic structures, where stability is defined by low energy above hull (Ehull < 0.1 eV/atom), and the generated structures must satisfy physical constraints including non-overlapping atomic radii and net neutral charge.

## Metadata

- Dataset use ID: `dataset_use_aa52e3702da9`
- Original dataset title: Extended Materials Project Dataset
- Tags: materials generation, crystal structure prediction, stability prediction, text-to-structure generation
