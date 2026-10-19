# Dataset: CIF Instruction Dataset

- Dataset ID: `D_P311_cif_instruction_dataset`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- CIF Instruction Dataset
- CIF instruction-output pairs
- crystallographic information files (CIF) dataset
- instruction-output pairs based on CIF files

## Observed material scopes

- inorganic materials
- crystals

## Observed research tasks

- crystal structure generation

## Observed research stages

- model_training

## Observed properties

- crystal stability
- elemental co-occurrence
- atomic spatial distributions
- stability-determining properties
- CIF file structure
- atomic frequency
- spatial coordinates
- crystal parameters
- site occupancy
- chemical formula

## Observed fields

- instruction-output pairs
- syntactic tasks
- semantic tasks
- training instances
- validation instances

## Usage evidence

- P102 (Foundational Large Language Models for Materials Research): training in instruction finetuning (IFT) on CIF — Train the LLaMat models to understand and reason about crystallographic concepts and principles.
- P102 (Foundational Large Language Models for Materials Research): training in parameter-efficient finetuning (PEFT) for generation — Enable the LLaMat-CIF models to generate novel crystal structures.

## Dataset evidence

- P311, PDF page 2, Results: "Concurrently, we developed LLaMat-CIF models through IFT of LLaMat models on crystallographic information files, a hand-curated dataset comprising five syntactic and four semantic tasks."
- P311, PDF page 7, Crystal Generation: "The instruction finetuning phase employed a dual-framework approach comprising syntactic tasks focused on CIF file structure interpretation (e.g., atomic frequency quantification, spatial coordinate analysis, and crystallographic parameter determination) and semantic tasks targeting crystal stability principles (e.g., elemental co-occurrence patterns, atomic spatial distributions, and stability-determining properties). This methodology generated approximately 7 million instruction-output pairs (6,941,865 training instances and 27,183 validation instances), enabling LLaMat to develop robust comprehension of both CIF file architecture and fundamental materials science principles."
- P311, PDF page 12, Methods: "To train the language models to generate crystals, we created a new set of tasks that enable the language models to train on various aspects of CIF. Specifically, we developed instruction-output pairs from CIF files sourced from AMCSD, Google GNoME, and the Materials Project to enhance LLaMat’s crystallographic comprehension and natural language query resolution capabilities. To this extent, we developed an instruction set implementing a dual-task framework comprising syntactic and semantic components."
