# `com.bylazar.opmodecontrol`

_panels fullpanels-1.0.12 — 7 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class ActiveOpMode

```java
public final class com.bylazar.opmodecontrol.ActiveOpMode {
  public com.bylazar.opmodecontrol.ActiveOpMode(com.bylazar.opmodecontrol.OpModeDetails, com.bylazar.opmodecontrol.OpModeStatus, java.lang.Long);
  public final com.bylazar.opmodecontrol.OpModeDetails getOpMode();
  public final com.bylazar.opmodecontrol.OpModeStatus getStatus();
  public final java.lang.Long getStartTimestamp();
  public final void setStartTimestamp(java.lang.Long);
  public final com.bylazar.opmodecontrol.OpModeDetails component1();
  public final com.bylazar.opmodecontrol.OpModeStatus component2();
  public final java.lang.Long component3();
  public final com.bylazar.opmodecontrol.ActiveOpMode copy(com.bylazar.opmodecontrol.OpModeDetails, com.bylazar.opmodecontrol.OpModeStatus, java.lang.Long);
  public static com.bylazar.opmodecontrol.ActiveOpMode copy.default(com.bylazar.opmodecontrol.ActiveOpMode, com.bylazar.opmodecontrol.OpModeDetails, com.bylazar.opmodecontrol.OpModeStatus, java.lang.Long, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class OpModeControlPluginConfig

```java
public class com.bylazar.opmodecontrol.OpModeControlPluginConfig extends com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.opmodecontrol.OpModeControlPluginConfig();
}
```

## class OpModeDetails

```java
public final class com.bylazar.opmodecontrol.OpModeDetails {
  public com.bylazar.opmodecontrol.OpModeDetails(java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Flavor, org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Source, java.lang.String, java.lang.String);
  public final java.lang.String getName();
  public final void setName(java.lang.String);
  public final java.lang.String getGroup();
  public final void setGroup(java.lang.String);
  public final org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Flavor getFlavour();
  public final void setFlavour(org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Flavor);
  public final org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Source getSource();
  public final void setSource(org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Source);
  public final java.lang.String getDefaultGroup();
  public final void setDefaultGroup(java.lang.String);
  public final java.lang.String getAutoTransition();
  public final void setAutoTransition(java.lang.String);
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Flavor component3();
  public final org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Source component4();
  public final java.lang.String component5();
  public final java.lang.String component6();
  public final com.bylazar.opmodecontrol.OpModeDetails copy(java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Flavor, org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Source, java.lang.String, java.lang.String);
  public static com.bylazar.opmodecontrol.OpModeDetails copy.default(com.bylazar.opmodecontrol.OpModeDetails, java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Flavor, org.firstinspires.ftc.robotcore.internal.opmode.OpModeMeta.Source, java.lang.String, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class OpModeStatus

```java
public final class com.bylazar.opmodecontrol.OpModeStatus extends java.lang.Enum<com.bylazar.opmodecontrol.OpModeStatus> {
  public static final com.bylazar.opmodecontrol.OpModeStatus INIT;
  public static final com.bylazar.opmodecontrol.OpModeStatus RUNNING;
  public static final com.bylazar.opmodecontrol.OpModeStatus STOPPED;
  public static com.bylazar.opmodecontrol.OpModeStatus[] values();
  public static com.bylazar.opmodecontrol.OpModeStatus valueOf(java.lang.String);
  public static kotlin.enums.EnumEntries<com.bylazar.opmodecontrol.OpModeStatus> getEntries();
}
```

## class OpModesList

```java
public final class com.bylazar.opmodecontrol.OpModesList {
  public com.bylazar.opmodecontrol.OpModesList(java.util.List<com.bylazar.opmodecontrol.OpModeDetails>);
  public final java.util.List<com.bylazar.opmodecontrol.OpModeDetails> getOpModes();
  public final java.util.List<com.bylazar.opmodecontrol.OpModeDetails> component1();
  public final com.bylazar.opmodecontrol.OpModesList copy(java.util.List<com.bylazar.opmodecontrol.OpModeDetails>);
  public static com.bylazar.opmodecontrol.OpModesList copy.default(com.bylazar.opmodecontrol.OpModesList, java.util.List, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class Plugin

```java
public final class com.bylazar.opmodecontrol.Plugin extends com.bylazar.panels.plugins.Plugin<com.bylazar.panels.plugins.BasePluginConfig> {
  public static final com.bylazar.opmodecontrol.Plugin INSTANCE;
  public final java.util.List<com.bylazar.opmodecontrol.OpModeDetails> getOpModeList();
  public final void setOpModeList(java.util.List<com.bylazar.opmodecontrol.OpModeDetails>);
  public final com.bylazar.opmodecontrol.OpModeStatus getStatus();
  public final void setStatus(com.bylazar.opmodecontrol.OpModeStatus);
  public final com.qualcomm.robotcore.eventloop.opmode.OpMode getActiveOpMode();
  public final void setActiveOpMode(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public final java.lang.Long getActiveOpModeStartTimestamp();
  public final void setActiveOpModeStartTimestamp(java.lang.Long);
  public final java.lang.String getActiveOpModeName();
  public final void setActiveOpModeName(java.lang.String);
  public final com.bylazar.opmodecontrol.OpModeDetails getActiveOpModeInfo();
  public void onNewClient(com.bylazar.panels.server.Socket.ClientSocket);
  public void onMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.Object);
  public void onRegister(com.bylazar.panels.Panels, android.content.Context);
  public void onAttachEventLoop(com.qualcomm.ftccommon.FtcEventLoop);
  public void onOpModeManager(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl);
  public final void sendActiveOpMode();
  public void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onEnablePanels();
  public void onDisablePanels();
}
```

## class Plugin.FetcherRoutine

```java
public final class com.bylazar.opmodecontrol.Plugin.FetcherRoutine implements java.lang.Runnable {
  public com.bylazar.opmodecontrol.Plugin.FetcherRoutine();
  public void run();
}
```
