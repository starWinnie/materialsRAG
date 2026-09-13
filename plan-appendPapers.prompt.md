## Plan: 追加论文到现有 newLLMWiki

TL;DR: 现有 `newMethod/extract_llm_wiki.py` 脚本不是显式增量合并工具，但可以通过 `--resume` 复用已验正的抽取结果，并通过扩大 `--limit` 来将新论文加入已有输出。

**步骤**
1. 识别现有论文提取方式
   - 脚本按 PDF 文件名的自然数字前缀排序，选取前 `--limit` 个文件。
   - 处理结果写入 `output_root/newLLMWiki`，并在 `output_root/newLLMWiki/raw/extractions/<paper_id>/normalized.json` 中保存每篇论文的标准化结果。
   - `build_wiki()` 会基于本次运行的所有选中论文构建完整 Wiki 树，覆盖 `raw/papers.jsonl`、`pages/`、`relations/edges.jsonl` 等输出。

2. 使用 `--resume` 追加论文的推荐方式
   - 将新论文 PDF 放到同一输入目录，保证文件名以数字前缀开头，且编号在已抽取论文之后或一起排序。
   - 使用同样的 `--output-root` 指向已有 `newLLMWiki` 根目录。
   - 将 `--limit` 调整为“已抽取论文数 + 新论文数”或足够大，确保新的 PDF 被包含在选中列表中。
   - 运行脚本，例如：
     `python .\newMethod\extract_llm_wiki.py --limit 32 --resume`
   - 脚本会跳过已有 `normalized.json` 的论文，只对新论文再抽取，并重新生成整个 Wiki 输出。

3. 需要注意的行为和风险
   - 脚本没有直接读取旧 `manifest` 来做增量合并，`build_wiki` 会重写整个输出目录的 Wiki 文件。
   - 如果旧论文的 `normalized.json` 不在当前 `output_root/newLLMWiki/raw/extractions` 中，旧论文会重新抽取。
   - 如果希望只处理新论文而不重新构建旧论文，需要手动构建合并逻辑；当前脚本没有该功能。

4. 如果新论文在不同目录或编号不连续
   - 最稳妥的方式仍是把新论文统一放到同一输入目录，并用足够大的 `--limit` 包含所有目标论文。
   - 若只想增量抽取特定几篇，可先在单独目录运行脚本生成新结果，再手动合并现有 `newLLMWiki` 和新结果（该部分脚本当前不支持自动合并）。

**相关文件**
- `newMethod/extract_llm_wiki.py` — 主要实现抽取、`--resume` 复用、以及 `build_wiki()` 全量输出生成。
- `newMethod/README.md` — 说明了 `--resume` 的用途和运行方式。

**验证**
1. 确认已有 `newLLMWiki/raw/extractions/Pxxx/normalized.json` 存在。
2. 将新 PDF 加入输入目录，并设定 `--limit` 覆盖旧论文和新论文。
3. 运行 `python .\newMethod\extract_llm_wiki.py --limit <总数> --resume`。
4. 检查 `newLLMWiki/reports/validation_report.json` 是否通过验证，并确认新论文 `Pxxx` 已出现在 `newLLMWiki/pages/` 和 `raw/papers.jsonl` 中。

**进一步建议**
- 若你想要真正的“增量合并”功能，可考虑扩展脚本：读取已有 `raw/papers.jsonl`、`raw/datasets.jsonl`、`raw/dataset_uses.jsonl` 等，追加新论文结果后再写出完整合并结果。
- 也可以先把新论文抽取到独立 `output_root`，再按 `dataset_id`/`paper_id` 合并两个 Wiki 树。