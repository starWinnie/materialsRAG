# 71_A generative model for inorganic materials design - Alex-MP-ICSD

## Dataset Use

An extended reference dataset comprising 850,384 unique ordered structures from Materials Project, Alexandria, and the Inorganic Crystal Structure Database (ICSD), used to compute the convex hull for stability evaluation (energy above hull ≤ 0.1 eV/atom). It also forms the basis for novelty assessment—structures not matching any entry in Alex-MP-ICSD (augmented with 117,652 disordered ICSD entries) are deemed 'new'.

## Links

- Paper: [71 A generative model for inorganic materials design](../papers/71_A_generative_model_for_inorganic_materials_design.md)
- Task: [task page](../tasks/71_A_generative_model_for_inorganic_materials_design_task_1.md)
- Dataset: [Alex-MP-ICSD](../datasets/Alex-MP-ICSD.md)
- Dataset URL: https://materialsproject.org, https://doi.org/10.24435/materialscloud:m7-50, https://icsd.products.fiz-karlsruhe.de

## Task Context

Generating stable, diverse, and novel inorganic crystalline materials that satisfy user-specified property constraints—including target chemical composition, crystal symmetry, magnetic density, electronic bandgap, mechanical bulk modulus, and multi-objective criteria such as high magnetic density combined with low supply-chain risk (quantified by Herfindahl–Hirschman Index)—via fine-tuned diffusion-based generative modeling.

## Metadata

- Dataset use ID: `dataset_use_af9e59a425ae`
- Original dataset title: Alex-MP-ICSD
- Tags: inverse materials design, crystal structure generation, property-constrained generation
