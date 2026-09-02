# `com.bylazar.telemetry`

_panels fullpanels-1.0.12 — 7 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class ExampleObject

```java
public final class com.bylazar.telemetry.ExampleObject {
  public com.bylazar.telemetry.ExampleObject(java.lang.String);
  public final java.lang.String getData();
  public final java.lang.String component1();
  public final com.bylazar.telemetry.ExampleObject copy(java.lang.String);
  public static com.bylazar.telemetry.ExampleObject copy.default(com.bylazar.telemetry.ExampleObject, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class JoinedTelemetry

```java
public final class com.bylazar.telemetry.JoinedTelemetry implements org.firstinspires.ftc.robotcore.external.Telemetry {
  public com.bylazar.telemetry.JoinedTelemetry(org.firstinspires.ftc.robotcore.external.Telemetry...);
  public org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, java.lang.Object...);
  public org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.Object);
  public <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public boolean update();
  public java.lang.String getItemSeparator();
  public void setItemSeparator(java.lang.String);
  public java.lang.String getCaptionValueSeparator();
  public void setCaptionValueSeparator(java.lang.String);
  public boolean removeItem(org.firstinspires.ftc.robotcore.external.Telemetry.Item);
  public void clear();
  public void clearAll();
  public org.firstinspires.ftc.robotcore.external.Telemetry.Line addLine();
  public org.firstinspires.ftc.robotcore.external.Telemetry.Line addLine(java.lang.String);
  public boolean removeLine(org.firstinspires.ftc.robotcore.external.Telemetry.Line);
  public boolean isAutoClear();
  public void setAutoClear(boolean);
  public int getMsTransmissionInterval();
  public void setMsTransmissionInterval(int);
  public void setDisplayFormat(org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat);
  public org.firstinspires.ftc.robotcore.external.Telemetry.Log log();
  public java.lang.Object addAction(java.lang.Runnable);
  public boolean removeAction(java.lang.Object);
  public void speak(java.lang.String);
  public void speak(java.lang.String, java.lang.String, java.lang.String);
}
```

## class PanelsTelemetry

```java
public final class com.bylazar.telemetry.PanelsTelemetry {
  public static final com.bylazar.telemetry.PanelsTelemetry INSTANCE;
  public final com.bylazar.telemetry.TelemetryManager getTelemetry();
  public final com.bylazar.telemetry.TelemetryManager.TelemetryWrapper getFtcTelemetry();
}
```

## class Plugin

```java
public final class com.bylazar.telemetry.Plugin extends com.bylazar.panels.plugins.Plugin<com.bylazar.telemetry.TelemetryPluginConfig> {
  public static final com.bylazar.telemetry.Plugin INSTANCE;
  public final com.bylazar.telemetry.TelemetryManager getManager();
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

## class TelemetryManager

```java
public final class com.bylazar.telemetry.TelemetryManager {
  public com.bylazar.telemetry.TelemetryManager(kotlin.jvm.functions.Function0<? extends com.bylazar.telemetry.TelemetryPluginConfig>, kotlin.jvm.functions.Function1<? super java.util.List<java.lang.String>, kotlin.Unit>, kotlin.jvm.functions.Function1<? super java.lang.Long, kotlin.Unit>);
  public final kotlin.jvm.functions.Function0<com.bylazar.telemetry.TelemetryPluginConfig> getConfig();
  public final java.util.List<java.lang.String> getLines();
  public final void setLines(java.util.List<java.lang.String>);
  public final java.util.List<java.lang.String> getLastLines.Telemetry_release();
  public final void setLastLines.Telemetry_release(java.util.List<java.lang.String>);
  public final long getUpdateInterval();
  public final void setUpdateInterval(long);
  public final long getLastUpdate();
  public final void setLastUpdate(long);
  public final long getTimeSinceLastUpdate();
  public final boolean getShouldUpdateLines();
  public final void addData(java.lang.String, java.lang.Object);
  public final void addData(java.lang.String, java.lang.String);
  public final void addLine(java.lang.String);
  public final void debug(java.lang.String...);
  public final void debug(java.lang.Object...);
  public final void update();
  public final void update(org.firstinspires.ftc.robotcore.external.Telemetry);
  public final com.bylazar.telemetry.TelemetryManager.TelemetryWrapper getWrapper();
}
```

## class TelemetryManager.TelemetryWrapper

```java
public final class com.bylazar.telemetry.TelemetryManager.TelemetryWrapper implements org.firstinspires.ftc.robotcore.external.Telemetry {
  public com.bylazar.telemetry.TelemetryManager.TelemetryWrapper();
  public org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, java.lang.Object...);
  public org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.Object);
  public <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public boolean update();
  public java.lang.String getItemSeparator();
  public void setItemSeparator(java.lang.String);
  public java.lang.String getCaptionValueSeparator();
  public void setCaptionValueSeparator(java.lang.String);
  public org.firstinspires.ftc.robotcore.external.Telemetry.Line addLine();
  public org.firstinspires.ftc.robotcore.external.Telemetry.Line addLine(java.lang.String);
  public void setMsTransmissionInterval(int);
  public boolean removeItem(org.firstinspires.ftc.robotcore.external.Telemetry.Item);
  public void clear();
  public void clearAll();
  public boolean removeLine(org.firstinspires.ftc.robotcore.external.Telemetry.Line);
  public boolean isAutoClear();
  public void setAutoClear(boolean);
  public int getMsTransmissionInterval();
  public void setDisplayFormat(org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat);
  public org.firstinspires.ftc.robotcore.external.Telemetry.Log log();
  public java.lang.Object addAction(java.lang.Runnable);
  public boolean removeAction(java.lang.Object);
  public void speak(java.lang.String);
  public void speak(java.lang.String, java.lang.String, java.lang.String);
}
```

## class TelemetryPluginConfig

```java
public class com.bylazar.telemetry.TelemetryPluginConfig extends com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.telemetry.TelemetryPluginConfig();
  public long getTelemetryUpdateInterval();
  public void setTelemetryUpdateInterval(long);
}
```
