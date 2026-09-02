# Pedro Pathing

Docs: https://pedropathing.com/docs · A Bezier-curve path follower with odometry
localization. Package `com.pedropathing.*`.

> **Exact API (v2.1.2):** `ftc://sdk/pedro-pathing`, `sdk_search("...")`,
> `sdk_class("Follower")`. Pedro 2.x split into `com.pedropathing:core` (pure logic) +
> `com.pedropathing:ftc` (`FollowerBuilder`, localizers, drivetrains).

## Setup (Pedro 2.x)
- Keep a `pedroPathing/Constants.java` with your `FollowerConstants` (fluent setters:
  `.translationalPIDFCoefficients(...)`, `.mass(...)`, `.forwardZeroPowerAcceleration(...)`)
  plus the localizer + drivetrain constants (`PinpointConstants`, `MecanumConstants`, …).
- Build the follower with `com.pedropathing.ftc.FollowerBuilder`:
  ```java
  Follower follower = new FollowerBuilder(Constants.followerConstants, hardwareMap)
      .pinpointLocalizer(Constants.localizerConstants)
      .mecanumDrivetrain(Constants.driveConstants)
      .pathConstraints(Constants.pathConstraints)
      .build();
  ```
  (Older code used `Constants.createFollower(hardwareMap)` — that was Pedro 1.x.)
- Run the tuning opmodes to find the drive/heading/translational constants first.

## Core API (`com.pedropathing.follower.Follower`) — verified against 2.1.2
- `setStartingPose(Pose)` / `setPose(Pose)` / `setX/setY/setHeading`
- `pathBuilder()` → `.addPath(new BezierLine(p1, p2))` / `.addPath(new BezierCurve(...))`,
  `.setLinearHeadingInterpolation(a, b)` / `.setConstantHeadingInterpolation(h)` /
  `.setTangentHeadingInterpolation()`, `.addTemporalCallback(ms, Runnable)` /
  `.addParametricCallback(t, Runnable)` → `.build()` → `PathChain`
- `followPath(chain, holdEnd)` / `followPath(chain, maxPower, holdEnd)` — start following
- `update()` — call every loop; `pausePathFollowing()` / `resumePathFollowing()` / `breakFollowing()`
- status: `isBusy()`, `getPathCompletion()`, `atParametricEnd()`, `getCurrentTValue()`,
  `isRobotStuck()`, `getDistanceRemaining()`, `atPose(Pose, xTol, yTol, hTol)`,
  `getClosestPose()`
- pose: `getPose():Pose`, `getVelocity():com.pedropathing.math.Vector`, `getHeading()`,
  `getPoseHistory()`, `holdPoint(Pose)`
- TeleOp: `startTeleopDrive()` / `startTeleopDrive(useBrake)`, then
  `setTeleOpDrive(fwd, strafe, turn, robotCentric)`
- turns: `turnTo(rad)`, `turnToDegrees(deg)`, `turn(angle, isLeft)`, `isTurning()`
- speed: `setMaxPower(p)`, `setMaxPowerScaling(s)`

## Geometry
`com.pedropathing.geometry.Pose` — `getX() getY() getHeading()` (heading in radians),
`.mirror()` for the opposite alliance.

## How the reference repo uses it
- `Robot` creates the follower and calls `follower.update()` first each loop.
- `AutoRoutine.move(path, speed)` = `follower.setMaxPower(speed); follower.followPath(path, true)`;
  step completes when `!follower.isBusy() || follower.isRobotStuck()`.
- Paths/poses per routine live in `auto/constants/`.
