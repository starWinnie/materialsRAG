# New LLM Wiki extraction

This directory contains a clean implementation of the extraction standard in
`材料论文抽取与LLM_Wiki构建规范.md`. It does not read or reuse any legacy
`llm_wiki*`, `outputs`, or registry data.

## Run

From the repository root:

```powershell
python .\newMethod\extract_llm_wiki.py --limit 30
```

The extractor:

1. selects PDFs by the natural-number prefix in the file name;
2. stores page-level text and evidence-page selection;
3. calls the configured Qwen-compatible endpoint for Task/Stage extraction;
4. calls it again for Dataset/DatasetUse extraction;
5. validates evidence against the stated 1-based PDF page;
6. normalizes identifiers and generates the complete `newLLMWiki` tree.

Configuration is loaded from the repository `.env`:

```text
QWEN_API_KEY=...
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
QWEN_MODEL=qwen-plus
```

Use `--resume` to skip papers whose validated normalized extraction already
exists. Intermediate artifacts are retained under
`newLLMWiki/raw/extractions/<paper_id>/`.

## Verify

Run the independent audit without calling an LLM:

```powershell
python .\newMethod\verify_llm_wiki.py
```

The audit rechecks evidence against physical PDF pages, graph references,
enumerations, derived-source links, duplicate DatasetUse events, explicit sample
counts, intermediate artifacts, and Markdown page counts. Its machine-readable
result is written to `newLLMWiki/reports/independent_audit.json`.

## Hybrid retrieval

Build the local dense index after the Wiki changes:

```powershell
python .\newMethod\retrieve_llm_wiki.py --build-index
```

Run a complete query (query rewrite, dense/BM25 recall, RRF fusion, graph
expansion, dataset-level reranking, coverage selection, and grounded answer):

```powershell
python .\newMethod\retrieve_llm_wiki.py `
  --question "我想研发稳定且带隙合适的无机钙钛矿，需要哪些数据集？"
```

To return the smallest dataset set that jointly covers all required stages and
target properties, enable minimum-set selection. Dataset usage roles are used as
soft tie-breakers, while property aliases such as `enthalpy` and `energy` are
normalized before coverage is evaluated:

```powershell
python .\newMethod\retrieve_llm_wiki.py `
  --selection-mode minimum `
  --question "预测无机晶体的热力学稳定性和分解焓需要哪些数据集？"
```

The default `--selection-mode recommend` preserves the original behavior and
returns several useful alternatives. `--max-results` is an upper bound in both
modes; in `minimum` mode the actual result can be smaller.

## V3: evidence-gated Top-1 / minimal portfolio

`retrieve_llm_wiki_node_edge_rerank_v3.py` keeps **retrieval ranking** and
**final selection** separate. Its `evidence_top1` mode addresses the common
case where several datasets look semantically similar but only one carries the
fields and role requested by the user. It uses only the candidate Dataset and
DatasetUse facts as evidence; it never assumes that every dataset used in a
similar historical Task provides that Task's target property.

```powershell
python .\newMethod\retrieve_llm_wiki_node_edge_rerank_v3.py `
  --selection-mode evidence_top1 `
  --max-results 3 `
  --question "为无机晶体势能面模型寻找同时含原子构型、能量、力、应力和磁矩的数据集"
```

For one explicit need, this returns the highest-ranked candidate that has
evidence for that need (Top-1). For multiple explicit needs, it returns a
small portfolio: each later dataset must cover a previously uncovered need.
Requests such as "use a benchmark for comparison" or "perform experimental
validation" must be stated in the query before benchmark or validation-only
datasets become required. The trace field `selection_diagnostics` records the
required needs, supporting candidates, winners, and uncovered needs.

The draft task-need labels in `../testQuery/task_need_drafts.json` and their
annotation rules in `../testQuery/task_need_annotation_schema.md` are the
evaluation counterpart. Do not evaluate this mode solely against all datasets
used in the source paper: some are inactive unless their activation instruction
appears in the query.

The dense index is stored in `newMethod/newWikiIndex/`. Every query also writes
an auditable JSON trace to `newMethod/retrieval_runs/`; use `--trace-output` to
choose its location. A final recommendation must resolve to at least one
`DatasetUse` page with paper evidence. Derived or private subsets are redirected
to a reusable public source only when the Wiki records the source relationship
and reconstruction instructions.

For deterministic reranking and answer formatting, while retaining LLM query
rewrite and dense embeddings, use:

```powershell
python .\newMethod\retrieve_llm_wiki.py `
  --question "your question" --no-llm-rerank --no-answer-llm
```
