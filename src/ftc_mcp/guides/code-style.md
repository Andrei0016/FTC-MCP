# FTC code style

Goal: organized, easy to read, as simple and efficient as possible.

## Structure
- One responsibility per class. If a subsystem file grows past ~200 lines, look for a
  helper to extract into `core/utils/`.
- No premature abstraction. Add an interface/generic only when a second implementation
  actually exists.
- Constants are never inlined — they go in the matching `@Configurable` config class.
- **Placeholder constants get a `// TODO:` note.** Any tunable you set from a guess
  rather than a measured/verified value (PIDF gains, feedforward numbers, positions,
  timeouts, speeds, etc.) must be flagged right on that line, e.g.
  `public static double kP = 0.01; // TODO: tune on hardware, placeholder value` —
  never leave a guessed number looking like a finished one.
- No dead code, no commented-out blocks left behind. Delete it; git remembers.

## Comments
- Short. One line above a method saying **what it does / why**, not how.
  `/** Auto-aims the turret at the goal, compensating for robot velocity. */`
- Never restate the code (`// increment i`). Never write paragraph-length comments.
- Use section dividers inside config / long classes:
  `// ── PIDF ──────────────────────────────────`
- A tricky one-liner gets a trailing `// why` note; nothing else needs one.

## Efficiency (FTC loop runs ~50–100 Hz)
- No allocation in the hot loop where avoidable (reuse vectors/poses).
- Enable `LynxModule` bulk caching once in `Robot`'s constructor.
- Cache sensor reads per loop; don't read the same sensor twice.
- Prefer simple math over library calls in `update()`.

## Naming
- Subsystems + classes: `PascalCase`. Methods/fields: `camelCase`.
- Config fields that are tuned live: `SCREAMING_SNAKE` or `camelCase`, consistent per file.
- OpMode classes carry an `@TeleOp`/`@Autonomous` annotation with a clear `name`.
