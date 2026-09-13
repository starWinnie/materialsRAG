# 67_Generative Hierarchical Materials Search - Open Quantum Materials Database

## Dataset Use

A computational database of over 400,000 predicted inorganic crystal structures and their thermodynamic properties (e.g., formation energy), generated using density functional theory. In this paper, it is explicitly used alongside Materials Project and NOMAD to train the composition-conditioned diffusion model πlo (as stated in Section 3.2 and Appendix A.3), providing additional formula-to-structure pairs (Dlo) to expand coverage beyond Materials Project alone.

## Links

- Paper: [67 Generative Hierarchical Materials Search](../papers/67_Generative_Hierarchical_Materials_Search.md)
- Task: [task page](../tasks/67_Generative_Hierarchical_Materials_Search_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org

## Task Context

Generating novel, physically viable crystal structures that satisfy user-specified constraints expressed in natural language (e.g., 'a stable chalcogenide with atom ratio 1:1:2 that is not on ICSD'), by jointly optimizing for instruction compliance, structural validity, low formation energy, and uniqueness — without requiring pre-existing language-to-structure paired data.

## Metadata

- Dataset use ID: `dataset_use_fd435ba27da0`
- Original dataset title: Open Quantum Materials Database (OQMD)
- Tags: crystal structure generation, language-guided materials design, controllable generative modeling
