# `com.pedropathing.ftc.localization.localizers`

_pedro-pathing 2.1.2 — 9 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class DriveEncoderLocalizer

```java
public class com.pedropathing.ftc.localization.localizers.DriveEncoderLocalizer implements com.pedropathing.localization.Localizer {
  public static double FORWARD_TICKS_TO_INCHES;
  public static double STRAFE_TICKS_TO_INCHES;
  public static double TURN_TICKS_TO_RADIANS;
  public static double ROBOT_WIDTH;
  public static double ROBOT_LENGTH;
  public com.pedropathing.ftc.localization.localizers.DriveEncoderLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.DriveEncoderConstants);
  public com.pedropathing.ftc.localization.localizers.DriveEncoderLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.DriveEncoderConstants, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getVelocity();
  public com.pedropathing.math.Vector getVelocityVector();
  public void setStartPose(com.pedropathing.geometry.Pose);
  public void setPrevRotationMatrix(double);
  public void setPose(com.pedropathing.geometry.Pose);
  public void update();
  public void updateEncoders();
  public void resetEncoders();
  public com.pedropathing.math.Matrix getRobotDeltas();
  public double getTotalHeading();
  public double getForwardMultiplier();
  public double getLateralMultiplier();
  public double getTurningMultiplier();
  public void resetIMU();
  public double getIMUHeading();
  public boolean isNAN();
}
```

## class OTOSLocalizer

```java
public class com.pedropathing.ftc.localization.localizers.OTOSLocalizer implements com.pedropathing.localization.Localizer {
  public com.pedropathing.ftc.localization.localizers.OTOSLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.OTOSConstants);
  public com.pedropathing.ftc.localization.localizers.OTOSLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.OTOSConstants, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getVelocity();
  public com.pedropathing.math.Vector getVelocityVector();
  public void setStartPose(com.pedropathing.geometry.Pose);
  public void setPose(com.pedropathing.geometry.Pose);
  public void update();
  public void resetOTOS();
  public double getTotalHeading();
  public double getForwardMultiplier();
  public double getLateralMultiplier();
  public double getTurningMultiplier();
  public void resetIMU();
  public double getIMUHeading();
  public boolean isNAN();
}
```

## class OctoQuadLocalizer

```java
public class com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer implements com.pedropathing.localization.Localizer {
  protected final com.qualcomm.hardware.digitalchickenlabs.OctoQuad octoQuad;
  protected final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock localizerData;
  protected int headingWraps;
  protected double integratedHeading;
  protected float lastNormalizedHeading;
  protected com.pedropathing.geometry.Pose currentVelocity;
  protected com.pedropathing.geometry.Pose currentPose;
  protected com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.DataSupplier externalDataSupplier;
  public void setExternalDataSupplier(com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.DataSupplier);
  public com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.OctoQuadConstants, com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.InitMode);
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getVelocity();
  public com.pedropathing.math.Vector getVelocityVector();
  public void setStartPose(com.pedropathing.geometry.Pose);
  public void setPose(com.pedropathing.geometry.Pose);
  protected void updateFromHardware();
  protected void updateFromExternalSupplier();
  protected void updateInternal();
  public void update();
  public double getTotalHeading();
  public double getForwardMultiplier();
  public double getLateralMultiplier();
  public double getTurningMultiplier();
  public void resetIMU();
  public double getIMUHeading();
  public boolean isNAN();
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad getOctoQuad();
}
```

## interface OctoQuadLocalizer.DataSupplier

```java
public interface com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.DataSupplier {
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock onDataRequest();
}
```

## class OctoQuadLocalizer.InitMode

```java
public final class com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.InitMode extends java.lang.Enum<com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.InitMode> {
  public static final com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.InitMode INITIALIZE_OCTOQUAD;
  public static final com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.InitMode ASSUME_EXTERNAL_INITIALIZATION;
  public static com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.InitMode[] values();
  public static com.pedropathing.ftc.localization.localizers.OctoQuadLocalizer.InitMode valueOf(java.lang.String);
}
```

## class PinpointLocalizer

