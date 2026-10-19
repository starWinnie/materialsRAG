# Dataset: R2CID

- Dataset ID: `D_P311_r2cid`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- R2CID

## Observed material scopes

- inorganic materials
- crystals

## Observed research tasks

- crystal structure generation

## Observed research stages

- data_acquisition
- model_training

## Observed properties

- crystal structure
- atomic positions
- lattice parameters
- space group symmetry
- unit cell dimensions
- interaxial angles

## Observed fields

- CIF files
- natural language descriptions
- scientific literature
- RedPajama subset
- MatSci community discourse

## Usage evidence

- P102 (Foundational Large Language Models for Materials Research): source in pretraining dataset construction (R2CID) — Assemble a comprehensive, curated corpus of materials science knowledge for continued pretraining.
- P102 (Foundational Large Language Models for Materials Research): pretraining in continued pretraining (CPT) — Embed broad materials domain knowledge into the base LLaMA models through large-scale language modeling.

## Dataset evidence

- P311, PDF page 11, Methods: "Our pretraining dataset, designated R2CID, integrates three distinct components: scientific literature from materials research publications, a curated subset of RedPajama (the original pretraining corpus for LLaMA models), and crystallographic information files (CIF)."
- P311, PDF page 2, Results: "The initial stage comprised continued pretraining (CPT) on the base LLaMA models with an extensive and meticulously curated corpus developed in-house, namely R2CID... with greater than 30 billion tokens of MatSci knowledge, encompassing approximately 4 million peer-reviewed publications (94.43%), crystallographic information files (2.499%), and MatSci community discourse (0.019%). Additionally, we incorporated a strategic 3% subset of RedPajama data... to preserve fundamental linguistic capabilities while concurrently mitigating catastrophic forgetting."
