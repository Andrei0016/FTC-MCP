# `org.firstinspires.ftc.robotcore.external.navigation`

_ftc-sdk 11.1.0 — 26 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class Acceleration

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Acceleration {
  public static final double earthGravity = 9.80665d;
  public org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit unit;
  public double xAccel;
  public double yAccel;
  public double zAccel;
  public long acquisitionTime;
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration();
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, double, double, double, long);
  public static org.firstinspires.ftc.robotcore.external.navigation.Acceleration fromGravity(double, double, double, long);
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration toUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public java.lang.String toString();
}
```

## class AngleUnit

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.AngleUnit extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.AngleUnit> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.AngleUnit DEGREES;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AngleUnit RADIANS;
  public final byte bVal;
  protected static final double TwoPi = 6.283185307179586d;
  public static final float Pif = 3.1415927f;
  public static org.firstinspires.ftc.robotcore.external.navigation.AngleUnit[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.AngleUnit valueOf(java.lang.String);
  public double fromDegrees(double);
  public float fromDegrees(float);
  public double fromRadians(double);
  public float fromRadians(float);
  public double fromUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, double);
  public float fromUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float);
  public double toDegrees(double);
  public float toDegrees(float);
  public double toRadians(double);
  public float toRadians(float);
  public double normalize(double);
  public float normalize(float);
  public static double normalizeDegrees(double);
  public static float normalizeDegrees(float);
  public static double normalizeRadians(double);
  public static float normalizeRadians(float);
  public org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit getUnnormalized();
}
```

## class AngularVelocity

```java
public class org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity {
  public org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit angleUnit;
  public float xRotationRate;
  public float yRotationRate;
  public float zRotationRate;
  public long acquisitionTime;
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity();
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit, float, float, float, long);
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float, long);
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity toAngleUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public java.lang.String toString();
}
```

## class AxesOrder

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.AxesOrder extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.AxesOrder> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder XZX;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder XYX;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder YXY;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder YZY;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder ZYZ;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder ZXZ;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder XZY;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder XYZ;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder YXZ;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder YZX;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder ZYX;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesOrder ZXY;
  public static org.firstinspires.ftc.robotcore.external.navigation.AxesOrder[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.AxesOrder valueOf(java.lang.String);
  public int[] indices();
  public org.firstinspires.ftc.robotcore.external.navigation.Axis[] axes();
  public org.firstinspires.ftc.robotcore.external.navigation.AxesOrder reverse();
}
```

## class AxesReference

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.AxesReference extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.AxesReference> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesReference EXTRINSIC;
  public static final org.firstinspires.ftc.robotcore.external.navigation.AxesReference INTRINSIC;
  public static org.firstinspires.ftc.robotcore.external.navigation.AxesReference[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.AxesReference valueOf(java.lang.String);
  public org.firstinspires.ftc.robotcore.external.navigation.AxesReference reverse();
}
```

## class Axis

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.Axis extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.Axis> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.Axis X;
  public static final org.firstinspires.ftc.robotcore.external.navigation.Axis Y;
  public static final org.firstinspires.ftc.robotcore.external.navigation.Axis Z;
  public static final org.firstinspires.ftc.robotcore.external.navigation.Axis UNKNOWN;
  public int index;
  public static org.firstinspires.ftc.robotcore.external.navigation.Axis[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.Axis valueOf(java.lang.String);
  public static org.firstinspires.ftc.robotcore.external.navigation.Axis fromIndex(int);
}
```

## class CurrentUnit

```java
public class org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit AMPS;
  public static final org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit MILLIAMPS;
  public static org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit valueOf(java.lang.String);
  public double toAmps(double);
  public double toMilliAmps(double);
  public double convert(double, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
}
```

## class DistanceUnit

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit METER;
  public static final org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit CM;
  public static final org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit MM;
  public static final org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit INCH;
  public final byte bVal;
  public static final double infinity = 1.7976931348623157E308d;
  public static final double mmPerInch = 25.4d;
  public static final double mPerInch = 0.0254d;
  public static org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit valueOf(java.lang.String);
  public double fromMeters(double);
  public double fromInches(double);
  public double fromCm(double);
  public double fromMm(double);
  public double fromUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, double);
  public double toMeters(double);
  public double toInches(double);
  public double toCm(double);
  public double toMm(double);
  public java.lang.String toString(double);
  public java.lang.String toString();
}
```

## class MagneticFlux

```java
public class org.firstinspires.ftc.robotcore.external.navigation.MagneticFlux {
  public double x;
  public double y;
  public double z;
  public long acquisitionTime;
  public org.firstinspires.ftc.robotcore.external.navigation.MagneticFlux();
  public org.firstinspires.ftc.robotcore.external.navigation.MagneticFlux(double, double, double, long);
  public java.lang.String toString();
}
```

## class MotionDetection

