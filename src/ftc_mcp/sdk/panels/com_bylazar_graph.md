# `com.bylazar.graph`

_panels fullpanels-1.0.12 — 2 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class GraphPluginConfig

```java
public class com.bylazar.graph.GraphPluginConfig extends com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.graph.GraphPluginConfig();
}
```

## class Plugin

```java
public final class com.bylazar.graph.Plugin extends com.bylazar.panels.plugins.Plugin<com.bylazar.graph.GraphPluginConfig> {
  public static final com.bylazar.graph.Plugin INSTANCE;
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
