# Starter core (the toolkit)

The starter repo (configurable via `FTC_STARTER_REPO_URL`) ships the `core/` package that
every project builds on. If the repo isn't reachable, `create_ftc_project` generates a
lean version of the same classes.

## `core/interfaces/Subsystem.java`
```java
public interface Subsystem {
    boolean isBusy();
    void update(double deltaTime, TelemetryManager tm, SubsystemData data);
}
```

## `core/vars/`
- `Action` — enum of high-level actions (extend per game: `SHOOT`, `SCORE`, …).
- `Alliance` — `RED` / `BLUE`.
- `SubsystemData` — mutable per-loop bus; `Robot` fills it, subsystems read it.

## `core/Robot.java`
Holds every subsystem + the Pedro `Follower`, the shared `TelemetryManager`, an
`ElapsedTime`. Runs each action's state machine (`private enum <Action>State`) inside
`update()`. Exposes `isXBusy()` / `isXCycleActive()` + one method per action.

## `core/RobotConfig.java`
`@Configurable` robot-wide tunables (drive rates, toggles) and persisted state
(`ROBOT_POSE` carried between opmodes).

## `core/utils/`
Pure helpers, no hardware: `PIDF` (positional PID + sign(error)·kF), `SlewRateLimiter`,
filters, `Drawing`. Reuse these instead of re-implementing control math in a subsystem.

## `opmodes/`
`teleop/BaseTeleOp`, `auto/base/BaseAuto`, `auto/base/AutoRoutine` — see
`ftc://guide/architecture`.
