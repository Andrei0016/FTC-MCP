# `org.firstinspires.ftc.robotcore.external.stream`

_ftc-sdk 11.1.0 — 5 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class CameraStreamClient

```java
public class org.firstinspires.ftc.robotcore.external.stream.CameraStreamClient {
  public static org.firstinspires.ftc.robotcore.external.stream.CameraStreamClient getInstance();
  public synchronized void setListener(org.firstinspires.ftc.robotcore.external.stream.CameraStreamClient.Listener);
  public boolean isStreamAvailable();
  public org.firstinspires.ftc.robotcore.internal.network.CallbackResult handleStreamChange(java.lang.String);
  public org.firstinspires.ftc.robotcore.internal.network.CallbackResult handleReceiveFrameBegin(java.lang.String);
  public org.firstinspires.ftc.robotcore.internal.network.CallbackResult handleReceiveFrameChunk(java.lang.String);
}
```

## interface CameraStreamClient.Listener

```java
public interface org.firstinspires.ftc.robotcore.external.stream.CameraStreamClient.Listener {
  public abstract void onStreamAvailableChange(boolean);
  public abstract void onFrameBitmap(android.graphics.Bitmap);
}
```

## class CameraStreamClient.PartialFrame

```java
class org.firstinspires.ftc.robotcore.external.stream.CameraStreamClient.PartialFrame {
}
```

## class CameraStreamServer

```java
public class org.firstinspires.ftc.robotcore.external.stream.CameraStreamServer implements com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications {
  public static final int CHUNK_SIZE = 4096;
  public static org.firstinspires.ftc.robotcore.external.stream.CameraStreamServer getInstance();
  public synchronized void setSource(org.firstinspires.ftc.robotcore.external.stream.CameraStreamSource);
  public int getJpegQuality();
  public void setJpegQuality(int);
  public org.firstinspires.ftc.robotcore.internal.network.CallbackResult handleRequestFrame();
  public void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
}
```

## interface CameraStreamSource

```java
public interface org.firstinspires.ftc.robotcore.external.stream.CameraStreamSource {
  public abstract void getFrameBitmap(org.firstinspires.ftc.robotcore.external.function.Continuation<? extends org.firstinspires.ftc.robotcore.external.function.Consumer<android.graphics.Bitmap>>);
}
```
