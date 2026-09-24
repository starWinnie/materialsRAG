import argparse
import json
import os
import re
import sys
import subprocess
import hashlib
from datetime import datetime
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from ask_wiki import (
    DEFAULT_BASE_URL,
    DEFAULT_CHAT_MODEL,
    format_context,
    load_index,
    retrieve_by_subtasks,
)
from ask_wiki_graph import graph_expand_and_rerank, load_relation_index
from normalize_query_v2 import fallback_normalization, normalize_user_query_v2


QUERIES = [
    (
        "32_Perovskite_Bandgap_Database",
        "Predicting the bandgaps of mixed ABX3 perovskites (where A = Cs, FA, or MA; "
        "B = Pb or Sn; X = Br, Cl, or I) with continuously varying compositions to "
        "enable thermodynamic modeling and prediction of light-induced halide segregation "
        "behavior under illumination. Please help me find the dataset needed",
    ),
    (
        "33_DenseGNN",
        "Predicting material properties—including formation energy, band gap, bulk modulus, "
        "phonon frequencies, dielectric constant, and perovskite formation energy—for crystals, "
        "molecules, and catalytic materials using graph neural networks, with emphasis on "
        "achieving high accuracy on both large-scale computational datasets and small datasets.",
    ),
    (
        "34_GNoME",
        "Predicting the thermodynamic stability of inorganic crystal structures by estimating "
        "their decomposition energy relative to the convex hull of competing phases, enabling "
        "high-throughput screening and discovery of previously unknown stable materials.",
    ),
    (
        "35_CHGNet",
        "Predicting the potential energy surface of inorganic crystalline materials—including "
        "energy, forces, stresses, and magnetic moments—from atomic structure inputs, to enable "
        "charge-informed atomistic simulations that capture coupled ionic and electronic degrees "
        "of freedom for large-scale, long-time molecular dynamics and thermodynamic modeling.",
    ),
    (
        "36_PotNet",
        "Predicting crystal material properties—specifically total energy, formation energy, "
        "band gap, bulk moduli, shear moduli, and Ehull—from atomic-scale crystal structures, "
        "with a focus on accurately modeling infinite-range interatomic interactions arising "
        "from periodic lattice repetitions.",
    ),
    (
        "37_CrysGNN",
        "Predicting multiple physical and electronic properties of crystalline materials—including "
        "formation energy, bandgap, total energy, bulk modulus, shear modulus, Ehull, spillage, "
        "SLME, and dielectric-related properties—using graph neural network models enhanced by "
        "distilled knowledge from a pre-trained GNN on unlabeled crystal structures.",
    ),
    (
        "38_Matformer",
        "Predicting multiple physical and electronic properties of crystalline materials from "
        "their atomic structure, including formation energy, band gap, bulk modulus, and shear "
        "modulus, using periodic graph representations that respect crystal symmetry and "
        "repeating lattice patterns.",
    ),
    (
        "39_M3GNet_Preprint",
        "Predicting the potential energy surface (PES) of atomic systems—including energies, "
        "forces, and stresses—for arbitrary crystalline materials across the entire periodic "
        "table, enabling accurate, efficient, and transferable interatomic potentials usable "
        "for structural relaxation, molecular dynamics, phonon calculations, and materials "
        "discovery without retraining per chemistry.",
    ),
    (
        "40_ALIGNN",
        "Predicting 52 solid-state and molecular properties—including formation energies, band "
        "gaps, dielectric constants, piezoelectric coefficients, Seebeck coefficients, "
        "exfoliation energies, HOMO/LUMO levels, dipole moments, and thermodynamic energies—using "
        "atomistic graph neural networks that explicitly incorporate bond angle information via "
        "line graph message passing.",
    ),
    (
        "41_Cross_Property_Transfer_Learning",
        "Predicting diverse materials properties (e.g., band gap, exfoliation energy, dielectric "
        "constants, thermoelectric coefficients) for compositions in small target datasets by "
        "leveraging knowledge transferred from deep learning models pre-trained on large source "
        "datasets of different, often unrelated, materials properties, using only elemental "
        "fractions as input.",
    ),
    (
        "42_Matbench",
        "Predicting diverse physical and chemical properties of inorganic bulk materials—including "
        "optical, thermal, electronic, thermodynamic, tensile, and elastic properties—using only "
        "input materials primitives (chemical composition and/or crystal structure) as features, "
        "under standardized, bias-mitigated evaluation to enable fair, reproducible comparison "
        "of supervised machine learning algorithms.",
    ),
    (
        "43_Formation_Energy_Stability_Critical",
        "Predicting the thermodynamic stability of inorganic crystalline solids by estimating "
        "their decomposition enthalpy (ΔHd), determining whether a compound lies on the convex "
        "hull of formation enthalpies in its chemical space, using machine-learned formation "
        "energies as input to convex hull construction.",
    ),
    (
        "44_Synthesizability_Crystalline_Inorganic",
        "Predicting the synthesizability of crystalline inorganic materials solely from their "
        "chemical composition (elemental identity and stoichiometric ratios), without requiring "
        "crystal structure information, to identify which hypothetical compositions are likely "
        "to be experimentally realizable using current synthetic capabilities.",
    ),
]


