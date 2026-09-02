# ftc-mcp

An MCP server that teaches Claude to write **FTC** (FIRST Tech Challenge) robot code in a
consistent architecture — subsystems, an action system, and base TeleOp / Auto opmodes,
modeled on [`CNapSys-22586-Decode`](https://github.com/Andrei0016/CNapSys-22586-Decode) —
and keeps a live, human-readable **map** of the whole codebase.

## What it provides

**Guides** (`ftc://guide/*`): `architecture`, `code-style`, `planning`, `workflow`.
**Toolkit refs** (`ftc://toolkit/*`) + **Mermaid maps** (`ftc://map/*`): `ftc-sdk`,
`pedro-pathing`, `panels-bylazar`, `starter-core`.
**Project map** (`ftc://project/map`): the current project's generated `map/MAP.md`.

**Tools**
| tool | purpose |
|---|---|
| `create_ftc_project` | clone the starter repo (or generate a core skeleton), install the two planning agents, `LOG.md`, `map/project-map.yaml`, `CLAUDE.md`, render the map |
| `new_subsystem` | scaffold `subsystems/<Name>/<Name>.java` + `<Name>Config.java`, register it in the map, re-render |
| `update_map` | validate `map/project-map.yaml` and regenerate `overview.mmd` / `actions.mmd` / `dataflow.mmd` / `MAP.md` |
| `render_map` | preview YAML → generated files, no disk writes |
| `log_change` | prepend an entry (prompt, reply, files) to `LOG.md` |

**Prompts**: `start_ftc_project`, `ftc_change_workflow`.

## The codebase map

`map/project-map.yaml` is the single source of truth — subsystems, hardware, actions,
opmodes, routines and cross-subsystem data flow. `update_map` validates cross-references
and regenerates the Mermaid diagrams + `MAP.md` so a reader understands the project from
the map alone. After **every** code change: edit the YAML → `update_map` → `log_change`.

## Install

### Straight from GitHub (recommended)

Needs [`uv`](https://docs.astral.sh/uv/) on PATH (`curl -LsSf https://astral.sh/uv/install.sh | sh`).
No clone, no manual venv — `uvx` fetches, builds and runs it:

```bash
claude mcp add ftc -- uvx --from git+https://github.com/Andrei0016/FTC-MCP ftc-mcp
```

Pin a tag/branch/commit with `@`:

```bash
claude mcp add ftc -- uvx --from git+https://github.com/Andrei0016/FTC-MCP@v0.1.0 ftc-mcp
```

Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "ftc": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/Andrei0016/FTC-MCP", "ftc-mcp"]
    }
  }
}
```

`uvx` caches the build; force a refresh after pushing changes with `uvx --refresh --from git+... ftc-mcp` (or bump the tag).

No `uv`? `pipx install git+https://github.com/Andrei0016/FTC-MCP` then use `ftc-mcp` as the command.

### From a local checkout (for developing the server)

```bash
python -m venv .venv && .venv/bin/pip install -e .
claude mcp add ftc -- /ABS/PATH/FTC-MCP/.venv/bin/python -m ftc_mcp
```

Or in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ftc": { "command": "/ABS/PATH/FTC-MCP/.venv/bin/python", "args": ["-m", "ftc_mcp"] }
  }
}
```

Inspect locally: `.venv/bin/mcp dev src/ftc_mcp/server.py`.

## Configuration

| env var | default | meaning |
|---|---|---|
| `FTC_STARTER_REPO_URL` | `https://github.com/Andrei0016/ftc-starter` | repo cloned by `create_ftc_project` (not created yet — skeleton fallback runs until it exists) |
| `FTC_PACKAGE` | `org.firstinspires.ftc.teamcode.robot` | default team base package |
