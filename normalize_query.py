import argparse
import json
import os
import re
import sys

from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DEFAULT_CHAT_MODEL = "qwen-plus"


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


NORMALIZE_PROMPT = """
You are a materials-science R&D planning assistant.
Convert the user's fuzzy request into the minimal necessary R&D stages that can be supported by datasets.

Important:
- Do not answer the user's final question.
- Do not recommend specific datasets unless they are explicitly mentioned by the user.
- Produce compact JSON only.
- The stages should be minimal: include only stages needed to find or evaluate datasets for the user's task.
- Each stage must include a retrieval query suitable for searching a task-dataset LLM Wiki.

Allowed stage names:
- Problem Definition
- Candidate Space Construction
- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
- Optimization / Iteration
- Benchmarking / Evaluation

Output JSON schema:
{
  "user_intent": "dataset_search | task_search | paper_search | method_search | stage_planning | kg_query",
  "normalized_research_task": "short English phrase",
  "material_system": "short phrase or None",
  "target_properties": ["property 1", "property 2"],
  "task_type": "property prediction | materials discovery | catalyst screening | inverse design | benchmark | other",
  "constraints": ["constraint 1"],
  "minimal_rd_stages": [
    {
      "stage_id": "S1",
      "stage_name": "Dataset Selection",
      "stage_goal": "what this stage must accomplish",
      "required_data": ["data requirement 1", "data requirement 2"],
      "expected_evidence_types": ["Dataset", "DatasetUse", "Task"],
      "retrieval_query": "query string for searching the LLM Wiki"
    }
  ],
  "combined_retrieval_query": "single broad query string"
}
"""


def extract_json(text: str) -> dict:
    text = (text or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```json", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"^```", "", text).strip()
        text = re.sub(r"```$", "", text).strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if match:
            return json.loads(match.group(0))
    raise ValueError(f"Normalizer output is not valid JSON: {text[:500]}")


def fallback_normalization(question: str) -> dict:
    query = question.strip()
    return {
        "user_intent": "dataset_search",
        "normalized_research_task": query,
        "material_system": "None",
        "target_properties": [],
        "task_type": "other",
        "constraints": [],
        "minimal_rd_stages": [
            {
                "stage_id": "S1",
                "stage_name": "Dataset Selection",
                "stage_goal": "Find datasets and dataset-use records relevant to the user's research task.",
                "required_data": ["relevant datasets", "dataset usage evidence", "related tasks"],
                "expected_evidence_types": ["Dataset", "DatasetUse", "Task"],
                "retrieval_query": query,
            }
        ],
        "combined_retrieval_query": query,
    }


def normalize_user_query(client: OpenAI, model: str, question: str) -> dict:
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": NORMALIZE_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    plan = extract_json(response.choices[0].message.content)
    return validate_plan(plan, question)


def validate_plan(plan: dict, question: str) -> dict:
    if not isinstance(plan, dict):
        return fallback_normalization(question)

    stages = plan.get("minimal_rd_stages")
    if not isinstance(stages, list) or not stages:
        return fallback_normalization(question)

    clean_stages = []
    for index, stage in enumerate(stages, start=1):
        if not isinstance(stage, dict):
            continue
        retrieval_query = str(stage.get("retrieval_query") or "").strip()
        stage_goal = str(stage.get("stage_goal") or "").strip()
        stage_name = str(stage.get("stage_name") or "Dataset Selection").strip()
        if not retrieval_query:
            retrieval_query = " ".join(
                part
                for part in [
                    str(plan.get("normalized_research_task") or question),
                    stage_name,
                    stage_goal,
                    " ".join(stage.get("required_data") or []),
                ]
                if part
            )
        clean_stages.append(
            {
                "stage_id": str(stage.get("stage_id") or f"S{index}"),
                "stage_name": stage_name,
                "stage_goal": stage_goal,
                "required_data": [str(item) for item in (stage.get("required_data") or [])],
                "expected_evidence_types": [str(item) for item in (stage.get("expected_evidence_types") or [])],
                "retrieval_query": retrieval_query,
            }
        )

    if not clean_stages:
        return fallback_normalization(question)

    plan["minimal_rd_stages"] = clean_stages
    if not plan.get("combined_retrieval_query"):
        plan["combined_retrieval_query"] = " ".join(stage["retrieval_query"] for stage in clean_stages)
    return plan


def stage_queries(plan: dict) -> list[tuple[str, str]]:
    queries = []
    for stage in plan.get("minimal_rd_stages", []):
        label = f"{stage.get('stage_id', '')} {stage.get('stage_name', '')}".strip()
        query = str(stage.get("retrieval_query") or "").strip()
        if query:
            queries.append((label, query))
    combined = str(plan.get("combined_retrieval_query") or "").strip()
    if combined:
        queries.append(("Combined", combined))
    return queries


def format_plan(plan: dict) -> str:
    lines = [
        "最小必要研发阶段：",
        f"- 标准化任务: {plan.get('normalized_research_task', '')}",
        f"- 材料体系: {plan.get('material_system', 'None')}",
        f"- 目标性质: {', '.join(plan.get('target_properties') or []) or 'None'}",
        f"- 任务类型: {plan.get('task_type', '')}",
    ]
    for stage in plan.get("minimal_rd_stages", []):
        lines.extend(
            [
                f"- {stage.get('stage_id')} {stage.get('stage_name')}: {stage.get('stage_goal')}",
                f"  required_data: {', '.join(stage.get('required_data') or []) or 'None'}",
                f"  retrieval_query: {stage.get('retrieval_query')}",
            ]
        )
    return "\n".join(lines)


def parse_args():
    parser = argparse.ArgumentParser(description="Normalize a fuzzy user query into minimal R&D stages.")
    parser.add_argument("question", nargs="+")
    parser.add_argument("--model", default=os.getenv("QWEN_MODEL", DEFAULT_CHAT_MODEL))
    return parser.parse_args()


def main():
    load_dotenv()
    args = parse_args()
    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        raise ValueError("Please set QWEN_API_KEY in .env.")
    client = OpenAI(api_key=api_key, base_url=os.getenv("QWEN_BASE_URL", DEFAULT_BASE_URL))
    question = " ".join(args.question)
    plan = normalize_user_query(client, args.model, question)
    print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
