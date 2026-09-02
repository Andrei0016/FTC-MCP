# `com.pedropathing.ftc.localization.constants`

_pedro-pathing 2.1.2 — 7 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class DriveEncoderConstants

```java
public class com.pedropathing.ftc.localization.constants.DriveEncoderConstants {
  public double forwardTicksToInches;
  public double strafeTicksToInches;
  public double turnTicksToInches;
  public double robot_Width;
  public double robot_Length;
  public double leftFrontEncoderDirection;
  public double rightFrontEncoderDirection;
  public double leftRearEncoderDirection;
  public double rightRearEncoderDirection;
  public java.lang.String leftFrontMotorName;
  public java.lang.String leftRearMotorName;
  public java.lang.String rightFrontMotorName;
  public java.lang.String rightRearMotorName;
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants();
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants forwardTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants strafeTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants turnTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants robotWidth(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants robotLength(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants leftFrontEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants rightFrontEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants leftRearEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants rightRearEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants leftFrontMotorName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants leftRearMotorName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants rightFrontMotorName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.DriveEncoderConstants rightRearMotorName(java.lang.String);
  public void defaults();
}
```

## class OTOSConstants

```java
public class com.pedropathing.ftc.localization.constants.OTOSConstants {
  public java.lang.String hardwareMapName;
  public org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit linearUnit;
  public org.firstinspires.ftc.robotcore.external.navigation.AngleUnit angleUnit;
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D offset;
  public double linearScalar;
  public double angularScalar;
  public com.pedropathing.ftc.localization.constants.OTOSConstants();
  public com.pedropathing.ftc.localization.constants.OTOSConstants hardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.OTOSConstants linearUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public com.pedropathing.ftc.localization.constants.OTOSConstants angleUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public com.pedropathing.ftc.localization.constants.OTOSConstants offset(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D);
  public com.pedropathing.ftc.localization.constants.OTOSConstants linearScalar(double);
  public com.pedropathing.ftc.localization.constants.OTOSConstants angularScalar(double);
  public void defaults();
}
```

## class OctoQuadConstants

```java
public class com.pedropathing.ftc.localization.constants.OctoQuadConstants {
  public int DEADWHEEL_PORT_X;
  public int DEADWHEEL_PORT_Y;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection DEADWHEEL_X_DIR;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection DEADWHEEL_Y_DIR;
  public float X_TICKS_PER_MM;
  public float Y_TICKS_PER_MM;
  public float TCP_OFFSET_X_MM;
  public float TCP_OFFSET_Y_MM;
  public float IMU_SCALAR;
  public int VEL_INTVL_MS;
  public java.lang.String hardwareMapName;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode I2C_RECOVERY_MODE;
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants();
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants deadwheelPortX(int);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants deadwheelPortY(int);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants deadwheelXDir(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants deadwheelYDir(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants deadwheelXTicksPerMM(float);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants deadwheelYTicksPerMM(float);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants tcpOffsetXMM(float);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants tcpOffsetYMM(float);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants imuScalar(float);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants velocityIntervalMs(int);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants i2cRecoveryMode(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode);
  public com.pedropathing.ftc.localization.constants.OctoQuadConstants name(java.lang.String);
  public void defaults();
}
```

## class PinpointConstants

```java
public class com.pedropathing.ftc.localization.constants.PinpointConstants {
  public double forwardPodY;
  public double strafePodX;
  public org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit distanceUnit;
  public java.lang.String hardwareMapName;
  public java.util.OptionalDouble yawScalar;
  public com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods encoderResolution;
  public java.util.OptionalDouble customEncoderResolution;
  public com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection forwardEncoderDirection;
  public com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection strafeEncoderDirection;
  public com.pedropathing.ftc.localization.constants.PinpointConstants();
  public com.pedropathing.ftc.localization.constants.PinpointConstants forwardPodY(double);
  public com.pedropathing.ftc.localization.constants.PinpointConstants strafePodX(double);
  public com.pedropathing.ftc.localization.constants.PinpointConstants distanceUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public com.pedropathing.ftc.localization.constants.PinpointConstants hardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.PinpointConstants yawScalar(double);
  public com.pedropathing.ftc.localization.constants.PinpointConstants encoderResolution(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods);
  public com.pedropathing.ftc.localization.constants.PinpointConstants customEncoderResolution(double);
  public com.pedropathing.ftc.localization.constants.PinpointConstants forwardEncoderDirection(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection);
  public com.pedropathing.ftc.localization.constants.PinpointConstants strafeEncoderDirection(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection);
  public void defaults();
}
```

