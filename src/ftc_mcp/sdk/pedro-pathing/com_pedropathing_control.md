# `com.pedropathing.control`

_pedro-pathing 2.1.2 — 12 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class FilteredPIDFCoefficients

```java
public class com.pedropathing.control.FilteredPIDFCoefficients {
  public double P;
  public double I;
  public double D;
  public double F;
  public double T;
  public com.pedropathing.control.FilteredPIDFCoefficients(double, double, double, double, double);
  public void setCoefficients(double, double, double, double, double);
  public java.lang.String toString();
}
```

## class FilteredPIDFController

```java
public class com.pedropathing.control.FilteredPIDFController {
  public com.pedropathing.control.FilteredPIDFController(com.pedropathing.control.FilteredPIDFCoefficients);
  public double run();
  public void updatePosition(double);
  public void updateError(double);
  public void updateFeedForwardInput(double);
  public void reset();
  public void setTargetPosition(double);
  public double getTargetPosition();
  public void setCoefficients(com.pedropathing.control.FilteredPIDFCoefficients);
  public com.pedropathing.control.FilteredPIDFCoefficients getCoefficients();
  public void setP(double);
  public double P();
  public void setI(double);
  public double I();
  public void setD(double);
  public double D();
  public void setT(double);
  public double T();
  public void setF(double);
  public double F();
  public double getError();
}
```

## class KalmanFilter

```java
public class com.pedropathing.control.KalmanFilter implements com.pedropathing.control.NoiseFilter {
  public com.pedropathing.control.KalmanFilter(com.pedropathing.control.KalmanFilterParameters);
  public com.pedropathing.control.KalmanFilter(com.pedropathing.control.KalmanFilterParameters, double, double, double);
  public void reset(double, double, double);
  public void reset();
  public void update(double, double);
  public double getState();
  public java.lang.String[] output();
}
```

## class KalmanFilterParameters

```java
public class com.pedropathing.control.KalmanFilterParameters {
  public double modelCovariance;
  public double dataCovariance;
  public com.pedropathing.control.KalmanFilterParameters(double, double);
}
```

## class LowPassFilter

```java
public class com.pedropathing.control.LowPassFilter implements com.pedropathing.control.NoiseFilter {
  public com.pedropathing.control.LowPassFilter(double);
  public void update(double, double);
  public double getState();
  public void reset(double, double, double);
}
```

## interface NoiseFilter

```java
public interface com.pedropathing.control.NoiseFilter {
  public abstract double getState();
  public abstract void update(double, double);
  public default void reset();
  public abstract void reset(double, double, double);
}
```

## interface PIDFCoefficientSupplier

```java
public interface com.pedropathing.control.PIDFCoefficientSupplier {
  public abstract com.pedropathing.control.PIDFCoefficients get(double);
  public static com.pedropathing.control.PIDFCoefficientSupplier piecewise(com.pedropathing.control.PIDFCoefficientSupplier.PIDFPiecewiseNode...);
}
```

## class PIDFCoefficientSupplier.PIDFPiecewiseNode

```java
public class com.pedropathing.control.PIDFCoefficientSupplier.PIDFPiecewiseNode {
  public final double threshold;
  public final com.pedropathing.control.PIDFCoefficients coefficients;
  public com.pedropathing.control.PIDFCoefficientSupplier.PIDFPiecewiseNode(double, com.pedropathing.control.PIDFCoefficients);
  public com.pedropathing.control.PIDFCoefficientSupplier.PIDFPiecewiseNode(com.pedropathing.control.PIDFCoefficients);
}
```

## class PIDFCoefficients

```java
public class com.pedropathing.control.PIDFCoefficients implements com.pedropathing.control.PIDFCoefficientSupplier {
  public double P;
  public double I;
  public double D;
  public double F;
  public com.pedropathing.control.PIDFCoefficients(double, double, double, double);
  public double getCoefficient(double);
  public void setCoefficients(double, double, double, double);
  public java.lang.String toString();
  public com.pedropathing.control.PIDFCoefficients get(double);
}
```

## class PIDFController

```java
public class com.pedropathing.control.PIDFController {
  public com.pedropathing.control.PIDFController(com.pedropathing.control.PIDFCoefficientSupplier);
  public double run();
  public void updatePosition(double);
  public void updateError(double);
  public void updateFeedForwardInput(double);
  public void reset();
  public void setTargetPosition(double);
  public double getTargetPosition();
  public void setCoefficients(com.pedropathing.control.PIDFCoefficients);
  public com.pedropathing.control.PIDFCoefficients getCoefficients();
  public void setP(double);
  public double P();
  public void setI(double);
  public double I();
  public void setD(double);
  public double D();
  public void setF(double);
  public double F();
  public double getError();
  public double getErrorDerivative();
}
```

## class PredictiveBrakingCoefficients

```java
public class com.pedropathing.control.PredictiveBrakingCoefficients {
  public double kLinearBraking;
  public double kQuadraticFriction;
  public double P;
  public double maximumBrakingPower;
  public com.pedropathing.control.PredictiveBrakingCoefficients(double, double, double);
  public com.pedropathing.control.PredictiveBrakingCoefficients withMaximumBrakingPower(double);
  public void setCoefficients(double, double, double, double);
  public java.lang.String toString();
}
```

## class PredictiveBrakingController

```java
public class com.pedropathing.control.PredictiveBrakingController {
  public com.pedropathing.control.PredictiveBrakingController(com.pedropathing.control.PredictiveBrakingCoefficients);
  public void setCoefficients(com.pedropathing.control.PredictiveBrakingCoefficients);
  public double computeOutput(double, double);
  public double computeBrakingDisplacement(double, double);
}
```
