# `com.pedropathing.paths`

_pedro-pathing 2.1.2 — 11 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## interface HeadingInterpolator

```java
public interface com.pedropathing.paths.HeadingInterpolator {
  public static final com.pedropathing.paths.HeadingInterpolator tangent;
  public abstract double interpolate(com.pedropathing.paths.PathPoint);
  public static com.pedropathing.paths.HeadingInterpolator lazy(java.util.function.Supplier<com.pedropathing.paths.HeadingInterpolator>);
  public default com.pedropathing.paths.HeadingInterpolator offset(double);
  public default com.pedropathing.paths.HeadingInterpolator reverse();
  public static com.pedropathing.paths.HeadingInterpolator constant(double);
  public static com.pedropathing.paths.HeadingInterpolator linear(double, double);
  public static com.pedropathing.paths.HeadingInterpolator reversedLinear(double, double);
  public static com.pedropathing.paths.HeadingInterpolator linear(double, double, double);
  public static com.pedropathing.paths.HeadingInterpolator reversedLinear(double, double, double);
  public static com.pedropathing.paths.HeadingInterpolator facingPoint(double, double);
  public static com.pedropathing.paths.HeadingInterpolator facingPoint(com.pedropathing.geometry.Pose);
  public static com.pedropathing.paths.HeadingInterpolator piecewise(com.pedropathing.paths.HeadingInterpolator.PiecewiseNode...);
  public default void init();
  public static com.pedropathing.paths.HeadingInterpolator linearFromPoint(com.pedropathing.paths.HeadingInterpolator.FutureDouble, com.pedropathing.paths.HeadingInterpolator.FutureDouble, double);
  public static com.pedropathing.paths.HeadingInterpolator linearFromPoint(com.pedropathing.paths.HeadingInterpolator.FutureDouble, double, double);
  public static com.pedropathing.paths.HeadingInterpolator reversedLinearFromPoint(com.pedropathing.paths.HeadingInterpolator.FutureDouble, double, double);
  public static com.pedropathing.paths.HeadingInterpolator linearFromPoint(double, com.pedropathing.paths.HeadingInterpolator.FutureDouble, double);
  public static com.pedropathing.paths.HeadingInterpolator reversedLinearFromPoint(double, com.pedropathing.paths.HeadingInterpolator.FutureDouble, double);
  public static com.pedropathing.paths.HeadingInterpolator reversedLinearFromPoint(com.pedropathing.paths.HeadingInterpolator.FutureDouble, com.pedropathing.paths.HeadingInterpolator.FutureDouble, double);
}
```

## interface HeadingInterpolator.FutureDouble

```java
public interface com.pedropathing.paths.HeadingInterpolator.FutureDouble {
  public abstract double get();
}
```

## class HeadingInterpolator.PiecewiseNode

```java
public class com.pedropathing.paths.HeadingInterpolator.PiecewiseNode {
  public com.pedropathing.paths.HeadingInterpolator.PiecewiseNode(double, double, com.pedropathing.paths.HeadingInterpolator);
  public double getInitialTValue();
  public double getFinalTValue();
  public com.pedropathing.paths.HeadingInterpolator getInterpolator();
  public static com.pedropathing.paths.HeadingInterpolator.PiecewiseNode linear(double, double, double, double);
  public static com.pedropathing.paths.HeadingInterpolator.PiecewiseNode reversedLinear(double, double, double, double);
}
```

## class Path

