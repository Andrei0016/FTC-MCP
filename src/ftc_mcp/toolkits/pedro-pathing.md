# Pedro Pathing

Docs: https://pedropathing.com/docs · A Bezier-curve path follower with odometry
localization. Package `com.pedropathing.*`.

## Setup
- `pedroPathing/Constants.java` holds `FollowerConstants`, `PathConstraints`, localizer
  and drivetrain config. `Constants.createFollower(hardwareMap)` returns a `Follower`.
- Run the tuning opmodes (`pedroPathing/Tuning.java`) to find the drive/heading/translation
  constants before trusting paths.

## Core API (`com.pedropathing.follower.Follower`)
- `follower.setStartingPose(Pose)` / `setPose(Pose)`
- `follower.pathBuilder()` → add `BezierLine` / `BezierCurve`, `setLinearHeadingInterpolation`,
  `setConstantHeadingInterpolation` → `.build()` returns a `PathChain`
- `follower.followPath(pathChain, holdEnd)` — start following
- `follower.update()` — call every loop
- `follower.isBusy()`, `getPathCompletion()`, `isRobotStuck()`, `getPose()`,
  `getVelocity()` (a `com.pedropathing.math.Vector`)
- TeleOp drive: `follower.startTeleopDrive()`, then `setTeleOpDrive(fwd, strafe, turn, robotCentric)`
- `follower.turnTo(headingRadians)`, `follower.isTurning()`

## Geometry
`com.pedropathing.geometry.Pose` — `getX() getY() getHeading()` (heading in radians),
`.mirror()` for the opposite alliance.

## How the reference repo uses it
- `Robot` creates the follower and calls `follower.update()` first each loop.
- `AutoRoutine.move(path, speed)` = `follower.setMaxPower(speed); follower.followPath(path, true)`;
  step completes when `!follower.isBusy() || follower.isRobotStuck()`.
- Paths/poses per routine live in `auto/constants/`.
