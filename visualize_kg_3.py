import argparse
import json
from pathlib import Path


DEFAULT_GRAPH = Path("kg_outputs/kg_graph.json")
DEFAULT_OUTPUT = Path("kg_outputs/kg_visualization.html")


HTML_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Paper-Task-Dataset Knowledge Graph</title>
  <style>
    :root {
      --bg: #f6f7f9;
      --panel: #ffffff;
      --text: #17202a;
      --muted: #64748b;
      --line: #d7dde7;
      --paper: #2563eb;
      --task: #16a34a;
      --dataset: #dc2626;
      --tag: #7c3aed;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      min-height: 100vh;
      color: var(--text);
      background: var(--bg);
      font-family: "Segoe UI", Arial, "Microsoft YaHei", sans-serif;
      overflow: hidden;
    }

    .app {
      display: grid;
      grid-template-columns: 320px 1fr;
      height: 100vh;
    }

    aside {
      background: var(--panel);
      border-right: 1px solid var(--line);
      padding: 18px;
      overflow: auto;
    }

    main {
      position: relative;
      overflow: hidden;
    }

    h1 {
      margin: 0 0 6px;
      font-size: 20px;
      line-height: 1.25;
      letter-spacing: 0;
    }

    .meta {
      color: var(--muted);
      font-size: 13px;
      line-height: 1.5;
      margin-bottom: 18px;
    }

    .group {
      border-top: 1px solid var(--line);
      padding-top: 14px;
      margin-top: 14px;
    }

    .group h2 {
      margin: 0 0 10px;
      font-size: 13px;
      color: #334155;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    label {
      display: flex;
      align-items: center;
      gap: 8px;
      min-height: 28px;
      color: #263445;
      font-size: 14px;
    }

    input[type="search"] {
      width: 100%;
      height: 36px;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 0 10px;
      color: var(--text);
      background: #fff;
      outline: none;
    }

    input[type="range"] { width: 100%; }

    button {
      width: 100%;
      height: 36px;
      border: 1px solid var(--line);
      border-radius: 6px;
      color: var(--text);
      background: #fff;
      cursor: pointer;
      font: inherit;
    }

    button:hover { background: #f8fafc; }

    .legend {
      display: grid;
      gap: 8px;
      font-size: 14px;
    }

    .legend-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }

    .legend-left {
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 0;
    }

    .dot {
      width: 11px;
      height: 11px;
      border-radius: 50%;
      flex: 0 0 auto;
    }

    .count { color: var(--muted); }

    canvas {
      display: block;
      width: 100%;
      height: 100%;
      background: #fbfcfe;
    }

    .tooltip {
      position: absolute;
      max-width: 430px;
      pointer-events: none;
      background: #ffffff;
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 12px 32px rgba(15, 23, 42, 0.18);
      padding: 12px;
      font-size: 13px;
      line-height: 1.45;
      color: var(--text);
      display: none;
    }

    .tooltip .title {
      font-weight: 700;
      margin-bottom: 6px;
      word-break: break-word;
    }

    .tooltip .type {
      color: var(--muted);
      margin-bottom: 6px;
    }

    .hint {
      position: absolute;
      left: 14px;
      bottom: 12px;
      color: var(--muted);
      font-size: 12px;
      background: rgba(255, 255, 255, 0.84);
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 7px 9px;
    }

    @media (max-width: 820px) {
      .app {
        grid-template-columns: 1fr;
        grid-template-rows: auto 1fr;
      }

      aside {
        max-height: 42vh;
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <aside>
      <h1>论文-任务-数据集知识图谱</h1>
      <div class="meta" id="summary"></div>

      <div class="group">
        <h2>搜索</h2>
        <input id="search" type="search" placeholder="论文、任务、数据集、标签">
      </div>

      <div class="group">
        <h2>节点类型</h2>
        <label><input type="checkbox" class="label-filter" value="Paper" checked> Paper</label>
        <label><input type="checkbox" class="label-filter" value="Task" checked> Task</label>
        <label><input type="checkbox" class="label-filter" value="Dataset" checked> Dataset</label>
        <label><input type="checkbox" class="label-filter" value="Tag" checked> Tag</label>
      </div>

      <div class="group">
        <h2>显示</h2>
        <label><input id="showLabels" type="checkbox" checked> 显示标签</label>
        <label><input id="showEdgeLabels" type="checkbox"> 显示关系名</label>
        <label><input id="focusSearch" type="checkbox" checked> 搜索时保留邻居节点</label>
      </div>

      <div class="group">
        <h2>布局密度</h2>
        <input id="distance" type="range" min="70" max="230" value="135">
      </div>

      <div class="group">
        <h2>图例</h2>
        <div class="legend" id="legend"></div>
      </div>

      <div class="group">
        <button id="reset">重置视图</button>
      </div>
    </aside>
    <main>
      <canvas id="graph"></canvas>
      <div class="tooltip" id="tooltip"></div>
      <div class="hint">拖拽节点移动，滚轮缩放，拖拽空白区域平移</div>
    </main>
  </div>

  <script>
    const graph = __GRAPH_DATA__;
    const canvas = document.getElementById("graph");
    const ctx = canvas.getContext("2d");
    const tooltip = document.getElementById("tooltip");
    const colors = {
      Paper: "#2563eb",
      Task: "#16a34a",
      Dataset: "#dc2626",
      Tag: "#7c3aed"
    };
    const radius = {
      Paper: 8,
      Task: 9,
      Dataset: 7,
      Tag: 5
    };

    let width = 0;
    let height = 0;
    let scale = 1;
    let offsetX = 0;
    let offsetY = 0;
    let draggingNode = null;
    let draggingCanvas = false;
    let lastPointer = null;
    let hoveredNode = null;
    let animationFrame = null;

    const nodes = graph.nodes.map((node, index) => ({
      ...node,
      x: Math.cos(index * 2.399) * (160 + index * 0.9),
      y: Math.sin(index * 2.399) * (160 + index * 0.9),
      vx: 0,
      vy: 0,
      visible: true
    }));
    const nodeById = new Map(nodes.map(node => [node.id, node]));
    const edges = graph.edges
      .map(edge => ({...edge, sourceNode: nodeById.get(edge.source), targetNode: nodeById.get(edge.target)}))
      .filter(edge => edge.sourceNode && edge.targetNode);

    function nodeText(node) {
      return [
        node.title,
        node.paper_file,
        node.task_description,
        node.task_tags,
        node.db_title,
        node.db_description,
        node.db_link,
        node.name
      ].filter(Boolean).join(" ").toLowerCase();
    }

    function nodeLabel(node) {
      if (node.label === "Paper") return node.title || node.paper_file || node.id;
      if (node.label === "Task") return node.task_tags || node.task_description || node.id;
      if (node.label === "Dataset") return node.db_title || node.id;
      if (node.label === "Tag") return node.name || node.id;
      return node.id;
    }

    function nodeDetail(node) {
      if (node.label === "Paper") return node.paper_file || "";
      if (node.label === "Task") return node.task_description || "";
      if (node.label === "Dataset") return [node.db_description, node.db_link].filter(Boolean).join("\\n");
      if (node.label === "Tag") return node.name || "";
      return "";
    }

    function resize() {
      const rect = canvas.parentElement.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      width = rect.width;
      height = rect.height;
      canvas.width = Math.max(1, Math.floor(width * dpr));
      canvas.height = Math.max(1, Math.floor(height * dpr));
      canvas.style.width = width + "px";
      canvas.style.height = height + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      draw();
    }

    function graphToScreen(x, y) {
      return { x: width / 2 + (x + offsetX) * scale, y: height / 2 + (y + offsetY) * scale };
    }

    function screenToGraph(x, y) {
      return { x: (x - width / 2) / scale - offsetX, y: (y - height / 2) / scale - offsetY };
    }

    function visibleEdges() {
      return edges.filter(edge => edge.sourceNode.visible && edge.targetNode.visible);
    }

    function applyFilters() {
      const enabledLabels = new Set([...document.querySelectorAll(".label-filter:checked")].map(input => input.value));
      const query = document.getElementById("search").value.trim().toLowerCase();
      const focusSearch = document.getElementById("focusSearch").checked;
      const matched = new Set();

      if (query) {
        nodes.forEach(node => {
          if (nodeText(node).includes(query)) matched.add(node.id);
        });
        if (focusSearch) {
          edges.forEach(edge => {
            if (matched.has(edge.source) || matched.has(edge.target)) {
              matched.add(edge.source);
              matched.add(edge.target);
            }
          });
        }
      }

      nodes.forEach(node => {
        const labelOk = enabledLabels.has(node.label);
        const queryOk = !query || matched.has(node.id);
        node.visible = labelOk && queryOk;
      });
      draw();
    }

    function simulate() {
      const targetDistance = Number(document.getElementById("distance").value);
      const activeNodes = nodes.filter(node => node.visible);
      const activeEdges = visibleEdges();

      for (const edge of activeEdges) {
        const source = edge.sourceNode;
        const target = edge.targetNode;
        const dx = target.x - source.x;
        const dy = target.y - source.y;
        const dist = Math.max(1, Math.hypot(dx, dy));
        const force = (dist - targetDistance) * 0.004;
        const fx = (dx / dist) * force;
        const fy = (dy / dist) * force;
        if (source !== draggingNode) {
          source.vx += fx;
          source.vy += fy;
        }
        if (target !== draggingNode) {
          target.vx -= fx;
          target.vy -= fy;
        }
      }

      for (let i = 0; i < activeNodes.length; i += 1) {
        const a = activeNodes[i];
        for (let j = i + 1; j < activeNodes.length; j += 1) {
          const b = activeNodes[j];
          const dx = b.x - a.x;
          const dy = b.y - a.y;
          const distSq = Math.max(25, dx * dx + dy * dy);
          const dist = Math.sqrt(distSq);
          const force = Math.min(1.8, 1300 / distSq);
          const fx = (dx / dist) * force;
          const fy = (dy / dist) * force;
          if (a !== draggingNode) {
            a.vx -= fx;
            a.vy -= fy;
          }
          if (b !== draggingNode) {
            b.vx += fx;
            b.vy += fy;
          }
        }
      }

      for (const node of activeNodes) {
        if (node === draggingNode) continue;
        node.vx += -node.x * 0.0007;
        node.vy += -node.y * 0.0007;
        node.vx *= 0.86;
        node.vy *= 0.86;
        node.x += node.vx;
        node.y += node.vy;
      }
    }

    function draw() {
      ctx.clearRect(0, 0, width, height);
      const showLabels = document.getElementById("showLabels").checked;
      const showEdgeLabels = document.getElementById("showEdgeLabels").checked;

      ctx.lineWidth = 1;
      ctx.strokeStyle = "rgba(100, 116, 139, 0.28)";
      ctx.fillStyle = "rgba(71, 85, 105, 0.72)";
      ctx.font = "11px Segoe UI, Arial";

      for (const edge of visibleEdges()) {
        const s = graphToScreen(edge.sourceNode.x, edge.sourceNode.y);
        const t = graphToScreen(edge.targetNode.x, edge.targetNode.y);
        ctx.beginPath();
        ctx.moveTo(s.x, s.y);
        ctx.lineTo(t.x, t.y);
        ctx.stroke();

        if (showEdgeLabels) {
          const mx = (s.x + t.x) / 2;
          const my = (s.y + t.y) / 2;
          ctx.fillText(edge.relation, mx + 4, my - 4);
        }
      }

      for (const node of nodes) {
        if (!node.visible) continue;
        const p = graphToScreen(node.x, node.y);
        const r = radius[node.label] || 6;
        const isHover = hoveredNode === node;
        ctx.beginPath();
        ctx.arc(p.x, p.y, (isHover ? r + 4 : r) * scale, 0, Math.PI * 2);
        ctx.fillStyle = colors[node.label] || "#475569";
        ctx.globalAlpha = isHover ? 1 : 0.88;
        ctx.fill();
        ctx.globalAlpha = 1;
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        if (showLabels) {
          const label = nodeLabel(node);
          const maxLength = node.label === "Task" ? 38 : 30;
          const text = label.length > maxLength ? label.slice(0, maxLength - 1) + "…" : label;
          ctx.fillStyle = "#1f2937";
          ctx.font = node.label === "Task" ? "12px Segoe UI, Arial" : "11px Segoe UI, Arial";
          ctx.fillText(text, p.x + 9, p.y + 4);
        }
      }
    }

    function tick() {
      simulate();
      draw();
      animationFrame = requestAnimationFrame(tick);
    }

    function findNodeAt(clientX, clientY) {
      const rect = canvas.getBoundingClientRect();
      const x = clientX - rect.left;
      const y = clientY - rect.top;
      for (let i = nodes.length - 1; i >= 0; i -= 1) {
        const node = nodes[i];
        if (!node.visible) continue;
        const p = graphToScreen(node.x, node.y);
        const r = (radius[node.label] || 6) * scale + 6;
        if (Math.hypot(p.x - x, p.y - y) <= r) return node;
      }
      return null;
    }

    function showTooltip(node, clientX, clientY) {
      if (!node) {
        tooltip.style.display = "none";
        return;
      }
      const detail = nodeDetail(node).replace(/\\n/g, "<br>");
      tooltip.innerHTML = `
        <div class="title">${escapeHtml(nodeLabel(node))}</div>
        <div class="type">${escapeHtml(node.label)}</div>
        <div>${escapeHtml(detail).replace(/\\n/g, "<br>")}</div>
      `;
      tooltip.style.left = Math.min(width - 440, clientX + 14) + "px";
      tooltip.style.top = Math.max(8, clientY + 14) + "px";
      tooltip.style.display = "block";
    }

    function escapeHtml(text) {
      return String(text || "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }

    canvas.addEventListener("pointerdown", event => {
      const node = findNodeAt(event.clientX, event.clientY);
      lastPointer = { x: event.clientX, y: event.clientY };
      if (node) {
        draggingNode = node;
        canvas.setPointerCapture(event.pointerId);
      } else {
        draggingCanvas = true;
      }
    });

    canvas.addEventListener("pointermove", event => {
      const rect = canvas.getBoundingClientRect();
      const localX = event.clientX - rect.left;
      const localY = event.clientY - rect.top;

      if (draggingNode) {
        const point = screenToGraph(localX, localY);
        draggingNode.x = point.x;
        draggingNode.y = point.y;
        draggingNode.vx = 0;
        draggingNode.vy = 0;
        draw();
        return;
      }

      if (draggingCanvas && lastPointer) {
        offsetX += (event.clientX - lastPointer.x) / scale;
        offsetY += (event.clientY - lastPointer.y) / scale;
        lastPointer = { x: event.clientX, y: event.clientY };
        draw();
        return;
      }

      hoveredNode = findNodeAt(event.clientX, event.clientY);
      showTooltip(hoveredNode, localX, localY);
      draw();
    });

    canvas.addEventListener("pointerup", event => {
      draggingNode = null;
      draggingCanvas = false;
      lastPointer = null;
      try { canvas.releasePointerCapture(event.pointerId); } catch (_) {}
    });

    canvas.addEventListener("pointerleave", () => {
      hoveredNode = null;
      tooltip.style.display = "none";
      draggingNode = null;
      draggingCanvas = false;
      draw();
    });

    canvas.addEventListener("wheel", event => {
      event.preventDefault();
      const factor = event.deltaY < 0 ? 1.1 : 0.9;
      scale = Math.max(0.2, Math.min(4, scale * factor));
      draw();
    }, { passive: false });

    document.getElementById("search").addEventListener("input", applyFilters);
    document.getElementById("showLabels").addEventListener("change", draw);
    document.getElementById("showEdgeLabels").addEventListener("change", draw);
    document.getElementById("focusSearch").addEventListener("change", applyFilters);
    document.getElementById("distance").addEventListener("input", draw);
    document.querySelectorAll(".label-filter").forEach(input => input.addEventListener("change", applyFilters));
    document.getElementById("reset").addEventListener("click", () => {
      scale = 1;
      offsetX = 0;
      offsetY = 0;
      document.getElementById("search").value = "";
      document.querySelectorAll(".label-filter").forEach(input => input.checked = true);
      document.getElementById("showLabels").checked = true;
      document.getElementById("showEdgeLabels").checked = false;
      applyFilters();
    });

    function initSidebar() {
      const labelCounts = {};
      nodes.forEach(node => labelCounts[node.label] = (labelCounts[node.label] || 0) + 1);
      document.getElementById("summary").textContent = `${nodes.length} 个节点，${edges.length} 条关系`;

      const legend = document.getElementById("legend");
      legend.innerHTML = Object.entries(colors).map(([label, color]) => `
        <div class="legend-item">
          <div class="legend-left"><span class="dot" style="background:${color}"></span><span>${label}</span></div>
          <span class="count">${labelCounts[label] || 0}</span>
        </div>
      `).join("");
    }

    window.addEventListener("resize", resize);
    initSidebar();
    resize();
    applyFilters();
    tick();
  </script>
</body>
</html>
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Generate a standalone HTML visualization for kg_graph.json.")
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH, help="Path to kg_graph.json.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output HTML path.")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.graph.exists():
        raise FileNotFoundError(f"Graph JSON not found: {args.graph}")

    with args.graph.open("r", encoding="utf-8") as f:
        graph = json.load(f)

    if not isinstance(graph, dict) or "nodes" not in graph or "edges" not in graph:
        raise ValueError("Graph JSON must contain 'nodes' and 'edges'.")

    graph_json = json.dumps(graph, ensure_ascii=False)
    html = HTML_TEMPLATE.replace("__GRAPH_DATA__", graph_json)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as f:
        f.write(html)

    print(f"Visualization written to: {args.output}")
    print(f"Nodes: {len(graph.get('nodes', []))}")
    print(f"Edges: {len(graph.get('edges', []))}")


if __name__ == "__main__":
    main()
