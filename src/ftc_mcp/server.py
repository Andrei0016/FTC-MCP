"""FastMCP server exposing FTC coding guides, toolkit maps and project tools."""

from __future__ import annotations

from pathlib import Path

from mcp.server.fastmcp import FastMCP

from . import config
from .tools import changelog, mapping, project, sdk, subsystem

_PKG = Path(__file__).parent
_GUIDES = _PKG / "guides"
_TOOLKITS = _PKG / "toolkits"
_MAPS = _PKG / "maps"

mcp = FastMCP("ftc-mcp")


# ── resources ──────────────────────────────────────────────────────────────
def _read(base: Path, name: str, suffix: str) -> str:
    f = base / f"{name}{suffix}"
    if not f.exists():
        raise ValueError(f"unknown resource: {name}")
    return f.read_text()


@mcp.resource("ftc://guide/{name}")
def guide(name: str) -> str:
    """FTC coding guides: architecture, code-style, planning, workflow, accuracy."""
    return _read(_GUIDES, name, ".md")


@mcp.resource("ftc://toolkit/{name}")
def toolkit(name: str) -> str:
    """Toolkit references: ftc-sdk, pedro-pathing, panels-bylazar, starter-core."""
    return _read(_TOOLKITS, name, ".md")


@mcp.resource("ftc://map/{name}")
def toolkit_map(name: str) -> str:
    """Mermaid maps: ftc-sdk, pedro-pathing, panels-bylazar, starter-core."""
    return _read(_MAPS, name, ".mmd")


@mcp.resource("ftc://project/map")
def project_map() -> str:
    """The current working project's map/MAP.md, if one can be found nearby."""
    for start in (Path.cwd(), *Path.cwd().parents):
        md = start / "map" / "MAP.md"
        if md.exists():
            return md.read_text()
    return (
        "No map/MAP.md found from the current directory. Run create_ftc_project to "
        "scaffold one, or update_map inside an existing project."
    )


@mcp.resource("ftc://sdk")
def sdk_index() -> str:
    """Overview of the decompiled SDK reference (ftc-sdk, pedro-pathing, panels)."""
    return sdk.list_libs()


@mcp.resource("ftc://sdk/{lib}")
def sdk_lib_index(lib: str) -> str:
    """Per-library API index: every team-facing type, grouped by package."""
    return sdk.lib_index(lib)


@mcp.resource("ftc://sdk/{lib}/{package}")
def sdk_package(lib: str, package: str) -> str:
    """Exact signatures (javap -protected) for every type in one package."""
    return sdk.package_digest(lib, package)


@mcp.resource("ftc://config")
def show_config() -> str:
    """Effective server configuration."""
    return f"starter_repo_url = {config.starter_repo_url()}\ndefault_package = {config.default_package()}\n"


# ── tools ──────────────────────────────────────────────────────────────────
@mcp.tool()
def create_ftc_project(
    target_dir: str,
    team_package: str = "",
    team_number: str = "",
    starter_repo_url: str = "",
    project_name: str = "",
) -> str:
    """Scaffold a new FTC project: clone the starter repo (or generate a core skeleton),
    install the plan-pro-advocate / plan-critic agents, LOG.md, the project map and
    CLAUDE.md, then render the initial map. Returns a checklist + the generated MAP.md."""
    return project.create_ftc_project(
        target_dir,
        team_package or None,
        team_number or None,
        starter_repo_url or None,
        project_name or None,
    )


@mcp.tool()
def new_subsystem(
    project_dir: str,
    name: str,
    hardware: list[str] | None = None,
    has_states: bool = False,
    summary: str = "",
) -> str:
    """Create subsystems/<Name>/<Name>.java + <Name>Config.java from templates, register
    the subsystem (and its hardware) in map/project-map.yaml, and re-render the map.
    hardware entries are "name" or "name:Type" (default type DcMotorEx)."""
    return subsystem.new_subsystem(project_dir, name, hardware, has_states, summary)


@mcp.tool()
def update_map(project_dir: str) -> str:
    """Validate map/project-map.yaml and regenerate overview.mmd, actions.mmd,
    dataflow.mmd and MAP.md. Run after every edit to the project map."""
    return mapping.update_map(project_dir)


@mcp.tool()
def render_map(yaml_text: str) -> str:
    """Preview: turn project-map YAML text into the four generated files without writing
    to disk. Useful for checking a map edit before applying it."""
    return mapping.render_map(yaml_text)


@mcp.tool()
def log_change(
    project_dir: str,
    prompt: str,
    response: str,
    changes: list[str],
    title: str = "",
    map_updated: bool = True,
) -> str:
    """Prepend an entry to LOG.md: the user prompt, Claude's reply summary, and one line
    per changed file. Call this after every code change."""
    return changelog.log_change(
        project_dir, prompt, response, changes, title or None, map_updated
    )


@mcp.tool()
def sdk_search(query: str, lib: str = "") -> str:
    """Search the decompiled SDK reference for a class or method by substring
    (case-insensitive). Returns matching signature lines with their type + package.
    lib filters to one of: ftc-sdk, pedro-pathing, panels."""
    return sdk.search(query, lib)


@mcp.tool()
def sdk_class(fqcn: str) -> str:
    """Return the full exact signature block for one type (fully-qualified or simple
    name), plus a pointer to its decompiled source if generated locally."""
    return sdk.class_block(fqcn)


# ── prompts ────────────────────────────────────────────────────────────────
@mcp.prompt()
def start_ftc_project(target_dir: str, team_number: str = "") -> str:
    """Guide for standing up a new FTC project."""
    return (
        f"Set up a new FTC robot project in {target_dir}"
        + (f" for team {team_number}" if team_number else "")
        + ".\n\n"
        "1. Read ftc://guide/architecture, ftc://guide/code-style, ftc://guide/planning, "
        "ftc://guide/workflow and ftc://guide/accuracy.\n"
        "2. Skim ftc://map/starter-core, ftc://map/pedro-pathing, ftc://map/panels-bylazar.\n"
        "3. Call the create_ftc_project tool with target_dir set.\n"
        "4. Confirm the plan-pro-advocate and plan-critic agents exist in .claude/agents/.\n"
        "5. For the first subsystem, draft a plan, run BOTH planning agents, reconcile, "
        "then use the new_subsystem tool.\n"
        "6. After every change: update map/project-map.yaml → update_map → log_change."
    )


@mcp.prompt()
def ftc_change_workflow(request: str) -> str:
    """Wrap a change request in the mandatory FTC workflow."""
    return (
        f"Change request: {request}\n\n"
        "Follow ftc://guide/workflow:\n"
        "1. Consult ftc://project/map first; open Java only for the parts you change.\n"
        "2. Draft a plan. If non-trivial, run plan-pro-advocate AND plan-critic, reconcile.\n"
        "3. Implement per ftc://guide/architecture and ftc://guide/code-style "
        "(short one-line comments). Per ftc://guide/accuracy, only use API you have "
        "verified against the decompiled reference — never guess.\n"
        "4. Update map/project-map.yaml, then run update_map.\n"
        "5. Run log_change with this request, your reply summary and the files changed."
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