```java
public class org.firstinspires.ftc.robotcore.external.navigation.MotionDetection implements android.hardware.SensorEventListener {
  protected org.firstinspires.ftc.robotcore.external.navigation.MotionDetection.Vector gravity;
  protected org.firstinspires.ftc.robotcore.external.navigation.MotionDetection.Vector filter(android.hardware.SensorEvent);
  public org.firstinspires.ftc.robotcore.external.navigation.MotionDetection();
  public org.firstinspires.ftc.robotcore.external.navigation.MotionDetection(double, int);
  public void registerListener(org.firstinspires.ftc.robotcore.external.navigation.MotionDetection.MotionDetectionListener);
  public void purgeListeners();
  public boolean isAvailable();
  public void startListening();
  public void stopListening();
  protected void notifyListeners(double);
  public void onSensorChanged(android.hardware.SensorEvent);
  public void onAccuracyChanged(android.hardware.Sensor, int);
}
```

## interface MotionDetection.MotionDetectionListener

```java
public interface org.firstinspires.ftc.robotcore.external.navigation.MotionDetection.MotionDetectionListener {
  public abstract void onMotionDetected(double);
}
```

## class MotionDetection.Vector

```java
public class org.firstinspires.ftc.robotcore.external.navigation.MotionDetection.Vector {
  public org.firstinspires.ftc.robotcore.external.navigation.MotionDetection.Vector(org.firstinspires.ftc.robotcore.external.navigation.MotionDetection);
  public double magnitude();
}
```

## class NavUtil

```java
public class org.firstinspires.ftc.robotcore.external.navigation.NavUtil {
  public static org.firstinspires.ftc.robotcore.external.navigation.Position plus(org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.Position);
  public static org.firstinspires.ftc.robotcore.external.navigation.Velocity plus(org.firstinspires.ftc.robotcore.external.navigation.Velocity, org.firstinspires.ftc.robotcore.external.navigation.Velocity);
  public static org.firstinspires.ftc.robotcore.external.navigation.Acceleration plus(org.firstinspires.ftc.robotcore.external.navigation.Acceleration, org.firstinspires.ftc.robotcore.external.navigation.Acceleration);
  public static org.firstinspires.ftc.robotcore.external.navigation.Position minus(org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.Position);
  public static org.firstinspires.ftc.robotcore.external.navigation.Velocity minus(org.firstinspires.ftc.robotcore.external.navigation.Velocity, org.firstinspires.ftc.robotcore.external.navigation.Velocity);
  public static org.firstinspires.ftc.robotcore.external.navigation.Acceleration minus(org.firstinspires.ftc.robotcore.external.navigation.Acceleration, org.firstinspires.ftc.robotcore.external.navigation.Acceleration);
  public static org.firstinspires.ftc.robotcore.external.navigation.Position scale(org.firstinspires.ftc.robotcore.external.navigation.Position, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Velocity scale(org.firstinspires.ftc.robotcore.external.navigation.Velocity, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Acceleration scale(org.firstinspires.ftc.robotcore.external.navigation.Acceleration, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Position integrate(org.firstinspires.ftc.robotcore.external.navigation.Velocity, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Velocity integrate(org.firstinspires.ftc.robotcore.external.navigation.Acceleration, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Position meanIntegrate(org.firstinspires.ftc.robotcore.external.navigation.Velocity, org.firstinspires.ftc.robotcore.external.navigation.Velocity);
  public static org.firstinspires.ftc.robotcore.external.navigation.Velocity meanIntegrate(org.firstinspires.ftc.robotcore.external.navigation.Acceleration, org.firstinspires.ftc.robotcore.external.navigation.Acceleration);
}
```

