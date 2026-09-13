# 30-Paper Ontology Wiki Workflow

This workflow builds an ontology-organized LLM Wiki from the existing 30-paper `llm_wiki/raw` tables.

It does not modify the original `llm_wiki`, `wiki_index`, `ask_wiki.py`, or `build_wiki_index.py` files.

## 1. Build Ontology Wiki Pages

```powershell
python ontology_method/build_ontology_wiki_30.py
```

Output:

```text
ontology_method/ontology_wiki_30/
  raw/
  schema/
  pages/
    papers/
    tasks/
    datasets/
    dataset_uses/
    material_systems/
    target_properties/
    representations/
    methods/
    stages/
```

## 2. Build Retrieval Index

Use the existing indexing script, but point it to the new ontology wiki folder:

```powershell
python build_wiki_index.py --wiki-dir ontology_method/ontology_wiki_30 --output-dir ontology_method/ontology_wiki_index_30 --force
```

## 3. Ask With The Existing Retrieval Chain

Use the existing `ask_wiki.py`, but point it to the new ontology index:

```powershell
python ask_wiki.py --index-dir ontology_method/ontology_wiki_index_30 "钙钛矿带隙预测有哪些数据集"
```

This preserves the previous chain:

```text
Ontology Wiki pages -> index -> minimal subtask normalization -> hybrid retrieval -> LLM answer
```
