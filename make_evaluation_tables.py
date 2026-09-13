import argparse
from pathlib import Path

import pandas as pd


METRIC_ORDER = ["precision", "recall", "f1", "recall@1", "recall@3", "recall@5"]
MATCH_LABELS = {
    "strict": "Strict",
    "canonical": "Canonical",
    "family": "Family",
}
AGG_LABELS = {
    "macro": "Macro",
    "micro": "Micro",
}


def pct(value) -> str:
    if pd.isna(value):
        return "—"
    return f"{float(value) * 100:.2f}%"


def dash_for_micro_recall_at_k(row: pd.Series, metric: str) -> str:
    if row["aggregation"] == "micro" and metric.startswith("recall@"):
        return "—"
    return pct(row.get(metric))


def load_summary_table(summary_path: Path) -> pd.DataFrame:
    raw = pd.read_csv(summary_path)
    pivot = raw.pivot_table(
        index=["match_level", "aggregation"],
        columns="metric",
        values="value",
        aggfunc="first",
    ).reset_index()

    rows = []
    for match in ["strict", "canonical", "family"]:
        for agg in ["macro", "micro"]:
            hit = pivot[(pivot["match_level"] == match) & (pivot["aggregation"] == agg)]
            if hit.empty:
                continue
            item = hit.iloc[0]
            rows.append(
                {
                    "匹配方式": MATCH_LABELS.get(match, match),
                    "聚合方式": AGG_LABELS.get(agg, agg),
                    "Precision": pct(item.get("precision")),
                    "Recall": pct(item.get("recall")),
                    "F1": pct(item.get("f1")),
                    "Recall@1": dash_for_micro_recall_at_k(item, "recall@1"),
                    "Recall@3": dash_for_micro_recall_at_k(item, "recall@3"),
                    "Recall@5": dash_for_micro_recall_at_k(item, "recall@5"),
                }
            )
    return pd.DataFrame(rows)


def short_paper_name(value: str) -> str:
    text = str(value)
    text = text.replace(".pdf", "")
    if ". " in text[:5]:
        text = text.split(". ", 1)[1]
    return text


def split_items(value) -> list[str]:
    if pd.isna(value) or not str(value).strip():
        return []
    return [item.strip() for item in str(value).split("|") if item.strip()]


def summarize_row(row: pd.Series) -> str:
    tp = int(row.get("tp", 0))
    fp = int(row.get("fp", 0))
    fn = int(row.get("fn", 0))
    recall = float(row.get("recall", 0) or 0)
    precision = float(row.get("precision", 0) or 0)
    correct = split_items(row.get("correct", ""))
    false_negative = split_items(row.get("false_negative", ""))
    false_positive = split_items(row.get("false_positive", ""))

    if tp == 0 and fn > 0:
        if fp > 0:
            return "未命中真实数据集，检索到语义相关但不完全匹配的数据集"
        return "未命中真实数据集"
    if fn == 0 and fp == 0:
        return "推荐集合完全正确"
    if fn == 0 and fp > 0:
        return "真实数据集全部找回，但存在额外推荐"
    if tp > 0 and fn > 0 and fp == 0:
        return "命中部分真实数据集，但仍有遗漏"
    if tp > 0 and fp > 0 and fn > 0:
        if correct:
            return f"命中{tp}个，但存在遗漏和额外推荐"
        return "部分命中，但推荐集合仍需收敛"
    if recall >= 0.75 and precision < 0.5:
        return "召回较高，但推荐范围较宽"
    if precision >= 0.75 and recall < 0.5:
        return "推荐较准确，但真实数据集未找全"
    if false_negative and not false_positive:
        return "推荐较保守，仍有真实数据集遗漏"
    return "部分匹配"


def load_per_paper_table(per_paper_path: Path, match_level: str) -> pd.DataFrame:
    raw = pd.read_csv(per_paper_path)
    raw = raw[raw["match_level"] == match_level].copy()
    rows = []
    for _, row in raw.iterrows():
        rows.append(
            {
                "论文": short_paper_name(row["paper"]),
                "TP": int(row.get("tp", 0)),
                "FP": int(row.get("fp", 0)),
                "FN": int(row.get("fn", 0)),
                "Precision": pct(row.get("precision")),
                "Recall": pct(row.get("recall")),
                "F1": pct(row.get("f1")),
                "结果概括": summarize_row(row),
            }
        )
    return pd.DataFrame(rows)


