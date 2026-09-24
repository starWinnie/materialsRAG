# 材料论文 Task-Dataset LLM Wiki 项目说明

本项目用于从材料科学论文中抽取“研究任务 - 数据集使用”关系，并进一步构建标准三层 LLM Wiki、检索问答索引、知识图谱和研发阶段标注。当前系统的核心目标不是普通 PDF RAG，而是围绕材料研发任务、数据集和数据集使用场景组织知识。

## 1. 当前项目目标

项目当前支持以下流程：

```text
论文 PDF / 抽取结果
→ Task-Dataset 信息抽取
→ 标准三层 LLM Wiki
→ R&D 阶段标注
→ Wiki 页面检索索引
→ 阶段感知问答
→ 知识图谱与可视化
```

核心知识单元包括：

```text
Paper       论文
Task        论文中要解决的研究任务
Dataset     被使用的数据集或数据资源
DatasetUse  某个数据集在某篇论文某个任务中的具体使用方式
Tag         任务关键词
R&D Stage   研发阶段
```

其中 `DatasetUse` 是当前项目的关键设计：它不是只记录“论文用了某个数据集”，而是记录“这个数据集在该论文任务中具体支持了什么研发环节”。

## 2. 主要目录

```text
数据集论文/
```

原始 PDF 论文目录。

```text
outputs/
```

论文抽取结果目录。重要文件包括：

```text
outputs/30results.json      前 30 篇论文抽取结果
outputs/all_results.json    43 篇完整论文抽取结果
```

```text
llm_wiki/
```

基于 `outputs/30results.json` 构建的标准 LLM Wiki。

```text
llm_wiki_all/
```

基于 `outputs/all_results.json` 构建的完整 43 篇论文 LLM Wiki。当前主要实验建议使用这个目录。

```text
wiki_index/
```

基于 `llm_wiki/pages/` 构建的检索索引。

```text
wiki_index_all/
```

基于 `llm_wiki_all/pages/` 构建的完整检索索引。`ask_wiki_all.py` 默认使用这个目录。

```text
kg_outputs/
```

知识图谱输出目录，包括节点表、边表、JSON 图和 HTML 可视化。

```text
evaluation_output/
```

评估相关输出目录。

## 3. 标准 LLM Wiki 三层结构

每个 Wiki 目录都采用三层结构：

```text
llm_wiki_all/
├─ raw/
├─ pages/
└─ schema/
```

### 3.1 raw 原始资料层

```text
llm_wiki_all/raw/source_records.json
llm_wiki_all/raw/manifest.json
llm_wiki_all/raw/papers.csv
llm_wiki_all/raw/tasks.csv
llm_wiki_all/raw/datasets.csv
llm_wiki_all/raw/dataset_uses.csv
llm_wiki_all/raw/task_stages.csv
llm_wiki_all/raw/dataset_use_stages.csv
llm_wiki_all/raw/stage_summary.csv
```

其中：

```text
papers.csv              论文表
tasks.csv               任务表
datasets.csv            去重后的数据集表
dataset_uses.csv        数据集使用记录表
task_stages.csv         每个 Task 对应的研发阶段
dataset_use_stages.csv  每条 DatasetUse 对应的研发阶段
stage_summary.csv       阶段统计
```

### 3.2 pages Wiki 页面层

```text
llm_wiki_all/pages/papers/
llm_wiki_all/pages/tasks/
llm_wiki_all/pages/datasets/
llm_wiki_all/pages/dataset_uses/
llm_wiki_all/pages/stages/
```

每篇论文、每个任务、每个数据集、每条数据集使用记录、每个研发阶段都有 Markdown 页面。

### 3.3 schema 层

```text
llm_wiki_all/schema/wiki_schema.yaml
```

定义 Wiki 的实体、关系和页面组织规则。

## 4. 主要脚本说明

### 4.1 extract_paper_dataset_1.py

从 PDF 中抽取论文任务和数据集信息，输出 JSON。当前已有抽取结果，一般不需要频繁重跑。

### 4.2 build_llm_wiki.py

从抽取 JSON 构建标准三层 LLM Wiki。

常用命令：

```powershell
python .\build_llm_wiki.py --input .\outputs\all_results.json --output-dir .\llm_wiki_all
```

或构建前 30 篇版本：

```powershell
python .\build_llm_wiki.py --input .\outputs\30results.json --output-dir .\llm_wiki
```

### 4.3 annotate_rd_stages.py

给 Task 和 DatasetUse 标注研发阶段，并生成阶段页面。

当前阶段标注是规则法，不调用 API，结果可复现。它可以作为后续论文实验中的 baseline。

常用命令：

```powershell
python .\annotate_rd_stages.py --wiki-dir .\llm_wiki_all
```

### 4.4 build_wiki_index_all.py

从 `llm_wiki_all/pages/` 构建语义检索索引，默认输出到 `wiki_index_all/`。这一步会调用 Qwen embedding API。

常用命令：

```powershell
python .\build_wiki_index_all.py --wiki-dir .\llm_wiki_all --output-dir .\wiki_index_all --force
```

### 4.5 ask_wiki_all.py

完整 43 篇 Wiki 的问答入口。它默认使用 `wiki_index_all/`。

当前问答流程：

```text
用户模糊问题
→ normalize_query.py 生成最小必要研发阶段
→ 每个阶段生成 retrieval_query
→ 按阶段检索 LLM Wiki
→ 合并证据
→ Qwen 生成阶段化答案
```

常用命令：

```powershell
python .\ask_wiki_all.py "我想做钙钛矿带隙预测，需要哪些数据集？" --show-plan --show-context
```

关闭阶段规划，退回直接检索：

