# Change workflow — do this for EVERY code change

Before any of this: ask the user whatever you need to understand the task. If it looks
like a serious task (see `ftc://guide/planning`), ask the user whether it needs a plan
before drafting one — then, if they say yes, confirm your understanding and get the
reconciled plan approved before implementing.

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

3. **Review the changed files yourself** (see "Verifying correctness" below) — do this
   before `log_change`, so the log reflects code you've actually checked.

4. **Run the `log_change` tool** with:
   - `prompt` — the user's request verbatim
   - `response` — a short summary of what you decided and did
   - `changes` — one line per file: `path — what & why`

`new_subsystem` does steps 1–2 for you; you still review and call `log_change`.

## Verifying correctness — read, don't compile
There is no Android/Gradle toolchain here, so **do not try to build or compile the
project** to check your work — the build will not run in this environment and attempting
it just burns tokens on a failure that proves nothing.

Instead, after implementing, **read back every changed file** and check by hand:
- every method/constant called on an SDK, Pedro or Panels type matches a signature you
  verified per `ftc://guide/accuracy` (`sdk_class`, `sdk_search`)
- types match: constructor args, return types used correctly, no obvious null paths
- imports exist for everything referenced; no stray/unused imports
- braces/parens balanced, no leftover placeholder text from a template
- every placeholder constant (a guessed value, not a measured/verified one) has a
  `// TODO:` note on it per `ftc://guide/code-style` — nothing guessed should look finished
- the change matches `ftc://guide/architecture` (subsystem boundaries, no drivetrain
  subsystem, hardware only touched in `update()`, etc.) and `ftc://guide/code-style`
- the map (`project-map.yaml` + rendered files) matches what the code now does

If something is genuinely uncertain after this read-through, say so rather than guessing
— per `ftc://guide/accuracy`.

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