```java
public class com.pedropathing.paths.Path {
  public com.pedropathing.paths.Path(com.pedropathing.geometry.Curve, com.pedropathing.paths.PathConstraints);
  public com.pedropathing.paths.Path(com.pedropathing.geometry.Curve);
  public com.pedropathing.paths.Path();
  public void setLinearHeadingInterpolation(double, double);
  public void setLinearHeadingInterpolation(double, double, double);
  public void setLinearHeadingInterpolation(double, double, double, boolean);
  public void setConstantHeadingInterpolation(double);
  public com.pedropathing.paths.PathPoint getClosestPoint(com.pedropathing.geometry.Pose, int, double);
  public com.pedropathing.paths.PathPoint getClosestPoint(com.pedropathing.geometry.Pose, int);
  public com.pedropathing.paths.PathPoint getClosestPoint(com.pedropathing.geometry.Pose);
  public com.pedropathing.paths.PathPoint getClosestPose();
  public com.pedropathing.paths.PathPoint updateClosestPose(com.pedropathing.geometry.Pose, int);
  public com.pedropathing.paths.PathPoint updateClosestPose(com.pedropathing.geometry.Pose);
  public double getDistanceTraveled(double);
  public double getPathCompletion(double);
  public double getPathCompletion();
  public double getDistanceTraveled();
  public double getDistanceRemaining(double);
  public double getDistanceRemaining();
  public double getTFromPathCompletion(double);
  public void reverseHeadingInterpolation();
  public void setTangentHeadingInterpolation();
  public com.pedropathing.math.Vector getTangentVector(double);
  public com.pedropathing.math.Vector getEndTangent();
  public com.pedropathing.geometry.Pose getPoint(double);
  public com.pedropathing.geometry.Pose getPose(double);
  public com.pedropathing.paths.PathPoint getPoseInformation(double);
  public double getClosestPointTValue();
  public double length();
  public double getCurvature(double);
  public double getClosestPointCurvature();
  public com.pedropathing.math.Vector getClosestPointNormalVector();
  public com.pedropathing.math.Vector getClosestPointTangentVector();
  public double getClosestPointHeadingGoal();
  public double getHeadingGoal(com.pedropathing.paths.PathPoint);
  public double getHeadingGoal(double);
  public void setHeadingInterpolation(com.pedropathing.paths.HeadingInterpolator);
  public boolean isAtParametricEnd();
  public boolean isAtParametricStart();
  public java.util.ArrayList<com.pedropathing.geometry.Pose> getControlPoints();
  public com.pedropathing.geometry.Pose getFirstControlPoint();
  public com.pedropathing.geometry.Pose getSecondControlPoint();
  public com.pedropathing.geometry.Pose getSecondToLastControlPoint();
  public com.pedropathing.geometry.Pose getLastControlPoint();
  public void setBrakingStrength(double);
  public void setBrakingStart(double);
  public void setVelocityConstraint(double);
  public void setTranslationalConstraint(double);
  public void setHeadingConstraint(double);
  public void setTValueConstraint(double);
  public void setTimeoutConstraint(double);
  public double getBrakingStrength();
  public double getBrakingStartMultiplier();
  public double getPathEndVelocityConstraint();
  public double getPathEndTranslationalConstraint();
  public double getPathEndHeadingConstraint();
  public double getPathEndTValueConstraint();
  public double getPathEndTimeoutConstraint();
  public java.lang.String pathType();
  public double[][] getPanelsDrawingPoints();
  public com.pedropathing.paths.HeadingInterpolator getHeadingInterpolator();
  public com.pedropathing.geometry.Pose endPose();
  public com.pedropathing.paths.Path getReversed();
  public void setConstraints(com.pedropathing.paths.PathConstraints);
  public com.pedropathing.paths.PathConstraints getConstraints();
  public com.pedropathing.geometry.Curve getCurve();
  public void init();
  public com.pedropathing.math.Vector getClosestLeftGradientVector();
}
```

## class PathBuilder

