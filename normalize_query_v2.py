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


NORMALIZE_PROMPT_V2 = """
You are a materials-science metadata reasoning assistant.
Your job is to convert a fuzzy user research intent into the minimal data-requirement subtasks needed to support dataset retrieval from a paper-task-dataset LLM Wiki.

This follows a Metadata-Reasoner style:
- Identify what the user wants to accomplish.
- Decompose the intent into the smallest necessary data needs.
- Each subtask should correspond to one necessary evidence/data requirement.
- Do not recommend concrete datasets unless the user explicitly names them.
- Do not answer the final research question.
- Prefer minimality: include only subtasks that are necessary for finding or evaluating datasets.
- If one subtask can be skipped under a clear condition, state that condition.
- Return compact JSON only.

Materials-domain decomposition dimensions:
- material scope: material family, chemical system, application domain, or None
- target property: band gap, formation energy, adsorption energy, stability, conductivity, synthesis condition, etc.
- task type: property prediction, materials discovery, catalyst screening, inverse design, benchmark, literature/data survey, other
- data requirements: labels/properties, input representations, candidate space, validation evidence, benchmark/evaluation evidence, compatibility constraints

Output JSON schema:
{
  "user_intent": "dataset_search | task_search | paper_search | method_search | subtask_planning | kg_query",
  "normalized_goal": "short English phrase",
  "material_scope": "short phrase or None",
  "target_properties": ["property 1", "property 2"],
  "task_type": "property prediction | materials discovery | catalyst screening | inverse design | benchmark | literature/data survey | other",
  "constraints": ["constraint 1"],
  "minimal_subtasks": [
    {
      "subtask_id": "T1",
      "subtask_name": "Target property label data",
      "related_rd_stage": "Dataset Selection",
      "data_requirement": "what evidence/data must be found",
      "why_needed": "why this is necessary for the user's goal",
      "expected_evidence_types": ["Dataset", "DatasetUse", "Task"],
      "retrieval_query": "query string for searching the LLM Wiki",
      "success_criterion": "how to know this subtask is satisfied",
      "can_be_skipped_if": "condition under which this subtask is unnecessary, or None"
    }
  ],
  "coverage_checklist": [
    "criterion that the selected datasets must satisfy"
  ],
  "minimality_rule": "rule for removing unnecessary subtasks or datasets",
  "combined_retrieval_query": "single broad query string"
}

Allowed related_rd_stage values:
- Problem Definition
- Candidate Space Construction
- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
- Optimization / Iteration
- Benchmarking / Evaluation
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


def infer_task_type(question: str) -> str:
    lower = question.lower()
    if any(word in lower for word in ["predict", "prediction", "预测"]):
        return "property prediction"
    if any(word in lower for word in ["discover", "discovery", "screen", "screening", "发现", "筛选"]):
        return "materials discovery"
    if any(word in lower for word in ["catalyst", "催化"]):
        return "catalyst screening"
    if any(word in lower for word in ["inverse", "design", "生成", "反向设计"]):
        return "inverse design"
    if any(word in lower for word in ["benchmark", "基准", "评测"]):
        return "benchmark"
    return "other"


def fallback_normalization(question: str) -> dict:
    query = question.strip()
    task_type = infer_task_type(query)

    subtasks = [
        {
            "subtask_id": "T1",
            "subtask_name": "Task-relevant dataset evidence",
            "related_rd_stage": "Dataset Selection",
            "data_requirement": "Find datasets, dataset-use records, and related task pages relevant to the user's research intent.",
            "why_needed": "The system needs dataset evidence before it can recommend or compare data sources.",
            "expected_evidence_types": ["Dataset", "DatasetUse", "Task"],
            "retrieval_query": query,
            "success_criterion": "Retrieved evidence explicitly connects datasets to the user's material task.",
            "can_be_skipped_if": "None",
        }
    ]

    if task_type in {"property prediction", "materials discovery", "catalyst screening", "inverse design"}:
        subtasks.append(
            {
                "subtask_id": "T2",
                "subtask_name": "Input and target compatibility evidence",
                "related_rd_stage": "Representation / Feature Construction",
                "data_requirement": "Check whether the retrieved datasets contain usable target labels and input representations such as composition, structure, descriptors, or experimental conditions.",
                "why_needed": "A dataset is only useful if it supports both the intended prediction/screening target and the required model inputs.",
                "expected_evidence_types": ["Dataset", "DatasetUse"],
                "retrieval_query": f"{query} target property labels input representation composition structure",
                "success_criterion": "Evidence mentions both target-property information and usable material representations.",
                "can_be_skipped_if": "The user only asks for a broad literature or paper search.",
            }
        )

    combined = " ".join(subtask["retrieval_query"] for subtask in subtasks)
    return {
        "user_intent": "dataset_search",
        "normalized_goal": query,
        "material_scope": "None",
        "target_properties": [],
        "task_type": task_type,
        "constraints": [],
        "minimal_subtasks": subtasks,
        "coverage_checklist": [
            "Each selected dataset must be explicitly connected to the user's task.",
            "Each necessary data need should be covered by at least one retrieved evidence item.",
        ],
        "minimality_rule": "Keep only subtasks that add a distinct necessary data requirement; remove datasets that do not cover any uncovered requirement.",
        "combined_retrieval_query": combined,
    }


def normalize_user_query_v2(client: OpenAI, model: str, question: str) -> dict:
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": NORMALIZE_PROMPT_V2},
            {"role": "user", "content": question},
        ],
    )
    plan = extract_json(response.choices[0].message.content)
    return validate_plan(plan, question)


def clean_string_list(value) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def validate_plan(plan: dict, question: str) -> dict:
    if not isinstance(plan, dict):
        return fallback_normalization(question)

    subtasks = plan.get("minimal_subtasks")
    if not isinstance(subtasks, list) or not subtasks:
        return fallback_normalization(question)

    clean_subtasks = []
    for index, subtask in enumerate(subtasks, start=1):
        if not isinstance(subtask, dict):
            continue

        subtask_name = str(subtask.get("subtask_name") or "Task-relevant dataset evidence").strip()
        data_requirement = str(subtask.get("data_requirement") or "").strip()
        why_needed = str(subtask.get("why_needed") or "").strip()
        related_stage = str(subtask.get("related_rd_stage") or "Dataset Selection").strip()
        retrieval_query = str(subtask.get("retrieval_query") or "").strip()

        if not retrieval_query:
            retrieval_query = " ".join(
                part
                for part in [
                    str(plan.get("normalized_goal") or question),
                    subtask_name,
                    data_requirement,
                    " ".join(clean_string_list(plan.get("target_properties"))),
                    str(plan.get("material_scope") or ""),
                ]
                if part
            )

        clean_subtasks.append(
            {
                "subtask_id": str(subtask.get("subtask_id") or f"T{index}").strip(),
                "subtask_name": subtask_name,
                "related_rd_stage": related_stage,
                "data_requirement": data_requirement,
                "why_needed": why_needed,
                "expected_evidence_types": clean_string_list(subtask.get("expected_evidence_types")) or ["Dataset", "DatasetUse", "Task"],
                "retrieval_query": retrieval_query,
                "success_criterion": str(subtask.get("success_criterion") or "Relevant evidence is found in the LLM Wiki.").strip(),
                "can_be_skipped_if": str(subtask.get("can_be_skipped_if") or "None").strip(),
            }
        )

    if not clean_subtasks:
        return fallback_normalization(question)

    plan["user_intent"] = str(plan.get("user_intent") or "dataset_search").strip()
    plan["normalized_goal"] = str(plan.get("normalized_goal") or question).strip()
    plan["material_scope"] = str(plan.get("material_scope") or "None").strip()
    plan["target_properties"] = clean_string_list(plan.get("target_properties"))
    plan["task_type"] = str(plan.get("task_type") or infer_task_type(question)).strip()
    plan["constraints"] = clean_string_list(plan.get("constraints"))
    plan["minimal_subtasks"] = clean_subtasks
    plan["coverage_checklist"] = clean_string_list(plan.get("coverage_checklist")) or [
        "All necessary data requirements must be covered by retrieved evidence."
    ]
    plan["minimality_rule"] = str(
        plan.get("minimality_rule")
        or "Keep only subtasks and datasets that add necessary coverage for the user's goal."
    ).strip()
    if not str(plan.get("combined_retrieval_query") or "").strip():
        plan["combined_retrieval_query"] = " ".join(subtask["retrieval_query"] for subtask in clean_subtasks)

    return plan


def subtask_queries(plan: dict) -> list[tuple[str, str]]:
    queries = []
    for subtask in plan.get("minimal_subtasks", []):
        label = f"{subtask.get('subtask_id', '')} {subtask.get('subtask_name', '')}".strip()
        query = str(subtask.get("retrieval_query") or "").strip()
        if query:
            queries.append((label, query))

    combined = str(plan.get("combined_retrieval_query") or "").strip()
    if combined:
        queries.append(("Combined", combined))
    return queries


def format_subtask_plan(plan: dict) -> str:
    lines = [
        "最小必要子任务：",
        f"- 标准化目标: {plan.get('normalized_goal', '')}",
        f"- 材料范围: {plan.get('material_scope', 'None')}",
        f"- 目标性质: {', '.join(plan.get('target_properties') or []) or 'None'}",
        f"- 任务类型: {plan.get('task_type', '')}",
    ]
    constraints = plan.get("constraints") or []
    if constraints:
        lines.append(f"- 约束条件: {', '.join(constraints)}")

    for subtask in plan.get("minimal_subtasks", []):
        lines.extend(
            [
                f"- {subtask.get('subtask_id')} {subtask.get('subtask_name')}",
                f"  related_rd_stage: {subtask.get('related_rd_stage')}",
                f"  data_requirement: {subtask.get('data_requirement')}",
                f"  why_needed: {subtask.get('why_needed')}",
                f"  retrieval_query: {subtask.get('retrieval_query')}",
            ]
        )
    lines.append(f"- minimality_rule: {plan.get('minimality_rule', '')}")
    return "\n".join(lines)


def parse_args():
    parser = argparse.ArgumentParser(description="Normalize a fuzzy materials query into minimal data-requirement subtasks.")
    parser.add_argument("question", nargs="+")
    parser.add_argument("--model", default=os.getenv("QWEN_MODEL", DEFAULT_CHAT_MODEL))
    parser.add_argument("--format", choices=["json", "text"], default="json")
    parser.add_argument("--fallback-only", action="store_true", help="Use the deterministic fallback without calling the LLM API.")
    return parser.parse_args()


def main():
    load_dotenv()
    args = parse_args()
    question = " ".join(args.question)

    if args.fallback_only:
        plan = fallback_normalization(question)
    else:
        api_key = os.getenv("QWEN_API_KEY")
        if not api_key:
            raise ValueError("Please set QWEN_API_KEY in .env, or use --fallback-only.")
        client = OpenAI(api_key=api_key, base_url=os.getenv("QWEN_BASE_URL", DEFAULT_BASE_URL))
        plan = normalize_user_query_v2(client, args.model, question)

    if args.format == "text":
        print(format_subtask_plan(plan))
    else:
        print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
