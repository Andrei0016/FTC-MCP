# pedro-pathing 2.1.2 — API index

92 team-facing types across 15 packages. Read a package file for exact signatures; use the `sdk_search` / `sdk_class` tools to dig in.

## `com.pedropathing`  ·  [com_pedropathing.md](com_pedropathing.md)

- class `ErrorCalculator`
- class `VectorCalculator`

## `com.pedropathing.control`  ·  [com_pedropathing_control.md](com_pedropathing_control.md)

- class `FilteredPIDFCoefficients`
- class `FilteredPIDFController`
- class `KalmanFilter`
- class `KalmanFilterParameters`
- class `LowPassFilter`
- interface `NoiseFilter`
- interface `PIDFCoefficientSupplier`
- class `PIDFCoefficientSupplier$PIDFPiecewiseNode`
- class `PIDFCoefficients`
- class `PIDFController`
- class `PredictiveBrakingCoefficients`
- class `PredictiveBrakingController`

## `com.pedropathing.drivetrain`  ·  [com_pedropathing_drivetrain.md](com_pedropathing_drivetrain.md)

- class `CustomDrivetrain`
- class `Drivetrain`

## `com.pedropathing.follower`  ·  [com_pedropathing_follower.md](com_pedropathing_follower.md)

- class `Follower`
- class `FollowerConstants`

## `com.pedropathing.ftc`  ·  [com_pedropathing_ftc.md](com_pedropathing_ftc.md)

- class `FTCCoordinates`
- class `FollowerBuilder`
- class `InvertedFTCCoordinates`
- class `PoseConverter`

## `com.pedropathing.ftc.drivetrains`  ·  [com_pedropathing_ftc_drivetrains.md](com_pedropathing_ftc_drivetrains.md)

- class `CoaxialPod`
- class `Mecanum`
- class `MecanumConstants`
- class `MecanumEx`
- class `Swerve`
- class `SwerveBuilder`
- class `SwerveConstants`
- class `SwerveConstants$ZeroPowerBehavior`
- interface `SwervePod`

## `com.pedropathing.ftc.localization`  ·  [com_pedropathing_ftc_localization.md](com_pedropathing_ftc_localization.md)

- interface `CustomIMU`
- class `Encoder`
- class `RevHubIMU`

## `com.pedropathing.ftc.localization.constants`  ·  [com_pedropathing_ftc_localization_constants.md](com_pedropathing_ftc_localization_constants.md)

- class `DriveEncoderConstants`
- class `OTOSConstants`
- class `OctoQuadConstants`
- class `PinpointConstants`
- class `ThreeWheelConstants`
- class `ThreeWheelIMUConstants`
- class `TwoWheelConstants`

## `com.pedropathing.ftc.localization.localizers`  ·  [com_pedropathing_ftc_localization_localizers.md](com_pedropathing_ftc_localization_localizers.md)

- class `DriveEncoderLocalizer`
- class `OTOSLocalizer`
- class `OctoQuadLocalizer`
- interface `OctoQuadLocalizer$DataSupplier`
- class `OctoQuadLocalizer$InitMode`
- class `PinpointLocalizer`
- class `ThreeWheelIMULocalizer`
- class `ThreeWheelLocalizer`
- class `TwoWheelLocalizer`

## `com.pedropathing.geometry`  ·  [com_pedropathing_geometry.md](com_pedropathing_geometry.md)

- class `BezierCurve`
- class `BezierLine`
- class `BezierPoint`
- class `CharacteristicMatrixSupplier`
- interface `CoordinateSystem`
- interface `Curve`
- class `CustomCurve`
- class `FinetunedBezierCurve`
- class `FinetunedBezierLine`
- interface `FuturePose`
- class `PedroCoordinates`
- class `Pose`
- class `TVector`

## `com.pedropathing.localization`  ·  [com_pedropathing_localization.md](com_pedropathing_localization.md)

- interface `Localizer`
- class `PoseTracker`

## `com.pedropathing.math`  ·  [com_pedropathing_math.md](com_pedropathing_math.md)

- class `AbstractBijectiveMap`
- class `AbstractBijectiveMap$NumericBijectiveMap`
- class `AbstractBijectiveMap$NumericBijectiveMap$InterpolatableMap`
- interface `BijectiveMap`
- class `Kinematics`
- class `MathFunctions`
- class `Matrix`
- class `Vector`

## `com.pedropathing.paths`  ·  [com_pedropathing_paths.md](com_pedropathing_paths.md)

- interface `HeadingInterpolator`
- interface `HeadingInterpolator$FutureDouble`
- class `HeadingInterpolator$PiecewiseNode`
- class `Path`
- class `PathBuilder`
- interface `PathBuilder$CallbackCondition`
- class `PathChain`
- class `PathChain$DecelerationType`
- class `PathChain$PathT`
- class `PathConstraints`
- class `PathPoint`

## `com.pedropathing.paths.callbacks`  ·  [com_pedropathing_paths_callbacks.md](com_pedropathing_paths_callbacks.md)

- class `ParametricCallback`
- interface `PathCallback`
- class `PoseCallback`
- class `TemporalCallback`

## `com.pedropathing.util`  ·  [com_pedropathing_util.md](com_pedropathing_util.md)

- class `FiniteRunAction`
- class `NanoTimer`
- class `PoseHistory`
- class `Timer`
