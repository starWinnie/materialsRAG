import argparse
import json
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DEFAULT_CHAT_MODEL = "qwen-plus"


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


ONTOLOGY_PROMPT = """
You are an ontology-guided materials dataset discovery planner.
Convert the user's fuzzy intent into minimal data-requirement subtasks for an LLM Wiki search system.

Use this ontology:
Entities:
- Paper
- Task
- Dataset
- DatasetUse
- MaterialSystem
- TargetProperty
- Representation
- Method
- RDStage
- Evidence

Important relations:
- Paper HAS_TASK Task
- Paper USES_DATASET Dataset
- Task HAS_DATASET_USE DatasetUse
- DatasetUse DESCRIBES_DATASET Dataset
- Dataset SUPPORTS_TASK Task
- Task STUDIES_MATERIAL_SYSTEM MaterialSystem
- Task TARGETS_PROPERTY TargetProperty
- Task REQUIRES_REPRESENTATION Representation
- DatasetUse PROVIDES_REPRESENTATION Representation
- Task USES_METHOD Method
- DatasetUse SUPPORTS_RD_STAGE RDStage
- DatasetUse SUPPORTED_BY_EVIDENCE Evidence

Instructions:
- Do not answer the user's final question.
- Do not recommend specific datasets unless explicitly named by the user.
- Decompose only into minimal necessary data-requirement subtasks.
- Each subtask must include preferred_entity_types and ontology_path.
- Use DatasetUse as the main evidence entity when recommending datasets for a task.
- Return JSON only.

Output JSON schema:
{
  "user_intent": "dataset_search | task_search | paper_search | method_search | ontology_planning | kg_query",
  "normalized_goal": "short English phrase",
  "material_systems": ["material system"],
  "target_properties": ["target property"],
  "task_type": "property prediction | materials discovery | catalyst screening | inverse design | benchmark | literature/data survey | other",
  "constraints": ["constraint"],
  "minimal_subtasks": [
    {
      "subtask_id": "T1",
      "subtask_name": "Target property label data",
      "data_requirement": "what must be found",
      "why_needed": "why this is necessary",
      "preferred_entity_types": ["DatasetUse", "Dataset", "Task"],
      "ontology_path": ["TargetProperty", "Task", "DatasetUse", "Dataset", "Paper"],
      "retrieval_query": "query for searching the LLM Wiki",
      "success_criterion": "how to know this is satisfied",
      "can_be_skipped_if": "condition or None"
    }
  ],
  "coverage_checklist": ["coverage criterion"],
  "minimality_rule": "how to remove unnecessary subtasks or datasets",
  "combined_retrieval_query": "single broad query"
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
    raise ValueError(f"Planner output is not valid JSON: {text[:500]}")


def infer_task_type(question: str) -> str:
    lower = question.lower()
    if any(word in lower for word in ["predict", "prediction", "预测"]):
        return "property prediction"
    if any(word in lower for word in ["discover", "discovery", "发现"]):
        return "materials discovery"
    if any(word in lower for word in ["screen", "screening", "筛选"]):
        return "materials discovery"
    if any(word in lower for word in ["catalyst", "催化"]):
        return "catalyst screening"
    if any(word in lower for word in ["inverse", "design", "反向设计"]):
        return "inverse design"
    if any(word in lower for word in ["benchmark", "基准", "评测"]):
        return "benchmark"
    return "other"


def fallback_plan(question: str) -> dict:
    task_type = infer_task_type(question)
    subtasks = [
        {
            "subtask_id": "T1",
            "subtask_name": "Task-dataset evidence",
            "data_requirement": "Find DatasetUse records that explicitly connect datasets to the user's research task.",
            "why_needed": "DatasetUse is the ontology entity that preserves how a paper uses a dataset for a task.",
            "preferred_entity_types": ["DatasetUse", "Dataset", "Task"],
            "ontology_path": ["Task", "DatasetUse", "Dataset", "Paper"],
            "retrieval_query": question,
            "success_criterion": "Retrieved evidence names a dataset and explains how it supports the task.",
            "can_be_skipped_if": "None",
        }
    ]

    if task_type in {"property prediction", "materials discovery", "catalyst screening", "inverse design"}:
        subtasks.extend(
            [
                {
                    "subtask_id": "T2",
                    "subtask_name": "Target property coverage",
                    "data_requirement": "Find evidence that datasets provide the target property or label needed by the task.",
                    "why_needed": "The target property defines whether a dataset can support prediction, screening, or discovery.",
                    "preferred_entity_types": ["DatasetUse", "TargetProperty", "Task"],
                    "ontology_path": ["TargetProperty", "Task", "DatasetUse", "Dataset"],
                    "retrieval_query": f"{question} target property label dataset",
                    "success_criterion": "Evidence mentions the target property and links it to a dataset.",
                    "can_be_skipped_if": "The user only asks for paper or method search.",
                },
                {
                    "subtask_id": "T3",
                    "subtask_name": "Representation availability",
                    "data_requirement": "Find whether datasets contain usable input representations such as composition, crystal structure, descriptors, graphs, CIF, or SMILES.",
                    "why_needed": "Models require compatible input representations, not only labels.",
                    "preferred_entity_types": ["DatasetUse", "Representation", "Dataset"],
                    "ontology_path": ["Representation", "DatasetUse", "Dataset", "Task"],
                    "retrieval_query": f"{question} composition structure representation descriptor graph CIF SMILES",
                    "success_criterion": "Evidence states a usable representation or modality for the dataset.",
                    "can_be_skipped_if": "The user does not need model-ready datasets.",
                },
            ]
        )

    return {
        "user_intent": "dataset_search",
        "normalized_goal": question,
        "material_systems": [],
        "target_properties": [],
        "task_type": task_type,
        "constraints": [],
        "minimal_subtasks": subtasks,
        "coverage_checklist": [
            "At least one DatasetUse record should support each necessary data requirement.",
            "Recommended datasets should satisfy task relevance, target-property coverage, and representation compatibility when needed.",
        ],
        "minimality_rule": "Keep only subtasks and datasets that add necessary coverage along the ontology path.",
        "combined_retrieval_query": " ".join(item["retrieval_query"] for item in subtasks),
    }


def clean_list(value) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def validate_plan(plan: dict, question: str) -> dict:
    if not isinstance(plan, dict):
        return fallback_plan(question)
    subtasks = plan.get("minimal_subtasks")
    if not isinstance(subtasks, list) or not subtasks:
        return fallback_plan(question)

    clean_subtasks = []
    for index, item in enumerate(subtasks, start=1):
        if not isinstance(item, dict):
            continue
        retrieval_query = str(item.get("retrieval_query") or "").strip()
        if not retrieval_query:
            retrieval_query = " ".join(
                part
                for part in [
                    str(plan.get("normalized_goal") or question),
                    str(item.get("subtask_name") or ""),
                    str(item.get("data_requirement") or ""),
                ]
                if part
            )
        preferred = clean_list(item.get("preferred_entity_types")) or ["DatasetUse", "Dataset", "Task"]
        path = clean_list(item.get("ontology_path")) or ["Task", "DatasetUse", "Dataset", "Paper"]
        clean_subtasks.append(
            {
                "subtask_id": str(item.get("subtask_id") or f"T{index}"),
                "subtask_name": str(item.get("subtask_name") or "Ontology-guided dataset evidence"),
                "data_requirement": str(item.get("data_requirement") or "Find task-relevant dataset evidence."),
                "why_needed": str(item.get("why_needed") or "This is required to ground retrieval in the ontology."),
                "preferred_entity_types": preferred,
                "ontology_path": path,
                "retrieval_query": retrieval_query,
                "success_criterion": str(item.get("success_criterion") or "Relevant evidence is found."),
                "can_be_skipped_if": str(item.get("can_be_skipped_if") or "None"),
            }
        )

    if not clean_subtasks:
        return fallback_plan(question)

    plan["user_intent"] = str(plan.get("user_intent") or "dataset_search")
    plan["normalized_goal"] = str(plan.get("normalized_goal") or question)
    plan["material_systems"] = clean_list(plan.get("material_systems"))
    plan["target_properties"] = clean_list(plan.get("target_properties"))
    plan["task_type"] = str(plan.get("task_type") or infer_task_type(question))
    plan["constraints"] = clean_list(plan.get("constraints"))
    plan["minimal_subtasks"] = clean_subtasks
    plan["coverage_checklist"] = clean_list(plan.get("coverage_checklist")) or ["Each necessary ontology path must have evidence coverage."]
    plan["minimality_rule"] = str(plan.get("minimality_rule") or "Remove subtasks that do not add necessary ontology coverage.")
    if not str(plan.get("combined_retrieval_query") or "").strip():
        plan["combined_retrieval_query"] = " ".join(item["retrieval_query"] for item in clean_subtasks)
    return plan


def normalize_query_ontology(client: OpenAI, model: str, question: str) -> dict:
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": ONTOLOGY_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    return validate_plan(extract_json(response.choices[0].message.content), question)


def format_plan(plan: dict) -> str:
    lines = [
        "Ontology-aware minimal subtasks:",
        f"- normalized_goal: {plan.get('normalized_goal', '')}",
        f"- material_systems: {', '.join(plan.get('material_systems') or []) or 'None'}",
        f"- target_properties: {', '.join(plan.get('target_properties') or []) or 'None'}",
        f"- task_type: {plan.get('task_type', '')}",
    ]
    for item in plan.get("minimal_subtasks", []):
        lines.extend(
            [
                f"- {item.get('subtask_id')} {item.get('subtask_name')}",
                f"  data_requirement: {item.get('data_requirement')}",
                f"  preferred_entity_types: {', '.join(item.get('preferred_entity_types') or [])}",
                f"  ontology_path: {' -> '.join(item.get('ontology_path') or [])}",
                f"  retrieval_query: {item.get('retrieval_query')}",
            ]
        )
    lines.append(f"- minimality_rule: {plan.get('minimality_rule', '')}")
    return "\n".join(lines)


def parse_args():
    parser = argparse.ArgumentParser(description="Create ontology-aware minimal subtasks from a fuzzy materials query.")
    parser.add_argument("question", nargs="+")
    parser.add_argument("--model", default=os.getenv("QWEN_MODEL", DEFAULT_CHAT_MODEL))
    parser.add_argument("--format", choices=["json", "text"], default="json")
    parser.add_argument("--fallback-only", action="store_true")
    return parser.parse_args()


def main():
    load_dotenv(PROJECT_ROOT / ".env")
    args = parse_args()
    question = " ".join(args.question)

    if args.fallback_only:
        plan = fallback_plan(question)
    else:
        api_key = os.getenv("QWEN_API_KEY")
        if not api_key:
            raise ValueError("Please set QWEN_API_KEY in .env, or use --fallback-only.")
        client = OpenAI(api_key=api_key, base_url=os.getenv("QWEN_BASE_URL", DEFAULT_BASE_URL))
        plan = normalize_query_ontology(client, args.model, question)

    if args.format == "text":
        print(format_plan(plan))
    else:
        print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
