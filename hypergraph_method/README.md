# Ontology-Hypergraph Dataset Retrieval

This folder implements an independent hypergraph retrieval prototype for materials R&D intent to dataset recommendation.

It does not modify the existing LLM Wiki or `ask_wiki.py` files.

## Design

The graph is built only from `outputs/30results.json`.

The held-out test queries are built from papers that appear in `outputs/all_results.json` but not in `outputs/30results.json`.

## Hypernodes

Hypernodes are structured semantic conditions that a dataset recommendation should cover:

- `material_system`
- `target_property`
- `data_source_type`
- `representation`
- `rd_stage`
- `task_type`
- `dataset_family`

Examples:

```text
material_system:perovskite
target_property:band gap
data_source_type:experimental
representation:crystal structure
task_type:property prediction
```

## Hyperedges

The method uses two edge types:

1. `DatasetUseEdge`
   - A paper-level evidence edge.
   - It represents how one paper uses one dataset for one task.

2. `DatasetCapabilityEdge`
   - A dataset-level capability edge.
   - It aggregates all DatasetUse evidence for the same dataset in the 30-paper graph.

The retrieval first uses capability edges to find candidate datasets, then uses DatasetUse edges to provide paper-level evidence.

## Build 30-Paper Hypergraph

```powershell
python hypergraph_method/build_hypergraph_30.py
```

Outputs:

```text
hypergraph_method/outputs/hypergraph_30/
  hypernodes.json
  hyperedges.json
  dataset_use_edges.json
  dataset_capability_edges.json
  node_to_edges.json
  summary.json
```

## Retrieve

```powershell
python hypergraph_method/retrieve_hypergraph.py "我想找实验钙钛矿带隙预测数据集" --max-capability-edges 5 --max-use-edges 5
```

The algorithm:

```text
query
-> rule-based query nodes
-> candidate hyperedges through node_to_edges
-> weighted greedy set cover
-> selected dataset capabilities and DatasetUse evidence
```

## Build Held-Out Queries

```powershell
python hypergraph_method/build_heldout_queries.py
```

Output:

```text
hypergraph_method/outputs/heldout_queries.json
```

## Evaluate Held-Out Retrieval

```powershell
python hypergraph_method/evaluate_heldout_hypergraph.py
```

Outputs:

```text
hypergraph_method/outputs/heldout_eval/
  heldout_hypergraph_results.csv
  heldout_hypergraph_summary.json
```

## Why This Is Different From BM25/Embedding Retrieval

This method does not rank pages by text similarity.

It maps the query into ontology nodes and selects hyperedges that cover the query nodes. In other words, it asks:

```text
Which dataset evidence covers the user's material system, target property, data source type, and representation needs?
```

This makes ontology act as retrieval control rather than only page content.
