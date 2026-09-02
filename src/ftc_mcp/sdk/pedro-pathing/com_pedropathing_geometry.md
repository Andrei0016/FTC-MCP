# `com.pedropathing.geometry`

_pedro-pathing 2.1.2 — 13 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class BezierCurve

```java
public class com.pedropathing.geometry.BezierCurve implements com.pedropathing.geometry.Curve {
  protected java.util.ArrayList<com.pedropathing.geometry.FuturePose> futureControlPoints;
  protected boolean initialized;
  protected boolean lazyInitialize;
  protected final int APPROXIMATION_STEPS = 1000;
  protected com.pedropathing.paths.PathConstraints pathConstraints;
  protected com.pedropathing.math.AbstractBijectiveMap.NumericBijectiveMap completionMap;
  public com.pedropathing.geometry.BezierCurve();
  public com.pedropathing.geometry.BezierCurve(java.util.List<com.pedropathing.geometry.Pose>, com.pedropathing.paths.PathConstraints);
  protected com.pedropathing.geometry.BezierCurve(com.pedropathing.paths.PathConstraints, java.util.List<com.pedropathing.geometry.FuturePose>);
  public com.pedropathing.geometry.BezierCurve(java.util.List<com.pedropathing.geometry.Pose>);
  public com.pedropathing.geometry.BezierCurve(com.pedropathing.paths.PathConstraints, com.pedropathing.geometry.FuturePose...);
  public com.pedropathing.geometry.BezierCurve(com.pedropathing.geometry.FuturePose...);
  public void initialize();
  public void initializePanelsDrawingPoints();
  public double[][] getPanelsDrawingPoints();
  public void generateBezierCurve();
  public com.pedropathing.math.Vector getEndTangent();
  public double approximateLength();
  public void initializeDegreeArray();
  public void initializeCoefficientArray();
  public double[] getTVector(double, int);
  public com.pedropathing.geometry.Pose getPose(double);
  public double getCurvature(double);
  public com.pedropathing.math.Vector getDerivative(double);
  public com.pedropathing.math.Vector getSecondDerivative(double);
  public com.pedropathing.math.Matrix getPointCharacteristics(double);
  public com.pedropathing.math.Vector getNormalVector(double);
  public java.util.ArrayList<com.pedropathing.geometry.Pose> getControlPoints();
  public com.pedropathing.geometry.Pose getFirstControlPoint();
  public com.pedropathing.geometry.Pose getSecondControlPoint();
  public com.pedropathing.geometry.Pose getSecondToLastControlPoint();
  public com.pedropathing.geometry.Pose getLastControlPoint();
  public double length();
  public java.lang.String pathType();
  public com.pedropathing.geometry.BezierCurve getReversed();
  public double getClosestPoint(com.pedropathing.geometry.Pose, int, double);
  public double getClosestPoint(com.pedropathing.geometry.Pose, double);
  public boolean atParametricEnd(double);
  public void setControlPoints(java.util.ArrayList<com.pedropathing.geometry.Pose>);
  public void setPathConstraints(com.pedropathing.paths.PathConstraints);
  public com.pedropathing.paths.PathConstraints getPathConstraints();
  public double getPathCompletion(double);
  public double getT(double);
  public boolean isInitialized();
  public static com.pedropathing.geometry.BezierCurve through(com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose);
  public static com.pedropathing.geometry.BezierCurve through(com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose);
  public static com.pedropathing.geometry.BezierCurve through(com.pedropathing.geometry.Pose...);
  public com.pedropathing.geometry.Curve getReversed();
}
```

## class BezierLine

