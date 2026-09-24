# 任务需求与数据集组合标注规范

这份标注用于回答两个不同的问题：

1. 当前问题真正需要哪些数据能力；
2. 系统推荐的组合是否用有出处的证据支持了这些能力。

它不再把“原论文出现过哪些数据集”直接当成唯一标准答案。论文中用于消融、对比或附带分析的数据集，只有在用户问题明确要求相应工作时，才是当前问题的必需结果。

## 每个测试问题需要记录的内容

```json
{
  "case_id": "q001",
  "query": "用户原始问题",
  "source_paper_id": "Pxxx",
  "needs": [
    {
      "need_id": "N1",
      "description": "训练带隙预测模型所需的标签数据",
      "required": true,
      "trigger_text": "预测带隙",
      "acceptable_roles": ["training"],
      "required_material_scope": ["ABX3 perovskite"],
      "required_properties": ["band gap"],
      "required_fields": ["composition"],
      "evidence_rule": "同一DatasetUse记录或Dataset profile必须支持全部必需字段"
    },
    {
      "need_id": "N2",
      "description": "独立基准比较数据",
      "required": false,
      "activation_instruction": "在标准基准上与其他方法比较",
      "acceptable_roles": ["benchmark", "test"]
    }
  ],
  "paper_used_datasets": [
    {
      "dataset_id": "D_example",
      "paper_role": "benchmark",
      "need_ids": ["N2"],
      "include_for_current_query": false,
      "reason": "当前问题没有要求标准基准比较"
    }
  ],
  "review_status": "draft"
}
```

## 标注规则

- `required=true` 只放用户明确要求，或任务语义明确必需且两名标注者认可的需求。
- 原论文中使用的数据集必须写入 `paper_used_datasets`，但不自动进入任意 `needs`。
- 若某数据集 D 只用于基准比较、消融或额外验证，应写明 `activation_instruction`。用户没有该指令时，未召回 D 不算漏召回。
- 一个 Need 内的材料、性质、字段和角色是同时成立的条件；不能从不同 DatasetUse 记录拼接。
- 同一 Need 可以有多个合格数据集；记录全部人工认可的替代项，不把作者实际使用的单一数据集当作唯一正确答案。
- `review_status` 依次为 `draft`、`reviewed_by_annotator_1`、`adjudicated`。只有 `adjudicated` 可进入正式测试集。

## 新增评测指标

| 指标 | 计算方式 | 回答的问题 |
|---|---|---|
| 需求覆盖率 | 被证据支持的必需 Need / 必需 Need 总数 | 推荐组合支持了多少任务环节？ |
| 完整支持率 | 全部必需 Need 都被覆盖的问题比例 | 有多少问题可由推荐组合完整支持？ |
| 证据有效率 | 至少覆盖一个必需 Need 的推荐数据集 / 推荐数据集数 | 推荐中有多少不是冗余或无依据的？ |
| 冗余数 | 当前推荐数 - 同等覆盖下的最少推荐数 | 是否推荐了重复承担同一作用的数据集？ |
| 条件违反率 | 违反材料、性质、角色、字段任一硬条件的推荐比例 | “看起来相关但不能用”的比例有多高？ |

传统 Dataset Precision/Recall 仍保留，但只报告为“论文使用数据集命中”，不能单独代表任务推荐质量。
