# `com.pedropathing.ftc`

_pedro-pathing 2.1.2 — 4 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class FTCCoordinates

```java
public final class com.pedropathing.ftc.FTCCoordinates extends java.lang.Enum<com.pedropathing.ftc.FTCCoordinates> implements com.pedropathing.geometry.CoordinateSystem {
  public static final com.pedropathing.ftc.FTCCoordinates INSTANCE;
  public static com.pedropathing.ftc.FTCCoordinates[] values();
  public static com.pedropathing.ftc.FTCCoordinates valueOf(java.lang.String);
  public com.pedropathing.geometry.Pose convertFromPedro(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose convertToPedro(com.pedropathing.geometry.Pose);
}
```

## class FollowerBuilder

```java
public class com.pedropathing.ftc.FollowerBuilder {
  public com.pedropathing.ftc.FollowerBuilder(com.pedropathing.follower.FollowerConstants, com.qualcomm.robotcore.hardware.HardwareMap);
  public com.pedropathing.ftc.FollowerBuilder setLocalizer(com.pedropathing.localization.Localizer);
  public com.pedropathing.ftc.FollowerBuilder driveEncoderLocalizer(com.pedropathing.ftc.localization.constants.DriveEncoderConstants);
  public com.pedropathing.ftc.FollowerBuilder OTOSLocalizer(com.pedropathing.ftc.localization.constants.OTOSConstants);
  public com.pedropathing.ftc.FollowerBuilder pinpointLocalizer(com.pedropathing.ftc.localization.constants.PinpointConstants);
  public com.pedropathing.ftc.FollowerBuilder threeWheelIMULocalizer(com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants);
  public com.pedropathing.ftc.FollowerBuilder threeWheelLocalizer(com.pedropathing.ftc.localization.constants.ThreeWheelConstants);
  public com.pedropathing.ftc.FollowerBuilder twoWheelLocalizer(com.pedropathing.ftc.localization.constants.TwoWheelConstants);
  public com.pedropathing.ftc.FollowerBuilder setDrivetrain(com.pedropathing.drivetrain.Drivetrain);
  public com.pedropathing.ftc.FollowerBuilder mecanumDrivetrain(com.pedropathing.ftc.drivetrains.MecanumConstants);
  public com.pedropathing.ftc.FollowerBuilder mecanumExDrivetrain(com.pedropathing.ftc.drivetrains.MecanumConstants);
  public com.pedropathing.ftc.FollowerBuilder swerveDrivetrain(com.pedropathing.ftc.drivetrains.SwerveConstants, com.pedropathing.ftc.drivetrains.SwervePod...);
  public com.pedropathing.ftc.FollowerBuilder pathConstraints(com.pedropathing.paths.PathConstraints);
  public com.pedropathing.follower.Follower build();
}
```

## class InvertedFTCCoordinates

```java
public final class com.pedropathing.ftc.InvertedFTCCoordinates extends java.lang.Enum<com.pedropathing.ftc.InvertedFTCCoordinates> implements com.pedropathing.geometry.CoordinateSystem {
  public static final com.pedropathing.ftc.InvertedFTCCoordinates INSTANCE;
  public static com.pedropathing.ftc.InvertedFTCCoordinates[] values();
  public static com.pedropathing.ftc.InvertedFTCCoordinates valueOf(java.lang.String);
  public com.pedropathing.geometry.Pose convertFromPedro(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose convertToPedro(com.pedropathing.geometry.Pose);
}
```

## class PoseConverter

```java
public class com.pedropathing.ftc.PoseConverter {
  public com.pedropathing.ftc.PoseConverter();
  public static org.firstinspires.ftc.robotcore.external.navigation.Pose2D poseToPose2D(com.pedropathing.geometry.Pose, com.pedropathing.geometry.CoordinateSystem);
  public static com.pedropathing.geometry.Pose pose2DToPose(org.firstinspires.ftc.robotcore.external.navigation.Pose2D, com.pedropathing.geometry.CoordinateSystem);
}
```
