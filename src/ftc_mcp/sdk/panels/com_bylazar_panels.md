# `com.bylazar.panels`

_panels fullpanels-1.0.12 — 7 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class GlobalStats

```java
public final class com.bylazar.panels.GlobalStats {
  public static final com.bylazar.panels.GlobalStats INSTANCE;
  public static final java.lang.String pluginsCoreVersion = "1.1.43";
}
```

## class Logger

```java
public final class com.bylazar.panels.Logger {
  public static final com.bylazar.panels.Logger INSTANCE;
  public static final java.lang.String REFLECTION_PREFIX = "Reflection";
  public static final java.lang.String SOCKET_PREFIX = "Socket";
  public static final java.lang.String SERVER_PREFIX = "Server";
  public static final java.lang.String PLUGINS_PREFIX = "Plugins";
  public static final java.lang.String CORE_PREFIX = "Core";
  public final void log(java.lang.String, java.lang.String);
  public final void error(java.lang.String, java.lang.String);
  public final void reflectionLog(java.lang.String);
  public final void reflectionError(java.lang.String);
  public final void socketLog(java.lang.String);
  public final void socketError(java.lang.String);
  public final void serverLog(java.lang.String);
  public final void serverError(java.lang.String);
  public final void pluginsLog(java.lang.String);
  public final void pluginsError(java.lang.String);
  public final void coreLog(java.lang.String);
  public final void coreError(java.lang.String);
}
```

## class Panels

```java
public final class com.bylazar.panels.Panels implements com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications {
  public static final com.bylazar.panels.Panels INSTANCE;
  public static com.bylazar.panels.server.StaticServer server;
  public static com.bylazar.panels.server.Socket socket;
  public final com.bylazar.panels.server.StaticServer getServer();
  public final void setServer(com.bylazar.panels.server.StaticServer);
  public final com.bylazar.panels.server.Socket getSocket();
  public final void setSocket(com.bylazar.panels.server.Socket);
  public final com.bylazar.panels.PanelsConfig getConfig();
  public final void setConfig(com.bylazar.panels.PanelsConfig);
  public final boolean getWasStarted();
  public final void setWasStarted(boolean);
  public static final void registerOpMode(com.qualcomm.robotcore.eventloop.opmode.OpModeManager);
  public final int getClientsCount();
  public final void initPanels.Panels_release(android.content.Context, com.qualcomm.ftccommon.FtcEventLoop);
  public static final void start(android.content.Context);
  public static final void attachWebServer(android.content.Context, com.qualcomm.robotcore.util.WebHandlerManager);
  public static final void attachEventLoop(android.content.Context, com.qualcomm.ftccommon.FtcEventLoop);
  public static final void stop(android.content.Context);
  public void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public final void toggle();
  public final void enable();
  public final void disable();
}
```

## class Panels.StartRoutine

```java
public final class com.bylazar.panels.Panels.StartRoutine implements java.lang.Runnable {
  public com.bylazar.panels.Panels.StartRoutine(android.content.Context, com.qualcomm.ftccommon.FtcEventLoop);
  public final android.content.Context getContext();
  public final com.qualcomm.ftccommon.FtcEventLoop getEventLoop();
  public void run();
}
```

## class PanelsConfig

```java
public class com.bylazar.panels.PanelsConfig {
  public com.bylazar.panels.PanelsConfig();
  public boolean isDisabled();
  public void setDisabled(boolean);
  public boolean getEnableLogs();
  public void setEnableLogs(boolean);
  public boolean getEnableClassCallerLogs();
  public void setEnableClassCallerLogs(boolean);
  public java.lang.String toString();
}
```

## class TaskTimer

```java
public final class com.bylazar.panels.TaskTimer {
  public static final com.bylazar.panels.TaskTimer INSTANCE;
  public final java.util.concurrent.ConcurrentHashMap<java.lang.String, java.lang.Long> getActiveStarts();
  public final java.util.List<com.bylazar.panels.TaskTiming> getRecords();
  public final void clear();
  public final void start(java.lang.String);
  public final com.bylazar.panels.TaskTiming end(java.lang.String);
  public final <T> T measure(java.lang.String, kotlin.jvm.functions.Function0<? extends T>);
}
```

## class TaskTiming

```java
public final class com.bylazar.panels.TaskTiming {
  public com.bylazar.panels.TaskTiming(java.lang.String, long, long, long);
  public final java.lang.String getId();
  public final long getStartNanos();
  public final long getEndNanos();
  public final long getDurationMillis();
  public final java.lang.String component1();
  public final long component2();
  public final long component3();
  public final long component4();
  public final com.bylazar.panels.TaskTiming copy(java.lang.String, long, long, long);
  public static com.bylazar.panels.TaskTiming copy.default(com.bylazar.panels.TaskTiming, java.lang.String, long, long, long, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```
