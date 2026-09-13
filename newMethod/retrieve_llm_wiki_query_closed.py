#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LLM Wiki 检索的“查询闭合证据”版本。

本文件不修改 retrieve_llm_wiki.py，而是复用其索引、Query Rewrite、
Dense/BM25、RRF、图扩展、候选聚合、重排、集合选择和答案生成流程，只替换
candidate_context() 的证据范围。

原版本：
    DatasetCandidate 一旦被发现，就读取该 Dataset 的全部历史 DatasetUse，
    并把它们加入 candidate.supporting_use_ids。

本版本：
    只读取 aggregate_dataset_candidates() 在本轮召回和图扩展中写入的
    candidate.supporting_use_ids；不再用未被本轮路径发现的历史用途补齐
    Task、Property、Stage、Role、relation evidence 或最终 coverage。

运行方式与原脚本一致，例如：

    python .\\newMethod\\retrieve_llm_wiki_query_closed.py \
      --question "预测无机晶体形成能需要哪些数据集？"

原 retrieve_llm_wiki.py 保持不变，可用于基线对照。
"""

from __future__ import annotations

from typing import Any

import retrieve_llm_wiki as base


# ---------------------------------------------------------------------------
# 1. 查询闭合候选上下文
# ---------------------------------------------------------------------------

def query_closed_candidate_context(
    store: base.WikiStore,
    candidate: base.DatasetCandidate,
) -> dict[str, Any]:
    """
    只使用本轮候选聚合阶段已经记录的 DatasetUse。

    注意：
    1. 不调用 store.uses_by_dataset[candidate.dataset_id] 补齐全部历史用途；
    2. 不修改 candidate.supporting_use_ids，保证它始终表示本轮支持证据；
    3. 按 Wiki 原始 DatasetUse 顺序返回，确保多次运行结果稳定；
    4. 派生数据集映射到公共源时，supporting_use_ids 可能属于派生数据集，
       这些用途仍然保留，因为它们正是本轮“公共源 + 构建说明”的路径证据。
    """

    dataset = store.dataset_by_id[candidate.dataset_id]
    supporting_ids = set(candidate.supporting_use_ids)

    # 使用 store.uses 的稳定原始顺序，避免直接遍历 set 导致 LLM 输入顺序波动。
    uses = [
        use
        for use in store.uses
        if use["dataset_use_id"] in supporting_ids
    ]
    tasks = [
        store.task_by_id[use["task_id"]]
        for use in uses
        if use["task_id"] in store.task_by_id
    ]
    stages = [
        store.stage_by_id[use["stage_id"]]
        for use in uses
        if use["stage_id"] in store.stage_by_id
    ]
    return {
        "dataset": dataset,
        "uses": uses,
        "tasks": tasks,
        "stages": stages,
    }


# ---------------------------------------------------------------------------
# 2. 安装局部替换，并给检索轨迹增加实验模式标记
# ---------------------------------------------------------------------------

def install_query_closed_mode() -> None:
    """
    在当前 Python 进程中替换基础模块的候选上下文函数。

    基础模块的 deterministic_rerank()、rerank_payload()、
    candidate_coverage() 和 candidate_requirement_atoms() 都在运行时调用
    base.candidate_context，因此一次替换即可让下列环节统一使用本轮证据：

    - 确定性 task/material/property/stage/role 匹配；
    - relation_evidence；
    - LLM rerank 的 observed_uses；
    - recommend 模式的 adds_coverage；
    - minimum 模式的阶段和性质覆盖；
    - 最终 evidence package。
    """

    base.candidate_context = query_closed_candidate_context

    # 在 trace 中记录实验模式，防止后续把新旧逻辑的结果混在一起。
    original_run_query = base.run_query

    def run_query_with_scope_marker(*args: Any, **kwargs: Any) -> tuple[str, dict[str, Any]]:
        answer, trace = original_run_query(*args, **kwargs)
        trace["evidence_scope_mode"] = "query_closed_supporting_uses_only"
        trace["evidence_scope_description"] = (
            "Candidate scoring and coverage use only supporting_use_ids found "
            "during the current retrieval and graph-expansion run."
        )
        return answer, trace

    base.run_query = run_query_with_scope_marker


# ---------------------------------------------------------------------------
# 3. CLI入口：全部参数和原脚本保持一致
# ---------------------------------------------------------------------------

def main() -> int:
    install_query_closed_mode()
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
