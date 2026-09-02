# `org.firstinspires.ftc.vision`

_ftc-sdk 11.1.0 — 10 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class VisionPortal

```java
public abstract class org.firstinspires.ftc.vision.VisionPortal implements org.firstinspires.ftc.robotcore.external.stream.CameraStreamSource {
  public static final int DEFAULT_VIEW_CONTAINER_ID;
  public org.firstinspires.ftc.vision.VisionPortal();
  public static int[] makeMultiPortalView(int, org.firstinspires.ftc.vision.VisionPortal.MultiPortalLayout);
  public static org.firstinspires.ftc.vision.VisionPortal easyCreateWithDefaults(org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection, org.firstinspires.ftc.vision.VisionProcessor...);
  public static org.firstinspires.ftc.vision.VisionPortal easyCreateWithDefaults(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName, org.firstinspires.ftc.vision.VisionProcessor...);
  public abstract void setProcessorEnabled(org.firstinspires.ftc.vision.VisionProcessor, boolean);
  public abstract boolean getProcessorEnabled(org.firstinspires.ftc.vision.VisionProcessor);
  public abstract org.firstinspires.ftc.vision.VisionPortal.CameraState getCameraState();
  public abstract void saveNextFrameRaw(java.lang.String);
  public abstract void stopStreaming();
  public abstract void resumeStreaming();
  public abstract void stopLiveView();
  public abstract void resumeLiveView();
  public abstract float getFps();
  public abstract <T extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl> T getCameraControl(java.lang.Class<T>);
  public abstract void setActiveCamera(org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName);
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName getActiveCamera();
  public abstract void close();
}
```

## class VisionPortal.Builder

```java
public class org.firstinspires.ftc.vision.VisionPortal.Builder {
  public org.firstinspires.ftc.vision.VisionPortal.Builder();
  public org.firstinspires.ftc.vision.VisionPortal.Builder setCamera(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName);
  public org.firstinspires.ftc.vision.VisionPortal.Builder setCamera(org.firstinspires.ftc.robotcore.external.hardware.camera.BuiltinCameraDirection);
  public org.firstinspires.ftc.vision.VisionPortal.Builder setStreamFormat(org.firstinspires.ftc.vision.VisionPortal.StreamFormat);
  public org.firstinspires.ftc.vision.VisionPortal.Builder enableLiveView(boolean);
  public org.firstinspires.ftc.vision.VisionPortal.Builder setAutoStopLiveView(boolean);
  public org.firstinspires.ftc.vision.VisionPortal.Builder setLiveViewContainerId(int);
  public org.firstinspires.ftc.vision.VisionPortal.Builder setCameraResolution(android.util.Size);
  public org.firstinspires.ftc.vision.VisionPortal.Builder addProcessor(org.firstinspires.ftc.vision.VisionProcessor);
  public org.firstinspires.ftc.vision.VisionPortal.Builder addProcessors(org.firstinspires.ftc.vision.VisionProcessor...);
  public org.firstinspires.ftc.vision.VisionPortal.Builder setAutoStartStreamOnBuild(boolean);
  public org.firstinspires.ftc.vision.VisionPortal.Builder setShowStatsOverlay(boolean);
  public org.firstinspires.ftc.vision.VisionPortal build();
}
```

## class VisionPortal.CameraState

```java
public final class org.firstinspires.ftc.vision.VisionPortal.CameraState extends java.lang.Enum<org.firstinspires.ftc.vision.VisionPortal.CameraState> {
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState OPENING_CAMERA_DEVICE;
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState CAMERA_DEVICE_READY;
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState STARTING_STREAM;
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState STREAMING;
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState STOPPING_STREAM;
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState CLOSING_CAMERA_DEVICE;
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState CAMERA_DEVICE_CLOSED;
  public static final org.firstinspires.ftc.vision.VisionPortal.CameraState ERROR;
  public static org.firstinspires.ftc.vision.VisionPortal.CameraState[] values();
  public static org.firstinspires.ftc.vision.VisionPortal.CameraState valueOf(java.lang.String);
}
```

## class VisionPortal.MultiPortalLayout

```java
public final class org.firstinspires.ftc.vision.VisionPortal.MultiPortalLayout extends java.lang.Enum<org.firstinspires.ftc.vision.VisionPortal.MultiPortalLayout> {
  public static final org.firstinspires.ftc.vision.VisionPortal.MultiPortalLayout VERTICAL;
  public static final org.firstinspires.ftc.vision.VisionPortal.MultiPortalLayout HORIZONTAL;
  public static org.firstinspires.ftc.vision.VisionPortal.MultiPortalLayout[] values();
  public static org.firstinspires.ftc.vision.VisionPortal.MultiPortalLayout valueOf(java.lang.String);
}
```

