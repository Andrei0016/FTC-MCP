# `com.pedropathing.ftc.drivetrains`

_pedro-pathing 2.1.2 — 9 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class CoaxialPod

```java
public class com.pedropathing.ftc.drivetrains.CoaxialPod implements com.pedropathing.ftc.drivetrains.SwervePod {
  public com.pedropathing.ftc.drivetrains.CoaxialPod(com.qualcomm.robotcore.hardware.HardwareMap, java.lang.String, java.lang.String, java.lang.String, com.pedropathing.control.PIDFCoefficients, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction, double, com.pedropathing.geometry.Pose, double, double, boolean);
  public com.pedropathing.geometry.Pose getOffset();
  public double getAngle();
  public void setServoPower(double);
  public void setMotorPower(double);
  public void setToFloat();
  public void setToBreak();
  public void setMotorToFloat();
  public void setMotorToBreak();
  public boolean isEncoderReversed();
  public double adjustThetaForEncoder(double);
  public void move(double, double, boolean);
  public double getAngleAfterOffsetRad();
  public double getRawAngleRad();
  public double getOffsetAngleRad();
  public void setMotorCachingThreshold(double);
  public void setServoCachingThreshold(double);
  public java.lang.String debugString();
}
```

## class Mecanum

```java
public class com.pedropathing.ftc.drivetrains.Mecanum extends com.pedropathing.drivetrain.Drivetrain {
  public com.pedropathing.ftc.drivetrains.MecanumConstants constants;
  public com.pedropathing.ftc.drivetrains.Mecanum(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.drivetrains.MecanumConstants);
  public void updateConstants();
  public double[] calculateDrive(com.pedropathing.math.Vector, com.pedropathing.math.Vector, com.pedropathing.math.Vector, double);
  public void breakFollowing();
  public void runDrive(double[]);
  public void startTeleopDrive();
  public void startTeleopDrive(boolean);
  public void getAndRunDrivePowers(com.pedropathing.math.Vector, com.pedropathing.math.Vector, com.pedropathing.math.Vector, double);
  public double xVelocity();
  public double yVelocity();
  public void setXVelocity(double);
  public void setYVelocity(double);
  public double getStaticFrictionCoefficient();
  public double getVoltage();
  public java.lang.String debugString();
  public java.util.List<com.qualcomm.robotcore.hardware.DcMotorEx> getMotors();
}
```

## class MecanumConstants

```java
public class com.pedropathing.ftc.drivetrains.MecanumConstants {
  public double xVelocity;
  public double yVelocity;
  public com.pedropathing.math.Vector frontLeftVector;
  public double maxPower;
  public java.lang.String leftFrontMotorName;
  public java.lang.String leftRearMotorName;
  public java.lang.String rightFrontMotorName;
  public java.lang.String rightRearMotorName;
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction leftFrontMotorDirection;
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction leftRearMotorDirection;
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction rightFrontMotorDirection;
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction rightRearMotorDirection;
  public double motorCachingThreshold;
  public boolean useBrakeModeInTeleOp;
  public boolean useVoltageCompensation;
  public double nominalVoltage;
  public double staticFrictionCoefficient;
  public com.pedropathing.ftc.drivetrains.MecanumConstants();
  public com.pedropathing.ftc.drivetrains.MecanumConstants xVelocity(double);
  public com.pedropathing.ftc.drivetrains.MecanumConstants yVelocity(double);
  public com.pedropathing.ftc.drivetrains.MecanumConstants maxPower(double);
  public com.pedropathing.ftc.drivetrains.MecanumConstants leftFrontMotorName(java.lang.String);
  public com.pedropathing.ftc.drivetrains.MecanumConstants leftRearMotorName(java.lang.String);
  public com.pedropathing.ftc.drivetrains.MecanumConstants rightFrontMotorName(java.lang.String);
  public com.pedropathing.ftc.drivetrains.MecanumConstants rightRearMotorName(java.lang.String);
  public com.pedropathing.ftc.drivetrains.MecanumConstants leftFrontMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.pedropathing.ftc.drivetrains.MecanumConstants leftRearMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.pedropathing.ftc.drivetrains.MecanumConstants rightFrontMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.pedropathing.ftc.drivetrains.MecanumConstants rightRearMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.pedropathing.ftc.drivetrains.MecanumConstants motorCachingThreshold(double);
  public com.pedropathing.ftc.drivetrains.MecanumConstants useBrakeModeInTeleOp(boolean);
  public com.pedropathing.ftc.drivetrains.MecanumConstants useVoltageCompensation(boolean);
  public com.pedropathing.ftc.drivetrains.MecanumConstants nominalVoltage(double);
  public com.pedropathing.ftc.drivetrains.MecanumConstants staticFrictionCoefficient(double);
  public double getXVelocity();
  public void setXVelocity(double);
  public double getYVelocity();
  public void setYVelocity(double);
  public com.pedropathing.math.Vector getFrontLeftVector();
  public void setFrontLeftVector(com.pedropathing.math.Vector);
  public double getMaxPower();
  public void setMaxPower(double);
  public java.lang.String getLeftFrontMotorName();
  public void setLeftFrontMotorName(java.lang.String);
  public java.lang.String getLeftRearMotorName();
  public void setLeftRearMotorName(java.lang.String);
  public java.lang.String getRightFrontMotorName();
  public void setRightFrontMotorName(java.lang.String);
  public java.lang.String getRightRearMotorName();
  public void setRightRearMotorName(java.lang.String);
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getLeftFrontMotorDirection();
  public void setLeftFrontMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getLeftRearMotorDirection();
  public void setLeftRearMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getRightFrontMotorDirection();
  public void setRightFrontMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getRightRearMotorDirection();
  public void setRightRearMotorDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public double getMotorCachingThreshold();
  public void setMotorCachingThreshold(double);
  public boolean isUseBrakeModeInTeleOp();
  public void setUseBrakeModeInTeleOp(boolean);
  public void defaults();
}
```