```java
public class com.pedropathing.paths.PathBuilder {
  public com.pedropathing.paths.PathBuilder(com.pedropathing.follower.Follower, com.pedropathing.paths.PathConstraints);
  public com.pedropathing.paths.PathBuilder(com.pedropathing.follower.Follower);
  public com.pedropathing.paths.PathBuilder addPath(com.pedropathing.paths.Path);
  public com.pedropathing.paths.PathBuilder addPath(com.pedropathing.geometry.Curve);
  public com.pedropathing.paths.PathBuilder addPaths(com.pedropathing.paths.Path...);
  public com.pedropathing.paths.PathBuilder addPaths(com.pedropathing.geometry.Curve...);
  public com.pedropathing.paths.PathBuilder curveThrough(com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose, double, com.pedropathing.geometry.Pose...);
  public com.pedropathing.paths.PathBuilder curveThrough(double, com.pedropathing.geometry.Pose...);
  public com.pedropathing.paths.PathBuilder setLinearHeadingInterpolation(double, double);
  public com.pedropathing.paths.PathBuilder setGlobalLinearHeadingInterpolation(double, double);
  public com.pedropathing.paths.PathBuilder setLinearHeadingInterpolation(double, double, double);
  public com.pedropathing.paths.PathBuilder setGlobalLinearHeadingInterpolation(double, double, double);
  public com.pedropathing.paths.PathBuilder setLinearHeadingInterpolation(double, double, double, double);
  public com.pedropathing.paths.PathBuilder setGlobalLinearHeadingInterpolation(double, double, double, double);
  public com.pedropathing.paths.PathBuilder setConstantHeadingInterpolation(double);
  public com.pedropathing.paths.PathBuilder setGlobalConstantHeadingInterpolation(double);
  public com.pedropathing.paths.PathBuilder setReversed();
  public com.pedropathing.paths.PathBuilder setGlobalReversed();
  public com.pedropathing.paths.PathBuilder setTangentHeadingInterpolation();
  public com.pedropathing.paths.PathBuilder setGlobalTangentHeadingInterpolation();
  public com.pedropathing.paths.PathBuilder setHeadingInterpolation(com.pedropathing.paths.HeadingInterpolator);
  public com.pedropathing.paths.PathBuilder setGlobalHeadingInterpolation(com.pedropathing.paths.HeadingInterpolator);
  public com.pedropathing.paths.PathBuilder setBrakingStrength(double);
  public com.pedropathing.paths.PathBuilder setBrakingStart(double);
  public com.pedropathing.paths.PathBuilder setVelocityConstraint(double);
  public com.pedropathing.paths.PathBuilder setTranslationalConstraint(double);
  public com.pedropathing.paths.PathBuilder setHeadingConstraint(double);
  public com.pedropathing.paths.PathBuilder setTValueConstraint(double);
  public com.pedropathing.paths.PathBuilder setTimeoutConstraint(double);
  public com.pedropathing.paths.PathBuilder addTemporalCallback(double, java.lang.Runnable);
  public com.pedropathing.paths.PathBuilder addParametricCallback(double, java.lang.Runnable);
  public com.pedropathing.paths.PathBuilder addPoseCallback(com.pedropathing.geometry.Pose, java.lang.Runnable, double);
  public com.pedropathing.paths.PathBuilder addCallback(com.pedropathing.paths.callbacks.PathCallback);
  public com.pedropathing.paths.PathBuilder addCallback(com.pedropathing.paths.callbacks.PathCallback, int);
  public com.pedropathing.paths.PathBuilder addCallback(com.pedropathing.paths.PathBuilder.CallbackCondition, java.lang.Runnable);
  public com.pedropathing.paths.PathBuilder addCallback(com.pedropathing.paths.PathBuilder.CallbackCondition, java.lang.Runnable, int);
  public com.pedropathing.paths.PathBuilder addLoopedCallback(com.pedropathing.paths.callbacks.PathCallback);
  public com.pedropathing.paths.PathChain build();
  public com.pedropathing.paths.PathBuilder setGlobalDeceleration();
  public com.pedropathing.paths.PathBuilder setGlobalDeceleration(double);
  public com.pedropathing.paths.PathBuilder setNoDeceleration();
  public com.pedropathing.paths.PathBuilder setConstraints(com.pedropathing.paths.PathConstraints);
  public com.pedropathing.paths.PathBuilder setConstraintsForAll(com.pedropathing.paths.PathConstraints);
  public com.pedropathing.paths.PathBuilder setConstraintsForLast(com.pedropathing.paths.PathConstraints);
}
```

## interface PathBuilder.CallbackCondition

```java
public interface com.pedropathing.paths.PathBuilder.CallbackCondition {
  public abstract boolean isReady();
}
```

## class PathChain