## class ThreeWheelConstants

```java
public class com.pedropathing.ftc.localization.constants.ThreeWheelConstants {
  public double forwardTicksToInches;
  public double strafeTicksToInches;
  public double turnTicksToInches;
  public double leftPodY;
  public double rightPodY;
  public double strafePodX;
  public java.lang.String leftEncoder_HardwareMapName;
  public java.lang.String rightEncoder_HardwareMapName;
  public java.lang.String strafeEncoder_HardwareMapName;
  public double leftEncoderDirection;
  public double rightEncoderDirection;
  public double strafeEncoderDirection;
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants();
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants forwardTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants strafeTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants turnTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants leftPodY(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants rightPodY(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants strafePodX(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants leftEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants rightEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants strafeEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants leftEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants rightEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelConstants strafeEncoderDirection(double);
  public void defaults();
}
```

## class ThreeWheelIMUConstants

```java
public class com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants {
  public double forwardTicksToInches;
  public double strafeTicksToInches;
  public double turnTicksToInches;
  public double leftPodY;
  public double rightPodY;
  public double strafePodX;
  public java.lang.String IMU_HardwareMapName;
  public java.lang.String leftEncoder_HardwareMapName;
  public java.lang.String rightEncoder_HardwareMapName;
  public java.lang.String strafeEncoder_HardwareMapName;
  public com.qualcomm.hardware.rev.RevHubOrientationOnRobot IMU_Orientation;
  public double leftEncoderDirection;
  public double rightEncoderDirection;
  public double strafeEncoderDirection;
  public com.pedropathing.ftc.localization.CustomIMU imu;
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants();
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants forwardTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants strafeTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants turnTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants leftPodY(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants rightPodY(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants strafePodX(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants IMU_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants leftEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants rightEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants strafeEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants IMU_Orientation(com.qualcomm.hardware.rev.RevHubOrientationOnRobot);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants leftEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants rightEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants strafeEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants customIMU(com.pedropathing.ftc.localization.CustomIMU);
  public void defaults();
}
```

## class TwoWheelConstants

```java
public class com.pedropathing.ftc.localization.constants.TwoWheelConstants {
  public double forwardTicksToInches;
  public double strafeTicksToInches;
  public double forwardPodY;
  public double strafePodX;
  public java.lang.String IMU_HardwareMapName;
  public java.lang.String forwardEncoder_HardwareMapName;
  public java.lang.String strafeEncoder_HardwareMapName;
  public com.qualcomm.hardware.rev.RevHubOrientationOnRobot IMU_Orientation;
  public double forwardEncoderDirection;
  public double strafeEncoderDirection;
  public com.pedropathing.ftc.localization.CustomIMU imu;
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants();
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants forwardTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants strafeTicksToInches(double);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants forwardPodY(double);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants strafePodX(double);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants IMU_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants forwardEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants strafeEncoder_HardwareMapName(java.lang.String);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants IMU_Orientation(com.qualcomm.hardware.rev.RevHubOrientationOnRobot);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants forwardEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants strafeEncoderDirection(double);
  public com.pedropathing.ftc.localization.constants.TwoWheelConstants customIMU(com.pedropathing.ftc.localization.CustomIMU);
  public void defaults();
}
```