## class MecanumEx

```java
public class com.pedropathing.ftc.drivetrains.MecanumEx extends com.pedropathing.drivetrain.CustomDrivetrain {
  public com.pedropathing.ftc.drivetrains.MecanumConstants constants;
  public com.pedropathing.ftc.drivetrains.MecanumEx(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.drivetrains.MecanumConstants);
  public void arcadeDrive(double, double, double);
  public void updateConstants();
  public void breakFollowing();
  public void startTeleopDrive();
  public void startTeleopDrive(boolean);
  public void getAndRunDrivePowers(com.pedropathing.math.Vector, com.pedropathing.math.Vector, com.pedropathing.math.Vector, double, com.pedropathing.math.Vector);
  public double xVelocity();
  public double yVelocity();
  public void setXVelocity(double);
  public void setYVelocity(double);
  public double getStaticFrictionCoefficient();
  public double getVoltage();
  public java.lang.String debugString();
  public java.util.List<com.qualcomm.robotcore.hardware.DcMotorEx> getMotors();
}
```

## class Swerve

```java
public class com.pedropathing.ftc.drivetrains.Swerve extends com.pedropathing.drivetrain.CustomDrivetrain {
  protected double lastHeading;
  public com.pedropathing.ftc.drivetrains.Swerve(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.drivetrains.SwerveConstants, com.pedropathing.ftc.drivetrains.SwervePod...);
  public void arcadeDrive(double, double, double);
  public void updateConstants();
  public void breakFollowing();
  public void startTeleopDrive();
  public void startTeleopDrive(boolean);
  public double xVelocity();
  public double yVelocity();
  public void setXVelocity(double);
  public void setYVelocity(double);
  public double getStaticFrictionCoefficient();
  public double getVoltage();
  public java.lang.String debugString();
}
```

## class SwerveBuilder

```java
public class com.pedropathing.ftc.drivetrains.SwerveBuilder {
  public com.pedropathing.ftc.drivetrains.SwerveBuilder(com.qualcomm.robotcore.hardware.HardwareMap, com.pedropathing.ftc.drivetrains.SwerveConstants);
  public com.pedropathing.ftc.drivetrains.SwerveBuilder addPod(com.pedropathing.ftc.drivetrains.SwervePod);
  public com.pedropathing.ftc.drivetrains.Swerve build();
}
```

## class SwerveConstants

```java
public class com.pedropathing.ftc.drivetrains.SwerveConstants {
  public double xVelocity;
  public double yVelocity;
  public boolean useBrakeModeInTeleOp;
  public double maxPower;
  public boolean useVoltageCompensation;
  public double nominalVoltage;
  public double staticFrictionCoefficient;
  public double epsilon;
  public com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior zeroPowerBehavior;
  public com.pedropathing.ftc.drivetrains.SwerveConstants();
  public com.pedropathing.ftc.drivetrains.SwerveConstants velocity(double);
  public com.pedropathing.ftc.drivetrains.SwerveConstants xVelocity(double);
  public com.pedropathing.ftc.drivetrains.SwerveConstants yVelocity(double);
  public com.pedropathing.ftc.drivetrains.SwerveConstants useBrakeModeInTeleOp(boolean);
  public com.pedropathing.ftc.drivetrains.SwerveConstants maxPower(double);
  public com.pedropathing.ftc.drivetrains.SwerveConstants useVoltageCompensation(boolean);
  public com.pedropathing.ftc.drivetrains.SwerveConstants nominalVoltage(double);
  public com.pedropathing.ftc.drivetrains.SwerveConstants staticFrictionCoefficient(double);
  public com.pedropathing.ftc.drivetrains.SwerveConstants epsilon(double);
  public com.pedropathing.ftc.drivetrains.SwerveConstants zeroPowerBehavior(com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior);
  public double getVelocity();
  public double getXVelocity();
  public double getYVelocity();
  public boolean getUseBrakeModeInTeleOp();
  public double getMaxPower();
  public boolean getUseVoltageCompensation();
  public double getNominalVoltage();
  public double getStaticFrictionCoefficient();
  public double getEpsilon();
  public com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior getZeroPowerBehavior();
  public void setVelocity(double);
  public void setXVelocity(double);
  public void setYVelocity(double);
  public void setUseBrakeModeInTeleOp(boolean);
  public void setMaxPower(double);
  public void setUseVoltageCompensation(boolean);
  public void setNominalVoltage(double);
  public void setStaticFrictionCoefficient(double);
  public void setEpsilon(double);
  public void setZeroPowerBehavior(com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior);
  public void defaults();
}
```

## class SwerveConstants.ZeroPowerBehavior

```java
public final class com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior extends java.lang.Enum<com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior> {
  public static final com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior X_LOCK;
  public static final com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior IGNORE_ANGLE_CHANGES;
  public static com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior[] values();
  public static com.pedropathing.ftc.drivetrains.SwerveConstants.ZeroPowerBehavior valueOf(java.lang.String);
}
```

## interface SwervePod

```java
public interface com.pedropathing.ftc.drivetrains.SwervePod {
  public abstract com.pedropathing.geometry.Pose getOffset();
  public abstract double getAngle();
  public abstract double adjustThetaForEncoder(double);
  public abstract void move(double, double, boolean);
  public abstract void setToFloat();
  public abstract void setToBreak();
  public abstract java.lang.String debugString();
}
```
