# `com.pedropathing.math`

_pedro-pathing 2.1.2 — 8 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class AbstractBijectiveMap

```java
public class com.pedropathing.math.AbstractBijectiveMap<T, S> implements com.pedropathing.math.BijectiveMap<T, S> {
  public com.pedropathing.math.AbstractBijectiveMap();
  public void put(T, S);
  public java.util.HashMap<T, S> getForwardMap();
  public java.util.HashMap<S, T> getReverseMap();
  public S get(T);
  public T invert(S);
  public boolean containsKey(T);
  public boolean containsValue(S);
  public void remove(T);
  public void removeValue(S);
  public int size();
  public java.util.Map getReverseMap();
  public java.util.Map getForwardMap();
}
```

## class AbstractBijectiveMap.NumericBijectiveMap

```java
public class com.pedropathing.math.AbstractBijectiveMap.NumericBijectiveMap implements com.pedropathing.math.BijectiveMap<java.lang.Double, java.lang.Double> {
  public com.pedropathing.math.AbstractBijectiveMap.NumericBijectiveMap();
  public void put(java.lang.Double, java.lang.Double);
  public java.lang.Double get(java.lang.Double);
  public java.lang.Double invert(java.lang.Double);
  public boolean containsKey(java.lang.Double);
  public boolean containsValue(java.lang.Double);
  public void remove(java.lang.Double);
  public void removeValue(java.lang.Double);
  public int size();
  public java.util.TreeMap<java.lang.Double, java.lang.Double> getForwardMap();
  public java.util.TreeMap<java.lang.Double, java.lang.Double> getReverseMap();
  public double closestKey(double, double);
  public double closestKey(double);
  public double closestValue(double, double);
  public double closestValue(double);
  public double interpolateKey(double);
  public double interpolateValue(double);
  public java.util.Map getReverseMap();
  public java.util.Map getForwardMap();
  public void removeValue(java.lang.Object);
  public void remove(java.lang.Object);
  public boolean containsValue(java.lang.Object);
  public boolean containsKey(java.lang.Object);
  public java.lang.Object invert(java.lang.Object);
  public java.lang.Object get(java.lang.Object);
  public void put(java.lang.Object, java.lang.Object);
}
```

## class AbstractBijectiveMap.NumericBijectiveMap.InterpolatableMap

```java
public class com.pedropathing.math.AbstractBijectiveMap.NumericBijectiveMap.InterpolatableMap extends java.util.TreeMap<java.lang.Double, java.lang.Double> {
  public com.pedropathing.math.AbstractBijectiveMap.NumericBijectiveMap.InterpolatableMap();
}
```

## interface BijectiveMap

```java
public interface com.pedropathing.math.BijectiveMap<T, S> {
  public abstract void put(T, S);
  public abstract S get(T);
  public abstract T invert(S);
  public abstract boolean containsKey(T);
  public abstract boolean containsValue(S);
  public abstract void remove(T);
  public abstract void removeValue(S);
  public abstract int size();
  public abstract java.util.Map<T, S> getForwardMap();
  public abstract java.util.Map<S, T> getReverseMap();
}
```

## class Kinematics

```java
public final class com.pedropathing.math.Kinematics {
  public com.pedropathing.math.Kinematics();
  public static double getVelocityToStopWithDeceleration(double, double);
  public static double getFinalVelocityAtDistance(double, double, double);
  public static double predictNextLoopVelocity(double, double);
  public static double getDistanceToVelocity(double, double, double);
  public static double getStoppingDistance(double, double);
}
```

## class MathFunctions

```java
public class com.pedropathing.math.MathFunctions {
  public com.pedropathing.math.MathFunctions();
  public static double clamp(double, double, double);
  public static double normalizeAngle(double);
  public static double normalizeAngleSigned(double);
  public static double getSmallestAngleDifference(double, double);
  public static double getTurnDirection(double, double);
  public static boolean roughlyEquals(double, double, double);
  public static boolean roughlyEquals(double, double);
  public static double findNormalizingScaling(com.pedropathing.math.Vector, com.pedropathing.math.Vector, double);
  public static double scale(double, double, double, double, double);
  public static double[] quadraticFit(java.util.List<double[]>);
}
```

