# Dataset: MaScQA

- Dataset ID: `D_mascqa`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MaScQA
- MaScQA question answering (Q&A) benchmark
- MaScQA benchmark

## Observed material scopes

- materials science
- metallurgical engineering

## Observed research tasks

- Evaluate LLMs' question-answering capabilities in materials science and metallurgical engineering

## Observed research stages

- data_acquisition
- model_evaluation
- computational_validation

## Observed properties

- conceptual understanding
- numerical reasoning
- pattern recognition
- structured matching

## Observed fields

- question
- answer
- question_type
- sub_field

## Usage evidence

- P101 (Exploring the expertise of large language models in materials science and metallurgical engineering): source in Use MaScQA benchmark dataset — Acquire a domain-specific, manually curated question-answering dataset covering diverse sub-fields of materials science.
- P101 (Exploring the expertise of large language models in materials science and metallurgical engineering): test in Evaluate LLM responses on MaScQA — Quantify each LLM's accuracy across four question types (MATCH, MCQ, MCQN, NUM) via automated scoring using GPT-4o as judge.
- P101 (Exploring the expertise of large language models in materials science and metallurgical engineering): benchmark in Compare against random baseline — Validate that LLM performance meaningfully exceeds chance-level guessing across all question categories.

## Dataset evidence

- P310, PDF page 1, Introduction: "In this study, we evaluated 15 different LLMs using the MaScQA question answering (Q&A) benchmark. This benchmark comprises questions from the Graduate Aptitude Test in Engineering (GATE), tailored to test models' capabilities in answering questions related to materials science and metallurgical engineering."
- P310, PDF page 2, 1.2 The MaScQA benchmark: "The MaScQA benchmark1 addresses this gap by providing a curated dataset of 650 questions covering diverse sub-elds within materials science, including thermodynamics, atomic structure, mechanical behavior, and materials characterization."
- P310, PDF page 2, 1.2 The MaScQA benchmark: "Originally consisting of 650 questions derived from the Graduate Aptitude Test in Engineering (GATE), the MaScQA benchmark was rened by ourselves by manually removing 6 Q&A samples due to issues such as duplication or missing information"