```java
public class com.pedropathing.geometry.BezierLine extends com.pedropathing.geometry.BezierCurve {
  public com.pedropathing.geometry.BezierLine(com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.BezierLine(com.pedropathing.geometry.FuturePose, com.pedropathing.geometry.FuturePose);
  public com.pedropathing.geometry.BezierLine(com.pedropathing.geometry.Pose, com.pedropathing.geometry.Pose, boolean);
  public com.pedropathing.math.Vector getEndTangent();
  public double approximateLength();
  public com.pedropathing.geometry.Pose getPose(double);
  public double getCurvature(double);
  public com.pedropathing.math.Vector getDerivative(double);
  public com.pedropathing.math.Vector getSecondDerivative(double);
  public com.pedropathing.math.Vector getNormalVector(double);
  public java.util.ArrayList<com.pedropathing.geometry.Pose> getControlPoints();
  public com.pedropathing.geometry.Pose getFirstControlPoint();
  public com.pedropathing.geometry.Pose getSecondControlPoint();
  public com.pedropathing.geometry.Pose getSecondToLastControlPoint();
  public com.pedropathing.geometry.Pose getLastControlPoint();
  public double length();
  public java.lang.String pathType();
  public double getClosestPoint(com.pedropathing.geometry.Pose, int, double);
  public void initialize();
  public double getPathCompletion(double);
  public double getT(double);
}
```

## class BezierPoint

```java
public class com.pedropathing.geometry.BezierPoint extends com.pedropathing.geometry.BezierCurve {
  public com.pedropathing.geometry.BezierPoint(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.BezierPoint(com.pedropathing.geometry.FuturePose);
  public com.pedropathing.geometry.BezierPoint(double, double);
  public com.pedropathing.math.Vector getEndTangent();
  public double approximateLength();
  public com.pedropathing.geometry.Pose getPose(double);
  public double getCurvature(double);
  public com.pedropathing.math.Vector getDerivative(double);
  public com.pedropathing.math.Vector getSecondDerivative(double);
  public com.pedropathing.math.Vector getNormalVector(double);
  public java.util.ArrayList<com.pedropathing.geometry.Pose> getControlPoints();
  public com.pedropathing.geometry.Pose getFirstControlPoint();
  public com.pedropathing.geometry.Pose getSecondControlPoint();
  public com.pedropathing.geometry.Pose getSecondToLastControlPoint();
  public com.pedropathing.geometry.Pose getLastControlPoint();
  public double length();
  public java.lang.String pathType();
  public double getClosestPoint(com.pedropathing.geometry.Pose, int, double);
  public double getT(double);
  public double getPathCompletion(double);
  public void initialize();
}
```

## class CharacteristicMatrixSupplier

```java
public class com.pedropathing.geometry.CharacteristicMatrixSupplier {
  public com.pedropathing.geometry.CharacteristicMatrixSupplier();
  public void initialize();
  public static com.pedropathing.math.Matrix generateBezierCharacteristicMatrix(int);
  public static com.pedropathing.math.Matrix getBezierCharacteristicMatrix(int);
}
```

## interface CoordinateSystem

```java
public interface com.pedropathing.geometry.CoordinateSystem {
  public abstract com.pedropathing.geometry.Pose convertToPedro(com.pedropathing.geometry.Pose);
  public abstract com.pedropathing.geometry.Pose convertFromPedro(com.pedropathing.geometry.Pose);
}
```

## interface Curve

```java
public interface com.pedropathing.geometry.Curve {
  public abstract void initialize();
  public abstract com.pedropathing.math.Vector getNormalVector(double);
  public abstract com.pedropathing.geometry.Curve getReversed();
  public abstract com.pedropathing.math.Vector getDerivative(double);
  public abstract com.pedropathing.geometry.Pose getPose(double);
  public abstract com.pedropathing.math.Vector getSecondDerivative(double);
  public default boolean atParametricEnd(double);
  public abstract java.util.ArrayList<com.pedropathing.geometry.Pose> getControlPoints();
  public abstract void setPathConstraints(com.pedropathing.paths.PathConstraints);
  public abstract com.pedropathing.paths.PathConstraints getPathConstraints();
  public abstract double getPathCompletion(double);
  public abstract double getT(double);
  public default com.pedropathing.geometry.Pose getFirstControlPoint();
  public default com.pedropathing.geometry.Pose getLastControlPoint();
  public default com.pedropathing.geometry.Pose getSecondToLastControlPoint();
  public default com.pedropathing.geometry.Pose getSecondControlPoint();
  public default double getClosestPoint(com.pedropathing.geometry.Pose, int, double);
  public default double getClosestPoint(com.pedropathing.geometry.Pose, double);
  public default double getCurvature(double);
  public default double length();
  public default double[][] getPanelsDrawingPoints();
  public default com.pedropathing.math.Vector getEndTangent();
  public default java.lang.String pathType();
  public default com.pedropathing.math.Vector leftGradient(double);
  public default com.pedropathing.math.Vector rightGradient(double);
}
```

