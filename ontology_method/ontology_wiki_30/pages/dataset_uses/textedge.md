# TextEdge

## Ontology Type
DatasetUse

## Usage Description
TextEdge is a benchmark dataset curated by the authors, containing ~144,931 crystal structure-description pairs derived from the Materials Project database. Each entry includes a human-readable, Robocrystallographer-generated text description (e.g., space group, bonding geometry, Wyckoff sites, stoichiometry) and six labeled properties: band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap indicator. It is used to train and evaluate LLM-Prop for property prediction from text input, enabling fair comparison against GNN baselines on identical splits (125,098 train / 9,945 val / 9,888 test samples).

## Dataset
- [TextEdge](../datasets/textedge.md)

## Task
- [09_LLM_Prop.pdf](../tasks/09_llm_prop_pdf.md)

## Paper
- [09 LLM Prop](../papers/09_llm_prop.md)

## Provided Representations
- [composition](../representations/composition.md)
- [crystal structure](../representations/crystal_structure.md)
- [crystal graph](../representations/crystal_graph.md)
- [space group](../representations/space_group.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- TextEdge is a benchmark dataset curated by the authors, containing ~144,931 crystal structure-description pairs derived from the Materials Project database. Each entry includes a human-readable, Robocrystallographer-generated text description (e.g., space group, bonding geometry, Wyckoff sites, stoichiometry) and six labeled properties: band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap indicator. It is used to train and evaluate LLM-Prop for property prediction from text input, enabling fair comparison against GNN baselines on identical splits (125,098 train / 9,945 val / 9,888 test samples).

## Metadata
dataset_use_id: `dataset_use_1b2203043e7c`
link: https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG
