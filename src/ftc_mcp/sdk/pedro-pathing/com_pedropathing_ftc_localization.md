# `com.pedropathing.ftc.localization`

_pedro-pathing 2.1.2 — 3 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## interface CustomIMU

```java
public interface com.pedropathing.ftc.localization.CustomIMU {
  public abstract void initialize(com.qualcomm.robotcore.hardware.HardwareMap, java.lang.String, com.qualcomm.hardware.rev.RevHubOrientationOnRobot);
  public abstract double getHeading();
  public abstract void resetYaw();
}
```

## class Encoder

```java
public class com.pedropathing.ftc.localization.Encoder {
  public static final double FORWARD = 1.0d;
  public static final double REVERSE = -1.0d;
  public com.pedropathing.ftc.localization.Encoder(com.qualcomm.robotcore.hardware.DcMotorEx);
  public void setDirection(double);
  public void reset();
  public void update();
  public double getMultiplier();
  public double getDeltaPosition();
}
```

## class RevHubIMU

```java
public class com.pedropathing.ftc.localization.RevHubIMU implements com.pedropathing.ftc.localization.CustomIMU {
  public com.pedropathing.ftc.localization.RevHubIMU();
  public void initialize(com.qualcomm.robotcore.hardware.HardwareMap, java.lang.String, com.qualcomm.hardware.rev.RevHubOrientationOnRobot);
  public double getHeading();
  public void resetYaw();
}
```
