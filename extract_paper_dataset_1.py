import os
import json
import re
from pathlib import Path

import fitz  # pymupdf
from tqdm import tqdm
from openai import OpenAI
from dotenv import load_dotenv


PROMPT = """
You are a JSON extractor bot.
Please extract the research task → datasets mapping from this paper in JSON format.

The goal is to identify the concrete task/problem that the paper tries to solve, and then list all datasets or data resources used to solve or support that task. 
Important distinction:
- task_description should describe the task to be solved, not a summary of the whole paper, its method, its contributions, or its experimental results.
- db_description should describe both:
  1. what the dataset/data resource contains, and
  2. which task in this paper the dataset is used to solve or support.

Output format:
[
  {
    "task_description": "50 - 100 words describing the specific task or R&D problem the paper aims to solve, not a whole-paper summary",
    "task_tags": ["Core task keyword 1", "Core task keyword 2", "Core task keyword 3"],
    "datasets": [
      {
        "db_title": "the title of the dataset; use the official name if available",
        "db_description": "50 - 120 words describing what the dataset contains and what task it supports in this paper",
        "db_link": "the url of the dataset; use 'None' if not available"
      },
      {
        "db_title": "...",
        "db_description": "...",
        "db_link": "..."
      }
    ]
  }
]

Additional requirements:
- For task_description, focus on the actionable research task. Prefer wording such as "predicting...", "screening...", "designing...", "discovering...", "optimizing...", "classifying...", "constructing...", or "selecting...".
- Do not write task_description as a broad paper abstract. Avoid generic phrases such as "This paper proposes a machine learning framework..." unless they directly define the task.
- task_description should answer: "What task/problem does this paper need to solve?"
- db_description should answer: "What data does this dataset contain, and how is it used for the task in this paper?"
- db_description must include dataset content details when available, such as samples, fields, labels, source, scale, material system, experimental data, computational data, or candidate space.
- db_description must also mention the supported task, such as training a property predictor, screening candidates, validating synthesis outcomes, optimizing composition/process conditions, or benchmarking model performance.
- task_description and db_description must be clearly different: the former is the task/problem; the latter is the data content plus its role in solving that task.
- The dataset title or variations of its name must not appear in task_description.
- Do not treat code repositories, algorithms, software tools, instruments, characterization methods, or ordinary references as datasets.
- Extract author-curated data, experimental data, computational data, public databases, supplementary data, or candidate spaces only if they are clearly used in the paper.
- If a dataset is only mentioned in related work and is not used by the authors for their task, do not extract it.
- If no dataset is found, return [].
- Do not invent dataset names, links, fields, scales, or usages not stated in the paper.
- Return valid JSON only.
"""


def read_pdf_text(pdf_path: Path) -> str:
    """
    读取 PDF 文本。
    注意：如果 PDF 是扫描版图片，这个函数无法识别，需要额外 OCR。
    """
    text = []

    with fitz.open(pdf_path) as doc:
        for page_index, page in enumerate(doc, start=1):
            page_text = page.get_text("text")
            if page_text:
                text.append(f"\n\n--- Page {page_index} ---\n{page_text}")

    return "\n".join(text)


def clean_text(text: str) -> str:
    """
    简单清洗 PDF 文本。
    """
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_json(text: str):
    """
    解析模型返回的 JSON。
    兼容以下情况：
    1. 直接返回 JSON；
    2. 返回 ```json ... ```；
    3. JSON 前后夹杂少量说明文字。
    """
    if text is None:
        return []

    text = text.strip()

    if text.startswith("```"):
        text = re.sub(r"^```json", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"^```", "", text).strip()
        text = re.sub(r"```$", "", text).strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 尝试截取最外层 JSON 数组
    match = re.search(r"\[\s*{.*}\s*\]", text, flags=re.DOTALL)
    if match:
        return json.loads(match.group(0))

    # 兼容空数组
    if text.strip() == "[]" or "[]" in text:
        return []

    raise ValueError(f"模型输出不是合法 JSON，前 1000 个字符如下：\n{text[:1000]}")


