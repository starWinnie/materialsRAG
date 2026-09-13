# Ontology-Guided LLM Wiki Method

This folder is an independent prototype for adding ontology-guided reasoning to the existing materials LLM Wiki project.

It does not modify the existing `llm_wiki_all`, `wiki_index_all`, `ask_wiki.py`, `ask_wiki_all.py`, or README files.

## Goal

The current system retrieves over LLM Wiki pages. This ontology-guided layer adds an explicit schema for materials dataset discovery:

- Paper
- Task
- Dataset
- DatasetUse
- MaterialSystem
- TargetProperty
- Representation
- Method
- RDStage
- Evidence

The purpose is to make retrieval and agent planning more structured. Instead of only matching text similarity, the system can reason over entity types and ontology paths such as:

```text
MaterialSystem -> Task -> DatasetUse -> Dataset -> Paper
```

## Files

- `ontology_schema.yaml`
  - Defines the ontology entities, relations, and preferred retrieval behavior.

- `build_ontology_layer.py`
  - Reads the existing `llm_wiki_all/raw/*.csv` and derives ontology entities/relations using deterministic rules.
  - Writes new files only under `ontology_method/outputs/`.

- `normalize_query_ontology.py`
  - Converts a fuzzy user intent into minimal data-requirement subtasks with ontology-aware fields.
  - Each subtask includes `preferred_entity_types` and an `ontology_path`.

## Build Ontology Layer

Run from the project root:

```powershell
python ontology_method/build_ontology_layer.py
```

Outputs:

```text
ontology_method/outputs/ontology_entities.json
ontology_method/outputs/ontology_relations.json
ontology_method/outputs/ontology_summary.json
```

## Query Planning

LLM-based planning:

```powershell
python ontology_method/normalize_query_ontology.py "钙钛矿带隙预测有哪些数据集" --format text
```

Deterministic fallback without API:

```powershell
python ontology_method/normalize_query_ontology.py "钙钛矿带隙预测有哪些数据集" --fallback-only --format text
```

## How This Fits the Current Project

Current retrieval:

```text
Question -> minimal subtasks -> vector/BM25 over Wiki pages -> answer
```

Ontology-guided retrieval target:

```text
Question -> ontology-aware subtasks -> entity-type-aware retrieval -> relation expansion -> answer
```

This folder implements the ontology-aware representation and planning layer first. It can later be connected to `ask_wiki_all.py`, but this prototype intentionally leaves the existing scripts unchanged.
