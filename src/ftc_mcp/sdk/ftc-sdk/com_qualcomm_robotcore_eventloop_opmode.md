# `com.qualcomm.robotcore.eventloop.opmode`

_ftc-sdk 11.1.0 — 22 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface AnnotatedOpModeManager

```java
public interface com.qualcomm.robotcore.eventloop.opmode.AnnotatedOpModeManager extends com.qualcomm.robotcore.eventloop.opmode.OpModeManager {
  public abstract void register(java.lang.Class);
}
```

## class AnnotatedOpModeRegistrar

```java
public class com.qualcomm.robotcore.eventloop.opmode.AnnotatedOpModeRegistrar {
  public com.qualcomm.robotcore.eventloop.opmode.AnnotatedOpModeRegistrar();
  public static void register(com.qualcomm.robotcore.eventloop.opmode.OpModeManager);
}
```

## interface Autonomous

```java
public interface com.qualcomm.robotcore.eventloop.opmode.Autonomous extends java.lang.annotation.Annotation {
  public abstract java.lang.String name();
  public abstract java.lang.String group();
  public abstract java.lang.String preselectTeleOp();
}
```

## interface Disabled

```java
public interface com.qualcomm.robotcore.eventloop.opmode.Disabled extends java.lang.annotation.Annotation {
}
```

## interface EventLoopManagerClient

```java
public interface com.qualcomm.robotcore.eventloop.opmode.EventLoopManagerClient {
  public abstract com.qualcomm.robotcore.util.WebServer getWebServer();
  public abstract org.firstinspires.ftc.robotcore.internal.opmode.OnBotJavaHelper getOnBotJavaHelper();
}
```

## interface FtcRobotControllerServiceState

```java
public interface com.qualcomm.robotcore.eventloop.opmode.FtcRobotControllerServiceState extends com.qualcomm.robotcore.eventloop.opmode.EventLoopManagerClient {
  public abstract com.qualcomm.robotcore.eventloop.EventLoopManager getEventLoopManager();
}
```

## class LinearOpMode

```java
public abstract class com.qualcomm.robotcore.eventloop.opmode.LinearOpMode extends com.qualcomm.robotcore.eventloop.opmode.OpMode {
  public com.qualcomm.robotcore.eventloop.opmode.LinearOpMode();
  public abstract void runOpMode() throws java.lang.InterruptedException;
  public void waitForStart();
  public final void idle();
  public final void sleep(long);
  public final boolean opModeIsActive();
  public final boolean opModeInInit();
  public final boolean isStarted();
  public final boolean isStopRequested();
  public final void init();
  public final void init_loop();
  public final void start();
  public final void loop();
  public final void stop();
}
```

## class OpMode

```java
public abstract class com.qualcomm.robotcore.eventloop.opmode.OpMode extends com.qualcomm.robotcore.eventloop.opmode.OpModeInternal {
  public static final java.util.HashMap<java.lang.String, java.lang.Object> blackboard;
  public volatile double time;
  public int msStuckDetectInit;
  public int msStuckDetectInitLoop;
  public int msStuckDetectStart;
  public int msStuckDetectLoop;
  public com.qualcomm.robotcore.eventloop.opmode.OpMode();
  public abstract void init();
  public void init_loop();
  public void start();
  public abstract void loop();
  public void stop();
  public final void terminateOpModeNow();
  public double getRuntime();
  public void resetRuntime();
  public void updateTelemetry(org.firstinspires.ftc.robotcore.external.Telemetry);
  public final void internalUpdateTelemetryNow(com.qualcomm.robotcore.robocol.TelemetryMessage);
  public void internalPreInit();
  public void internalPostInitLoop();
  public void internalPostLoop();
}
```

## class OpModeInternal

```java
abstract class com.qualcomm.robotcore.eventloop.opmode.OpModeInternal {
  public static final int MS_BEFORE_FORCE_STOP_AFTER_STOP_REQUESTED = 900;
  public volatile com.qualcomm.robotcore.hardware.Gamepad gamepad1;
  public volatile com.qualcomm.robotcore.hardware.Gamepad gamepad2;
  public org.firstinspires.ftc.robotcore.external.Telemetry telemetry;
  public volatile com.qualcomm.robotcore.hardware.HardwareMap hardwareMap;
  public int msStuckDetectStop;
  public final void requestOpModeStop();
}
```

## interface OpModeManager

```java
public interface com.qualcomm.robotcore.eventloop.opmode.OpModeManager {
  public static final java.lang.String DEFAULT_OP_MODE_NAME = ".Stop.Robot.";
  public abstract void register(java.lang.String, java.lang.Class<? extends com.qualcomm.robotcore.eventloop.opmode.OpMode>);
  public abstract void register(org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta, java.lang.Class<? extends com.qualcomm.robotcore.eventloop.opmode.OpMode>);
  public abstract void register(java.lang.String, com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public abstract void register(org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta, com.qualcomm.robotcore.eventloop.opmode.OpMode);
}
```

## class OpModeManagerImpl