def normalize_result(result):
    """
    对模型输出做简单规整，保证最终结果是 list。
    """
    if result is None:
        return []

    if isinstance(result, dict):
        if "tasks" in result and isinstance(result["tasks"], list):
            result = result["tasks"]
        else:
            return []

    if not isinstance(result, list):
        return []

    normalized = []

    for task in result:
        if not isinstance(task, dict):
            continue

        task_description = task.get("task_description", "")
        task_tags = task.get("task_tags", [])
        datasets = task.get("datasets", [])

        if not isinstance(task_description, str):
            task_description = ""

        if not isinstance(task_tags, list):
            task_tags = []

        if not isinstance(datasets, list):
            datasets = []

        clean_datasets = []

        for ds in datasets:
            if not isinstance(ds, dict):
                continue

            db_title = str(ds.get("db_title", "")).strip()
            db_description = str(ds.get("db_description", "")).strip()
            db_link = str(ds.get("db_link", "None")).strip()

            if not db_title:
                continue

            if not db_link:
                db_link = "None"

            clean_datasets.append(
                {
                    "db_title": db_title,
                    "db_description": db_description,
                    "db_link": db_link,
                }
            )

        if clean_datasets:
            normalized.append(
                {
                    "task_description": task_description.strip(),
                    "task_tags": [str(tag).strip() for tag in task_tags if str(tag).strip()],
                    "datasets": clean_datasets,
                }
            )

    return normalized


def call_glm(client: OpenAI, model: str, paper_text: str):
    """
    调用 GLM-4.7 模型进行抽取。
    """
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        max_tokens=4096,
        messages=[
            {
                "role": "system",
                "content": PROMPT,
            },
            {
                "role": "user",
                "content": f"Here is the paper text:\n\n{paper_text}",
            },
        ],
    )

    raw_output = response.choices[0].message.content
    parsed = extract_json(raw_output)
    return normalize_result(parsed)


def safe_name(filename: str) -> str:
    """
    避免 Windows 文件名非法字符。
    """
    return re.sub(r'[\\/:*?"<>|]', "_", filename)


def main():
    load_dotenv()

    input_dir = Path(os.getenv("INPUT_DIR", "数据集论文/无机晶体材料论文语料_公开全文/papers"))
    output_dir = Path("outputs/50_papers_extracted_json")
    output_dir.mkdir(exist_ok=True)

    api_key = os.getenv("QWEN_API_KEY")
    base_url = os.getenv("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    model = os.getenv("QWEN_MODEL", "qwen-plus")

    if not api_key:
        raise ValueError("请先在 .env 文件中设置 QWEN_API_KEY")

    if not input_dir.exists():
        raise FileNotFoundError(f"没有找到输入文件夹：{input_dir}")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    pdf_files = sorted(input_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"输入文件夹中没有找到 PDF 文件：{input_dir}")
        return

    all_results = []

    for pdf_path in tqdm(pdf_files, desc="Extracting"):
        print(f"\nProcessing: {pdf_path.name}")

        try:
            paper_text = read_pdf_text(pdf_path)
            paper_text = clean_text(paper_text)

            if not paper_text:
                result = []
            else:
                result = call_glm(client, model, paper_text)

            single_result = {
                "paper_file": pdf_path.name,
                "result": result,
            }

            all_results.append(single_result)

            output_path = output_dir / f"{safe_name(pdf_path.stem)}.json"

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"Saved to: {output_path}")

        except Exception as e:
            print(f"Failed: {pdf_path.name}")
            print(e)

            all_results.append(
                {
                    "paper_file": pdf_path.name,
                    "error": str(e),
                    "result": [],
                }
            )

    summary_path = output_dir / "50_papers_all_results.json"

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print(f"\nAll results saved to: {summary_path}")


if __name__ == "__main__":
    main()