## class Orientation

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Orientation {
  public org.firstinspires.ftc.robotcore.external.navigation.AxesReference axesReference;
  public org.firstinspires.ftc.robotcore.external.navigation.AxesOrder axesOrder;
  public org.firstinspires.ftc.robotcore.external.navigation.AngleUnit angleUnit;
  public float firstAngle;
  public float secondAngle;
  public float thirdAngle;
  public long acquisitionTime;
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation();
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float, long);
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation toAngleUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation toAxesReference(org.firstinspires.ftc.robotcore.external.navigation.AxesReference);
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation toAxesOrder(org.firstinspires.ftc.robotcore.external.navigation.AxesOrder);
  public java.lang.String toString();
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix getRotationMatrix();
  public static org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix getRotationMatrix(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation getOrientation(org.firstinspires.ftc.robotcore.external.matrices.MatrixF, org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation getOrientation(org.firstinspires.ftc.robotcore.external.matrices.MatrixF, org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, org.firstinspires.ftc.robotcore.external.navigation.Orientation.AngleSet);
}
```

## class Orientation.AngleSet

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.Orientation.AngleSet extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.Orientation.AngleSet> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.Orientation.AngleSet THEONE;
  public static final org.firstinspires.ftc.robotcore.external.navigation.Orientation.AngleSet THEOTHER;
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation.AngleSet[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation.AngleSet valueOf(java.lang.String);
}
```

## class Pose2D

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Pose2D {
  protected final double x;
  protected final double y;
  protected final org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit distanceUnit;
  protected final double heading;
  protected final org.firstinspires.ftc.robotcore.external.navigation.AngleUnit headingUnit;
  public org.firstinspires.ftc.robotcore.external.navigation.Pose2D(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, double, double, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, double);
  public double getX(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getY(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getHeading(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public java.lang.String toString();
}
```

## class Pose3D

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Pose3D {
  protected final org.firstinspires.ftc.robotcore.external.navigation.Position position;
  protected final org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles orientation;
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D(org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles);
  public java.lang.String toString();
  public org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles getOrientation();
  public org.firstinspires.ftc.robotcore.external.navigation.Position getPosition();
}
```

## class Position

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Position {
  public org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit unit;
  public double x;
  public double y;
  public double z;
  public long acquisitionTime;
  public org.firstinspires.ftc.robotcore.external.navigation.Position();
  public org.firstinspires.ftc.robotcore.external.navigation.Position(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, double, double, double, long);
  public org.firstinspires.ftc.robotcore.external.navigation.Position toUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public java.lang.String toString();
}
```

## class Quaternion

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Quaternion {
  public float w;
  public float x;
  public float y;
  public float z;
  public long acquisitionTime;
  public static org.firstinspires.ftc.robotcore.external.navigation.Quaternion identityQuaternion();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion(float, float, float, float, long);
  public static org.firstinspires.ftc.robotcore.external.navigation.Quaternion fromMatrix(org.firstinspires.ftc.robotcore.external.matrices.MatrixF, long);
  public float magnitude();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion normalized();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion conjugate();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion congugate();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion inverse();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion multiply(org.firstinspires.ftc.robotcore.external.navigation.Quaternion, long);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF applyToVector(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF toMatrix();
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation toOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public java.lang.String toString();
}
```

## class Rotation

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.Rotation extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.Rotation> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.Rotation CW;
  public static final org.firstinspires.ftc.robotcore.external.navigation.Rotation CCW;
  public static org.firstinspires.ftc.robotcore.external.navigation.Rotation[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.Rotation valueOf(java.lang.String);
}
```

## class TempUnit

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.TempUnit extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.TempUnit> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.TempUnit CELSIUS;
  public static final org.firstinspires.ftc.robotcore.external.navigation.TempUnit FARENHEIT;
  public static final org.firstinspires.ftc.robotcore.external.navigation.TempUnit KELVIN;
  public final byte bVal;
  public static final double zeroCelsiusK = 273.15d;
  public static final double zeroCelsiusF = 32.0d;
  public static final double CperF = 0.5555555555555556d;
  public static org.firstinspires.ftc.robotcore.external.navigation.TempUnit[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.TempUnit valueOf(java.lang.String);
  public double fromCelsius(double);
  public double fromKelvin(double);
  public double fromFarenheit(double);
  public double fromUnit(org.firstinspires.ftc.robotcore.external.navigation.TempUnit, double);
}
```

## class Temperature

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Temperature {
  public org.firstinspires.ftc.robotcore.external.navigation.TempUnit unit;
  public double temperature;
  public long acquisitionTime;
  public org.firstinspires.ftc.robotcore.external.navigation.Temperature();
  public org.firstinspires.ftc.robotcore.external.navigation.Temperature(org.firstinspires.ftc.robotcore.external.navigation.TempUnit, double, long);
  public org.firstinspires.ftc.robotcore.external.navigation.Temperature toUnit(org.firstinspires.ftc.robotcore.external.navigation.TempUnit);
}
```

## class UnnormalizedAngleUnit

```java
public final class org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit DEGREES;
  public static final org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit RADIANS;
  public final byte bVal;
  public static org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit valueOf(java.lang.String);
  public double fromDegrees(double);
  public float fromDegrees(float);
  public double fromRadians(double);
  public float fromRadians(float);
  public double fromUnit(org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit, double);
  public float fromUnit(org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit, float);
  public double fromUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, double);
  public float fromUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float);
  public double toDegrees(double);
  public float toDegrees(float);
  public double toRadians(double);
  public float toRadians(float);
  public org.firstinspires.ftc.robotcore.external.navigation.AngleUnit getNormalized();
}
```

## class Velocity

```java
public class org.firstinspires.ftc.robotcore.external.navigation.Velocity {
  public org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit unit;
  public double xVeloc;
  public double yVeloc;
  public double zVeloc;
  public long acquisitionTime;
  public org.firstinspires.ftc.robotcore.external.navigation.Velocity();
  public org.firstinspires.ftc.robotcore.external.navigation.Velocity(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, double, double, double, long);
  public org.firstinspires.ftc.robotcore.external.navigation.Velocity toUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public java.lang.String toString();
}
```

## class VoltageUnit

```java
public class org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit> {
  public static final org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit VOLTS;
  public static final org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit MILLIVOLTS;
  public static org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit[] values();
  public static org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit valueOf(java.lang.String);
  public double toVolts(double);
  public double toMilliVolts(double);
  public double convert(double, org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit);
}
```

## class YawPitchRollAngles

```java
public class org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles {
  public org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, double, double, double, long);
  public double getYaw();
  public double getYaw(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public double getPitch();
  public double getPitch(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public double getRoll();
  public double getRoll(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public long getAcquisitionTime();
  public java.lang.String toString();
}
```
