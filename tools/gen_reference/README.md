# SDK reference generator

Produces the exact API digests the MCP server serves at `ftc://sdk/*`, plus (locally)
the full decompiled source under `reference/`.

## Run

```bash
tools/gen_reference/build.sh
```

Needs: `bash`, `curl`, `unzip`, `python3`, and a JDK 11+ (`javap`).
On macOS: `brew install --cask temurin` (the script auto-detects it via `/usr/libexec/java_home`).

## What it does

1. Downloads the artifacts pinned in `manifest.json` (cached in `.cache/`).
2. Extracts each `classes.jar`.
3. `javap -protected -constants` over every class whose package matches
   `include_prefixes` and misses `exclude_substrings` → exact signatures.
4. CFR-decompiles every jar → `reference/<lib>/` (gitignored; used by the `sdk_class`
   tool for full method bodies when present).
5. Writes `src/ftc_mcp/sdk/<lib>/<package>.md`, `index.md`, `_classes.json`.

## Updating for a new season

Bump the versions + URLs in `manifest.json` to match the current
[Pedro Pathing Quickstart](https://github.com/Pedro-Pathing/Quickstart)
`build.dependencies.gradle`, then rerun `build.sh` and commit the changed digests.

## Scope

`include_prefixes` targets the **team-facing** surface — hardware, opmodes, telemetry,
navigation/geometry, vision entry points, vendor device drivers, and all of Pedro
Pathing / Panels. Android plumbing, USB/serial, robocol, blocks and OnBotJava internals
are excluded (`exclude_substrings`). Widen the manifest if you need more.
