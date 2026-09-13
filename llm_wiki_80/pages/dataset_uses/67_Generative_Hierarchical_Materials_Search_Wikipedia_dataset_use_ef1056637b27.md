# 67_Generative Hierarchical Materials Search - Wikipedia

## Dataset Use

A general-purpose, collaboratively edited online encyclopedia containing high-level textual descriptions of materials, crystal families (e.g., perovskites, spinels), chemical concepts, and domain knowledge. In this paper, it serves as the primary source for high-level language-to-symbolic knowledge (Dhi), used in retrieval-augmented generation (RAG) to retrieve context about user queries (e.g., 'double perovskite') and guide the LLM πhi in generating chemically plausible and instruction-compliant formulae.

## Links

- Paper: [67 Generative Hierarchical Materials Search](../papers/67_Generative_Hierarchical_Materials_Search.md)
- Task: [task page](../tasks/67_Generative_Hierarchical_Materials_Search_task_1.md)
- Dataset: [Wikipedia](../datasets/Wikipedia.md)
- Dataset URL: https://en.wikipedia.org

## Task Context

Generating novel, physically viable crystal structures that satisfy user-specified constraints expressed in natural language (e.g., 'a stable chalcogenide with atom ratio 1:1:2 that is not on ICSD'), by jointly optimizing for instruction compliance, structural validity, low formation energy, and uniqueness — without requiring pre-existing language-to-structure paired data.

## Metadata

- Dataset use ID: `dataset_use_ef1056637b27`
- Original dataset title: Wikipedia
- Tags: crystal structure generation, language-guided materials design, controllable generative modeling