```java
public class com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl implements org.firstinspires.ftc.robotcore.internal.opmode.OpModeServices,com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier {
  protected static int matchNumber;
  protected static volatile boolean preventDangerousHardwareAccess;
  public static final java.lang.String TAG = "OpModeManager";
  public static final java.lang.String DEFAULT_OP_MODE_NAME = ".Stop.Robot.";
  protected android.content.Context context;
  protected java.lang.String activeOpModeName;
  protected com.qualcomm.robotcore.eventloop.opmode.OpModeInternal activeOpMode;
  protected org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta queuedOpModeMetadata;
  protected com.qualcomm.robotcore.hardware.HardwareMap hardwareMap;
  protected com.qualcomm.robotcore.eventloop.EventLoopManager eventLoopManager;
  protected final com.qualcomm.robotcore.util.WeakReferenceSet<com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications> listeners;
  protected com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStuckCodeMonitor stuckMonitor;
  protected boolean peerWasConnected;
  protected com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeState opModeState;
  protected boolean opModeSwapNeeded;
  protected boolean callToInitNeeded;
  protected boolean callToStartNeeded;
  protected boolean gamepadResetNeeded;
  protected boolean telemetryClearNeeded;
  protected java.util.concurrent.atomic.AtomicReference<com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStateTransition> nextOpModeState;
  protected static final java.util.WeakHashMap<android.app.Activity, com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl> mapActivityToOpModeManager;
  public static boolean shouldPreventDangerousHardwareAccess();
  public com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl(android.app.Activity, com.qualcomm.robotcore.hardware.HardwareMap);
  public static com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl getOpModeManagerOfActivity(android.app.Activity);
  public void init(com.qualcomm.robotcore.eventloop.EventLoopManager);
  public void teardown();
  public com.qualcomm.robotcore.eventloop.opmode.OpMode registerListener(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications);
  public void unregisterListener(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications);
  protected void setActiveOpMode(com.qualcomm.robotcore.eventloop.opmode.OpMode, java.lang.String);
  public void setHardwareMap(com.qualcomm.robotcore.hardware.HardwareMap);
  public com.qualcomm.robotcore.hardware.HardwareMap getHardwareMap();
  public com.qualcomm.robotcore.robot.RobotState getRobotState();
  public java.lang.String getActiveOpModeName();
  public com.qualcomm.robotcore.eventloop.opmode.OpMode getActiveOpMode();
  protected void doMatchLoggingWork(java.lang.String, boolean);
  public void setMatchNumber(int);
  public void initOpMode(java.lang.String);
  public void initOpMode(java.lang.String, boolean);
  public void startActiveOpMode();
  public void stopActiveOpMode();
  public void runActiveOpMode(com.qualcomm.robotcore.hardware.Gamepad[], com.qualcomm.robotcore.hardware.Gamepad, com.qualcomm.robotcore.hardware.Gamepad);
  protected void resetHardwareForOpMode();
  protected void callActiveOpModeStop();
  protected void detectStuck(int, java.lang.String, java.lang.Runnable);
  protected void detectStuck(int, java.lang.String, java.lang.Runnable, boolean);
  protected void callActiveOpModeInit();
  protected void callActiveOpModeStart();
  protected void checkOnActiveOpMode();
  protected void handleUserCodeException(java.lang.Exception);
  protected void handleSendStacktrace(java.lang.Exception);
  public static void updateTelemetryNow(com.qualcomm.robotcore.eventloop.opmode.OpMode, com.qualcomm.robotcore.robocol.TelemetryMessage);
  public void refreshUserTelemetry(com.qualcomm.robotcore.robocol.TelemetryMessage, double);
  public void requestOpModeStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
}
```

## class OpModeManagerImpl.DefaultOpMode

```java
public class com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.DefaultOpMode extends com.qualcomm.robotcore.eventloop.opmode.OpMode {
  public com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.DefaultOpMode();
  public void init();
  public void init_loop();
  public void loop();
  public void stop();
}
```

## class OpModeManagerImpl.ForceStopException

```java
public class com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.ForceStopException extends java.lang.RuntimeException {
  public com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.ForceStopException();
}
```

## class OpModeManagerImpl.OpModeState

```java
public final class com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeState extends java.lang.Enum<com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeState> {
  public static final com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeState INIT;
  public static final com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeState LOOPING;
  public static com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeState[] values();
  public static com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeState valueOf(java.lang.String);
}
```

## class OpModeManagerImpl.OpModeStateTransition

```java
class com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStateTransition {
}
```

## class OpModeManagerImpl.OpModeStuckCodeMonitor

```java
public class com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStuckCodeMonitor {
  protected com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStuckCodeMonitor(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl);
  public void startMonitoring(int, java.lang.String, boolean);
  public void stopMonitoring();
  public void shutdown();
  protected boolean checkForDebugger();
}
```

## class OpModeManagerImpl.OpModeStuckCodeMonitor.Runner

```java
public class com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStuckCodeMonitor.Runner implements java.lang.Runnable {
  protected com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStuckCodeMonitor.Runner(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl.OpModeStuckCodeMonitor);
  public void run();
}
```

## interface OpModeManagerNotifier

```java
public interface com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier {
  public abstract com.qualcomm.robotcore.eventloop.opmode.OpMode registerListener(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications);
  public abstract void unregisterListener(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications);
}
```

## interface OpModeManagerNotifier.Notifications

```java
public interface com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications {
  public abstract void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public abstract void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public abstract void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
}
```

## interface OpModeRegister

```java
public interface com.qualcomm.robotcore.eventloop.opmode.OpModeRegister {
  public abstract void register(com.qualcomm.robotcore.eventloop.opmode.OpModeManager);
}
```

## interface OpModeRegistrar

```java
public interface com.qualcomm.robotcore.eventloop.opmode.OpModeRegistrar extends java.lang.annotation.Annotation {
}
```

## interface TeleOp

```java
public interface com.qualcomm.robotcore.eventloop.opmode.TeleOp extends java.lang.annotation.Annotation {
  public abstract java.lang.String name();
  public abstract java.lang.String group();
}
```
