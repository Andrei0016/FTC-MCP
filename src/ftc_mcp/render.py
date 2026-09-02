"""Render a ProjectMap into Mermaid diagrams and a Markdown summary.

Outputs (all under `map/`, never hand-edited):
  overview.mmd   flowchart: OpMode -> Robot -> Subsystem -> Hardware
  actions.mmd    one stateDiagram-v2 per action sequence
  dataflow.mmd   graph of cross-subsystem data edges
  MAP.md         embeds the three diagrams + per-subsystem API tables + routine steps
"""

from __future__ import annotations

import re
from pathlib import Path

from .schema import ProjectMap


def _mmid(name: str) -> str:
    """Safe mermaid node id."""
    return re.sub(r"\W", "_", name) or "n"


def overview_mmd(pm: ProjectMap) -> str:
    lines = ["flowchart TD"]
    lines.append("    Robot([Robot])")

    for o in pm.teleop + pm.auto:
        nid = _mmid(o.cls)
        lines.append(f"    {nid}[{o.cls}]")
        lines.append(f"    {nid} --> Robot")

    for s in pm.subsystems:
        sid = _mmid(s.name)
        lines.append(f"    Robot --> {sid}[{s.name}]")
        for hw in s.hardware:
            hid = _mmid(hw)
            lines.append(f"    {sid} --> {hid}[/{hw}/]")

    # subsystem dependencies on shared utils
    for s in pm.subsystems:
        for dep in s.depends_on:
            lines.append(f"    {_mmid(s.name)} -.uses.-> {_mmid(dep)}({dep})")

    return "\n".join(lines) + "\n"


def actions_mmd(pm: ProjectMap) -> str:
    if not pm.actions:
        return "%% no actions defined yet\n"
    blocks: list[str] = []
    for a in pm.actions:
        block = [f"stateDiagram-v2", f"    %% {a.name} — entry: {a.entrypoint or 'n/a'}"]
        stages = [s.strip() for s in re.split(r"->|→", a.sequence) if s.strip()]
        if not stages:
            block.append("    [*] --> IDLE")
        else:
            block.append(f"    [*] --> {_mmid(stages[0])}")
            for x, y in zip(stages, stages[1:]):
                block.append(f"    {_mmid(x)} --> {_mmid(y)}")
            block.append(f"    {_mmid(stages[-1])} --> [*]")
        blocks.append("\n".join(block))
    # Mermaid renders one diagram per file; join with separators for the .mmd bundle.
    return ("\n\n---\n\n").join(blocks) + "\n"


def dataflow_mmd(pm: ProjectMap) -> str:
    lines = ["flowchart LR"]
    if not pm.dataflow:
        lines.append("    %% no cross-subsystem data flow defined yet")
    for f in pm.dataflow:
        label = f" |{f.via}| " if f.via else " "
        lines.append(f"    {_mmid(f.src)}[{f.src}] --{label}--> {_mmid(f.dst)}[{f.dst}]")
    return "\n".join(lines) + "\n"


def map_md(pm: ProjectMap) -> str:
    md: list[str] = ["# Project Map", ""]
    md.append(f"**Package:** `{pm.package or 'unset'}`")
    md.append("")
    md.append("> Generated from `map/project-map.yaml` by the `update_map` MCP tool. "
              "Do not edit by hand — edit the YAML and re-run `update_map`.")
    md.append("")

    md += ["## Overview", "", "```mermaid", overview_mmd(pm).rstrip(), "```", ""]

    md += ["## Subsystems", ""]
    for s in pm.subsystems:
        md.append(f"### {s.name}")
        if s.summary:
            md.append(f"_{s.summary}_")
        md.append("")
        md.append(f"- **File:** `{s.file or '?'}` · **Config:** `{s.config or '?'}`")
        if s.hardware:
            md.append(f"- **Hardware:** {', '.join(f'`{h}`' for h in s.hardware)}")
        if s.states:
            md.append(f"- **States:** {' → '.join(s.states)}")
        if s.depends_on:
            md.append(f"- **Depends on:** {', '.join(s.depends_on)}")
        if s.api:
            md.append("- **API:**")
            for m in s.api:
                md.append(f"  - `{m}`")
        md.append("")

    if pm.actions:
        md += ["## Actions", "", "```mermaid", actions_mmd(pm).rstrip(), "```", ""]
        for a in pm.actions:
            md.append(f"- **{a.name}** — entry `{a.entrypoint or 'n/a'}`; "
                      f"touches {', '.join(a.touches) or 'n/a'}")
        md.append("")

    if pm.dataflow:
        md += ["## Data flow", "", "```mermaid", dataflow_mmd(pm).rstrip(), "```", ""]

    if pm.teleop or pm.auto:
        md += ["## OpModes", ""]
        for o in pm.teleop:
            md.append(f"- **TeleOp** `{o.cls}` ({o.alliance or '?'}) extends `{o.base or 'BaseTeleOp'}`")
        for o in pm.auto:
            md.append(f"- **Auto** `{o.cls}` ({o.alliance or '?'}) runs routine `{o.routine or '?'}`")
        md.append("")

    if pm.routines:
        md += ["## Routines", ""]
        for r in pm.routines:
            md.append(f"### {r.name}")
            for i, step in enumerate(r.steps, 1):
                md.append(f"{i}. `{step}`")
            md.append("")

    return "\n".join(md).rstrip() + "\n"


def render_all(pm: ProjectMap) -> dict[str, str]:
    """Return {relpath: content} for every generated map file."""
    return {
        "map/overview.mmd": overview_mmd(pm),
        "map/actions.mmd": actions_mmd(pm),
        "map/dataflow.mmd": dataflow_mmd(pm),
        "map/MAP.md": map_md(pm),
    }


def write_all(project_dir: str | Path, pm: ProjectMap) -> list[str]:
    root = Path(project_dir)
    written: list[str] = []
    for rel, content in render_all(pm).items():
        dest = root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)
        written.append(rel)
    return written
