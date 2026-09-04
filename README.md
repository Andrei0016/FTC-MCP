# ftc-mcp

An MCP server that teaches Claude to write **FTC** (FIRST Tech Challenge) robot code in a
consistent architecture — subsystems, an action system, and base TeleOp / Auto opmodes,
modeled on [`CNapSys-22586-Decode`](https://github.com/Andrei0016/CNapSys-22586-Decode) —
and keeps a live, human-readable **map** of the whole codebase.

## What it provides

**Guides** (`ftc://guide/*`): `architecture`, `code-style`, `planning`, `workflow`, `accuracy`.
**Toolkit refs** (`ftc://toolkit/*`) + **Mermaid maps** (`ftc://map/*`): `ftc-sdk`,
`pedro-pathing`, `panels-bylazar`, `starter-core`.
**Project map** (`ftc://project/map`): the current project's generated `map/MAP.md`.

**Decompiled SDK reference** (`ftc://sdk/*`): exact `javap` signatures for every
team-facing type in the FTC SDK (RobotCore/Hardware/Vision 11.1.0), Pedro Pathing 2.1.2
and Panels 1.0.12 — because the FTC SDK is barely documented. `ftc://sdk` (overview),
`ftc://sdk/<lib>` (class index), `ftc://sdk/<lib>/<package>` (signatures). Plus tools
`sdk_search("setVelocity")` and `sdk_class("DcMotorEx")`. Regenerate for a new season
with `tools/gen_reference/build.sh` (needs a JDK). Digests are committed; the full
CFR-decompiled source lands in `reference/` (gitignored).

**Tools**
| tool | purpose |
|---|---|
| `create_ftc_project` | clone the starter repo (or generate a core skeleton), install the two planning agents, `LOG.md`, `map/project-map.yaml`, `CLAUDE.md`, render the map |
| `new_subsystem` | scaffold `subsystems/<Name>/<Name>.java` + `<Name>Config.java`, register it in the map, re-render |
| `update_map` | validate `map/project-map.yaml` and regenerate `overview.mmd` / `actions.mmd` / `dataflow.mmd` / `MAP.md` |
| `render_map` | preview YAML → generated files, no disk writes |
| `log_change` | prepend an entry (prompt, reply, files) to `LOG.md` |
| `sdk_search` | substring search for a class/method across the decompiled SDK reference |
| `sdk_class` | full exact signature block for one type + pointer to decompiled source |

**Prompts**: `start_ftc_project`, `ftc_change_workflow`.

## The codebase map

`map/project-map.yaml` is the single source of truth — subsystems, hardware, actions,
opmodes, routines and cross-subsystem data flow. `update_map` validates cross-references
and regenerates the Mermaid diagrams + `MAP.md` so a reader understands the project from
the map alone. After **every** code change: edit the YAML → `update_map` → `log_change`.

## Install from GitHub

No clone and no manual virtualenv — `uvx` fetches the repo, builds the package and runs
the `ftc-mcp` command in one step.

### 1. Install `uv`

`uvx` ships with [`uv`](https://docs.astral.sh/uv/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh      # macOS / Linux
# Windows (PowerShell):
#   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Open a new shell afterwards so `uvx` is on `PATH` (check with `uvx --version`).

### 2. Register the server

**Claude Code** — one command:

```bash
claude mcp add ftc -- uvx --from git+https://github.com/Andrei0016/FTC-MCP ftc-mcp
```

Add `-s user` to make it available in every project instead of just the current one.

**Claude Desktop** — add to `claude_desktop_config.json`
(`~/Library/Application Support/Claude/` on macOS,
`%APPDATA%\Claude\` on Windows), then restart the app:

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

### 3. Verify

In a Claude Code session run `/mcp` — `ftc` should list as connected with its tools,
resources and prompts. Or ask Claude to read `ftc://guide/architecture`.

### Pinning a version

Append `@<tag|branch|commit>` to the git URL:

```bash
claude mcp add ftc -- uvx --from git+https://github.com/Andrei0016/FTC-MCP@v0.1.0 ftc-mcp
```

### Updating

`uvx` caches the build per revision. After new commits are pushed to the same
branch, force a rebuild once:

```bash
uvx --refresh --from git+https://github.com/Andrei0016/FTC-MCP ftc-mcp
```

Subsequent runs use the refreshed cache. Bumping a pinned tag also picks up changes.

### Removing

```bash
claude mcp remove ftc
```

### No `uv`?

```bash
pipx install git+https://github.com/Andrei0016/FTC-MCP
claude mcp add ftc -- ftc-mcp
```

## From a local checkout (for developing the server)

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
| `FTC_STARTER_REPO_URL` | `https://github.com/Pedro-Pathing/Quickstart` | repo cloned by `create_ftc_project` (not created yet — skeleton fallback runs until it exists) |
| `FTC_PACKAGE` | `org.firstinspires.ftc.teamcode.robot` | default team base package |
