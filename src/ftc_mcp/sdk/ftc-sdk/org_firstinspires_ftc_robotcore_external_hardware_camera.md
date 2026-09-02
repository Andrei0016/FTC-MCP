# `org.firstinspires.ftc.robotcore.external.hardware.camera`

_ftc-sdk 11.1.0 — 23 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class BuiltinCameraDirection

```java
public final class org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection> {
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection BACK;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection FRONT;
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection[] values();
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection valueOf(java.lang.String);
}
```

## interface BuiltinCameraName

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraName extends org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName {
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection getCameraDirection();
}
```

## interface Camera

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.Camera extends org.firstinspires.ftc.robotcore.external.hardware.camera.CameraControls {
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName getCameraName();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureRequest createCaptureRequest(int, org.firstinspires.ftc.robotcore.external.android.util.Size, int) throws org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException;
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession createCaptureSession(org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StateCallback>) throws org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException;
  public abstract void close();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.Camera dup();
}
```

## class Camera.Error

```java
public final class org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error> {
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error None;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error OtherError;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error Disconnected;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error Connected;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error StreamingRequestNotSupported;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error Timeout;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error InternalError;
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error[] values();
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error valueOf(java.lang.String);
}
```

## class Camera.OpenFailure

```java
public final class org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure> {
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure None;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure OtherFailure;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure CameraTypeNotSupported;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure InUseOrAccessDenied;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure Disconnected;
  public static final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure InternalError;
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure[] values();
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure valueOf(java.lang.String);
}
```

## interface Camera.StateCallback

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.StateCallback {
  public abstract void onOpened(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera);
  public abstract void onOpenFailed(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName, org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure);
  public abstract void onClosed(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera);
  public abstract void onError(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera, org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error);
}
```

## class Camera.StateCallbackDefault

```java
public class org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.StateCallbackDefault implements org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.StateCallback {
  public org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.StateCallbackDefault();
  public void onOpened(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera);
  public void onOpenFailed(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName, org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.OpenFailure);
  public void onClosed(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera);
  public void onError(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera, org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error);
}
```

## interface CameraCaptureRequest

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureRequest {
  public abstract int getAndroidFormat();
  public abstract org.firstinspires.ftc.robotcore.external.android.util.Size getSize();
  public abstract long getNsFrameDuration();
  public abstract int getFramesPerSecond();
  public abstract android.graphics.Bitmap createEmptyBitmap();
}
```

## interface CameraCaptureSequenceId

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSequenceId {
  public abstract int getIdValue();
}
```

## interface CameraCaptureSession

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession {
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.Camera getCamera();
  public abstract void close();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSequenceId startCapture(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureRequest, org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.CaptureCallback, org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StatusCallback>) throws org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException;
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSequenceId startCapture(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureRequest, org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.CaptureCallback>, org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StatusCallback>) throws org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException;
  public abstract void stopCapture();
}
```

## interface CameraCaptureSession.CaptureCallback

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.CaptureCallback {
  public abstract void onNewFrame(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession, org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureRequest, org.firstinspires.ftc.robotcore.external.hardware.camera.CameraFrame);
}
```

## interface CameraCaptureSession.StateCallback

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StateCallback {
  public abstract void onConfigured(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession);
  public abstract void onClosed(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession);
}
```

## class CameraCaptureSession.StateCallbackDefault

```java
public abstract class org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StateCallbackDefault implements org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StateCallback {
  public org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StateCallbackDefault();
  public void onConfigured(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession);
  public void onClosed(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession);
}
```