def style_summary(df: pd.DataFrame) -> str:
    def row_style(row):
        if row.get("匹配方式") == "Canonical" and row.get("聚合方式") == "Macro":
            return ["font-weight:700;background:#f7f7f7"] * len(row)
        return [""] * len(row)

    return (
        df.style.apply(row_style, axis=1)
        .hide(axis="index")
        .set_table_styles(
            [
                {"selector": "table", "props": "border-collapse:collapse;font-family:Arial,'Microsoft YaHei',sans-serif;font-size:14px;"},
                {"selector": "th,td", "props": "border:1px solid #d0d0d0;padding:6px 8px;text-align:right;"},
                {"selector": "th", "props": "font-weight:700;background:#fafafa;"},
                {"selector": "td:nth-child(1),td:nth-child(2)", "props": "text-align:left;"},
            ]
        )
        .to_html()
    )


def style_detail(df: pd.DataFrame) -> str:
    return (
        df.style.hide(axis="index")
        .set_table_styles(
            [
                {"selector": "table", "props": "border-collapse:collapse;font-family:Arial,'Microsoft YaHei',sans-serif;font-size:14px;"},
                {"selector": "th,td", "props": "border:1px solid #d0d0d0;padding:6px 8px;"},
                {"selector": "th", "props": "font-weight:700;background:#fafafa;"},
                {"selector": "td:nth-child(2),td:nth-child(3),td:nth-child(4),td:nth-child(5),td:nth-child(6),td:nth-child(7)", "props": "text-align:right;"},
                {"selector": "td:nth-child(1),td:nth-child(8)", "props": "text-align:left;"},
            ]
        )
        .to_html()
    )


def write_html(path: Path, title: str, summary_html: str, detail_html: str):
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
    body {{ margin: 28px; color: #111; font-family: Arial, 'Microsoft YaHei', sans-serif; }}
    h1 {{ font-size: 22px; }}
    h2 {{ margin-top: 28px; font-size: 18px; }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  <h2>总体指标汇总</h2>
  {summary_html}
  <h2>逐论文结果诊断</h2>
  {detail_html}
</body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def parse_args():
    parser = argparse.ArgumentParser(description="Generate publication-style evaluation tables from evaluation_output CSV files.")
    parser.add_argument("--input-dir", type=Path, default=Path("evaluation_output"))
    parser.add_argument("--output-dir", type=Path, default=Path("evaluation_output") / "tables")
    parser.add_argument("--detail-match-level", choices=["strict", "canonical", "family"], default="canonical")
    return parser.parse_args()


def main():
    args = parse_args()
    summary_path = args.input_dir / "summary_metrics.csv"
    per_paper_path = args.input_dir / "per_paper_metrics.csv"
    if not summary_path.exists():
        raise FileNotFoundError(f"Missing summary metrics: {summary_path}")
    if not per_paper_path.exists():
        raise FileNotFoundError(f"Missing per-paper metrics: {per_paper_path}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary_table = load_summary_table(summary_path)
    detail_table = load_per_paper_table(per_paper_path, args.detail_match_level)

    summary_table.to_csv(args.output_dir / "summary_table.csv", index=False, encoding="utf-8-sig")
    detail_table.to_csv(args.output_dir / "per_paper_table.csv", index=False, encoding="utf-8-sig")
    write_html(
        args.output_dir / "evaluation_tables.html",
        f"Evaluation Tables ({args.input_dir})",
        style_summary(summary_table),
        style_detail(detail_table),
    )
    print(f"Wrote: {args.output_dir / 'summary_table.csv'}")
    print(f"Wrote: {args.output_dir / 'per_paper_table.csv'}")
    print(f"Wrote: {args.output_dir / 'evaluation_tables.html'}")


if __name__ == "__main__":
    main()