## class CustomCurve

```java
public abstract class com.pedropathing.geometry.CustomCurve implements com.pedropathing.geometry.Curve {
  protected java.util.ArrayList<com.pedropathing.geometry.Pose> controlPoints;
  protected com.pedropathing.paths.PathConstraints pathConstraints;
  protected com.pedropathing.math.AbstractBijectiveMap.NumericBijectiveMap completionMap;
  public com.pedropathing.geometry.CustomCurve(java.util.List<com.pedropathing.geometry.Pose>, com.pedropathing.paths.PathConstraints);
  public com.pedropathing.geometry.CustomCurve(com.pedropathing.geometry.Pose...);
  public com.pedropathing.geometry.CustomCurve(com.pedropathing.geometry.FuturePose...);
  public com.pedropathing.geometry.CustomCurve(com.pedropathing.paths.PathConstraints, com.pedropathing.geometry.FuturePose...);
  public java.util.ArrayList<com.pedropathing.geometry.Pose> getControlPoints();
  public void setPathConstraints(com.pedropathing.paths.PathConstraints);
  public com.pedropathing.paths.PathConstraints getPathConstraints();
  public void initialization();
  public void initialize();
  public void initializePanelsDrawingPoints();
  public double[][] getPanelsDrawingPoints();
  public double approximateLength();
  public double length();
  public abstract java.lang.String pathType();
  public abstract com.pedropathing.geometry.CustomCurve getReversed();
  public double getPathCompletion(double);
  public double getT(double);
  public com.pedropathing.math.Vector getNormalVector(double);
  public com.pedropathing.geometry.Curve getReversed();
}
```

## class FinetunedBezierCurve

```java
public class com.pedropathing.geometry.FinetunedBezierCurve extends com.pedropathing.geometry.BezierCurve {
  public com.pedropathing.geometry.FinetunedBezierCurve(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose, int);
  public com.pedropathing.geometry.FinetunedBezierCurve(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose, int, com.pedropathing.paths.PathConstraints);
  public com.pedropathing.geometry.FinetunedBezierCurve(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.FinetunedBezierCurve(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose, com.pedropathing.paths.PathConstraints);
  public com.pedropathing.geometry.Pose getEndPoint();
  public void setCrossingThreshold(double);
  public com.pedropathing.geometry.Pose getPose(double);
  public com.pedropathing.math.Vector getDerivative(double);
  public com.pedropathing.math.Vector getSecondDerivative(double);
  public boolean atParametricEnd(double);
  public double approximateLength();
  public com.pedropathing.geometry.BezierCurve getReversed();
  public com.pedropathing.geometry.Curve getReversed();
}
```

## class FinetunedBezierLine

```java
public class com.pedropathing.geometry.FinetunedBezierLine extends com.pedropathing.geometry.BezierLine {
  public com.pedropathing.geometry.FinetunedBezierLine(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose, int);
  public com.pedropathing.geometry.FinetunedBezierLine(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose, int, com.pedropathing.paths.PathConstraints);
  public com.pedropathing.geometry.FinetunedBezierLine(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.FinetunedBezierLine(java.util.ArrayList<com.pedropathing.geometry.Pose>, com.pedropathing.geometry.Pose, com.pedropathing.paths.PathConstraints);
  public com.pedropathing.geometry.Pose getEndPoint();
  public void setCrossingThreshold(double);
  public com.pedropathing.geometry.Pose getPose(double);
  public com.pedropathing.math.Vector getDerivative(double);
  public com.pedropathing.math.Vector getSecondDerivative(double);
  public boolean atParametricEnd(double);
  public double approximateLength();
  public double getPathCompletion(double);
  public com.pedropathing.geometry.BezierLine getReversed();
  public com.pedropathing.geometry.BezierCurve getReversed();
  public com.pedropathing.geometry.Curve getReversed();
}
```

