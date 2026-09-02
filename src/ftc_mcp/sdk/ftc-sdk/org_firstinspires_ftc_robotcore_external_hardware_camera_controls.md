# `org.firstinspires.ftc.robotcore.external.hardware.camera.controls`

_ftc-sdk 11.1.0 — 10 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface CameraControl

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl {
}
```

## interface ExposureControl

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl {
  public static final long unknownExposure = 0l;
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode getMode();
  public abstract boolean setMode(org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode);
  public abstract boolean isModeSupported(org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode);
  public abstract long getMinExposure(java.util.concurrent.TimeUnit);
  public abstract long getMaxExposure(java.util.concurrent.TimeUnit);
  public abstract long getExposure(java.util.concurrent.TimeUnit);
  public abstract long getCachedExposure(java.util.concurrent.TimeUnit, org.firstinspires.ftc.robotcore.internal.collections.MutableReference<java.lang.Boolean>, long, java.util.concurrent.TimeUnit);
  public abstract boolean setExposure(long, java.util.concurrent.TimeUnit);
  public abstract boolean isExposureSupported();
  public abstract boolean getAePriority();
  public abstract boolean setAePriority(boolean);
}
```

## class ExposureControl.Mode

```java
public final class org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode> {
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode Unknown;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode Auto;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode ContinuousAuto;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode Manual;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode ShutterPriority;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode AperturePriority;
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode[] values();
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode valueOf(java.lang.String);
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl.Mode fromId(int);
}
```

## interface FocusControl

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl {
  public static final double unknownFocusLength = -1.0d;
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode getMode();
  public abstract boolean setMode(org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode);
  public abstract boolean isModeSupported(org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode);
  public abstract double getMinFocusLength();
  public abstract double getMaxFocusLength();
  public abstract double getFocusLength();
  public abstract boolean setFocusLength(double);
  public abstract boolean isFocusLengthSupported();
}
```

## class FocusControl.Mode

```java
public final class org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode> {
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode Unknown;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode Auto;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode ContinuousAuto;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode Macro;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode Infinity;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode Fixed;
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode[] values();
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode valueOf(java.lang.String);
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.FocusControl.Mode fromId(int);
}
```

## interface GainControl

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.controls.GainControl extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl {
  public abstract int getMinGain();
  public abstract int getMaxGain();
  public abstract int getGain();
  public abstract boolean setGain(int);
}
```

## interface PtzControl

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.controls.PtzControl extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl {
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.controls.PtzControl.PanTiltHolder getPanTilt();
  public abstract boolean setPanTilt(org.firstinspires.ftc.robotcore.external.hardware.camera.controls.PtzControl.PanTiltHolder);
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.controls.PtzControl.PanTiltHolder getMinPanTilt();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.controls.PtzControl.PanTiltHolder getMaxPanTilt();
  public abstract int getZoom();
  public abstract boolean setZoom(int);
  public abstract int getMinZoom();
  public abstract int getMaxZoom();
}
```

## class PtzControl.PanTiltHolder

```java
public class org.firstinspires.ftc.robotcore.external.hardware.camera.controls.PtzControl.PanTiltHolder {
  public int pan;
  public int tilt;
  public org.firstinspires.ftc.robotcore.external.hardware.camera.controls.PtzControl.PanTiltHolder();
}
```

## interface WhiteBalanceControl

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl {
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode getMode();
  public abstract boolean setMode(org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode);
  public abstract int getMinWhiteBalanceTemperature();
  public abstract int getMaxWhiteBalanceTemperature();
  public abstract int getWhiteBalanceTemperature();
  public abstract boolean setWhiteBalanceTemperature(int);
}
```

## class WhiteBalanceControl.Mode

```java
public final class org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode> {
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode UNKNOWN;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode AUTO;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode MANUAL;
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode[] values();
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl.Mode valueOf(java.lang.String);
}
```
