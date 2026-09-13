# 63_Fine-Tuned Language Models Generate Stable Inorganic Materials as Text - Materials Project MP-20

## Dataset Use

A curated dataset of 45,231 experimentally and computationally validated stable inorganic crystalline materials from the Materials Project database, each containing full crystallographic information (lattice parameters, fractional atomic coordinates, space group, composition) and computed DFT-derived properties including energy above hull (Ehull), band gap, and formation energy. It is used in this paper to train fine-tuned LLaMA-2 models for unconditional generation and to construct the ground-truth convex energy hull for evaluating the predicted stability (Ehull) of generated samples.

## Links

- Paper: [63 Fine-Tuned Language Models Generate Stable Inorganic Materials as Text](../papers/63_Fine-Tuned_Language_Models_Generate_Stable_Inorganic_Materials_as_Text.md)
- Task: [task page](../tasks/63_Fine-Tuned_Language_Models_Generate_Stable_Inorganic_Materials_as_Text_task_1.md)
- Dataset: [Materials Project MP-20](../datasets/Materials_Project_MP-20.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Generating stable inorganic crystalline materials as text-encoded 3D atomic structures, where stability is defined by low energy above hull (Ehull < 0.1 eV/atom), and the generated structures must satisfy physical constraints including non-overlapping atomic radii and net neutral charge.

## Metadata

- Dataset use ID: `dataset_use_8c029cf057e0`
- Original dataset title: Materials Project MP-20
- Tags: materials generation, crystal structure prediction, stability prediction, text-to-structure generation
