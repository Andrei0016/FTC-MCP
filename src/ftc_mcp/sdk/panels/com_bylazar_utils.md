# `com.bylazar.utils`

_panels fullpanels-1.0.12 — 4 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class LoopTimer

```java
public final class com.bylazar.utils.LoopTimer {
  public com.bylazar.utils.LoopTimer(int);
  public com.bylazar.utils.LoopTimer(int, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final long getStartTime();
  public final long getEndTime();
  public final long getMs();
  public final double getHz();
  public final void start();
  public final void end();
  public com.bylazar.utils.LoopTimer();
}
```

## class MovingAverageSmoother

```java
public final class com.bylazar.utils.MovingAverageSmoother {
  public com.bylazar.utils.MovingAverageSmoother(int);
  public final double getValue();
  public final double addValue(double);
  public final void reset();
}
```

## class Plugin

```java
public final class com.bylazar.utils.Plugin extends com.bylazar.panels.plugins.Plugin<com.bylazar.utils.UtilsPluginConfig> {
  public static final com.bylazar.utils.Plugin INSTANCE;
  public void onNewClient(com.bylazar.panels.server.Socket.ClientSocket);
  public void onMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.Object);
  public void onRegister(com.bylazar.panels.Panels, android.content.Context);
  public void onAttachEventLoop(com.qualcomm.ftccommon.FtcEventLoop);
  public void onOpModeManager(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl);
  public void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onEnablePanels();
  public void onDisablePanels();
}
```

## class UtilsPluginConfig

```java
public class com.bylazar.utils.UtilsPluginConfig extends com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.utils.UtilsPluginConfig();
}
```
