"""Scaffold a new FTC project: clone the starter repo (or fall back to a skeleton),
drop in the planning agents, the change log, the project map and CLAUDE.md."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .. import config
from . import mapping

_TMPL = Path(__file__).parent.parent / "templates"
_PROJECT_TMPL = _TMPL / "project"
_CORE_TMPL = _TMPL / "core"


def _fill(text: str, package: str, project_name: str) -> str:
    return (
        text.replace("<<PACKAGE>>", package)
        .replace("<<PACKAGE_PATH>>", package.replace(".", "/"))
        .replace("<<PROJECT_NAME>>", project_name)
    )


def _scaffold_core(target: Path, package: str) -> list[str]:
    """Generate a minimal core/ + opmodes/ skeleton when the starter repo is unavailable."""
    pkg_root = target / "TeamCode/src/main/java" / package.replace(".", "/")
    written = []
    for tmpl in _CORE_TMPL.rglob("*.tmpl"):
        rel = tmpl.relative_to(_CORE_TMPL)
        dest = pkg_root / str(rel)[: -len(".tmpl")]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(_fill(tmpl.read_text(), package, target.name))
        written.append(str(dest.relative_to(target)))
    return written


def _write_project_files(target: Path, package: str, project_name: str) -> None:
    for tmpl in _PROJECT_TMPL.rglob("*"):
        if tmpl.is_dir():
            continue
        rel = str(tmpl.relative_to(_PROJECT_TMPL))
        if rel.endswith(".tmpl"):
            rel = rel[: -len(".tmpl")]
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        content = tmpl.read_text()
        if tmpl.suffix in {".tmpl", ".yaml", ".md"}:
            content = _fill(content, package, project_name)
        dest.write_text(content)


def create_ftc_project(
    target_dir: str,
    team_package: str | None = None,
    team_number: str | None = None,
    starter_repo_url: str | None = None,
    project_name: str | None = None,
) -> str:
    target = Path(target_dir).expanduser().resolve()
    package = team_package or config.default_package()
    url = starter_repo_url or config.starter_repo_url()
    project_name = project_name or target.name
    notes: list[str] = []

    target.mkdir(parents=True, exist_ok=True)
    empty = not any(target.iterdir())
    cloned = False

    if empty:
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", url, str(target)],
                check=True, capture_output=True, text=True, timeout=120,
            )
            shutil.rmtree(target / ".git", ignore_errors=True)
            cloned = True
            notes.append(f"Cloned starter repo: {url}")
            notes.append(
                "NOTE: rename the cloned base package to "
                f"`{package}` (dirs + `package`/`import` lines) if it differs."
            )
        except Exception as e:  # noqa: BLE001 - want the message whatever it is
            detail = getattr(e, "stderr", "") or str(e)
            notes.append(f"Could not clone {url} ({detail.strip()[:200]}). Using skeleton instead.")
    else:
        notes.append("Target directory not empty — skipped clone.")

    if not cloned:
        written = _scaffold_core(target, package)
        notes.append(f"Generated skeleton: {len(written)} core/opmode files under {package}.")

    _write_project_files(target, package, project_name)
    notes.append("Wrote: LOG.md, map/project-map.yaml, CLAUDE.md, .claude/agents/{plan-pro-advocate,plan-critic}.md")

    map_result = mapping.update_map(target)
    map_md = (target / "map/MAP.md").read_text()

    checklist = "\n".join(f"  - {n}" for n in notes)
    return (
        f"# FTC project ready at {target}\n\n"
        f"{checklist}\n\n"
        f"{map_result}\n\n"
        "## Next steps\n"
        "  1. Open the project in Android Studio; confirm it builds.\n"
        "  2. The planning agents `plan-pro-advocate` and `plan-critic` are installed in "
        "`.claude/agents/` — run BOTH before any non-trivial change, then reconcile.\n"
        "  3. Add subsystems with the `new_subsystem` tool.\n"
        "  4. After every change: edit `map/project-map.yaml` → `update_map` → `log_change`.\n\n"
        "## Current map (map/MAP.md)\n\n"
        f"{map_md}"
    )
