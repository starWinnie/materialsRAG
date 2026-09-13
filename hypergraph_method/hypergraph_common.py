import json
import re
import sys
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from build_llm_wiki import build_entities, canonical_dataset_title, read_records


NODE_WEIGHTS = {
    "target_property": 3.0,
    "material_system": 2.5,
    "data_source_type": 2.0,
    "representation": 1.8,
    "rd_stage": 1.3,
    "task_type": 1.0,
    "dataset_family": 0.5,
}


PATTERNS = {
    "material_system": {
        "perovskite": [r"perovskite", r"钙钛矿", r"\babx\s*3\b"],
        "inorganic crystal": [r"inorganic", r"crystalline", r"crystal structures?", r"无机", r"晶体"],
        "2d material": [r"\b2d\b", r"two-dimensional", r"layered", r"二维"],
        "catalyst": [r"catalyst", r"catalysis", r"催化"],
        "battery material": [r"battery", r"electrode", r"electrolyte", r"电池", r"电极", r"电解质"],
        "molecule": [r"molecule", r"molecular", r"organic molecules?", r"分子"],
        "alloy": [r"alloy", r"合金"],
    },
    "target_property": {
        "band gap": [r"band\s*gap", r"bandgap", r"带隙"],
        "formation energy": [r"formation\s+energy", r"形成能"],
        "energy above hull": [r"energy\s+above\s+hull", r"\behull\b", r"hull\s+distance", r"凸包", r"稳定性"],
        "stability": [r"stability", r"stable", r"thermodynamic\\s+stability", r"稳定性", r"稳定"],
        "total energy": [r"total\s+energy", r"总能"],
        "bulk modulus": [r"bulk\s+modulus", r"体模量"],
        "shear modulus": [r"shear\s+modulus", r"剪切模量"],
        "young's modulus": [r"young'?s\s+modulus", r"杨氏模量"],
        "dielectric property": [r"dielectric", r"refractive\s+index", r"介电", r"折射率"],
        "adsorption energy": [r"adsorption\s+energy", r"吸附能"],
        "conductivity": [r"conductivity", r"导电", r"电导"],
        "synthesis condition": [r"synthesis", r"synthesizability", r"合成"],
    },
    "data_source_type": {
        "DFT": [r"\bdft\b", r"density\s+functional", r"first[- ]principles", r"计算", r"第一性原理"],
        "experimental": [r"experimental\s+(dataset|data|database|label|labels|bandgap|band\s*gap|formation\s+energy)", r"experimentally\s+(measured|reported|determined)", r"measured\s+(bandgap|band\s*gap|formation\s+energy|property|properties)", r"实验", r"测量"],
        "literature-curated": [r"literature", r"curated", r"reported", r"文献", r"整理"],
        "high-throughput calculated": [r"high[- ]throughput", r"computed database", r"高通量"],
        "simulation trajectory": [r"trajectory", r"relaxation", r"molecular dynamics", r"轨迹", r"弛豫"],
        "benchmark suite": [r"benchmark", r"matbench", r"基准", r"评测"],
    },
    "representation": {
        "composition": [r"composition", r"chemical formula", r"stoichiometry", r"成分", r"化学式"],
        "crystal structure": [r"crystal structure", r"structures?", r"晶体结构"],
        "atomic coordinates": [r"atomic coordinates", r"fractional coordinates", r"原子坐标", r"分数坐标"],
        "lattice vectors": [r"lattice vectors?", r"lattice parameters?", r"晶格"],
        "crystal graph": [r"crystal graph", r"graph", r"晶体图"],
        "CIF": [r"\bcif\b"],
        "SMILES": [r"smiles", r"selfies"],
        "descriptor": [r"descriptor", r"feature", r"featur", r"描述符", r"特征"],
        "spectrum or tensor": [r"spectra?", r"spectrum", r"tensor", r"张量", r"谱"],
    },
    "task_type": {
        "property prediction": [r"predict", r"prediction", r"regression", r"classification", r"预测", r"分类", r"回归"],
        "materials discovery": [r"discover", r"discovery", r"screening", r"pre-screening", r"发现", r"筛选"],
        "inverse design": [r"inverse design", r"generative", r"generation", r"反向设计", r"生成"],
        "benchmark": [r"benchmark", r"evaluation", r"评测", r"基准"],
        "synthesis assessment": [r"synthesizability", r"synthesis", r"合成"],
    },
    "rd_stage": {
        "Dataset Selection": [r"dataset", r"database", r"数据集"],
        "Representation / Feature Construction": [r"representation", r"feature", r"descriptor", r"graph", r"表征", r"特征"],
        "Model Training": [r"train", r"training", r"训练"],
        "Screening / Prediction": [r"predict", r"prediction", r"screening", r"预测", r"筛选"],
        "Validation": [r"validation", r"validate", r"experimental", r"验证", r"实验"],
        "Benchmarking / Evaluation": [r"benchmark", r"evaluation", r"评测", r"基准"],
    },
}


DATASET_FAMILY_PATTERNS = {
    "materials project family": [r"materials project", r"\bmp\b", r"mptraj", r"mptrj", r"\bmpf\b"],
    "jarvis family": [r"jarvis"],
    "oqmd family": [r"open quantum materials database", r"\boqmd\b"],
    "matbench family": [r"matbench"],
    "icsd family": [r"inorganic crystal structure database", r"\bicsd\b"],
    "qm9 family": [r"\bqm9\b"],
}


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def node_id(node_type: str, value: str) -> str:
    value = normalize_space(value).lower()
    return f"{node_type}:{value}"


def find_values(text: str, category: str) -> list[str]:
    result = []
    text = normalize_space(text)
    for value, patterns in PATTERNS[category].items():
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
            if category == "data_source_type" and value == "experimental":
                if re.search(r"\bno\s+experimental\b|\bwithout\s+experimental\b|\bnot\s+experimental\b|no experimental property labels", text, flags=re.IGNORECASE):
                    continue
            result.append(value)
    return result


def find_dataset_families(text: str) -> list[str]:
    result = []
    text = normalize_space(text)
    for value, patterns in DATASET_FAMILY_PATTERNS.items():
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
            result.append(value)
    return result


def infer_nodes(*texts: str, include_dataset_family: bool = True) -> set[str]:
    joined = " ".join(normalize_space(text) for text in texts if text)
    nodes = set()
    for category in PATTERNS:
        for value in find_values(joined, category):
            nodes.add(node_id(category, value))
    if include_dataset_family:
        for value in find_dataset_families(joined):
            nodes.add(node_id("dataset_family", value))
    return nodes


def weighted_coverage(nodes: Iterable[str]) -> float:
    total = 0.0
    for item in nodes:
        node_type = item.split(":", 1)[0]
        total += NODE_WEIGHTS.get(node_type, 1.0)
    return total


def load_entities_from_extraction(path: Path) -> dict:
    return build_entities(read_records(path))


def canonical_dataset_key(name: str) -> str:
    return canonical_dataset_title(name).strip().lower()


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))