## interface FuturePose

```java
public interface com.pedropathing.geometry.FuturePose {
  public abstract com.pedropathing.geometry.Pose getPose();
  public default boolean initialized();
}
```

## class PedroCoordinates

```java
public final class com.pedropathing.geometry.PedroCoordinates extends java.lang.Enum<com.pedropathing.geometry.PedroCoordinates> implements com.pedropathing.geometry.CoordinateSystem {
  public static final com.pedropathing.geometry.PedroCoordinates INSTANCE;
  public static com.pedropathing.geometry.PedroCoordinates[] values();
  public static com.pedropathing.geometry.PedroCoordinates valueOf(java.lang.String);
  public com.pedropathing.geometry.Pose convertFromPedro(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose convertToPedro(com.pedropathing.geometry.Pose);
}
```

## class Pose

```java
public final class com.pedropathing.geometry.Pose implements com.pedropathing.geometry.FuturePose {
  public com.pedropathing.geometry.Pose(double, double, double, com.pedropathing.geometry.CoordinateSystem);
  public com.pedropathing.geometry.Pose(double, double, double);
  public com.pedropathing.geometry.Pose(double, double);
  public com.pedropathing.geometry.Pose();
  public double getX();
  public double getY();
  public double getHeading();
  public com.pedropathing.geometry.CoordinateSystem getCoordinateSystem();
  public com.pedropathing.geometry.Pose withX(double);
  public com.pedropathing.geometry.Pose withY(double);
  public com.pedropathing.geometry.Pose withHeading(double);
  public com.pedropathing.math.Vector getAsVector();
  public com.pedropathing.math.Vector getHeadingAsUnitVector();
  public com.pedropathing.geometry.Pose plus(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose minus(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose times(double);
  public com.pedropathing.geometry.Pose scale(double);
  public com.pedropathing.geometry.Pose div(double);
  public com.pedropathing.geometry.Pose unaryMinus();
  public com.pedropathing.geometry.Pose linearCombination(com.pedropathing.geometry.Pose, double, double);
  public boolean roughlyEquals(com.pedropathing.geometry.Pose, double);
  public double distanceFrom(com.pedropathing.geometry.Pose);
  public double distSquared(com.pedropathing.geometry.Pose);
  public com.pedropathing.geometry.Pose rotate(double, boolean);
  public com.pedropathing.geometry.Pose mirror();
  public com.pedropathing.geometry.Pose mirror(double);
  public com.pedropathing.geometry.Pose getAsCoordinateSystem(com.pedropathing.geometry.CoordinateSystem);
  public static double[] polarToCartesian(double, double);
  public static double[] cartesianToPolar(double, double);
  public com.pedropathing.geometry.Pose setHeading(double);
  public com.pedropathing.geometry.Pose copy();
  public java.lang.String toString();
  public boolean initialized();
  public com.pedropathing.geometry.Pose getPose();
}
```

## class TVector

```java
public class com.pedropathing.geometry.TVector {
  public com.pedropathing.geometry.TVector(int, int);
  public com.pedropathing.geometry.TVector(int);
  public void reload();
  public void initializeCoefficientArray();
  public com.pedropathing.math.Matrix getRowVector(double, int);
  public com.pedropathing.math.Matrix getTMatrix(double, int);
  public int[][] getDiffPowers();
  public int[][] getDiffCoefficients();
  public int getControlPointCount();
  public void setControlPointCount(int);
  public int getDifferentiationLevel();
  public void setDifferentiationLevel(int);
}
```
