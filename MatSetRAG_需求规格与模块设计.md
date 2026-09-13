# MatSet-RAG 需求规格与模块设计说明

## 0. 文档信息

| 项目 | 内容 |
|---|---|
| 文档名称 | MatSet-RAG 需求规格与模块设计说明 |
| 文档版本 | v1.0-draft |
| 编写日期 | 2026-09-09 |
| 当前状态 | 需求与设计评审稿，尚未进入代码实现 |
| 目标系统 | 面向材料研发任务的关系约束最小数据集集合检索系统 |
| 建议方法名称 | MatSet-RAG |
| 建议问题名称 | Exact Dataset Portfolio Retrieval（EDPR） |
| 目标研究方向 | 数据库、信息检索与知识增强系统，长期目标为 KDD 等会议投稿 |

本文档用于冻结 MatSet-RAG 最小可执行版本的需求、数据结构、模块职责、接口边界、检索语义、评测方法和验收条件。未经需求评审，不进入正式代码实现。

---

## 1. 背景与问题

现有项目从材料论文中抽取 Paper、Task、Stage、Dataset 和 DatasetUse，并利用文本检索、向量检索、图扩展、语义重排和集合选择推荐数据集。现有方法已经证明“任务—数据集使用关系”比普通论文切块更适合材料数据推荐，但仍存在以下问题：

1. 查询中的材料、性质、阶段、数据角色和输入表示主要作为文本字段处理，缺少严格的 AND、OR 和变量约束语义。
2. 同一数据集在不同论文、不同任务中的历史用途可能被合并，容易产生跨证据拼接和通用数据库流行度偏置。
3. 当前流程以候选排序为主，最终“最小集合”更多是启发式选择，而不是带完整约束的精确集合优化。
4. DatasetUse 当前主要作为候选的支持证据，没有成为判断一个数据集是否真正满足一组联合条件的原子事实。
5. 当前实现集中在少数大型脚本中，查询解析、召回、图扩展、重排、集合选择和答案生成边界不清楚，难以消融、测试和复现。
6. 当前知识库包含部分测试论文，且现有 13 个测试问题已经被多轮使用，存在测试泄漏和调参污染风险。

MatSet-RAG 需要将问题从“给数据集打相关性分数”重新定义为：

> 给定一个包含多个材料研发条件、多个数据角色和显式布尔关系的用户任务，仅依据知识库中已存在且可追溯的关系事实，找到能够联合覆盖全部需求的最小公开数据集集合；如果无法完整覆盖，返回最优部分覆盖及其缺口，不允许隐式放宽硬约束。

---

## 2. 参考方法与设计边界

### 2.1 OG-RAG 提供的启发

OG-RAG 将本体映射后的复合事实表示为超边，并通过最小超边覆盖生成紧凑上下文。MatSet-RAG 借鉴以下思想：

- 使用本体约束领域术语；
- 将同一事实上下文中的多个字段组织为不可随意拆分的证据单元；
- 将“最小覆盖”作为显式优化目标；
- 输出可以快速追溯到来源的结构化证据。

MatSet-RAG 与 OG-RAG 的区别是：OG-RAG 最小化用于回答的上下文超边数量；MatSet-RAG 最小化最终推荐的数据集实体数量，并要求每个覆盖判断都有 DatasetUse 证据证书。