SELECT_PROMPT = """You select datasets for a materials-science task.
Use only the supplied retrieved evidence. Return compact JSON in this exact form:
{"datasets": ["exact dataset name 1", "exact dataset name 2"]}

Rules:
- Recommend datasets that provide necessary labels, structures/compositions, pretraining data,
  validation data, or benchmark targets for the stated task.
- Use dataset names exactly as written in the evidence.
- Do not invent datasets, links, sizes, properties, or availability.
- Exclude papers, tasks, methods, software, and clearly unrelated datasets.
- Prefer a concise set, but include multiple datasets when the task spans multiple properties.
- Return an empty list when the evidence is insufficient.
"""


def parse_dataset_json(text: str) -> list[str]:
    text = (text or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```json", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"^```", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not match:
            raise
        payload = json.loads(match.group(0))
    datasets = payload.get("datasets", []) if isinstance(payload, dict) else []
    return [str(item).strip() for item in datasets if str(item).strip()]


def save_results(path: Path, results: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args():
    parser = argparse.ArgumentParser(description="Run the 13 held-out tasks on the raw-name 30-paper Wiki.")
    parser.add_argument("--index-dir", type=Path, default=Path("wiki_index_30_raw_names"))
    parser.add_argument("--wiki-dir", type=Path, default=Path("llm_wiki_30_raw_names"))
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--seed-top-k", type=int, default=30)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--stage-top-k", type=int, default=8)
    parser.add_argument("--bm25-weight", type=float, default=0.35)
    parser.add_argument("--chat-model", default=os.getenv("QWEN_MODEL", DEFAULT_CHAT_MODEL))
    parser.add_argument("--backend", choices=("legacy", "v3", "v4", "v5"), default="v5")
    parser.add_argument("--dry-run", action="store_true", help="Print backend, output and all tasks without API calls")
    parser.add_argument("--v3-index-dir", "--node-index-dir", type=Path, default=Path("evaluation_output/v3_test_index"))
    parser.add_argument("--v3-rerank-url", "--rerank-url", default=None)
    parser.add_argument("--resume", action="store_true", help="V3: reuse successful cases from this output")
    parser.add_argument("--selection-mode", default=None,
                        choices=("scoped", "topk", "evidence_top1", "minimum", "recommend"))
    return parser.parse_args()


def run_v3(args):
    """Run the exact held-out questions through V3/V4, preserving every trace."""
    root = Path(__file__).resolve().parent
    trace_dir = args.output.parent / "traces"
    trace_dir.mkdir(parents=True, exist_ok=True)
    code_paths = [root / f"newMethod/retrieve_llm_wiki_node_edge_rerank_{args.backend}.py", root / "newMethod/retrieve_llm_wiki.py"]
    if args.backend in {"v4", "v5"}:
        code_paths.append(root / f"newMethod/{args.backend}_scoped_selection.py")
    if args.backend == "v5":
        code_paths.extend([root / "newMethod/v5_family_evidence.py", root / "newMethod/dataset_families_v5.json"])
    fingerprint = hashlib.sha256(b"".join(p.read_bytes() for p in code_paths)).hexdigest()
    registry = root / "newMethod/newLLMWiki/registry/dataset_registry.jsonl"
    names = {d["dataset_id"]: d["canonical_name"] for d in
             (json.loads(line) for line in registry.read_text(encoding="utf-8").splitlines() if line.strip())}
    previous = {}
    if args.resume and args.output.exists():
        previous = {r["number"]: r for r in json.loads(args.output.read_text(encoding="utf-8"))}
    completed = []
    for number, (label, question) in enumerate(QUERIES, 1):
        old = previous.get(number, {})
        if (old.get("status") == "success" and old.get("question") == question
                and old.get("backend") == args.backend
                and old.get("code_fingerprint") == fingerprint
                and old.get("rerank_url") == args.v3_rerank_url
                and old.get("selection_mode") == args.selection_mode
                and Path(old.get("trace_file", "")).is_file()):
            completed.append(old)
            print(f"[{number}/{len(QUERIES)}] {label}: reused successful case", flush=True)
            continue
        print(f"[{number}/{len(QUERIES)}] {label}", flush=True)
        trace_path = (trace_dir / f"q{number:03d}.json").resolve()
        started = time.monotonic()
        command = [sys.executable, str(root / f"newMethod/retrieve_llm_wiki_node_edge_rerank_{args.backend}.py"),
                   "--index-dir", str(args.v3_index_dir.resolve()),
                   "--question", question, "--selection-mode", args.selection_mode,
                   "--trace-output", str(trace_path)]
        if args.v3_rerank_url:
            command.extend(["--rerank-url", args.v3_rerank_url])
        result = subprocess.run(command, cwd=root, capture_output=True, encoding="utf-8", errors="replace")
        (trace_dir / f"q{number:03d}.stdout.txt").write_text(result.stdout, encoding="utf-8")
        (trace_dir / f"q{number:03d}.stderr.txt").write_text(result.stderr, encoding="utf-8")
        trace = json.loads(trace_path.read_text(encoding="utf-8")) if result.returncode == 0 and trace_path.exists() else {}
        record = {"number": number, "label": label, "question": question,
                  "backend": args.backend, "selection_mode": args.selection_mode,
                  "code_fingerprint": fingerprint,
                  "rerank_url": args.v3_rerank_url,
                  "status": "success" if trace else "failed", "return_code": result.returncode,
                  "elapsed_seconds": round(time.monotonic() - started, 2),
                  "selected_dataset_ids": trace.get("selected_dataset_ids", []),
                  "portfolio_dataset_ids": trace.get("portfolio_dataset_ids", trace.get("selected_dataset_ids", [])),
                  "datasets": [names[i] for i in trace.get("selected_dataset_ids", [])],
                  "fallback_used": trace.get("selection_diagnostics", {}).get("fallback_used", False),
                  "fallback_candidates": trace.get("selection_diagnostics", {}).get("fallback_candidates", []),
                  "selection_diagnostics": trace.get("selection_diagnostics", {}),
                  "trace_file": str(trace_path)}
        completed.append(record)
        save_results(args.output, completed)
        print(f"  {record['status']}: {record['selected_dataset_ids']}", flush=True)
        if args.backend in {"v4", "v5"} and record["status"] == "success":
            print(f"  main portfolio: {record['portfolio_dataset_ids']}", flush=True)
    print(f"Saved: {args.output}", flush=True)
    return 0 if all(r["status"] == "success" for r in completed) else 1


def main():
    load_dotenv()
    args = parse_args()
    args.selection_mode = args.selection_mode or ("scoped" if args.backend in {"v4", "v5"} else "evidence_top1")
    if args.output is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = Path("evaluation_output") / f"{args.backend}_{args.selection_mode}_{stamp}" / "query_results.json"
    if args.backend == "v3" and args.selection_mode == "scoped":
        raise ValueError("scoped selection requires --backend v4 or v5")
    print(f"Backend: {args.backend}; selection: {args.selection_mode}; tasks: {len(QUERIES)}; output: {args.output}", flush=True)
    if args.dry_run:
        for number, (label, _) in enumerate(QUERIES, 1):
            print(f"[{number}/{len(QUERIES)}] {label}")
        return 0
    if args.backend in {"v3", "v4", "v5"}:
        return run_v3(args)
    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        raise ValueError("Please set QWEN_API_KEY in .env.")

    docs, embeddings, meta = load_index(args.index_dir)
    embedding_model = meta.get("embedding_model", "text-embedding-v4")
    relation_index = load_relation_index(docs, args.wiki_dir)
    client = OpenAI(
        api_key=api_key,
        base_url=os.getenv("QWEN_BASE_URL", DEFAULT_BASE_URL),
    )

    completed = []
    for number, (label, question) in enumerate(QUERIES, start=1):
        print(f"[{number}/{len(QUERIES)}] {label}", flush=True)
        try:
            plan = normalize_user_query_v2(client, args.chat_model, question)
        except Exception as exc:
            print(f"  normalization fallback: {exc}", flush=True)
            plan = fallback_normalization(question)

        seeds = retrieve_by_subtasks(
            client,
            docs,
            embeddings,
            plan,
            embedding_model,
            args.stage_top_k,
            args.seed_top_k,
            args.bm25_weight,
        )
        ranked = graph_expand_and_rerank(seeds, relation_index, plan, args.top_k)
        context = format_context(ranked)
        response = client.chat.completions.create(
            model=args.chat_model,
            temperature=0,
            messages=[
                {"role": "system", "content": SELECT_PROMPT},
                {
                    "role": "user",
                    "content": f"Task:\n{question}\n\nRetrieved evidence:\n{context}",
                },
            ],
        )
        datasets = parse_dataset_json(response.choices[0].message.content)
        completed.append(
            {
                "number": number,
                "backend": "legacy",
                "label": label,
                "question": question,
                "datasets": datasets,
                "evidence": [
                    {
                        "rank": rank,
                        "type": doc.get("type"),
                        "title": doc.get("title"),
                        "score": doc.get("score"),
                    }
                    for rank, doc in enumerate(ranked, start=1)
                ],
            }
        )
        save_results(args.output, completed)
        print(f"  datasets: {' | '.join(datasets) if datasets else 'None'}", flush=True)

    print(f"Saved: {args.output}", flush=True)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
