# `com.pedropathing.localization`

_pedro-pathing 2.1.2 — 2 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## interface Localizer

```java
public interface com.pedropathing.localization.Localizer {
  public abstract com.pedropathing.geometry.Pose getPose();
  public abstract com.pedropathing.geometry.Pose getVelocity();
  public abstract com.pedropathing.math.Vector getVelocityVector();
  public abstract void setStartPose(com.pedropathing.geometry.Pose);
  public abstract void setPose(com.pedropathing.geometry.Pose);
  public abstract void update();
  public abstract double getTotalHeading();
  public abstract double getForwardMultiplier();
  public abstract double getLateralMultiplier();
  public abstract double getTurningMultiplier();
  public abstract void resetIMU() throws java.lang.InterruptedException;
  public abstract double getIMUHeading();
  public abstract boolean isNAN();
  public default void setX(double);
  public default void setY(double);
  public default void setHeading(double);
}
```

## class PoseTracker

```java
public class com.pedropathing.localization.PoseTracker {
  public com.pedropathing.localization.PoseTracker(com.pedropathing.localization.Localizer);
  public void update();
  public void setStartingPose(com.pedropathing.geometry.Pose);
  public void setCurrentPoseWithOffset(com.pedropathing.geometry.Pose);
  public void setXOffset(double);
  public void setYOffset(double);
  public void setHeadingOffset(double);
  public double getXOffset();
  public double getYOffset();
  public double getHeadingOffset();
  public com.pedropathing.geometry.Pose applyOffset(com.pedropathing.geometry.Pose);
  public void resetOffset();
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.geometry.Pose getRawPose();
  public void setPose(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose getPreviousPose();
  public com.pedropathing.geometry.Pose getDeltaPose();
  public com.pedropathing.math.Vector getVelocity();
  public double getAngularVelocity();
  public com.pedropathing.math.Vector getAcceleration();
  public void resetHeadingToIMU();
  public void resetHeadingToIMUWithOffsets();
  public double getNormalizedIMUHeading();
  public double getTotalHeading();
  public com.pedropathing.localization.Localizer getLocalizer();
  public double getIMUHeadingEstimate();
  public void resetIMU() throws java.lang.InterruptedException;
  public java.lang.String debugString();
}
```