参考论文：[OG-RAG: Ontology-grounded retrieval-augmented generation for large language models](https://aclanthology.org/2025.emnlp-main.1674/)

### 2.2 SG-RAG 提供的启发

SG-RAG 将多条件事实查询建模为查询图，通过查询路径分解、实体归一化、结构匹配和子图组装，要求结果同时满足全部条件。MatSet-RAG 借鉴以下思想：

- 将自然语言问题转换为显式查询结构；
- 将多条件满足视为结构包含问题，而不是单纯相似度排序；
- 使用查询规划降低结构匹配成本；
- 区分完整匹配和回退结果；
- 单独评估查询条件数量对准确率和效率的影响。

MatSet-RAG 与 SG-RAG 的区别是：SG-RAG主要寻找一个满足全部条件的未知中心实体；MatSet-RAG允许多个数据集分别承担训练、验证、筛选等角色，并在角色需求全部满足的前提下最小化不同数据集数量。

参考论文：[Structure Guided Retrieval-Augmented Generation for Factual Queries](https://aclanthology.org/2026.acl-long.1873/)

### 2.3 已确认的系统边界

最小可执行版本必须遵守以下约定：

1. 允许多个数据集协同完成一个任务。
2. 查询必须支持 AND、OR 和数据角色分组。
3. 允许重构现有实体和关系 Schema。
4. 不允许自动创造新关系，不进行链路预测或数据集适用性推断。
5. 允许使用知识库中已经显式保存的别名、IS_A、DERIVED_FROM 和 VERSION_OF 等关系。
6. 不训练新的神经网络、图神经网络、重排模型或嵌入模型。
7. 可以使用现成 LLM 进行离线抽取和在线查询结构化，但 LLM 不决定候选是否满足关系约束。
8. 系统只推荐公开且可推荐的数据集；非公开、受限或不可直接获得的数据集必须过滤。
9. 暂不优化下载成本、许可成本、存储成本或计算成本。
10. 如果无法完整覆盖，必须明确返回未覆盖条件，不能偷偷放宽硬约束。
11. 测试论文的 Task、Stage、DatasetUse 和证据不得进入检索知识库。
12. 现有项目不能被覆盖；未来实现应建立独立项目。

---

## 3. 项目目标与非目标

### 3.1 最小版本目标

最小版本应完成以下闭环：

1. 读取现有 dataset-centered LLM Wiki 或符合新契约的 JSONL 数据。
2. 将 DatasetUse 转换为证据保持的关系事实束。
3. 接收人工编写的结构化查询。
4. 支持多个需求组之间的 AND。
5. 支持一个需求组内部多个候选模式之间的 OR。
6. 支持一个证据模式内部多个条件之间的 AND。
7. 支持一个条件内部多个可接受值之间的 OR。
8. 基于显式关系检索 DatasetUse 证据束。
9. 验证候选数据集是否满足每个角色需求组。
10. 精确求解最小数据集组合。
11. 过滤不公开或不可推荐数据集。
12. 输出完整覆盖证书或部分覆盖缺口。
13. 对 13 个固定案例进行论文级隔离评测。
14. 记录每个检索阶段的候选保留情况和运行时间。

### 3.2 后续版本目标

后续版本可以增加：

- 自然语言到查询图的 LLM 自动解析；
- 新论文 PDF 的自动抽取模块；
- 本体和别名自动候选发现后人工确认；
- 更大规模的论文语料；
- Web 界面；
- 专家适用性评测；
- 外部材料数据库接口。

### 3.3 明确不属于最小版本的内容

以下内容不进入第一版：

- 训练 GNN 或复现 SG-RAG 的支配嵌入；
- 训练任务专用 reranker；
- 使用 LLM 为候选数据集创造新的“适用于”关系；
- 自动推断两个数据集互补或可替代；
- 对非公开数据进行访问；
- 成本、许可和下载速度多目标优化；
- 端到端聊天界面；
- 在生成阶段添加知识库证据之外的推荐。

---

## 4. 核心术语与形式化定义

### 4.1 Dataset Profile

Dataset Profile 描述数据集本身已经明确记录的事实，包括：

- 数据集唯一标识；
- 规范名称、别名和版本；
- 数据集类型；
- 公开性和可推荐状态；
- 明确包含的材料范围；
- 明确包含的性质；
- 明确包含的数据字段或表示；
- 显式来源数据集或版本关系；
- 事实出处。

Dataset Profile 不能包含从多个历史用途推断出的综合能力。

### 4.2 DatasetUse Evidence Bundle

DatasetUse Evidence Bundle 是检索和约束验证的最小事实单元。它表示：

> 一个数据集在一篇论文的一个任务和一个研发阶段中，以某种角色，使用某些字段，服务于某种目的，并由具体原文证据支持。

一个 Evidence Bundle 至少包含：

| 字段 | 说明 |
|---|---|
| bundle_id | 证据束唯一标识 |
| dataset_id | 数据集标识 |
| dataset_use_id | DatasetUse标识 |
| paper_id | 来源论文 |
| task_id | 关联任务 |
| stage_id | 关联阶段 |
| usage_role | 使用角色 |
| material_scope | 本次用途明确涉及的材料范围 |
| target_properties | 本次用途明确支持的性质 |
| used_fields | 本次用途实际使用的字段 |
| representation | 本次用途所需表示 |
| purpose | 具体用途 |
| constraints | 筛选或使用约束 |
| evidence | 原文、页码、章节 |
| confidence | 抽取或人工确认置信度 |

一条 AND 模式默认必须在同一个 Evidence Bundle 内成立。禁止从不相关 Bundle 中分别拿出材料、性质和角色后拼成新的事实。

### 4.3 Requirement Need

Need 是用户任务中必须被覆盖的一个数据角色或需求组，例如：

- 训练数据；
- 预训练数据；
- 实验验证数据；
- 计算验证数据；
- 候选空间；
- 筛选数据；
- Benchmark 数据。

不同 Need 之间采用 AND 语义，即每个必需 Need 都必须得到满足。

### 4.4 Witness Pattern

一个 Need 可以有多个可接受的 Witness Pattern，它们之间采用 OR 语义。一个 Pattern 内包含：

- 可接受的数据角色集合；
- 材料条件；
- 性质条件；
- 表示条件；
- 阶段条件；
- 任务条件；
- 其他硬约束。

Pattern 内不同条件采用 AND；同一条件的多个可接受值采用 OR。

### 4.5 Exact Cover 与 Partial Cover

若所选数据集集合能覆盖全部 Need，则为 Exact Cover。

若不存在 Exact Cover，系统寻找覆盖 Need 数量最多的集合，并返回 Partial Cover。Partial Cover 必须列出未覆盖 Need 和导致失败的具体条件。

### 4.6 最小集合目标

第一版采用字典序目标：

1. 最大化硬需求覆盖数量；
2. 在完整覆盖可行时，最小化数据集数量；
3. 在数据集数量相同时，最大化证据质量；
4. 在证据质量相同时，优先精确实体与精确关系匹配；
5. 最后使用稳定的数据集 ID 排序保证可复现性。

不在第一版中考虑下载、许可、算力或存储成本。

---

## 5. 总体系统架构

```text
离线知识构建
论文 PDF / 已有抽取 JSONL
        │
        ▼
[M1] 抽取接入与格式校验
        │
        ▼
[M2] 实体规范化与显式本体映射
        │
        ▼
[M3] Dataset Profile + DatasetUse Evidence Bundle
        │
        ▼
[M4] 关系存储、倒排索引与统计信息

在线查询执行
用户问题 / 人工查询计划
        │
        ▼
[M5] 查询编译与逻辑校验
        │
        ▼
[M6] 选择性驱动的关系查询规划
        │
        ▼
[M7] Evidence Bundle 召回与见证验证
        │
        ▼
[M8] 最小数据集组合求解
        │
        ▼
[M9] 证据证书、缺口报告与答案生成
        │
        ▼
[M10] Trace、评估与实验分析
```

---

## 6. 模块详细设计

## M1. 抽取接入与格式校验模块

### 职责

负责接收现有 LLM Wiki JSONL 或未来自动 PDF 抽取模块的结果，检查字段、引用和标识完整性。该模块只接入和校验数据，不执行检索。

### 输入

- papers.jsonl；
- tasks.jsonl；
- stages.jsonl；
- datasets.jsonl；
- dataset_uses.jsonl；
- relations/edges.jsonl；
- 可选的 PDF 页级文本；
- 测试论文排除清单。

### 处理要求

1. 检查每个 ID 唯一。
2. 检查所有外键指向存在的实体。
3. 检查 DatasetUse 至少关联 Dataset、Paper、Task 和 Stage。
4. 检查原文证据包含 paper_id 和物理页码。
5. 检查 evidence 文本能在声明页中找到；找不到则标记无效。
6. 检查测试论文相关的 Task、Stage、DatasetUse 和 Evidence 是否已经排除。
7. 检查 restricted、not_directly_available 和 recommendable=false 的数据集状态。
8. 不允许在接入阶段静默修复缺失关系。

### 输出

- 通过校验的统一中间数据；
- 数据质量报告；
- 被拒绝记录及原因；
- 测试泄漏报告；
- 输入数据版本指纹。

### 禁止事项

- 不调用检索模型；
- 不生成新的 DatasetUse；
- 不根据文本相似性补外键；
- 不将缺失证据的记录自动设为有效。

### 验收标准

- 所有有效外键完整；
- 无重复主键；
- 测试论文泄漏数量为 0；
- 所有进入检索的 Evidence Bundle 至少包含一个通过页码核验的证据；
- 校验失败时返回非零状态并生成明确报告。

## M2. 实体规范化与显式本体模块

### 职责

将原始名称映射到稳定的规范实体，并维护明确批准的别名和上下位关系。该模块只做实体对齐和显式本体闭包，不做适用性推断。

### 管理对象

- Dataset Registry；
- Material Concept Registry；
- Property Concept Registry；
- Representation Registry；
- Role Registry；
- Stage Taxonomy；
- 别名关系；
- IS_A 关系；
- DERIVED_FROM 和 VERSION_OF 关系。

### 匹配等级

1. exact_id：相同规范 ID；
2. canonical_name：规范名称相同；
3. explicit_alias：命中人工或已批准别名；
4. explicit_is_a：通过知识库中明确保存的 IS_A 链匹配；
5. unresolved：无法安全映射。

不同等级必须被记录在 Trace 中。unresolved 不得自动当作满足条件。

### 输入

- 原始实体名称；
- Registry；
- 显式本体；
- 查询中出现的材料、性质、角色和表示术语。

### 输出

- 规范实体 ID；
- 匹配等级；
- 匹配路径；
- 未解析术语列表；
- 多义候选列表。

### 禁止事项

- 不根据 embedding 自动生成 ALIAS_OF；
- 不将 formation energy 自动等同于 thermodynamic stability，除非关系已被明确注册；
- 不将同一数据集家族的不同版本自动视为严格相同实体；
- 不创建 alternative_to 或 complements 关系。

### 验收标准

- 相同输入和相同 Registry 得到确定性结果；
- 每个非精确匹配都能返回显式映射路径；
- 所有未解析术语进入缺口报告；
- Registry 修改有版本号和变更记录。

## M3. 证据超图构建模块

### 职责

将规范化后的 Paper、Task、Stage、Dataset 和 DatasetUse 构造成证据保持的异构超图。DatasetUse Evidence Bundle 是该图的主要检索事实单元。

### 核心实体

- Paper；
- Task；
- StageInstance；
- Dataset；
- DatasetUseEvent；
- MaterialConcept；
- PropertyConcept；
- RepresentationConcept；
- RoleConcept；
- EvidenceSpan。

### 核心关系

| 关系 | 来源 | 目标 | 含义 |
|---|---|---|---|
| REPORTS_TASK | Paper | Task | 论文报告任务 |
| HAS_STAGE | Task | StageInstance | 任务包含阶段 |
| NEXT_STAGE | StageInstance | StageInstance | 论文中明确或按顺序记录的阶段关系 |
| FOR_TASK | DatasetUseEvent | Task | 此使用事件服务的任务 |
| AT_STAGE | DatasetUseEvent | StageInstance | 此使用事件所在阶段 |
| USES_DATASET | DatasetUseEvent | Dataset | 此事件使用的数据集 |
| HAS_ROLE | DatasetUseEvent | RoleConcept | 训练、验证、筛选等角色 |
| TARGETS_MATERIAL | DatasetUseEvent | MaterialConcept | 此用途涉及的材料体系 |
| PROVIDES_PROPERTY | DatasetUseEvent | PropertyConcept | 此用途实际提供或使用的性质 |
| USES_REPRESENTATION | DatasetUseEvent | RepresentationConcept | 此用途实际使用的表示或字段 |
| EVIDENCED_BY | DatasetUseEvent | EvidenceSpan | 证据来源 |
| DERIVED_FROM | Dataset | Dataset | 显式派生关系 |
| VERSION_OF | Dataset | Dataset | 显式版本关系 |

### 关键一致性约束

1. Dataset Profile 与 DatasetUse Event 分离。
2. DatasetUse 的局部性质不能直接由 Task 的全部 target_properties 无条件继承。
3. DatasetUse 的局部材料、性质、表示和角色必须有本次用途证据或明确的数据集字段支持。
4. 同一数据集的不同使用事件不得在构建阶段合并为一个万能 Evidence Bundle。
5. 数据集可以具有多个 Bundle，但查询验证时必须保留 bundle_id。
6. 测试论文的 Bundle 不得构建或载入。

### 输出

- 规范节点集合；
- 规范边集合；
- Evidence Bundle 集合；
- bundle_id 到原文证据的映射；
- 图统计和完整性报告。

### 验收标准

- 任意 DatasetUse 均可追溯到 Paper、Task、Stage、Dataset 和 Evidence；
- 任意推荐能力均能指出具体 bundle_id；
- 不存在跨论文合并后的匿名能力；
- 从 Bundle 到原始证据的反向定位成功率为 100%。

## M4. 关系索引与统计模块

### 职责

为无训练结构检索建立可复现的倒排索引，并维护查询规划所需的选择性统计。

### 必需索引

```text
material_concept_id       -> bundle_id 列表
property_concept_id       -> bundle_id 列表
representation_concept_id -> bundle_id 列表
role_concept_id           -> bundle_id 列表
stage_type                -> bundle_id 列表
task_type                 -> bundle_id 列表
dataset_id                -> bundle_id 列表
paper_id                  -> bundle_id 列表
bundle_id                 -> 完整 Evidence Bundle
dataset_id                -> Dataset Profile
```

### 统计信息

- 每个关系值的 posting 长度；
- 每类节点和关系数量；
- 每个数据集的 Bundle 数量；
- 每个角色和性质的频率；
- 公开且可推荐数据集数量；
- 每个索引版本对应的知识库指纹。

### 设计要求

1. 索引只能包含通过 M1 和 M3 验证的数据。
2. DatasetUse Bundle 可以被直接索引和召回。
3. 不以 DatasetUse 出现次数直接提高数据集相关性。
4. 高频数据集不能因拥有更多历史 Bundle 获得重复票数。
5. 索引重建必须是确定性的。

### 验收标准

- 相同输入生成相同索引摘要；
- 每个 posting 中无重复 bundle_id；
- 删除测试论文后，所有索引都不包含其 bundle_id；
- 支持输出索引大小、构建时间和频率统计。

## M5. 查询编译与逻辑校验模块

### 职责

将人工结构化查询或自然语言问题转换为统一的 EDPR Query Plan。最小版本优先支持人工 Query Plan，自然语言解析放在核心正确性验证之后。

### Query Plan 必需内容

- query_id；
- original_question；
- required_needs；
- 每个 Need 的 alternatives；
- 每个 Pattern 的 role_any_of；
- 每个 Pattern 的条件字段；
- 每个条件的 any_of；
- 硬约束标识；
- 排除论文清单；
- 未解析术语；
- Query Plan 版本。

### 布尔语义

- Needs 之间为 AND；
- 一个 Need 的 Patterns 之间为 OR；
- Pattern 内不同字段之间为 AND；
- 一个字段的 values 之间为 OR。

### 示例语义

用户需求：无机钙钛矿带隙预测，需要训练数据和实验验证数据。

```text
Need: training_data
  role = training OR pretraining
  AND material = inorganic_perovskite
  AND property = band_gap

Need: experimental_validation_data
  role = experimental_validation
  AND material = inorganic_perovskite
  AND property = band_gap
```

### LLM 使用边界

LLM只可以：

- 提取用户明确表达的条件；
- 建议 Query Plan 结构；
- 输出待校验的 JSON。

LLM不可以：

- 推荐具体数据集；
- 添加用户未表达的材料、性质或角色；
- 将软偏好改成硬约束；
- 创造新本体关系；
- 直接决定条件已经满足。

### 验收标准

- 人工 Query Plan 能通过 Schema 校验；
- 同一 Query Plan 的执行结果可复现；
- LLM Query Plan 必须经过字段白名单和本体校验；
- 解析失败时停止执行并列出问题，不退化成无约束语义检索。

## M6. 结构查询规划模块

### 职责

为每个 Need 生成低成本的关系检索计划，优先执行选择性高的条件，减少 Evidence Bundle 扫描量。

### 规划过程

1. 根据索引统计估计每个条件的候选规模。
2. 优先选择 posting 最短的条件作为锚点。
3. 对同一 Pattern 的条件执行 posting 交集。
4. OR 值先求并集，再参与其他字段的交集。
5. OR Patterns 分别执行，最后求候选并集。
6. 对候选 Bundle 执行完整见证验证。
7. 记录每一步的输入规模、输出规模和耗时。

### 关键原则

- 查询规划只改变执行顺序，不改变查询语义。
- 不能因为候选过少而删除硬条件。
- 不能设置会让正确结构不可达的固定 Top-K 截断。
- 如果需要语义索引帮助术语归一化，它只能产生规范实体候选，不能作为最终满足证据。

### 输出

- 每个 Need/Pattern 的执行计划；
- 候选 bundle_id；
- 计划成本估计；
- 实际扫描量；
- 未命中条件。

### 验收标准

- 与全量扫描产生完全相同的结构匹配结果；
- 不因执行顺序造成 Recall 损失；
- 能证明相对全量扫描的 Bundle 访问量下降；
- Trace 中可以定位候选在哪个条件交集步骤被移除。

## M7. 见证保持的候选验证模块

### 职责

验证某个 DatasetUse Evidence Bundle 是否完整满足某个 Witness Pattern，并聚合为“数据集能够覆盖哪些 Need”的可证明结论。

### 验证规则

1. 硬条件必须全部满足。
2. role、material、property、representation、stage 等条件必须通过规范实体或显式本体路径匹配。
3. 同一 Pattern 的 AND 条件默认必须由同一 Bundle 支持。
4. 若允许多个 Bundle 联合支持一个 Pattern，必须预先定义合法连接模板，例如共享 dataset_id、task_id 和兼容 stage_id；第一版建议不开启。
5. 一个数据集可以使用不同 Bundle 分别覆盖不同 Need。
6. 同一个 Bundle 无论被多少检索通道命中，都只计一次。
7. 证据不完整或来自排除论文时不得通过。

### 输出

对每个 dataset_id 输出：

- covered_need_ids；
- 每个 Need 的最佳 witness bundle；
- 每个条件的匹配值和匹配等级；
- 原文证据；
- 未满足的条件；
- 数据集资格状态。

### 验收标准

- 构造“跨 Bundle 拼接”的反例时必须拒绝；
- 单一 Bundle 同时满足全部条件时必须接受；
- 同一数据集通过不同 Bundle 覆盖不同 Need 时可以进入组合优化；
- 任意 covered Need 都有唯一可展示的 witness 证书。

## M8. 最小数据集组合优化模块

### 职责

从已经通过 M7 验证的数据集候选中，选择覆盖全部 Need 的最少数据集；若不可行，则返回最大覆盖的最小部分集合。

### 输入

- Need 集合；
- 每个数据集的 covered_need_ids；
- 每个覆盖关系的 witness 质量；
- 数据集公开性和 recommendable 状态。

### 约束

1. 仅 eligible 数据集可以进入求解。
2. Exact Cover 必须覆盖所有必需 Need。
3. 一个数据集可以覆盖多个 Need，但每个覆盖必须有独立 witness。
4. 不允许使用数据集家族替代严格数据集实体，除非查询明确允许 family 匹配。
5. 不允许为达到完整覆盖而使用未验证候选。

### 求解建议

第一版使用精确位图动态规划或分支定界：

- 每个 Need 对应一个 bit；
- 每个数据集对应一个覆盖 bitmask；
- 对完全相同或被支配的候选进行安全剪枝；
- 完整覆盖时最小化集合基数；
- 不可完整覆盖时先最大化 bit 数，再最小化集合基数；
- 证据质量只作为同基数结果的次级排序依据。

### 输出

- exact_cover；
- selected_dataset_ids；
- selected_dataset_count；
- covered_need_ids；
- uncovered_need_ids；
- 每次选择或剪枝的原因；
- 求解耗时；
- 是否达到数学意义上的精确最小解。

### 验收标准

- 使用穷举小样本验证求解结果最优；
- 一个数据集覆盖全部 Need 时返回一个；
- 两个互补数据集是唯一完整方案时返回两个；
- 不存在完整方案时 exact_cover=false；
- 重复运行结果一致。

## M9. 证据证书与结果生成模块

### 职责

将优化结果转换为机器可读证书和用户可读答案。答案生成不改变求解结果。

### 机器可读输出

- query_id；
- exact_cover；
- 选中数据集；
- 数据集承担的角色；
- 覆盖的 Need 和条件；
- witness bundle_id；
- paper_id、页码和原文；
- 未覆盖 Need；
- 未解析术语；
- 检索和求解诊断信息。

### 用户可读输出

必须优先说明：

1. 是否满足全部需求；
2. 最小集合有多少个数据集；
3. 每个数据集承担什么角色；
4. 哪些证据支持该角色；
5. 是否存在未覆盖条件；
6. 数据集是严格实体匹配还是家族/版本匹配。

### LLM 生成边界

如果使用 LLM 润色答案：

- 输入只能是已生成的证据证书；
- 输出的数据集 ID 必须属于 selected_dataset_ids；
- 输出的能力声明必须出现在 witness 证书中；
- 校验失败时退回确定性模板答案。

### 验收标准

- 每个推荐数据集至少有一条证据；
- 每个覆盖 Need 至少有一条 witness；
- 生成答案不出现证书以外的数据集；
- Partial Cover 的缺口必须在答案开头显式说明。

## M10. Trace、评估与实验模块

### 职责

记录端到端执行链路，计算检索、集合、结构、证据和效率指标，并支持 Baseline 与消融实验。

### Trace 必需阶段

```text
query_parse
entity_normalization
query_plan
posting_retrieval
posting_intersection
bundle_verification
dataset_coverage
eligibility_filter
minimum_set_solver
evidence_certificate
final_output
```

### 每阶段至少记录

- 输入数量；
- 输出数量；
- 被删除对象及原因；
- Gold 是否仍在候选中；
- 耗时；
- 使用的配置与数据版本。

### 评估输出

- 单案例结果；
- Macro/Micro 指标；
- 按材料、性质、角色和条件数量分组的结果；
- 错误类型；
- Gold 覆盖上限；
- 效率统计；
- 实验配置清单。

### 验收标准

- 能定位任意 Gold 在哪一阶段丢失；
- 不混淆检索 Top-K 与最终组合结果；
- 所有实验可由同一配置复现；
- Trace 不保存 API Key 或其他敏感信息。

## M11. 自动论文抽取模块（后续阶段）

### 职责

从新增材料论文中自动抽取能够进入 M1 的结构化事实。该模块是扩充知识库和构造新测试数据的入口，但不属于第一版检索闭环的阻塞项。

### 推荐处理流程

1. PDF 有效性检查；
2. 页级文本提取；
3. Paper 和 Task 抽取；
4. Stage 抽取；
5. Dataset 抽取；
6. DatasetUse 局部事实抽取；
7. 原文页码验证；
8. Dataset Registry 对齐；
9. 显式关系生成；
10. 独立审计；
11. 进入 M1。

### 特别要求

- DatasetUse 必须抽取局部 material、property、role 和 used_fields；
- 不得用 Task 的全部 target_properties 自动填充每条 DatasetUse；
- 自动抽取结果作为知识库数据时必须有证据核验；
- 自动抽取的测试答案如果未经人工检查，只能称为 Silver，而不能称为 Gold；
- 测试论文证据不得进入正式检索索引。

---

## 7. 数据资格与过滤规则

第一版不计算成本，但必须执行资格过滤。

### 7.1 可以推荐

同时满足：

```text
availability = public
AND recommendable = true
```

### 7.2 不可以推荐

任意满足：

```text
availability = restricted
OR availability = not_directly_available
OR recommendable = false
```

### 7.3 派生数据集处理

如果派生数据集不可直接获得，但显式记录了 DERIVED_FROM：

- 不得自动把来源数据集当作等价答案；
- 可以在缺口报告中说明存在来源关系；
- 只有当 Query Plan 或方法规范明确允许“可重建来源”时，后续版本才可将其作为替代；
- 第一版默认严格过滤不可推荐派生数据集。

---

## 8. 测试隔离与数据泄漏要求

### 8.1 严格隔离对象

对每个测试论文 P_test，知识库必须删除：

- Paper(P_test)；
- 该论文的 Task；
- 该论文的 Stage；
- 该论文的 DatasetUse；
- 该论文的 EvidenceSpan；
- 仅由该论文产生的任务—数据集关系。

### 8.2 可以保留的对象

公共 Dataset 节点及其独立 Registry 元数据可以保留，但不得包含从测试论文抽取出的用途能力。

### 8.3 评估分层

每个 Gold 数据集需要标记：

| 标记 | 含义 |
|---|---|
| exists_as_dataset | Dataset Registry 中存在 |
| has_non_test_witness | 具有非测试论文的有效 DatasetUse 证据 |
| eligible | 公开且可推荐 |
| exactly_answerable | 现有知识库原则上能够严格回答 |

必须同时报告：

- 全部 Gold 上的 Recall；
- exists_as_dataset=true 的 Gold Recall；
- has_non_test_witness=true 的 Gold Recall；
- exactly_answerable=true 的 Gold Recall。

### 8.4 现有 13 题的使用约束

现有 13 题已被多轮用于系统开发和参数调整，因此严格意义上已经不是完全未见测试集。后续应：

1. 立即冻结这 13 题，不再基于逐题结果修改规则；
2. 将其标记为 Legacy Test 或固定诊断集；
3. 新增一套从未用于开发的 Final Test；
4. 在论文中如实说明数据划分和开发历史。

---

## 9. 实验设计

### 9.1 研究问题

| 编号 | 研究问题 |
|---|---|
| RQ1 | MatSet-RAG 是否提高数据集实体检索准确率？ |
| RQ2 | MatSet-RAG 是否能更完整地满足多条件、多个角色需求？ |
| RQ3 | Witness-Preserving 约束是否减少跨证据拼接和通用数据库偏置？ |
| RQ4 | 最小集合优化是否减少冗余推荐，同时保持需求覆盖？ |
| RQ5 | 系统能否正确识别不可完整回答的查询？ |
| RQ6 | 关系索引和查询规划能否降低 Bundle 扫描量和查询延迟？ |
| RQ7 | 性能是否随查询条件数量和知识库规模稳定扩展？ |

### 9.2 Baseline

1. BM25 文本检索；
2. Dense Retrieval；
3. BM25 + Dense + RRF；
4. 当前 Wiki-RAG；
5. 当前 node-edge rerank v3；
6. OG-RAG-style：先最小覆盖证据超边，再聚合 Dataset；
7. SG-RAG-style：强制寻找一个满足全部条件的数据集；
8. MatSet-RAG 完整版本。

### 9.3 主要指标

#### 数据集实体指标

- Strict Precision、Recall、F1；
- Canonical Precision、Recall、F1；
- Family Precision、Recall、F1；
- Recall@1、Recall@3、Recall@5；
- Exact Set Match。

#### 结构指标

- Need Coverage Rate；
- All-Constraint Satisfaction Rate；
- Role Coverage Rate；
- Hard Constraint Violation Rate；
- Witness Consistency Rate；
- Exact Cover Detection Accuracy；
- Uncovered Need Detection Accuracy。

#### 证据指标

- Evidence Precision；
- Evidence Page Accuracy；
- DatasetUse Attribution Accuracy；
- 无证据推荐比例。

#### 集合指标

- 预测集合大小；
- Gold 集合大小；
- Cardinality Difference；
- 完整覆盖前提下的冗余数据集数量；
- 精确求解器与贪心求解器的集合大小差异。

论文作者采用的数据集集合不一定是真正最小，因此不能只根据“比 Gold 少”判断更优。数学最小性应由求解器正确性证明和小规模穷举验证；实际适用性需要人工分析或专家评估。

#### 效率指标

- 离线索引构建时间；
- 索引大小；
- 查询延迟 P50/P95；
- 每次查询访问的 Bundle 数量；
- posting 交集剪枝率；
- 最小集合求解时间；
- LLM 调用次数和 token 数；
- 不同知识库规模下的吞吐量。

### 9.4 消融实验

1. 去掉 Evidence Bundle 一致性，允许历史用途字段并集；
2. 去掉角色 Need，将全部条件展平；
3. 去掉显式本体，只保留原始字符串；
4. 用 Top-K 替换最小集合求解；
5. 用贪心集合覆盖替换精确求解；
6. 去掉选择性驱动规划，扫描全部 Bundle；
7. 不执行数据资格过滤；
8. 人工 Query Plan 与 LLM Query Plan 对比；
9. 无完整覆盖时强制返回 Top-1，而不是返回缺口；
10. 允许测试论文 DatasetUse 进入知识库，用于展示泄漏带来的虚假提升。

第 10 项只能作为泄漏敏感性实验，不能作为正式方法结果。

### 9.5 扩展性实验

- 查询条件数量：1、2、3、4、5、6；
- Need 数量：1、2、3、4；
- 论文数量：当前规模及后续扩展规模；
- Bundle 数量：按真实知识库逐级增加；
- 高频数据集占比：观察 Materials Project、JARVIS、OQMD 等高频实体的偏置；
- 不完整图：随机删除一部分非测试证据，评估 Partial Cover 稳定性。

---

## 10. 非功能需求

### 10.1 可复现性

- 核心检索与求解不依赖随机数；
- 同一数据、Query Plan 和配置必须得到相同结果；
- 所有 Registry、Ontology、Index 和 Query Plan 都有版本；
- 所有实验保存完整配置。

### 10.2 可解释性

- 每个推荐必须有 DatasetUse witness；
- 每个匹配条件必须显示证据值和匹配等级；
- 每个被过滤候选必须能说明原因；
- 每个未覆盖 Need 必须能定位到失败条件。

### 10.3 可维护性

- 单个模块只承担一种职责；
- LLM 调用不得散落在检索和求解模块中；
- 数据 Schema 与算法实现分离；
- 实验配置与源代码分离；
- 不允许再次形成单文件端到端巨型脚本。

### 10.4 安全性

- API Key 只从环境变量读取；
- Trace 中不得保存 API Key；
- 不修改原始 PDF；
- 不覆盖现有 newMethod 数据和实验输出；
- 新项目默认只读加载旧知识库。

### 10.5 性能

第一版不预设绝对毫秒目标，但必须满足：

- 结构索引检索结果与全量扫描一致；
- 查询规划显著减少平均 Bundle 访问量；
- 最小集合求解不成为当前规模下的主要延迟；
- 报告 P50/P95，而不仅报告平均值。

---

## 11. 推荐项目模块与目录职责

未来确认实现后，建议建立独立项目：

```text
MatSetRAG/
├─ README.md                 项目入口、运行方式、边界
├─ docs/                     方法、Schema、实验和决策记录
├─ schema/                   输入、知识图和Query Plan契约
├─ ontology/                 显式别名、IS_A和版本关系
├─ ingestion/                旧Wiki适配与抽取结果接入
├─ validation/               外键、证据和泄漏检查
├─ graph/                    Evidence Bundle和关系存储
├─ indexing/                 倒排索引、统计、版本指纹
├─ query/                    查询解析、规范化和逻辑编译
├─ planner/                  关系查询计划和执行顺序
├─ retrieval/                Bundle候选召回
├─ verification/             Witness-Preserving条件验证
├─ optimizer/                精确最小集合求解
├─ provenance/               证据证书和缺口报告
├─ evaluation/               指标、Baseline、消融和Trace
├─ configs/                  实验配置，不存密钥
├─ examples/                 示例Query Plan和预期结果
├─ tests/                    单元、集成、回归测试
└─ outputs/                  新项目输出，不写回旧目录
```

各模块不得反向依赖高层模块。例如 optimizer 只能接收候选覆盖矩阵，不应读取 PDF、调用 LLM 或访问原始 Wiki。

---

## 12. 实施阶段与退出条件

### Phase 0：需求和数据冻结

任务：

- 确认本文档；
- 确认测试论文清单；
- 冻结 13 题；
- 定义 Query Plan Schema；
- 定义 Evidence Bundle Schema。

退出条件：所有核心字段、AND/OR语义和测试隔离方案通过评审。

### Phase 1：旧数据适配与审计

任务：

- 只读加载现有 dataset-centered Wiki；
- 转换 DatasetUse Bundle；
- 生成公开性、证据和外键报告；
- 删除或屏蔽测试论文关系；
- 报告 Gold 理论可达率。

退出条件：测试泄漏为 0，Bundle 可追溯率为 100%。

### Phase 2：人工 Query Plan 的结构检索闭环

任务：

- 建立倒排索引；
- 编译 AND/OR/Need；
- 实现选择性驱动检索；
- 实现 Witness 验证；
- 输出候选覆盖矩阵。

退出条件：索引检索与全扫描结果一致，跨 Bundle 拼接反例全部被拒绝。

### Phase 3：最小组合与证据输出

任务：

- 实现精确最小集合求解；
- 实现 Partial Cover；
- 生成证据证书；
- 用小样本穷举验证最优性。

退出条件：全部求解器测试通过，结果可复现。

### Phase 4：13题隔离评测

任务：

- 为 13 题生成冻结 Query Plan；
- 执行论文级隔离；
- 运行 Baseline、完整方法和消融；
- 输出逐阶段 Gold 保留率。

退出条件：实验配置和 Trace 完整，所有指标可以一条命令重现。

### Phase 5：自然语言解析与语料扩展

任务：

- 接入 LLM Query Plan；
- 增加自动 PDF 抽取；
- 构造新的 Final Test；
- 增加规模和效率实验。

退出条件：自动解析和自动抽取误差可以与检索误差分开报告。

---

## 13. 当前工作符合性审计

审计时间：2026-09-09。

审计对象：当前根项目、`newMethod/LLMWiki_dataset_centered`、`retrieve_llm_wiki_node_edge_rerank_v3.py`、现有 13 题测试输出。

### 13.1 当前数据状态

当前 dataset-centered Wiki 的验证报告显示：

- 40 篇成功处理论文；
- 40 个 Task；
- 251 个 Stage；
- 138 个 Dataset；
- 136 个 DatasetUse；
- 1,691 条边；
- 2 篇论文抽取失败；
- 总体结构校验为 valid=true。

数据集资格状态：

- public 且 recommendable=true：80；
- public 且 recommendable=false：14；
- not_directly_available 且 recommendable=false：41；
- restricted 且 recommendable=false：2；
- restricted 且 recommendable=true：1。

这说明当前知识库已经具备公开性和可推荐字段，但不能只检查 recommendable；必须同时执行 availability=public。

### 13.2 当前关系状态

当前边类型包括：

- HAS_DATASET_USE：672；
- EVIDENCES_DATASET_USE：336；
- HAS_STAGE：251；
- NEXT_STAGE：211；
- USES_DATASET：136；
- DERIVED_FROM：45；
- REPORTS_TASK：40。

当前尚未将 Role、Material、Property 和 Representation 建模为可以直接参与结构查询的规范关系，因此无法完整执行本需求定义的查询图匹配。

### 13.3 符合性矩阵

| 需求 | 当前状态 | 判断 | 说明 |
|---|---|---|---|
| Paper/Task/Stage/Dataset/DatasetUse 基础实体 | 已存在 | 符合 | 已有可复用基础结构 |
| DatasetUse 原文和页码证据 | 已存在 | 部分符合 | 已有证据字段，但仍有2篇抽取失败，需要独立审计 |
| Dataset Profile 与 DatasetUse 分离 | 已存在 | 部分符合 | 实体已分离，但检索时仍会聚合多个 Task-Dataset 关系得分 |
| DatasetUse 作为直接检索事实 | 未实现 | 不符合 | v3 明确设置 dataset_use_direct_retrieval=false |
| 同一 Bundle 内验证全部 AND 条件 | 未实现 | 不符合 | 当前以节点召回、Pair重排和数据集聚合为主 |
| Role/Material/Property/Representation 关系节点 | 未完整实现 | 不符合 | 主要还是字段或重排文本，不是结构约束 |
| AND/OR/角色化 Query Plan | 部分存在 | 部分符合 | 已有QueryPlan字段，但没有完整布尔查询语义 |
| 不训练新模型 | 满足 | 符合 | 当前未见针对本任务重新训练模型 |
| 核心检索不依赖语义 reranker | 默认不满足 | 不符合 | v3 默认可执行一次语义 rerank，且候选排序依赖其结果 |
| 显式关系之外不创造新关系 | 基本遵守 | 部分符合 | 图扩展基于已有边，但语义重排和意图校准会影响能力判断 |
| 公开且可推荐硬过滤 | 未完全确认 | 部分符合 | 聚合逻辑处理 recommendable 和来源映射，但需要统一 availability=public Gate |
| 精确最小数据集集合 | 未实现 | 不符合 | 当前 minimum 与 adaptive minimum 均为候选池上的启发式选择 |
| 无完整覆盖时明确返回缺口 | 已有部分诊断 | 部分符合 | adaptive trace记录uncovered needs，但可能因分数阈值提前停止 |
| 不偷偷放宽硬约束 | 未保证 | 不符合 | 当前基于相似度、阈值和fallback top1，可能返回未完整满足结果 |
| 测试论文严格隔离 | 未实现 | 不符合 | 当前知识库包含 P032、P033 等测试范围论文 |
| 13题是未调参测试集 | 已不满足 | 不符合 | 13题已被多轮运行和调整，应视为Legacy Test/诊断集 |
| 每阶段 Gold 保留率诊断 | 已有部分Trace | 部分符合 | Trace很丰富，但需统一Gold注入和逐阶段统计 |
| 模块职责清晰 | 未满足 | 不符合 | 核心脚本超过十万字符并承担多个阶段职责 |
| 独立新项目且不覆盖旧系统 | 当前尚未创建 | 符合当前约定 | 此时只生成需求文档，没有保留新项目代码 |

### 13.4 审计结论

当前系统不是无效系统，而是一个具有丰富候选召回和 Trace 的关系检索原型。它已经满足以下前置条件：

- 有可用的实体化 Wiki；
- 有 DatasetUse 与原文证据；
- 有阶段结构；
- 有数据集公开性和可推荐状态；
- 有派生关系；
- 有节点检索、关系补全和候选诊断能力。

但是，当前系统尚不符合 MatSet-RAG 的核心正确性约定，主要缺口按优先级排序为：

1. 测试论文未严格隔离；
2. DatasetUse 没有作为 AND 条件验证的原子 Evidence Bundle；
3. 查询没有完整 AND/OR/角色分组语义；
4. 当前最小选择不是精确集合优化；
5. 公开性和可推荐状态尚未形成统一硬 Gate；
6. 核心结果仍受语义 rerank 和启发式阈值影响；
7. 大型脚本职责过多，难以进行可靠消融。

因此，当前工作可以作为 Baseline、旧数据来源和错误案例库，但不应直接继续在 v3 脚本中堆叠功能。推荐建立独立 MatSet-RAG 项目，以只读方式接入现有 Wiki，并按 Phase 0 至 Phase 4 重构。

---

## 14. 最小版本验收清单

只有全部满足以下条件，第一版才算完成：

- [ ] 已冻结 Evidence Bundle Schema；
- [ ] 已冻结 Query Plan Schema；
- [ ] 已明确13题对应的排除论文 ID；
- [ ] 所有测试论文关系已从索引中排除；
- [ ] 所有推荐数据集同时满足 public 和 recommendable；
- [ ] DatasetUse 可以作为完整 Bundle 直接检索；
- [ ] 支持 Need 间 AND；
- [ ] 支持 Pattern 间 OR；
- [ ] 支持 Pattern 内条件 AND；
- [ ] 支持条件值 OR；
- [ ] 不同历史 Bundle 不会被错误拼接；
- [ ] 每个覆盖判断都有 bundle_id；
- [ ] 最小集合求解经过穷举对照验证；
- [ ] 不完整覆盖能够返回 uncovered Need；
- [ ] 不使用 fallback top1 冒充完整覆盖；
- [ ] 核心检索和求解无需训练模型；
- [ ] LLM仅用于抽取、查询解析或受约束答案表达；
- [ ] Trace 可以定位 Gold 丢失阶段；
- [ ] 13题可以在隔离设置下一次性运行；
- [ ] Baseline、消融和完整方法使用相同知识库快照；
- [ ] 没有修改现有 newMethod 文件和输出；
- [ ] README能够解释每个模块的输入、输出和职责。

---

## 15. 需求评审待确认项

在生成代码前，需要最终确认：

1. MatSet-RAG 是否作为正式项目名；
2. Exact Dataset Portfolio Retrieval 是否作为正式问题名称；
3. 第一版是否只支持人工结构化 Query Plan；
4. 第一版是否坚持一个 Witness Pattern 必须由单个 Evidence Bundle 满足；
5. 现有13题分别对应哪些必须排除的 paper_id；
6. 家族匹配是只用于评估，还是允许进入实际推荐；
7. public 且 recommendable 是否是唯一资格条件；
8. 需求评审通过后是否按 Phase 0—Phase 4 建立独立项目。


==========================================================================
离线阶段：
```text
公开论文 PDF
    │
    ▼
第一步：离线知识库构建
    │
    ├─ 生成可验证的 DatasetUse Evidence Bundle
    ├─ 生成数据集实体、版本、子集及显式关系
    └─ 生成检索索引和知识库版本
    │
    ▼
第二步：在线检索
    │
    ├─ 解析用户任务中的 AND / OR / 角色需求
    ├─ 召回并验证 Evidence Bundle
    ├─ 求解最小公开数据集集合
    └─ 返回推荐、证据和未覆盖条件
```

两步之间只通过“冻结的知识库文件和索引”连接。在线检索不得临时修改知识库，也不得调用论文抽取流程。

# 第一步：离线知识库构建

## 1.1 建设目标

离线构建阶段不是简单地从论文中抽取数据集名称，而是要构建能够回答以下问题的事实库：

> 哪一个明确版本或子集的数据集，在什么论文、任务和阶段中，以什么角色，被用于哪些材料、性质和数据字段，并由哪一段原文支持？

最小事实单位不是 Dataset，而是：

> DatasetUse Evidence Bundle。

## 1.2 离线总体流程

```text
论文 PDF
  │
  ▼
O1 文档接入与页级解析
  │
  ▼
O2 Paper / Task / Stage 抽取
  │
  ▼
O3 Dataset 提及与精确身份抽取
  │
  ▼
O4 DatasetUse 局部用途抽取
  │
  ▼
O5 原文证据绑定
  │
  ▼
O6 数据集实体规范化
  │
  ▼
O7 Evidence Bundle 构建
  │
  ▼
O8 关系图构建
  │
  ▼
O9 倒排、稠密和关系索引构建
  │
  ▼
O10 质量校验与知识库发布
```

## 1.3 O1：文档接入与页级解析

### 职责

- 接收公开论文 PDF；
- 为每篇论文生成稳定的 `paper_id`；
- 提取每一物理页的文本；
- 保存页码、章节、表格标题、图注；
- 计算文件指纹，防止重复导入；
- 根据测试论文排除清单，标记论文用途。

### 关键输出

```json
{
  "paper_id": "P001",
  "file_name": "01_PRDNet.pdf",
  "sha256": "...",
  "page_count": 26,
  "is_test_paper": false,
  "pages": [
    {
      "physical_page": 8,
      "section": "EXPERIMENTS",
      "text": "..."
    }
  ]
}
```

### 重要约束

- 页码必须是 PDF 物理页码；
- 不能只保存整篇拼接文本；
- 测试论文可以用于构造 gold，但其 Task、DatasetUse 和证据不能进入检索知识库。

## 1.4 O2：Paper、Task、Stage 抽取

### Paper

保存标题、年份、作者、研究摘要和公开状态等论文级信息。

### Task

Task 只描述论文解决的问题，例如：

```json
{
  "task_id": "T_P001_01",
  "task_type": "crystal_property_prediction",
  "material_scope": ["crystalline_material"],
  "input_requirements": ["crystal_structure"],
  "target_properties": [
    "formation_energy",
    "band_gap",
    "bulk_modulus"
  ]
}
```

Task 中的性质集合只能表示论文总体任务，不能直接继承到所有 DatasetUse。

### Stage

Stage 表示实际研发或数据使用阶段，例如：

- data acquisition；
- data preparation；
- pretraining；
- model training；
- validation；
- benchmark evaluation；
- virtual screening；
- experimental validation；
- computational validation。

不应进入材料检索 Stage 体系的内容包括：

- 普通模型组件对比；
- 损失函数说明；
- 网络架构消融；
- 论文段落顺序。

例如 PRDNet 的“pseudo-particle 与 X-ray form factor 比较”应属于模型分析，而不是 `candidate_screening`。

### Stage顺序

只有论文明确描述先后依赖时，才建立 `NEXT_STAGE`。

不能简单按照论文段落出现顺序生成完整线性链。

## 1.5 O3：Dataset 精确身份抽取

这是当前知识库最需要修正的部分。

同一个数据集家族需要区分四层概念：

```text
Dataset Family
    └─ Dataset Version / Snapshot
           └─ Dataset Subset / View
                  └─ Benchmark Task Dataset
```

例如：

```text
JARVIS-DFT
├─ JARVIS dft_3d，75,993条
└─ JARVIS-DFT-3D-2021，55,723条
```

```text
Matbench
├─ matbench_jdft2d
├─ matbench_mp_e_form
├─ matbench_log_gvrh
└─ matbench_dielectric
```

这些实体不能只作为别名合并。

### Dataset Profile 建议字段

```json
{
  "dataset_id": "D_matbench_jdft2d",
  "canonical_name": "matbench_jdft2d",
  "entity_level": "benchmark_task",
  "parent_dataset_id": "D_matbench",
  "version": null,
  "material_scope": ["two_dimensional_layered_material"],
  "available_properties": ["exfoliation_energy"],
  "available_fields": ["crystal_structure", "exfoliation_energy"],
  "sample_count": 636,
  "availability": "public",
  "public_verified": true,
  "recommendable": true,
  "access_url": "...",
  "evidence": []
}
```

### 数据集身份合并规则

只有以下条件都满足时才能合并：

- 规范名称或官方标识一致；
- 版本或快照一致；
- 样本规模没有明显冲突；
- 数据来源一致；
- 数据集层级一致。

以下情况禁止合并：

- 家族与具体版本；
- 原始数据库与论文清洗后的子集；
- 不同年份快照；
- Matbench父套件与具体任务；
- 相同来源但具有不同筛选条件的数据集。

## 1.6 O4：DatasetUse 局部用途抽取

DatasetUse 描述“这一次具体使用”，不是数据集的全局能力。

建议每条原子记录至少包含：

```json
{
  "dataset_use_id": "DU_P001_007",
  "paper_id": "P001",
  "task_id": "T_P001_01",
  "stage_id": "S_P001_04",
  "dataset_id": "D_matbench_jdft2d",

  "usage_role": "benchmark",
  "material_scope": ["two_dimensional_layered_material"],
  "target_properties": ["exfoliation_energy"],
  "used_fields": ["crystal_structure", "exfoliation_energy"],
  "representation": ["periodic_crystal_structure"],
  "purpose": "evaluate exfoliation energy prediction",
  "constraints": [],
  "sample_count": 636,

  "evidence_ids": ["EV_P001_008_03"],
  "confidence": 1.0
}
```

### 原子化规则

出现以下任一差异时，必须拆成不同 Bundle：

- 数据集版本不同；
- 阶段不同；
- 使用角色不同；
- 样本量不同；
- 筛选条件不同；
- 性质的有效样本范围不同；
- 证据无法同时支持全部字段。

例如 Materials Project 在 PRDNet 中至少要区分：

```text
Bundle A
122,959条
formation energy + band gap + metal/non-metal

Bundle B
9,473条
bulk modulus + shear modulus + Young's modulus
```

不能把它们合成“122,959条同时包含六种性质”。

## 1.7 O5：证据绑定

每条证据独立保存：

```json
{
  "evidence_id": "EV_P001_008_03",
  "paper_id": "P001",
  "physical_page": 8,
  "section": "EXPERIMENTS",
  "evidence_type": "dataset_usage",
  "text": "...",
  "verified": true
}
```

### 证据支持规则

一个 Bundle 中的事实必须能够由该 Bundle 的证据共同支持：

- 数据集身份；
- 使用角色；
- 材料范围；
- 目标性质；
- 样本量；
- 筛选条件；
- 数据拆分。

例如摘要中“experiments are conducted on Matbench”只能证明使用了 Matbench，不能证明：

- 全部数据是 test set；
- test样本量等于数据集总量；
- 使用了某个特定拆分。

## 1.8 O6：规范化与显式本体

MVP 只允许保存或使用以下显式关系：

- `ALIAS_OF`；
- `IS_A`；
- `DERIVED_FROM`；
- `VERSION_OF`。

例如：

```text
matbench_jdft2d DERIVED_FROM Matbench
JARVIS-DFT-3D-2021 VERSION_OF JARVIS-DFT
two_dimensional_material IS_A crystalline_material
```

不允许离线构建阶段通过语义相似度自动生成新的事实关系。

模糊匹配可以产生“待审核候选”，但不能直接写入正式知识库。

## 1.9 O7：Evidence Bundle 构建

最终 Bundle 应包含完整的局部事实，而不是依赖在线阶段从多个全局字段中拼接。

建议 Bundle 结构：

```json
{
  "bundle_id": "B_P001_007",
  "dataset_use_id": "DU_P001_007",
  "dataset_id": "D_matbench_jdft2d",
  "paper_id": "P001",
  "task_id": "T_P001_01",
  "stage_id": "S_P001_04",

  "role": "benchmark",
  "materials": ["two_dimensional_layered_material"],
  "properties": ["exfoliation_energy"],
  "representations": ["periodic_crystal_structure"],
  "fields": ["crystal_structure", "exfoliation_energy"],
  "constraints": [],
  "evidence_ids": ["EV_P001_008_03"],

  "public_verified": true,
  "recommendable": true
}
```

MVP 的一条 AND 条件必须由同一个 Bundle 满足。

## 1.10 O8：关系图构建

DatasetUse Bundle 在图中作为中心事件节点：

```text
Paper ──EVIDENCES──► DatasetUseBundle
Task  ──FOR_TASK───► DatasetUseBundle
Stage ──AT_STAGE───► DatasetUseBundle

DatasetUseBundle ──USES_DATASET──────► Dataset
DatasetUseBundle ──HAS_ROLE──────────► Role
DatasetUseBundle ──TARGETS_MATERIAL──► Material
DatasetUseBundle ──PROVIDES_PROPERTY─► Property
DatasetUseBundle ──USES_REPRESENTATION► Representation
DatasetUseBundle ──EVIDENCED_BY──────► Evidence
```

### 最重要的禁止规则

DatasetUse 不允许按 `dataset_id` 全局合并。

正确主键应对应一次具体使用，例如：

```text
paper_id
+ task_id
+ stage_id
+ dataset_id
+ usage_role
+ 局部性质/约束分组
```

同一个 Materials Project 可以对应几十个 DatasetUse Bundle，这是正常的。

## 1.11 O9：索引构建

MVP 建议构建四类索引。

### 精确倒排索引

```text
material_id       -> bundle_id
property_id       -> bundle_id
role_id           -> bundle_id
stage_type        -> bundle_id
representation_id -> bundle_id
dataset_id        -> bundle_id
```

这是后续 AND 验证的主要索引。

### 文本索引

对以下文本建立 BM25：

- Task 描述；
- Dataset Profile；
- DatasetUse purpose；
- Evidence text。

### 稠密向量索引

使用已有预训练嵌入模型，只做推理，不训练模型。

向量检索只负责扩大候选召回，不能直接证明条件成立。

### 关系邻接索引

保存允许扩展的显式关系：

- Dataset到版本、父数据集和派生数据集；
- Material/Property本体的 `IS_A`；
- 显式别名。

## 1.12 O10：离线质量校验

正式发布知识库前，至少执行以下检查：

- 所有主键唯一；
- 所有外键存在；
- Bundle 没有跨论文合并；
- Bundle 没有跨阶段或角色合并；
- Evidence 具有 `paper_id + physical_page + text`；
- Evidence 文本能在对应页找到；
- 样本量与对应性质绑定；
- Dataset版本和父级实体没有混淆；
- 测试论文泄漏数量为0；
- `availability=public`；
- `public_verified=true`；
- `recommendable=true`；
- 非公开数据不会进入在线候选索引。

不能再只生成一个结构性的 `valid: true`，而应产生：

```text
结构完整性报告
证据一致性报告
Dataset身份冲突报告
DatasetUse原子性报告
公开性报告
测试泄漏报告
```

## 1.13 离线发布产物

```text
kb_release/
├─ manifest.json
├─ papers.jsonl
├─ tasks.jsonl
├─ stages.jsonl
├─ datasets.jsonl
├─ dataset_uses.jsonl
├─ evidence.jsonl
├─ bundles.jsonl
├─ relations.jsonl
├─ ontology/
├─ indexes/
└─ reports/
```

`manifest.json` 保存：

- 知识库版本；
- 构建时间；
- 输入论文指纹；
- Schema版本；
- 本体版本；
- 测试论文排除清单；
- 各类实体数量；
- 质量检查结果。

# 第二步：在线检索

## 2.1 在线检索目标

给定用户任务，返回：

> 能够联合覆盖全部硬需求的最小公开数据集集合。

如果不存在完整覆盖，则返回：

- 覆盖最多的公开数据集集合；
- 已覆盖条件；
- 未覆盖条件；
- 不能满足的具体原因。

## 2.2 在线检索总体流程

```text
用户查询
  │
  ▼
R1 Query Plan 构建
  │
  ▼
R2 术语规范化
  │
  ▼
R3 关系查询规划
  │
  ▼
R4 Evidence Bundle 候选召回
  │
  ▼
R5 同一 Bundle 内硬条件验证
  │
  ▼
R6 显式关系扩展
  │
  ▼
R7 Dataset–Need 覆盖矩阵
  │
  ▼
R8 最小数据集集合求解
  │
  ▼
R9 证据证书与缺口报告
```

## 2.3 R1：Query Plan 构建

查询首先转换成结构化 Need。

例如用户输入：

> 我需要用于训练无机晶体形成能预测模型的数据，以及用于二维材料剥离能评估的数据。

应转换为：

```json
{
  "needs": [
    {
      "need_id": "N1",
      "required": true,
      "witness_patterns": [
        {
          "roles": ["training", "benchmark"],
          "materials": ["inorganic_crystal"],
          "properties": ["formation_energy"],
          "representations": ["crystal_structure"]
        }
      ]
    },
    {
      "need_id": "N2",
      "required": true,
      "witness_patterns": [
        {
          "roles": ["benchmark", "test"],
          "materials": ["two_dimensional_material"],
          "properties": ["exfoliation_energy"],
          "representations": ["crystal_structure"]
        }
      ]
    }
  ],
  "dataset_policy": {
    "availability": "public",
    "recommendable": true
  }
}
```

### 逻辑语义

- 不同 Need 之间：AND；
- 同一个 Need 的多个 Witness Pattern：OR；
- 一个 Pattern 内的材料、性质、角色、表示：AND；
- 同一个字段的多个可接受取值：OR。

## 2.4 R2：术语规范化

只使用冻结的别名表和显式本体关系。

例如：

```text
formation energy → formation_energy
2D material → two_dimensional_material
MP → Materials Project
validation set → validation
```

规范化阶段不能偷偷扩展用户需求。

例如用户要求“实验数据”，不能自动改成“DFT计算数据也可以”。

## 2.5 R3：公开性硬过滤

进入候选池前必须满足：

```text
availability = public
AND public_verified = true
AND recommendable = true
```

以下数据可以保留在知识库中用于解释或溯源，但不能参与推荐：

- restricted；
- private；
- not directly available；
- public状态不确定；
- recommendable=false。

公开性过滤应该在最小集合求解前完成，而不是生成答案后再删除。

## 2.6 R4：候选召回

候选召回应采用三条通道。

### 通道A：精确关系召回

根据规范化后的：

- role；
- material；
- property；
- representation；
- stage；

执行倒排表交集。

这是主要通道。

### 通道B：文本召回

BM25 检索：

- DatasetUse purpose；
- Task；
- Dataset Profile；
- Evidence。

用于召回用户使用了未知表达方式的候选。

### 通道C：稠密语义召回

使用预训练嵌入进行向量召回。

它只能补充候选，最终仍必须经过关系验证。

三路候选可以使用 RRF 合并，但 RRF 分数不代表条件满足。

## 2.7 R5：Evidence Bundle 验证

对每个 Need 和 Bundle 执行确定性验证：

```text
role_match
AND material_match
AND property_match
AND representation_match
AND stage_match
AND public_gate
AND evidence_valid
```

所有条件默认必须在同一个 Bundle 中成立。

禁止：

```text
从论文A的Bundle取得材料
+ 从论文B的Bundle取得性质
+ 从论文C的Bundle取得角色
= 声称该数据集满足全部条件
```

### 匹配类型

每个匹配应记录类型：

- exact；
- alias；
- explicit IS_A；
- VERSION_OF；
- DERIVED_FROM；
- no_match。

这样最终可以解释为什么某个数据集被认为满足要求。

## 2.8 R6：有限关系扩展

只有直接召回不足时，才沿显式关系进行有限跳扩展。

MVP允许：

```text
ALIAS_OF
IS_A
VERSION_OF
DERIVED_FROM
```

建议最大2跳，并记录完整路径。

例如：

```text
matbench_jdft2d
DERIVED_FROM
Matbench
```

如果用户要求的是 Matbench 家族，可以找到子任务；但如果用户严格要求 `matbench_jdft2d`，不能用其他 Matbench 子任务替代。

## 2.9 R7：构造覆盖矩阵

验证结束后生成：

| Dataset | N1 | N2 | 证据质量 |
|---|---:|---:|---:|
| Dataset A | 1 | 0 | 0.95 |
| Dataset B | 0 | 1 | 0.93 |
| Dataset C | 1 | 1 | 0.78 |

其中 `1` 只能来自已经通过验证的 Bundle。

同一个 Dataset 可以使用不同 Bundle 覆盖不同 Need，但每个 Need 的 Witness Pattern 必须由单个 Bundle 满足。

## 2.10 R8：最小数据集集合求解

MVP使用确定性的精确求解，不使用训练模型。

目标按字典序执行：

1. 最大化硬需求覆盖数量；
2. 如果可以完整覆盖，最小化不同数据集数量；
3. 数据集数量相同时，最大化证据质量；
4. 优先 exact 匹配；
5. 最后按稳定 Dataset ID 排序。

形式上：

```text
max coverage
→ min dataset count
→ max evidence score
→ max exact-match count
→ stable ID tie-break
```

候选数据集规模较小时，可以：

- 穷举组合；
- branch-and-bound；
- 整数规划。

### 数据集计数单位

只计算“实际可推荐和可访问的数据集实体”。

Dataset Family 容器节点不计入结果。例如返回两个 Matbench 子任务时：

```text
matbench_mp_e_form
matbench_jdft2d
```

计为两个数据集，而不是因为它们都属于 Matbench 就计为一个。

如果系统未来把整个 Matbench suite 定义为一个可一次下载的交付单元，必须在 Schema 中明确，MVP暂不做这种成本折叠。

## 2.11 R9：结果生成

完整覆盖时返回：

```json
{
  "status": "exact_cover",
  "selected_datasets": [],
  "dataset_count": 2,
  "need_coverage": [],
  "evidence_certificates": [],
  "discarded_candidates": []
}
```

答案需要向用户说明：

- 推荐了哪些精确数据集版本或子集；
- 每个数据集覆盖哪个 Need；
- 承担什么角色；
- 支持哪些材料和性质；
- 使用哪条 DatasetUse 证据；
- 原文来自哪篇论文、哪一页；
- 为什么这是最小集合；
- 哪些相似候选被排除以及原因。

无法完整覆盖时返回：

```json
{
  "status": "partial_cover",
  "covered_needs": ["N1"],
  "uncovered_needs": ["N2"],
  "gaps": [
    {
      "need_id": "N2",
      "failed_conditions": [
        "没有公开数据集同时满足二维材料和实验验证角色"
      ]
    }
  ]
}
```

系统不得通过放宽材料、性质或角色条件伪造完整覆盖。

# 两步之间的核心接口

离线构建向在线检索提供以下只读内容：

```text
Dataset Profile
DatasetUse Evidence Bundle
Evidence Span
显式本体和版本关系
公开性状态
倒排索引
文本/向量索引
知识库版本指纹
```

在线检索不得：

- 修改 Dataset Profile；
- 合并 DatasetUse；
- 创建新本体关系；
- 把语义相似当作事实；
- 将测试论文证据加入知识库；
- 绕过公开性过滤。

# MVP实施顺序

建议严格按照以下顺序推进：

1. 冻结 Dataset、DatasetUse Bundle 和 Evidence Schema。
2. 用 PRDNet 一篇论文人工构造正确 gold。
3. 修改离线抽取，使 PRDNet 能稳定生成正确结果。
4. 再抽取3—5篇差异较大的论文做 Schema 压力测试。
5. 通过后批量重建知识库。
6. 冻结一个知识库版本。
7. 实现在线 Query Plan。
8. 实现 Bundle 召回和同束验证。
9. 实现精确最小集合求解。
10. 最后加入自然语言解析和答案生成。

最重要的边界是：

> 离线阶段负责生成可信事实；在线阶段只负责检索、验证和组合事实。不能让在线模型去修补离线知识库中的错误。