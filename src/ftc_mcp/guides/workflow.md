# Change workflow — do this for EVERY code change

The `map/` directory must always fully describe the project's logic. A teammate (or a
fresh Claude session) should be able to read `map/MAP.md` and understand the whole
codebase without opening the Java.

## After making any code change

1. **Update `map/project-map.yaml`** to reflect reality:
   - new subsystem → add to `subsystems:` (+ its `hardware:` entries)
   - new action / state machine → add to `actions:` with its `sequence:`
   - new opmode → add under `opmodes:`
   - new auto routine → add to `routines:` with its step list
   - new cross-subsystem data → add to `dataflow:`
   - changed public API / summary → edit the subsystem's `api:` / `summary:`

2. **Run the `update_map` tool** — it validates the YAML (cross-references, files on
   disk) and regenerates `map/overview.mmd`, `map/actions.mmd`, `map/dataflow.mmd`,
   `map/MAP.md`. Fix any reported issues.

3. **Run the `log_change` tool** with:
   - `prompt` — the user's request verbatim
   - `response` — a short summary of what you decided and did
   - `changes` — one line per file: `path — what & why`

`new_subsystem` does steps 1–2 for you; you still call `log_change`.

## Reading the map
- `ftc://project/map` resource returns the current `MAP.md`.
- Prefer consulting the map first; only open Java files for the parts you're changing.

## Before calling any SDK / library API
The FTC SDK is poorly documented — do not guess method names or signatures. Check the
decompiled reference:
- `sdk_search("setVelocity")` — find a method or class across ftc-sdk / pedro-pathing / panels
- `sdk_class("DcMotorEx")` — full exact signature block for one type
- `ftc://sdk/<lib>/<package>` — every signature in a package
- `ftc://sdk/<lib>` — the package/class index for a library
