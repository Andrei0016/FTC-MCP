# `com.pedropathing.drivetrain`

_pedro-pathing 2.1.2 — 2 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class CustomDrivetrain

```java
public abstract class com.pedropathing.drivetrain.CustomDrivetrain extends com.pedropathing.drivetrain.Drivetrain {
  protected com.pedropathing.math.Vector lastTranslationalVector;
  protected com.pedropathing.math.Vector lastHeadingPower;
  protected com.pedropathing.math.Vector lastCorrectivePower;
  protected com.pedropathing.math.Vector lastPathingPower;
  protected double lastHeading;
  public com.pedropathing.drivetrain.CustomDrivetrain();
  public abstract void arcadeDrive(double, double, double);
  public double[] calculateDrive(com.pedropathing.math.Vector, com.pedropathing.math.Vector, com.pedropathing.math.Vector, double);
  protected boolean scaleDown(com.pedropathing.math.Vector, com.pedropathing.math.Vector, boolean);
  protected com.pedropathing.math.Vector scaledVector(com.pedropathing.math.Vector, com.pedropathing.math.Vector, boolean);
  public void runDrive(com.pedropathing.math.Vector, com.pedropathing.math.Vector, com.pedropathing.math.Vector, double, com.pedropathing.math.Vector);
  public void runDrive(double[]);
}
```

## class Drivetrain

```java
public abstract class com.pedropathing.drivetrain.Drivetrain {
  protected com.pedropathing.math.Vector[] vectors;
  protected double maxPowerScaling;
  protected boolean voltageCompensation;
  protected double nominalVoltage;
  public com.pedropathing.drivetrain.Drivetrain();
  public abstract double[] calculateDrive(com.pedropathing.math.Vector, com.pedropathing.math.Vector, com.pedropathing.math.Vector, double);
  public void setMaxPowerScaling(double);
  public double getMaxPowerScaling();
  public abstract void updateConstants();
  public abstract void breakFollowing();
  public abstract void runDrive(double[]);
  public void runDrive(com.pedropathing.math.Vector, com.pedropathing.math.Vector, com.pedropathing.math.Vector, double, com.pedropathing.math.Vector);
  public abstract void startTeleopDrive();
  public abstract void startTeleopDrive(boolean);
  public abstract double xVelocity();
  public abstract double yVelocity();
  public abstract void setXVelocity(double);
  public abstract void setYVelocity(double);
  public void useVoltageCompensation(boolean);
  public boolean isVoltageCompensation();
  public double getNominalVoltage();
  public void setNominalVoltage(double);
  public abstract double getVoltage();
  public abstract java.lang.String debugString();
}
```