```java
public class com.pedropathing.ftc.localization.localizers.PinpointLocalizer implements com.pedropathing.localization.Localizer {
  public com.pedropathing.ftc.localization.localizers.PinpointLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.PinpointConstants);
  public com.pedropathing.ftc.localization.localizers.PinpointLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.PinpointConstants, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getVelocity();
  public com.pedropathing.math.Vector getVelocityVector();
  public void setStartPose(com.pedropathing.geometry.Pose);
  public void setPose(com.pedropathing.geometry.Pose);
  public void update();
  public double getTotalHeading();
  public double getForwardMultiplier();
  public double getLateralMultiplier();
  public double getTurningMultiplier();
  public void resetIMU();
  public double getIMUHeading();
  public void recalibrate();
  public boolean isNAN();
  public com.qualcomm.hardware.gobilda.GoBildaPinpointDriver getPinpoint();
  public void setX(double);
  public void setY(double);
  public void setHeading(double);
}
```

## class ThreeWheelIMULocalizer

```java
public class com.pedropathing.ftc.localization.localizers.ThreeWheelIMULocalizer implements com.pedropathing.localization.Localizer {
  public final com.pedropathing.ftc.localization.CustomIMU imu;
  public static double FORWARD_TICKS_TO_INCHES;
  public static double STRAFE_TICKS_TO_INCHES;
  public static double TURN_TICKS_TO_RADIANS;
  public static boolean useIMU;
  public com.pedropathing.ftc.localization.localizers.ThreeWheelIMULocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants);
  public com.pedropathing.ftc.localization.localizers.ThreeWheelIMULocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.ThreeWheelIMUConstants, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getVelocity();
  public com.pedropathing.math.Vector getVelocityVector();
  public void setStartPose(com.pedropathing.geometry.Pose);
  public void setPrevRotationMatrix(double);
  public void setPose(com.pedropathing.geometry.Pose);
  public void update();
  public void updateEncoders();
  public void resetEncoders();
  public com.pedropathing.math.Matrix getRobotDeltas();
  public double getTotalHeading();
  public double getForwardMultiplier();
  public double getLateralMultiplier();
  public double getTurningMultiplier();
  public void resetIMU();
  public double getIMUHeading();
  public boolean isNAN();
}
```

## class ThreeWheelLocalizer

```java
public class com.pedropathing.ftc.localization.localizers.ThreeWheelLocalizer implements com.pedropathing.localization.Localizer {
  public static double FORWARD_TICKS_TO_INCHES;
  public static double STRAFE_TICKS_TO_INCHES;
  public static double TURN_TICKS_TO_RADIANS;
  public com.pedropathing.ftc.localization.localizers.ThreeWheelLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.ThreeWheelConstants);
  public com.pedropathing.ftc.localization.localizers.ThreeWheelLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.ThreeWheelConstants, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getVelocity();
  public com.pedropathing.math.Vector getVelocityVector();
  public void setStartPose(com.pedropathing.geometry.Pose);
  public void setPrevRotationMatrix(double);
  public void setPose(com.pedropathing.geometry.Pose);
  public void update();
  public void updateEncoders();
  public void resetEncoders();
  public com.pedropathing.math.Matrix getRobotDeltas();
  public double getTotalHeading();
  public double getForwardMultiplier();
  public double getLateralMultiplier();
  public double getTurningMultiplier();
  public void resetIMU();
  public double getIMUHeading();
  public boolean isNAN();
}
```

## class TwoWheelLocalizer

```java
public class com.pedropathing.ftc.localization.localizers.TwoWheelLocalizer implements com.pedropathing.localization.Localizer {
  public static double FORWARD_TICKS_TO_INCHES;
  public static double STRAFE_TICKS_TO_INCHES;
  public com.pedropathing.ftc.localization.localizers.TwoWheelLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.TwoWheelConstants);
  public com.pedropathing.ftc.localization.localizers.TwoWheelLocalizer(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.localization.constants.TwoWheelConstants, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getVelocity();
  public com.pedropathing.math.Vector getVelocityVector();
  public void setStartPose(com.pedropathing.geometry.Pose);
  public void setPrevRotationMatrix(double);
  public void setPose(com.pedropathing.geometry.Pose);
  public void update();
  public void updateEncoders();
  public void resetEncoders();
  public com.pedropathing.math.Matrix getRobotDeltas();
  public double getTotalHeading();
  public double getForwardMultiplier();
  public double getLateralMultiplier();
  public double getTurningMultiplier();
  public void resetIMU();
  public double getIMUHeading();
  public boolean isNAN();
}
```