## class Matrix

```java
public class com.pedropathing.math.Matrix {
  public com.pedropathing.math.Matrix();
  public com.pedropathing.math.Matrix(int, int);
  public com.pedropathing.math.Matrix(double[][]);
  public com.pedropathing.math.Matrix(com.pedropathing.math.Matrix);
  public void setMatrix(com.pedropathing.math.Matrix);
  public void setMatrix(double[][]);
  public com.pedropathing.math.Matrix copy();
  public static double[][] deepCopy(double[][]);
  public double[][] getMatrix();
  public int getRows();
  public int getColumns();
  public int[] getSize();
  public double[] get(int);
  public boolean set(int, double[]);
  public double[] getRow(int);
  public void setRow(int, double...);
  public double[] getCol(int);
  public void setCol(int, double...);
  public double get(int, int);
  public void set(int, int, double);
  public com.pedropathing.math.Matrix plus(com.pedropathing.math.Matrix);
  public com.pedropathing.math.Matrix minus(com.pedropathing.math.Matrix);
  public com.pedropathing.math.Matrix multiply(double);
  public com.pedropathing.math.Matrix times(double);
  public com.pedropathing.math.Matrix multiply(com.pedropathing.math.Matrix);
  public com.pedropathing.math.Matrix times(com.pedropathing.math.Matrix);
  public static com.pedropathing.math.Matrix multiply(com.pedropathing.math.Matrix, com.pedropathing.math.Matrix);
  public com.pedropathing.math.Matrix unaryMinus();
  public com.pedropathing.math.Matrix transposed();
  public void rowSwap(int, int);
  public void rowScale(int, double);
  public void rowAdd(int, int, double);
  public static com.pedropathing.math.Matrix[] rref(com.pedropathing.math.Matrix, com.pedropathing.math.Matrix);
  public double determinant();
  public com.pedropathing.math.Matrix adjoint();
  public static com.pedropathing.math.Matrix inverse2x2(com.pedropathing.math.Matrix);
  public static com.pedropathing.math.Matrix inverse3x3(com.pedropathing.math.Matrix);
  public com.pedropathing.math.Matrix inverse();
  public static com.pedropathing.math.Matrix identity(int);
  public static com.pedropathing.math.Matrix zeros(int);
  public static com.pedropathing.math.Matrix zeros(int, int);
  public static com.pedropathing.math.Matrix diag(double...);
  public static com.pedropathing.math.Matrix translation(double, double);
  public static com.pedropathing.math.Matrix createRotation(double);
  public static com.pedropathing.math.Matrix createTransformation(double, double, double);
  public java.lang.String toString();
  public boolean equals(com.pedropathing.math.Matrix, double);
  public boolean equals(java.lang.Object);
  public int hashCode();
}
```

## class Vector

```java
public class com.pedropathing.math.Vector {
  public com.pedropathing.math.Vector();
  public com.pedropathing.math.Vector(com.pedropathing.geometry.Pose);
  public com.pedropathing.math.Vector(double, double);
  public void setComponents(double, double);
  public void setMagnitude(double);
  public void setTheta(double);
  public void rotateVector(double);
  public void setOrthogonalComponents(double, double);
  public com.pedropathing.math.Vector times(double);
  public com.pedropathing.math.Vector normalize();
  public com.pedropathing.math.Vector plus(com.pedropathing.math.Vector);
  public com.pedropathing.math.Vector minus(com.pedropathing.math.Vector);
  public double dot(com.pedropathing.math.Vector);
  public double cross(com.pedropathing.math.Vector);
  public com.pedropathing.math.Vector linearCombination(com.pedropathing.math.Vector, double, double);
  public double getMagnitude();
  public double getTheta();
  public double getXComponent();
  public double getYComponent();
  public com.pedropathing.math.Vector copy();
  public java.lang.String toString();
  public com.pedropathing.math.Vector transform(com.pedropathing.math.Matrix);
  public com.pedropathing.math.Vector projectOnto(com.pedropathing.math.Vector);
}
```