## interface CameraCaptureSession.StatusCallback

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession.StatusCallback {
  public abstract void onCaptureSequenceCompleted(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSession, org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSequenceId, long);
}
```

## interface CameraCharacteristics

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCharacteristics {
  public abstract int[] getAndroidFormats();
  public abstract org.firstinspires.ftc.robotcore.external.android.util.Size[] getSizes(int);
  public abstract org.firstinspires.ftc.robotcore.external.android.util.Size getDefaultSize(int);
  public abstract long getMinFrameDuration(int, org.firstinspires.ftc.robotcore.external.android.util.Size);
  public abstract int getMaxFramesPerSecond(int, org.firstinspires.ftc.robotcore.external.android.util.Size);
  public abstract java.util.List<org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCharacteristics.CameraMode> getAllCameraModes();
}
```

## class CameraCharacteristics.CameraMode

```java
public class org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCharacteristics.CameraMode {
  public final int androidFormat;
  public final org.firstinspires.ftc.robotcore.external.android.util.Size size;
  public final long nsFrameDuration;
  public final int fps;
  public final boolean isDefaultSize;
  public org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCharacteristics.CameraMode(int, org.firstinspires.ftc.robotcore.external.android.util.Size, long, boolean);
  public java.lang.String toString();
  public boolean equals(java.lang.Object);
  public int hashCode();
}
```

## interface CameraControls

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraControls {
  public abstract <T extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl> T getControl(java.lang.Class<T>);
}
```

## class CameraException

```java
public class org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException extends java.lang.Exception {
  public final org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error error;
  public org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error);
  public org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error, java.lang.Throwable);
  public org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error, java.lang.String, java.lang.Object...);
  public org.firstinspires.ftc.robotcore.external.hardware.camera.CameraException(org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.Error, java.lang.Throwable, java.lang.String, java.lang.Object...);
}
```

## interface CameraFrame

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraFrame {
  public static final long UnknownFrameNumber = -1l;
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureRequest getRequest();
  public abstract long getFrameNumber();
  public abstract org.firstinspires.ftc.robotcore.external.android.util.Size getSize();
  public abstract int getImageSize();
  public abstract byte[] getImageData();
  public abstract byte[] getImageData(byte[]);
  public abstract long getImageBuffer();
  public abstract long getCaptureTime();
  public abstract org.firstinspires.ftc.robotcore.internal.camera.libuvc.constants.UvcFrameFormat getUvcFrameFormat();
  public abstract int getStride();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCaptureSequenceId getCaptureSequenceId();
  public abstract void copyToBitmap(android.graphics.Bitmap);
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraFrame copy();
  public abstract void addRef();
  public abstract int releaseRef();
}
```

## interface CameraManager

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraManager {
  public abstract java.util.List<org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName> getAllWebcams();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName nameFromCameraDirection(org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection);
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName nameForUnknownCamera();
  public abstract org.firstinspires.ftc.robotcore.internal.camera.delegating.SwitchableCameraName nameForSwitchableCamera(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName...);
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.Camera requestPermissionAndOpenCamera(org.firstinspires.ftc.robotcore.internal.system.Deadline, org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName, org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.StateCallback>);
  public abstract void asyncOpenCameraAssumingPermission(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName, org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.hardware.camera.Camera.StateCallback>, long, java.util.concurrent.TimeUnit);
}
```

## interface CameraName

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName {
  public abstract boolean isWebcam();
  public abstract boolean isCameraDirection();
  public abstract boolean isSwitchable();
  public abstract boolean isUnknown();
  public abstract void asyncRequestCameraPermission(android.content.Context, org.firstinspires.ftc.robotcore.internal.system.Deadline, org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.function.Consumer<java.lang.Boolean>>);
  public abstract boolean requestCameraPermission(org.firstinspires.ftc.robotcore.internal.system.Deadline);
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraCharacteristics getCameraCharacteristics();
}
```

## interface SwitchableCamera

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.SwitchableCamera extends org.firstinspires.ftc.robotcore.external.hardware.camera.Camera {
  public abstract void setActiveCamera(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName);
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName getActiveCamera();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName[] getMembers();
}
```

## interface WebcamName

```java
public interface org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName extends org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName,com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public abstract java.lang.String getUsbDeviceNameIfAttached();
  public abstract boolean isAttached();
}
```
