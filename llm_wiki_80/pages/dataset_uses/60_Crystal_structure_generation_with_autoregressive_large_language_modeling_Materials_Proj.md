# 60_Crystal structure generation with autoregressive large language modeling - Materials Project

## Dataset Use

A DFT-optimized database of inorganic crystal structures, containing ~3.6 million total structures obtained from the Materials Project (downloaded April 2022), covering compounds with 1–10 elements, up to atomic number 94 (excluding Po, At, Rn, Fr, Ra). It includes ~800,000 unique formulas and 1.2 million unique cell compositions. This dataset was converted to CIF format using pymatgen and formed the core training corpus (~2.3 million CIF files after deduplication) for CrystaLLM, directly supporting the autoregressive language modeling task of generating syntactically and physically valid CIF files from compositional prompts.

## Links

- Paper: [60 Crystal structure generation with autoregressive large language modeling](../papers/60_Crystal_structure_generation_with_autoregressive_large_language_modeling.md)
- Task: [task page](../tasks/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Generating plausible, physically valid crystal structures for inorganic compounds given only their chemical composition (and optionally space group), with the goal of producing candidates suitable for downstream crystal structure prediction (CSP) and materials discovery workflows.

## Metadata

- Dataset use ID: `dataset_use_59d69b053f0d`
- Original dataset title: Materials Project (MP)
- Tags: crystal structure generation, inorganic materials design, CSP candidate generation