```java
public class com.pedropathing.paths.PathChain {
  public com.pedropathing.paths.HeadingInterpolator headingInterpolator;
  public com.pedropathing.paths.PathChain(com.pedropathing.paths.Path...);
  public com.pedropathing.paths.PathChain(com.pedropathing.paths.PathConstraints, com.pedropathing.paths.Path...);
  public com.pedropathing.paths.PathChain(java.util.ArrayList<com.pedropathing.paths.Path>);
  public com.pedropathing.paths.PathChain(com.pedropathing.paths.PathConstraints, java.util.ArrayList<com.pedropathing.paths.Path>);
  public com.pedropathing.paths.Path getPath(int);
  public int size();
  public void setCallbacks(com.pedropathing.paths.callbacks.PathCallback...);
  public void setCallbacks(java.util.ArrayList<com.pedropathing.paths.callbacks.PathCallback>);
  public java.util.ArrayList<com.pedropathing.paths.callbacks.PathCallback> getCallbacks();
  public void resetCallbacks();
  public void setDecelerationType(com.pedropathing.paths.PathChain.DecelerationType);
  public com.pedropathing.paths.PathChain.DecelerationType getDecelerationType();
  public double length();
  public com.pedropathing.geometry.Pose endPose();
  public com.pedropathing.geometry.Pose endPoint();
  public void setConstraintsForAll(com.pedropathing.paths.PathConstraints);
  public void setHeadingInterpolator(com.pedropathing.paths.HeadingInterpolator);
  public double getHeadingGoal(com.pedropathing.paths.PathChain.PathT);
  public double getClosestPointHeadingGoal(com.pedropathing.paths.PathChain.PathT);
  public com.pedropathing.math.Vector getTangentVector(com.pedropathing.paths.PathChain.PathT);
  public com.pedropathing.geometry.Pose getPose(com.pedropathing.paths.PathChain.PathT);
  public com.pedropathing.geometry.Pose getPoint(com.pedropathing.paths.PathChain.PathT);
  public com.pedropathing.paths.PathPoint getPoseInformation(com.pedropathing.paths.PathChain.PathT);
  public com.pedropathing.paths.Path lastPath();
  public com.pedropathing.paths.Path firstPath();
  public java.lang.Double getFinalHeadingGoal();
  public double getDistanceRemaining(com.pedropathing.paths.PathChain.PathT);
  public double getDistanceRemaining(int);
  public void update();
  public java.util.Queue<com.pedropathing.paths.callbacks.PathCallback> getNextPathCallbacks(int);
}
```

## class PathChain.DecelerationType

```java
public final class com.pedropathing.paths.PathChain.DecelerationType extends java.lang.Enum<com.pedropathing.paths.PathChain.DecelerationType> {
  public static final com.pedropathing.paths.PathChain.DecelerationType NONE;
  public static final com.pedropathing.paths.PathChain.DecelerationType GLOBAL;
  public static final com.pedropathing.paths.PathChain.DecelerationType LAST_PATH;
  public static com.pedropathing.paths.PathChain.DecelerationType[] values();
  public static com.pedropathing.paths.PathChain.DecelerationType valueOf(java.lang.String);
}
```

## class PathChain.PathT

```java
public class com.pedropathing.paths.PathChain.PathT {
  public com.pedropathing.paths.PathChain.PathT(int, double);
  public int pathIndex();
  public double t();
  public com.pedropathing.paths.Path getPath(com.pedropathing.paths.PathChain);
  public com.pedropathing.geometry.Pose getPose(com.pedropathing.paths.PathChain);
  public com.pedropathing.geometry.Pose getPoint(com.pedropathing.paths.PathChain);
  public com.pedropathing.math.Vector getTangentVector(com.pedropathing.paths.PathChain);
  public double getHeadingGoal(com.pedropathing.paths.PathChain);
  public boolean equals(java.lang.Object);
  public int hashCode();
  public java.lang.String toString();
}
```

## class PathConstraints

```java
public final class com.pedropathing.paths.PathConstraints {
  public static com.pedropathing.paths.PathConstraints defaultConstraints;
  public com.pedropathing.paths.PathConstraints(double, double, double, double, double, double, int, double);
  public com.pedropathing.paths.PathConstraints(double, double, double, double);
  public com.pedropathing.paths.PathConstraints(double, double);
  public double getVelocityConstraint();
  public double getTranslationalConstraint();
  public double getHeadingConstraint();
  public double getTValueConstraint();
  public double getTimeoutConstraint();
  public double getBrakingStrength();
  public double getBrakingStart();
  public int getBEZIER_CURVE_SEARCH_LIMIT();
  public static void setDefaultConstraints(com.pedropathing.paths.PathConstraints);
  public void setBEZIER_CURVE_SEARCH_LIMIT(int);
  public void setBrakingStart(double);
  public void setBrakingStrength(double);
  public void setHeadingConstraint(double);
  public void setTimeoutConstraint(double);
  public void setTranslationalConstraint(double);
  public void setTValueConstraint(double);
  public void setVelocityConstraint(double);
  public com.pedropathing.paths.PathConstraints copy();
}
```

## class PathPoint

```java
public class com.pedropathing.paths.PathPoint {
  public final double tValue;
  public final com.pedropathing.geometry.Pose pose;
  public final com.pedropathing.math.Vector tangentVector;
  public com.pedropathing.paths.PathPoint();
  public com.pedropathing.paths.PathPoint(double, com.pedropathing.geometry.Pose, com.pedropathing.math.Vector);
  public double getTValue();
  public com.pedropathing.geometry.Pose getPose();
  public com.pedropathing.math.Vector getTangentVector();
}
```
