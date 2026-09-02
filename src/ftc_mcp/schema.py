"""Schema, load/dump and validation for `map/project-map.yaml`.

The project map is the single source of truth for project structure. Tools read and
patch it; `render.py` turns it into Mermaid + Markdown. Keeping it structured (not raw
Mermaid) lets us validate cross-references and regenerate diagrams deterministically.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

MAP_RELPATH = "map/project-map.yaml"


@dataclass
class Hardware:
    name: str
    type: str = "DcMotorEx"
    subsystem: str = ""


@dataclass
class Subsystem:
    name: str
    file: str = ""
    config: str = ""
    implements: str = "Subsystem"
    hardware: list[str] = field(default_factory=list)
    states: list[str] = field(default_factory=list)
    api: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    summary: str = ""


@dataclass
class Action:
    name: str
    entrypoint: str = ""
    sequence: str = ""
    touches: list[str] = field(default_factory=list)


@dataclass
class OpMode:
    cls: str
    alliance: str = ""
    base: str = ""
    routine: str = ""


@dataclass
class Routine:
    name: str
    steps: list[str] = field(default_factory=list)


@dataclass
class DataFlow:
    src: str
    dst: str
    via: str = ""


@dataclass
class ProjectMap:
    package: str = ""
    hardware: list[Hardware] = field(default_factory=list)
    subsystems: list[Subsystem] = field(default_factory=list)
    actions: list[Action] = field(default_factory=list)
    teleop: list[OpMode] = field(default_factory=list)
    auto: list[OpMode] = field(default_factory=list)
    routines: list[Routine] = field(default_factory=list)
    dataflow: list[DataFlow] = field(default_factory=list)

    # ── serialization ──────────────────────────────────────────────────────
    @staticmethod
    def from_dict(d: dict[str, Any]) -> "ProjectMap":
        d = d or {}
        opmodes = d.get("opmodes", {}) or {}

        def _op(item: dict[str, Any]) -> OpMode:
            return OpMode(
                cls=item.get("class", item.get("cls", "")),
                alliance=item.get("alliance", ""),
                base=item.get("base", ""),
                routine=item.get("routine", ""),
            )

        def _flow(item: dict[str, Any]) -> DataFlow:
            return DataFlow(
                src=item.get("from", item.get("src", "")),
                dst=item.get("to", item.get("dst", "")),
                via=item.get("via", ""),
            )

        return ProjectMap(
            package=d.get("package", ""),
            hardware=[Hardware(**h) for h in d.get("hardware", []) or []],
            subsystems=[Subsystem(**s) for s in d.get("subsystems", []) or []],
            actions=[Action(**a) for a in d.get("actions", []) or []],
            teleop=[_op(o) for o in opmodes.get("teleop", []) or []],
            auto=[_op(o) for o in opmodes.get("auto", []) or []],
            routines=[Routine(**r) for r in d.get("routines", []) or []],
            dataflow=[_flow(f) for f in d.get("dataflow", []) or []],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "package": self.package,
            "hardware": [vars(h) for h in self.hardware],
            "subsystems": [vars(s) for s in self.subsystems],
            "actions": [vars(a) for a in self.actions],
            "opmodes": {
                "teleop": [_op_to_dict(o) for o in self.teleop],
                "auto": [_op_to_dict(o) for o in self.auto],
            },
            "routines": [vars(r) for r in self.routines],
            "dataflow": [{"from": f.src, "to": f.dst, "via": f.via} for f in self.dataflow],
        }


def _op_to_dict(o: OpMode) -> dict[str, Any]:
    out = {"class": o.cls, "alliance": o.alliance}
    if o.base:
        out["base"] = o.base
    if o.routine:
        out["routine"] = o.routine
    return out


# ── file helpers ───────────────────────────────────────────────────────────
def map_path(project_dir: str | Path) -> Path:
    return Path(project_dir) / MAP_RELPATH


def load(project_dir: str | Path) -> ProjectMap:
    p = map_path(project_dir)
    if not p.exists():
        raise FileNotFoundError(f"No project map at {p}. Run create_ftc_project first.")
    return ProjectMap.from_dict(yaml.safe_load(p.read_text()) or {})


def dump(project_dir: str | Path, pm: ProjectMap) -> Path:
    p = map_path(project_dir)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump(pm.to_dict(), sort_keys=False, allow_unicode=True))
    return p


# ── validation ─────────────────────────────────────────────────────────────
def validate(pm: ProjectMap, project_dir: str | Path | None = None) -> list[str]:
    """Return a list of human-readable problems. Empty list == valid."""
    errors: list[str] = []
    sub_names = {s.name for s in pm.subsystems}

    for h in pm.hardware:
        if h.subsystem and h.subsystem not in sub_names:
            errors.append(f"hardware '{h.name}' points at unknown subsystem '{h.subsystem}'")

    hw_names = {h.name for h in pm.hardware}
    for s in pm.subsystems:
        for hw in s.hardware:
            if hw not in hw_names:
                errors.append(f"subsystem '{s.name}' lists hardware '{hw}' not in hardware:")

    for a in pm.actions:
        for t in a.touches:
            if t.lower() not in {n.lower() for n in sub_names}:
                errors.append(f"action '{a.name}' touches unknown subsystem '{t}'")

    routine_names = {r.name for r in pm.routines}
    for o in pm.auto:
        if o.routine and o.routine not in routine_names:
            errors.append(f"auto opmode '{o.cls}' references unknown routine '{o.routine}'")

    for f in pm.dataflow:
        for endpoint in (f.src, f.dst):
            if endpoint and endpoint not in sub_names:
                errors.append(f"dataflow endpoint '{endpoint}' is not a subsystem")

    if project_dir is not None:
        root = Path(project_dir)
        for s in pm.subsystems:
            if s.file and not (root / s.file).exists():
                errors.append(f"subsystem '{s.name}' file missing on disk: {s.file}")

    return errors
