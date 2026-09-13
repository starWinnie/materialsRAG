# 67_Generative Hierarchical Materials Search - Task 1

## Task Description

Generating novel, physically viable crystal structures that satisfy user-specified constraints expressed in natural language (e.g., 'a stable chalcogenide with atom ratio 1:1:2 that is not on ICSD'), by jointly optimizing for instruction compliance, structural validity, low formation energy, and uniqueness — without requiring pre-existing language-to-structure paired data.

## Metadata

- Task ID: `task_2aa8e2c04581`
- Source paper: [67 Generative Hierarchical Materials Search](../papers/67_Generative_Hierarchical_Materials_Search.md)
- Tags: crystal structure generation, language-guided materials design, controllable generative modeling

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/67_Generative_Hierarchical_Materials_Search_Materials_Project_dataset_use_80a2b088a4b4.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A publicly accessible database containing computed properties and crystal structures for over 140,000 inorganic materials, including CIF files, space groups, formation energies, and chemical formulae. In this paper, it is used to (1) provide formula-to-structure pairs (Dlo) for training the diffusion model πlo, (2) serve as a reference set for match rate evaluation via pymatgen's StructureMatcher, (3) assess uniqueness by checking whether generated formulae exist in its collection, and (4) supply DFT-computed formation energies for GNN pretraining and validation.

### [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)

- Usage page: [usage note](../dataset_uses/67_Generative_Hierarchical_Materials_Search_Inorganic_Crystal_Structure_Database_dataset_u.md)
- Original title in paper: Inorganic Crystal Structure Database (ICSD)
- Link: https://icsd.fiz-karlsruhe.de

A curated collection of experimentally determined inorganic crystal structures, containing over 200,000 entries with detailed structural information (atomic positions, lattice parameters, space groups) and chemical formulae. In this paper, it is used to (1) define uniqueness by filtering out generated formulae already present in ICSD, (2) support the high-level heuristic Rhi via a uniqueness checker against known structures, and (3) form part of the reference set for match rate evaluation alongside Materials Project.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/67_Generative_Hierarchical_Materials_Search_Open_Quantum_Materials_Database_dataset_use_fd.md)
- Original title in paper: Open Quantum Materials Database (OQMD)
- Link: https://oqmd.org

A computational database of over 400,000 predicted inorganic crystal structures and their thermodynamic properties (e.g., formation energy), generated using density functional theory. In this paper, it is explicitly used alongside Materials Project and NOMAD to train the composition-conditioned diffusion model πlo (as stated in Section 3.2 and Appendix A.3), providing additional formula-to-structure pairs (Dlo) to expand coverage beyond Materials Project alone.

### [NOMAD Repository](../datasets/NOMAD_Repository.md)

- Usage page: [usage note](../dataset_uses/67_Generative_Hierarchical_Materials_Search_NOMAD_Repository_dataset_use_e7320ad26156.md)
- Original title in paper: NOMAD Repository
- Link: https://nomad-lab.eu

A large-scale, FAIR-compliant repository of materials science data, including DFT-calculated crystal structures, energies, and metadata from published studies and automated workflows. In this paper, it is explicitly listed (alongside Materials Project and OQMD) as one of the sources used to train the diffusion model πlo for crystal structure generation, contributing formula-to-structure pairs (Dlo) and enabling broader compositional and structural diversity in training.

### [Wikipedia](../datasets/Wikipedia.md)

- Usage page: [usage note](../dataset_uses/67_Generative_Hierarchical_Materials_Search_Wikipedia_dataset_use_ef1056637b27.md)
- Original title in paper: Wikipedia
- Link: https://en.wikipedia.org

A general-purpose, collaboratively edited online encyclopedia containing high-level textual descriptions of materials, crystal families (e.g., perovskites, spinels), chemical concepts, and domain knowledge. In this paper, it serves as the primary source for high-level language-to-symbolic knowledge (Dhi), used in retrieval-augmented generation (RAG) to retrieve context about user queries (e.g., 'double perovskite') and guide the LLM πhi in generating chemically plausible and instruction-compliant formulae.
