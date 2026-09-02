# `com.pedropathing`

_pedro-pathing 2.1.2 — 2 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class ErrorCalculator

```java
public class com.pedropathing.ErrorCalculator {
  public com.pedropathing.ErrorCalculator(com.pedropathing.follower.FollowerConstants);
  public void update(com.pedropathing.geometry.Pose, com.pedropathing.paths.Path, com.pedropathing.paths.PathChain, boolean, com.pedropathing.geometry.Pose, com.pedropathing.math.Vector, int, double, double, double, boolean);
  public com.pedropathing.math.Vector getTranslationalError(com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose);
  public com.pedropathing.math.Vector getTranslationalError();
  public double getHeadingError(double, double);
  public double getHeadingError();
  public double getDriveError();
  public double getRawDriveError();
  public double[] getDriveErrors();
  public void breakFollowing();
  public void setConstants(com.pedropathing.follower.FollowerConstants);
  public java.lang.String debugString();
}
```

## class VectorCalculator

```java
public class com.pedropathing.VectorCalculator {
  public com.pedropathing.math.Vector driveVector;
  public com.pedropathing.math.Vector headingVector;
  public com.pedropathing.math.Vector translationalVector;
  public com.pedropathing.math.Vector centripetalVector;
  public com.pedropathing.math.Vector correctiveVector;
  public com.pedropathing.math.Vector translationalError;
  public static double drivePIDFSwitch;
  public static double headingPIDFSwitch;
  public static double translationalPIDFSwitch;
  public static boolean useSecondaryDrivePID;
  public static boolean useSecondaryHeadingPID;
  public static boolean useSecondaryTranslationalPID;
  public com.pedropathing.control.PredictiveBrakingController predictiveBrakingController;
  public com.pedropathing.VectorCalculator(com.pedropathing.follower.FollowerConstants);
  public void updateConstants();
  public void update(boolean, boolean, boolean, boolean, boolean, int, double, boolean, double, com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose, com.pedropathing.math.Vector, com.pedropathing.paths.Path, com.pedropathing.paths.PathChain, double, com.pedropathing.math.Vector, double, double, double, boolean);
  public void breakFollowing();
  public void teleopUpdate();
  public com.pedropathing.math.Vector getDriveVector();
  public com.pedropathing.math.Vector getHeadingVector();
  public com.pedropathing.math.Vector getHeadingVector(double, com.pedropathing.geometry.Pose, double);
  public com.pedropathing.math.Vector getCorrectiveVector();
  public com.pedropathing.math.Vector getTranslationalCorrection();
  public com.pedropathing.math.Vector getTranslationalCorrection(com.pedropathing.math.Vector, com.pedropathing.geometry.Pose);
  public com.pedropathing.math.Vector getCentripetalForceCorrection();
  public void setTeleOpMovementVectors(double, double, double, boolean, double);
  public void setTeleOpMovementVectors(double, double, double);
  public void setTeleOpMovementVectors(double, double, double, boolean);
  public void calculateAveragedVelocityAndAcceleration();
  public boolean isTeleopDrive();
  public com.pedropathing.math.Vector getCentripetalVector();
  public com.pedropathing.math.Vector getTranslationalVector();
  public com.pedropathing.math.Vector getTeleopHeadingVector();
  public com.pedropathing.math.Vector getTeleopDriveVector();
  public com.pedropathing.math.Vector getTranslationalIntegralVector();
  public com.pedropathing.math.Vector getAverageAcceleration();
  public com.pedropathing.math.Vector getSecondaryTranslationalIntegralVector();
  public com.pedropathing.math.Vector getAveragePreviousVelocity();
  public com.pedropathing.math.Vector getAverageVelocity();
  public void setDrivePIDFCoefficients(com.pedropathing.control.FilteredPIDFCoefficients);
  public void setSecondaryDrivePIDFCoefficients(com.pedropathing.control.FilteredPIDFCoefficients);
  public void setHeadingPIDFCoefficients(com.pedropathing.control.PIDFCoefficients);
  public void setSecondaryHeadingPIDFCoefficients(com.pedropathing.control.PIDFCoefficients);
  public void setTranslationalPIDFCoefficients(com.pedropathing.control.PIDFCoefficients);
  public void setSecondaryTranslationalPIDFCoefficients(com.pedropathing.control.PIDFCoefficients);
  public void setConstants(com.pedropathing.follower.FollowerConstants);
  public java.lang.String debugString();
}
```
