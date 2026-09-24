#!/usr/bin/env python3
"""批量运行 DatasetUse 超图检索测试。

默认读取同目录的 ``query.md``，逐条调用：

    newMethod/retrieve_llm_wiki_hyperedge_rerank.py

每条 Query 都在独立子进程中运行，避免检索模块中的全局状态在不同测试案例
之间串扰。程序会为每条 Query 保存 trace、stdout、stderr，并持续更新
``summary.json``、``summary.csv`` 和 ``summary.md``，便于中断后检查或续跑。

推荐的 query.md 格式：

    # 测试问题

    ## Q01
    帮我推荐适合……的数据集。

    ## Q02
    我要完成……，应使用哪些数据集？

同时兼容编号列表（``1. ...``）和空行分隔的普通段落。
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class QueryCase:
    """从 Markdown 中解析出的一条测试问题。"""

    case_id: str
    title: str
    query: str


@dataclass
class CaseResult:
    """单条 Query 的运行结果及其产物位置。"""

    case_id: str
    title: str
    query: str
    status: str
    return_code: int | None
    elapsed_seconds: float
    trace_file: str
    stdout_file: str
    stderr_file: str
    selected_dataset_ids: list[str]
    error: str


HEADING_RE = re.compile(r"^#{2,6}\s+(.+?)\s*$")
NUMBERED_RE = re.compile(r"^\s*(\d+)\s*[.、)]\s+(.+?)\s*$")
TOP_LEVEL_HEADING_RE = re.compile(r"^#\s+.+$")
FENCE_RE = re.compile(r"^```")


def normalize_query(lines: list[str]) -> str:
    """合并多行 Query，同时保留必要的语义边界。"""

    parts: list[str] = []
    for line in lines:
        value = line.strip()
        if not value or FENCE_RE.match(value):
            continue
        # Query 内容中允许使用普通 Markdown 列表，去掉列表符号后参与检索。
        value = re.sub(r"^[-*+]\s+", "", value)
        parts.append(value)
    return " ".join(parts).strip()


def unique_cases(cases: list[QueryCase]) -> list[QueryCase]:
    """按 Query 文本去重，并生成稳定、唯一的案例编号。"""

    seen_queries: set[str] = set()
    seen_ids: set[str] = set()
    output: list[QueryCase] = []
    for position, case in enumerate(cases, start=1):
        query_key = re.sub(r"\s+", " ", case.query).casefold().strip()
        if not query_key or query_key in seen_queries:
            continue
        seen_queries.add(query_key)

        raw_id = re.sub(r"[^0-9A-Za-z_-]+", "_", case.case_id).strip("_")
        raw_id = raw_id or f"q{position:03d}"
        candidate_id = raw_id
        suffix = 2
        while candidate_id.casefold() in seen_ids:
            candidate_id = f"{raw_id}_{suffix}"
            suffix += 1
        seen_ids.add(candidate_id.casefold())
        output.append(QueryCase(candidate_id, case.title, case.query))
    return output


def parse_heading_cases(lines: list[str]) -> list[QueryCase]:
    """优先将二级及以下标题识别为 Query 案例边界。"""

    cases: list[QueryCase] = []
    current_title: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_lines
        if current_title is None:
            return
        query = normalize_query(current_lines)
        if query:
            cases.append(
                QueryCase(
                    case_id=current_title,
                    title=current_title,
                    query=query,
                )
            )
        current_lines = []

    for line in lines:
        match = HEADING_RE.match(line)
        if match:
            flush()
            current_title = match.group(1).strip()
        elif current_title is not None:
            current_lines.append(line)
    flush()
    return cases


def parse_numbered_cases(lines: list[str]) -> list[QueryCase]:
    """兼容 ``1. Query`` 形式，并把后续缩进行视为同一条 Query。"""

    cases: list[QueryCase] = []
    current_number: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_number, current_lines
        if current_number is None:
            return
        query = normalize_query(current_lines)
        if query:
            cases.append(QueryCase(f"q{int(current_number):03d}", f"Query {current_number}", query))
        current_lines = []

    for line in lines:
        match = NUMBERED_RE.match(line)
        if match:
            flush()
            current_number = match.group(1)
            current_lines = [match.group(2)]
        elif current_number is not None:
            current_lines.append(line)
    flush()
    return cases


def parse_paragraph_cases(lines: list[str]) -> list[QueryCase]:
    """没有标题或编号时，将空行分隔的每个段落作为一条 Query。"""

    cases: list[QueryCase] = []
    paragraph: list[str] = []

    def flush() -> None:
        nonlocal paragraph
        query = normalize_query(paragraph)
        if query:
            number = len(cases) + 1
            cases.append(QueryCase(f"q{number:03d}", f"Query {number}", query))
        paragraph = []

    for line in lines:
        if TOP_LEVEL_HEADING_RE.match(line):
            continue
        if not line.strip():
            flush()
        else:
            paragraph.append(line)
    flush()
    return cases


def parse_line_cases(lines: list[str]) -> list[QueryCase]:
    """Parse the current one-query-per-line Markdown format."""

    cases: list[QueryCase] = []
    for line in lines:
        value = line.strip()
        if not value or TOP_LEVEL_HEADING_RE.match(value) or FENCE_RE.match(value):
            continue
        number = len(cases) + 1
        cases.append(QueryCase(f"q{number:03d}", f"Query {number}", value))
    return cases


def parse_query_markdown(path: Path) -> list[QueryCase]:
    """按标题、编号列表、普通段落的优先级解析 Markdown。"""

    if not path.is_file():
        raise FileNotFoundError(f"Query 文件不存在：{path}")
    text = path.read_text(encoding="utf-8-sig")
    if not text.strip():
        raise ValueError(f"Query 文件为空，请先保存测试问题：{path}")

    lines = text.splitlines()
    cases = parse_heading_cases(lines)
    if not cases:
        cases = parse_numbered_cases(lines)
    if not cases:
        # The current test file stores one complete query per physical line.
        # Keep paragraph parsing when blank separators are present so wrapped
        # Markdown prose is not accidentally split into multiple queries.
        content_lines = [
            line for line in lines
            if line.strip() and not TOP_LEVEL_HEADING_RE.match(line)
        ]
        has_blank_separator = any(not line.strip() for line in lines)
        if len(content_lines) > 1 and not has_blank_separator:
            cases = parse_line_cases(lines)
        else:
            cases = parse_paragraph_cases(lines)
    cases = unique_cases(cases)
    if not cases:
        raise ValueError(f"没有从 Markdown 中解析到有效 Query：{path}")
    return cases


def relative_to_output(path: Path, output_dir: Path) -> str:
    """在汇总文件中使用相对于本次实验目录的可移植路径。"""

    try:
        return str(path.resolve().relative_to(output_dir.resolve()))
    except ValueError:
        return str(path.resolve())


def read_selected_dataset_ids(trace_path: Path, result_field: str) -> list[str]:
    """从 trace 中抽取指定选择器实际返回的数据集编号。"""

    if not trace_path.is_file():
        return []
    try:
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    key = (
        "adaptive_selected_dataset_ids"
        if result_field == "adaptive" else "selected_dataset_ids"
    )
    values = trace.get(key, [])
    return [str(value) for value in values] if isinstance(values, list) else []


def write_summaries(
    output_dir: Path,
    query_file: Path,
    retriever: Path,
    result_field: str,
    results: list[CaseResult],
) -> None:
    """每完成一条 Query 就重写汇总，保证中断后仍保留已有结果。"""

    payload: dict[str, Any] = {
        "updated_at": datetime.now().astimezone().isoformat(),
        "query_file": str(query_file.resolve()),
        "retriever": str(retriever.resolve()),
        "result_field": result_field,
        "total_recorded": len(results),
        "success_count": sum(item.status in {"success", "skipped_existing"} for item in results),
        "failed_count": sum(item.status == "failed" for item in results),
        "results": [asdict(item) for item in results],
    }
    summary_json = output_dir / "summary.json"
    temporary_json = output_dir / "summary.json.tmp"
    temporary_json.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporary_json.replace(summary_json)

    csv_fields = [
        "case_id", "title", "status", "return_code", "elapsed_seconds",
        "selected_dataset_ids", "trace_file", "stdout_file", "stderr_file",
        "error", "query",
    ]
    with (output_dir / "summary.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields)
        writer.writeheader()
        for item in results:
            row = asdict(item)
            row["selected_dataset_ids"] = " | ".join(item.selected_dataset_ids)
            writer.writerow({key: row[key] for key in csv_fields})

    markdown_lines = [
        "# 超图检索批量测试汇总",
        "",
        f"- Query 文件：`{query_file.resolve()}`",
        f"- 检索脚本：`{retriever.resolve()}`",
        f"- 已记录：{len(results)}",
        f"- 成功：{payload['success_count']}",
        f"- 失败：{payload['failed_count']}",
        "",
        "| Case | 状态 | 耗时/秒 | 推荐数据集 | Trace |",
        "|---|---|---:|---|---|",
    ]
    for item in results:
        datasets = "<br>".join(item.selected_dataset_ids) or "—"
        trace_link = item.trace_file.replace("\\", "/")
        markdown_lines.append(
            f"| {item.case_id} | {item.status} | {item.elapsed_seconds:.2f} | "
            f"{datasets} | [{Path(trace_link).name}]({trace_link}) |"
        )
    (output_dir / "summary.md").write_text(
        "\n".join(markdown_lines) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    parser = argparse.ArgumentParser(
        description="批量调用 DatasetUse 超图检索脚本测试 query.md",
        epilog=(
            "如需把额外参数传给检索脚本，请放在 -- 后，例如："
            " -- --selection-mode minimum --max-results 5"
        ),
    )
    parser.add_argument("--query-file", type=Path, default=script_dir / "query.md")
    parser.add_argument(
        "--retriever",
        type=Path,
        default=project_root / "newMethod" / "retrieve_llm_wiki_node_edge_rerank_v3.py",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=script_dir / "results" / f"hyperedge_{timestamp}",
    )
    parser.add_argument("--python", default=sys.executable, help="运行检索脚本的 Python")
    parser.add_argument("--start", type=int, default=1, help="从第几条 Query 开始，1-based")
    parser.add_argument("--limit", type=int, help="本次最多执行多少条 Query")
    parser.add_argument("--timeout", type=float, default=900.0, help="每条 Query 最长运行秒数")
    parser.add_argument("--delay", type=float, default=0.0, help="相邻 Query 间等待秒数")
    parser.add_argument("--resume", action="store_true", help="已有合法 trace 时跳过该 Query")
    parser.add_argument("--fail-fast", action="store_true", help="第一条失败后立即停止")
    parser.add_argument("--dry-run", action="store_true", help="只解析并打印 Query，不调用 API")
    parser.add_argument(
        "--result-field",
        choices=("selected", "adaptive"),
        default="selected",
        help=(
            "汇总和评测的结果来源；默认selected与--selection-mode实际输出一致，"
            "adaptive仅用于单独分析旧的自适应诊断选择器"
        ),
    )
    parser.add_argument(
        "retriever_args",
        nargs=argparse.REMAINDER,
        help="传递给检索脚本的额外参数；前面需要使用 --",
    )
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    query_file = args.query_file.resolve()
    retriever = args.retriever.resolve()

    try:
        all_cases = parse_query_markdown(query_file)
    except (OSError, ValueError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 2

    if args.start < 1:
        print("[error] --start 必须大于或等于 1", file=sys.stderr)
        return 2
    cases = all_cases[args.start - 1 :]
    if args.limit is not None:
        if args.limit < 1:
            print("[error] --limit 必须大于或等于 1", file=sys.stderr)
            return 2
        cases = cases[: args.limit]
    if not cases:
        print("[error] 所选范围内没有 Query", file=sys.stderr)
        return 2

    print(f"已从 {query_file} 解析 {len(all_cases)} 条 Query，本次选择 {len(cases)} 条。")
    for case in cases:
        print(f"  [{case.case_id}] {case.query}")
    if args.dry_run:
        print("dry-run 完成：未调用检索/API。")
        return 0

    if not retriever.is_file():
        print(f"[error] 检索脚本不存在：{retriever}", file=sys.stderr)
        return 2

    output_dir = args.output_dir.resolve()
    traces_dir = output_dir / "traces"
    logs_dir = output_dir / "logs"
    traces_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    # argparse.REMAINDER 会保留显式分隔符 --，子进程不需要该标记。
    forwarded_args = list(args.retriever_args)
    if forwarded_args and forwarded_args[0] == "--":
        forwarded_args = forwarded_args[1:]
    if "--question" in forwarded_args or "--trace-output" in forwarded_args:
        print(
            "[error] 额外参数不能包含 --question 或 --trace-output，二者由批处理器管理。",
            file=sys.stderr,
        )
        return 2

    results: list[CaseResult] = []
    failed = False
    environment = os.environ.copy()
    environment["PYTHONIOENCODING"] = "utf-8"

    for position, case in enumerate(cases, start=1):
        trace_path = traces_dir / f"{case.case_id}.json"
        stdout_path = logs_dir / f"{case.case_id}.stdout.txt"
        stderr_path = logs_dir / f"{case.case_id}.stderr.txt"
        relative_trace = relative_to_output(trace_path, output_dir)
        relative_stdout = relative_to_output(stdout_path, output_dir)
        relative_stderr = relative_to_output(stderr_path, output_dir)

        if args.resume and trace_path.is_file():
            selected_ids = read_selected_dataset_ids(trace_path, args.result_field)
            if selected_ids:
                result = CaseResult(
                    case_id=case.case_id,
                    title=case.title,
                    query=case.query,
                    status="skipped_existing",
                    return_code=0,
                    elapsed_seconds=0.0,
                    trace_file=relative_trace,
                    stdout_file=relative_stdout,
                    stderr_file=relative_stderr,
                    selected_dataset_ids=selected_ids,
                    error="",
                )
                results.append(result)
                write_summaries(output_dir, query_file, retriever, args.result_field, results)
                print(f"[{position}/{len(cases)}] {case.case_id}: 已有 trace，跳过。")
                continue

        command = [
            args.python,
            str(retriever),
            "--question",
            case.query,
            "--trace-output",
            str(trace_path),
            *forwarded_args,
        ]
        print(f"[{position}/{len(cases)}] {case.case_id}: 开始运行……")
        started = time.perf_counter()
        return_code: int | None = None
        error = ""
        status = "failed"
        stdout_text = ""
        stderr_text = ""

        try:
            completed = subprocess.run(
                command,
                cwd=str(retriever.parent.parent),
                env=environment,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=args.timeout,
                check=False,
            )
            return_code = completed.returncode
            stdout_text = completed.stdout
            stderr_text = completed.stderr
            if completed.returncode == 0 and trace_path.is_file():
                status = "success"
            elif completed.returncode == 0:
                error = "检索脚本返回成功，但没有生成 trace 文件"
            else:
                error = f"检索脚本退出码为 {completed.returncode}"
        except subprocess.TimeoutExpired as exc:
            stdout_text = exc.stdout or ""
            stderr_text = exc.stderr or ""
            if isinstance(stdout_text, bytes):
                stdout_text = stdout_text.decode("utf-8", errors="replace")
            if isinstance(stderr_text, bytes):
                stderr_text = stderr_text.decode("utf-8", errors="replace")
            error = f"超过单条 Query 超时限制：{args.timeout} 秒"
        except OSError as exc:
            error = f"无法启动检索脚本：{exc}"

        elapsed = time.perf_counter() - started
        stdout_path.write_text(stdout_text, encoding="utf-8")
        stderr_path.write_text(stderr_text, encoding="utf-8")
        selected_ids = read_selected_dataset_ids(trace_path, args.result_field)
        result = CaseResult(
            case_id=case.case_id,
            title=case.title,
            query=case.query,
            status=status,
            return_code=return_code,
            elapsed_seconds=round(elapsed, 3),
            trace_file=relative_trace,
            stdout_file=relative_stdout,
            stderr_file=relative_stderr,
            selected_dataset_ids=selected_ids,
            error=error,
        )
        results.append(result)
        write_summaries(output_dir, query_file, retriever, args.result_field, results)

        if status == "success":
            print(
                f"[{position}/{len(cases)}] {case.case_id}: 成功，"
                f"推荐 {len(selected_ids)} 个数据集，耗时 {elapsed:.1f} 秒。"
            )
        else:
            failed = True
            print(
                f"[{position}/{len(cases)}] {case.case_id}: 失败，{error}；"
                f"详见 {stderr_path}",
                file=sys.stderr,
            )
            if args.fail_fast:
                break

        if args.delay > 0 and position < len(cases):
            time.sleep(args.delay)

    print(f"批量测试完成，汇总文件：{output_dir / 'summary.md'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
