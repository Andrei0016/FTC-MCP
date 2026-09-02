# `com.bylazar.panels.plugins`

_panels fullpanels-1.0.12 — 3 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class BasePluginConfig

```java
public class com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.panels.plugins.BasePluginConfig();
  public boolean isDev();
  public void setDev(boolean);
  public boolean isEnabled();
  public void setEnabled(boolean);
}
```

## class Plugin

```java
public abstract class com.bylazar.panels.plugins.Plugin<T extends com.bylazar.panels.plugins.BasePluginConfig> {
  public com.bylazar.panels.plugins.Plugin(T);
  public final T getConfig();
  public final void setConfig(T);
  public final com.bylazar.panels.json.PluginDetails getDetails();
  public final void setDetails(com.bylazar.panels.json.PluginDetails);
  public final java.lang.String getDetailsString();
  public final void setDetailsString(java.lang.String);
  public final boolean isDev();
  public final boolean isEnabled();
  public final boolean getWasRegistered();
  public final void setWasRegistered(boolean);
  public final void setConfig.Panels_release(java.lang.Object);
  public final void log(java.lang.String);
  public final void error(java.lang.String);
  public final void send(java.lang.String, java.lang.Object);
  public final void sendClient(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.Object);
  public final java.lang.String getId();
  public abstract void onRegister(com.bylazar.panels.Panels, android.content.Context);
  public abstract void onAttachEventLoop(com.qualcomm.ftccommon.FtcEventLoop);
  public abstract void onOpModeManager(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl);
  public abstract void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public abstract void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public abstract void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public abstract void onNewClient(com.bylazar.panels.server.Socket.ClientSocket);
  public abstract void onMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.Object);
  public abstract void onEnablePanels();
  public abstract void onDisablePanels();
  public final java.lang.String toInfo.Panels_release();
  public final java.lang.String toDetails.Panels_release();
  public final void registerInternal.Panels_release(com.bylazar.panels.Panels, android.content.Context);
  public final void newClientInternal.Panels_release(com.bylazar.panels.server.Socket.ClientSocket);
  public final void preInitInternal.Panels_release(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public final void preStartInternal.Panels_release(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public final void postStopInternal.Panels_release(com.qualcomm.robotcore.eventloop.opmode.OpMode);
}
```

## class PluginsManager

```java
public final class com.bylazar.panels.plugins.PluginsManager {
  public static final com.bylazar.panels.plugins.PluginsManager INSTANCE;
  public static java.lang.ref.WeakReference<android.content.Context> contextRef;
  public final java.util.Map<java.lang.String, com.bylazar.panels.plugins.Plugin<?>> getPlugins();
  public final java.util.Map<java.lang.String, com.bylazar.panels.json.PluginDetails> getSkippedPlugins();
  public final java.util.Map<java.lang.String, java.lang.String> getSkippedPluginsStrings();
  public final boolean isRegistered();
  public final void setRegistered(boolean);
  public final java.lang.ref.WeakReference<android.content.Context> getContextRef();
  public final void setContextRef(java.lang.ref.WeakReference<android.content.Context>);
  public final com.bylazar.panels.json.PluginDetails loadPluginConfig(android.content.Context, java.lang.String);
  public static com.bylazar.panels.json.PluginDetails loadPluginConfig.default(com.bylazar.panels.plugins.PluginsManager, android.content.Context, java.lang.String, int, java.lang.Object);
  public final java.lang.String loadPluginConfigString(android.content.Context, java.lang.String);
  public final void init(android.content.Context);
}
```