## class VisionPortal.StreamFormat

```java
public final class org.firstinspires.ftc.vision.VisionPortal.StreamFormat extends java.lang.Enum<org.firstinspires.ftc.vision.VisionPortal.StreamFormat> {
  public static final org.firstinspires.ftc.vision.VisionPortal.StreamFormat YUY2;
  public static final org.firstinspires.ftc.vision.VisionPortal.StreamFormat MJPEG;
  public static org.firstinspires.ftc.vision.VisionPortal.StreamFormat[] values();
  public static org.firstinspires.ftc.vision.VisionPortal.StreamFormat valueOf(java.lang.String);
}
```

## class VisionPortalImpl

```java
public class org.firstinspires.ftc.vision.VisionPortalImpl extends org.firstinspires.ftc.vision.VisionPortal {
  protected org.openftc.easyopencv.OpenCvCamera camera;
  protected final int cameraMonitorViewId;
  protected volatile org.firstinspires.ftc.vision.VisionPortal.CameraState cameraState;
  protected org.firstinspires.ftc.vision.VisionProcessor[] processors;
  protected volatile boolean[] processorsEnabled;
  protected volatile org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration calibration;
  protected final boolean autoPauseCameraMonitor;
  protected final boolean autoStartStream;
  protected final boolean showStats;
  protected final java.util.concurrent.Semaphore userStateSemaphore;
  protected final android.util.Size cameraResolution;
  protected final org.firstinspires.ftc.vision.VisionPortal.StreamFormat webcamStreamFormat;
  protected static final org.openftc.easyopencv.OpenCvCameraRotation CAMERA_ROTATION;
  protected java.lang.String captureNextFrame;
  protected final java.lang.Object captureFrameMtx;
  protected org.firstinspires.ftc.vision.VisionPortalImpl.OpModeNotificationsListener opModeNotificationsListener;
  protected static final java.lang.Object viewUseMtx;
  protected static java.util.ArrayList<java.lang.Integer> viewsInUse;
  public org.firstinspires.ftc.vision.VisionPortalImpl(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName, int, boolean, android.util.Size, org.firstinspires.ftc.vision.VisionPortal.StreamFormat, boolean, boolean, org.firstinspires.ftc.vision.VisionProcessor[]);
  protected void startCamera();
  protected void createCamera(org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName, int);
  public void setProcessorEnabled(org.firstinspires.ftc.vision.VisionProcessor, boolean);
  public boolean getProcessorEnabled(org.firstinspires.ftc.vision.VisionProcessor);
  public org.firstinspires.ftc.vision.VisionPortal.CameraState getCameraState();
  public void setActiveCamera(org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName);
  public org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName getActiveCamera();
  public <T extends org.firstinspires.ftc.robotcore.external.hardware.camera.controls.CameraControl> T getCameraControl(java.lang.Class<T>);
  public void getFrameBitmap(org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.function.Consumer<android.graphics.Bitmap>>);
  public void saveNextFrameRaw(java.lang.String);
  public void stopStreaming();
  public void resumeStreaming();
  public void stopLiveView();
  public void resumeLiveView();
  public float getFps();
  public void close();
}
```

## class VisionPortalImpl.OpModeNotificationsListener

```java
public class org.firstinspires.ftc.vision.VisionPortalImpl.OpModeNotificationsListener implements com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications {
  protected org.firstinspires.ftc.vision.VisionPortalImpl.OpModeNotificationsListener(org.firstinspires.ftc.vision.VisionPortalImpl);
  public void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
}
```

## class VisionPortalImpl.ProcessingPipeline

```java
class org.firstinspires.ftc.vision.VisionPortalImpl.ProcessingPipeline extends org.openftc.easyopencv.TimestampedOpenCvPipeline {
  public org.firstinspires.ftc.vision.VisionPortalImpl.ProcessingPipeline(org.firstinspires.ftc.vision.VisionPortalImpl);
  public void init(org.opencv.core.Mat);
  public org.opencv.core.Mat processFrame(org.opencv.core.Mat, long);
  public void onDrawFrame(android.graphics.Canvas, int, int, float, float, java.lang.Object);
}
```

## interface VisionProcessor

```java
public interface org.firstinspires.ftc.vision.VisionProcessor extends org.firstinspires.ftc.vision.VisionProcessorInternal {
}
```

## interface VisionProcessorInternal

```java
interface org.firstinspires.ftc.vision.VisionProcessorInternal {
  public abstract void init(int, int, org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration);
  public abstract java.lang.Object processFrame(org.opencv.core.Mat, long);
  public abstract void onDrawFrame(android.graphics.Canvas, int, int, float, float, java.lang.Object);
}
```