```powershell
python .\ask_wiki_all.py "哪些论文使用 Materials Project？" --no-normalize-query
```

提高证据数量：

```powershell
python .\ask_wiki_all.py "哪些论文使用 Materials Project？" --top-k 30 --stage-top-k 10
```

### 4.6 normalize_query.py

将用户模糊输入转成最小必要研发阶段。

单独测试：

```powershell
python .\normalize_query.py "我想做钙钛矿带隙预测，需要哪些数据集？"
```

输出包括：

```text
normalized_research_task
material_system
target_properties
task_type
minimal_rd_stages
retrieval_query
```

### 4.7 build_kg_from_wiki.py

从 `llm_wiki_all/raw/` 构建知识图谱。

常用命令：

```powershell
python .\build_kg_from_wiki.py --wiki-dir .\llm_wiki_all --output-dir .\kg_outputs
```

输出：

```text
kg_outputs/kg_nodes.csv
kg_outputs/kg_edges.csv
kg_outputs/kg_graph.json
```

### 4.8 visualize_kg_3.py

根据 `kg_outputs/kg_graph.json` 生成本地 HTML 知识图谱可视化页面。

常用命令：

```powershell
python .\visualize_kg_3.py
```

输出：

```text
kg_outputs/kg_visualization.html
```

### 4.9 evaluate_llm_dataset_recommendations.py

用于评估 LLM Wiki 问答/推荐结果的脚本。后续论文实验可以继续扩展。

## 5. 推荐完整工作流

如果使用完整 43 篇论文，推荐按下面顺序运行：

```powershell
python .\build_llm_wiki.py --input .\outputs\all_results.json --output-dir .\llm_wiki_all
python .\annotate_rd_stages.py --wiki-dir .\llm_wiki_all
python .\build_wiki_index_all.py --wiki-dir .\llm_wiki_all --output-dir .\wiki_index_all --force
python .\ask_wiki_all.py "我想做钙钛矿带隙预测，需要哪些数据集？" --show-plan --show-context
```

如果还要生成知识图谱：

```powershell
python .\build_kg_from_wiki.py --wiki-dir .\llm_wiki_all --output-dir .\kg_outputs
python .\visualize_kg_3.py
```

## 6. 30 篇版本和 43 篇版本的区别

```text
30 篇版本：
outputs/30results.json
llm_wiki/
wiki_index/
ask_wiki.py

43 篇版本：
outputs/all_results.json
llm_wiki_all/
wiki_index_all/
ask_wiki_all.py
```

当前如果做完整实验，建议使用 43 篇版本。

## 7. 当前 43 篇版本规模

截至当前版本，`llm_wiki_all` 包含：

```text
Papers: 43
Tasks: 43
Unique datasets: 70
Dataset uses: 140
```

研发阶段标注统计大致为：

```text
Problem Definition: 43 tasks
Dataset Selection: 43 tasks, 140 dataset uses
Representation / Feature Construction: 18 tasks
Model Training: 17 tasks
Screening / Prediction: 42 tasks, 140 dataset uses
Validation: 9 tasks, 73 dataset uses
Benchmarking / Evaluation: 4 tasks, 60 dataset uses
```

## 8. R&D 阶段说明

当前定义的研发阶段包括：

```text
Problem Definition
Candidate Space Construction
Dataset Selection
Representation / Feature Construction
Model Training
Screening / Prediction
Validation
Optimization / Iteration
Benchmarking / Evaluation
```

当前 `annotate_rd_stages.py` 使用规则法标注阶段：

```text
关键词 / 模式匹配 → 阶段标签
```

优点：

```text
不调用 API
不消耗额度
速度快
结果可复现
适合作为 baseline
```

缺点：

```text
语义理解有限
可能漏判或误判
不如 LLM-based annotation 灵活
```

后续如果写科研论文，可以将规则法作为 baseline，再设计 LLM-based stage annotation 与人工标注进行对比。

## 9. 注意事项

1. `.env` 中包含 API Key，不要外传。

2. 构建 Wiki 本身不需要 API，但构建检索索引和问答需要调用 Qwen API。

3. 如果修改了 `llm_wiki_all/pages/`，需要重新运行：

```powershell
python .\build_wiki_index_all.py --wiki-dir .\llm_wiki_all --output-dir .\wiki_index_all --force
```

4. 如果重新生成 `llm_wiki_all/`，需要重新运行阶段标注：

```powershell
python .\annotate_rd_stages.py --wiki-dir .\llm_wiki_all
```

5. RAG 问答不等于精确数据库查询。如果要完整枚举某个数据集被哪些论文使用，优先查：

```text
llm_wiki_all/raw/dataset_uses.csv
```

6. `top-k` 会影响问答是否完整。需要更全的证据时提高：

```powershell
--top-k 30 --stage-top-k 10
```

## 10. 后续可扩展方向

可以继续补充：

```text
1. LLM-based R&D stage annotation
2. 人工 gold annotation 数据集
3. PDF-RAG / JSON-RAG / Wiki-RAG 对比实验
4. Graph-aware retrieval
5. Dataset role classification
6. Human-in-the-loop Wiki 修正
7. Web UI 问答界面
```

## 11. 项目当前定位

本项目可以定位为：

```text
面向材料科学论文的数据集使用知识发现的 Schema-guided Wiki-RAG + Knowledge Graph 系统
```

和普通 RAG 的区别在于：

```text
普通 RAG：原始文档切片 → 检索 → 回答
本项目：论文抽取结果 → Schema 化 Wiki 页面 → R&D 阶段标注 → Wiki 检索 / 知识图谱 → 回答
```
#   m a t e r i a l s R A G  
 