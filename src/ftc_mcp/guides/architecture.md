# FTC code architecture

The structure below mirrors the reference repo
`github.com/Andrei0016/CNapSys-22586-Decode`. Follow it for every project.

```
TeamCode/src/main/java/<package>/
  core/
    Robot.java              owns all subsystems + Pedro Follower; runs action state machines
    RobotConfig.java        @Configurable robot-wide tunables + shared state
    interfaces/Subsystem.java
    vars/                   Action.java, Alliance.java, SubsystemData.java, enums
    utils/                  PIDF, SlewRateLimiter, filters, drawing — pure helpers
  subsystems/<Name>/
    <Name>.java             implements Subsystem
    <Name>Config.java       @Configurable static tunables (@Sorter ordered)
  opmodes/
    teleop/
      BaseTeleOp.java        abstract OpMode: all shared teleop logic
      TeleOpConfig.java
      teleOpRED.java / teleOpBLUE.java   ~10-line per-alliance subclasses
    auto/
      base/BaseAuto.java     abstract OpMode: runs an AutoRoutine step machine
      base/AutoRoutine.java  step builder (move/shootSequence/turnTo/waitUntil)
      constants/             per-routine pose + path constants
      routines/              one AutoRoutine subclass per auto
    calibration/             throwaway test opmodes (servoTest, sensorTest, ...)
  pedroPathing/              Constants.java, Tuning.java (Pedro setup)
```

## Subsystem rules
- One folder per subsystem. `<Name>.java implements Subsystem`.
- Hardware handles are **constructor parameters** — `Robot` pulls them from
  `hardwareMap` and passes them in. A subsystem never touches `hardwareMap`.
- Public API is small verbs: `enable()`, `disable()`, `goTo(x)`, `isBusy()`.
- `isBusy()` reports whether the mechanism still has work to do (used for sequencing).
- `update(dt, tm, data)` is the only place hardware outputs are written. It is called
  once per loop by `Robot`. Read tunables from `<Name>Config`, read cross-subsystem
  info from `data` (`SubsystemData`).
- **All** magic numbers live in `<Name>Config` as `public static` fields with `@Sorter`.

## Robot rules
- Holds a field per subsystem (`public final`), plus the Pedro `Follower`.
- Owns **action** orchestration: each multi-step action (e.g. `shoot()`) is a private
  `enum <Action>State` + a `switch` advanced inside `update()`. Expose `isXBusy()` /
  `isXCycleActive()` so opmodes can gate inputs.
- `update()` order each loop: update follower → fill `SubsystemData` → call every
  subsystem's `update()` → telemetry.

## Action system
- `core/vars/Action.java` enumerates high-level actions (used by auto steps).
- Keep orchestration in `Robot`, not in the opmodes. Opmodes call `robot.shoot()`,
  they don't sequence the blocker/intake/shooter themselves.

## TeleOp
- `BaseTeleOp extends OpMode` contains driving, button mapping, brake logic.
- Abstract hooks for per-alliance differences: `getAlliance()`, `getParkPose()`,
  `getResetPose()`. Per-alliance class overrides only those (mirror poses for BLUE).

## Auto
- `BaseAuto extends OpMode` drives the `AutoRoutine` step machine — do not edit per auto.
- An `AutoRoutine` subclass builds `steps` in its constructor via helpers:
  `move(path, speed)`, `shootSequence()`, `turnTo(rad, timeout)`, `waitUntil(cond)`,
  `waitMs(ms)`. Each `Step` has an `action` + a completion `BooleanSupplier`.
- Poses/paths/fractions go in `auto/constants/<Routine>Constants.java`.
