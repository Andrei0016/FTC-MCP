# `com.bylazar.gamepad`

_panels fullpanels-1.0.12 — 8 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class Gamepad

```java
public final class com.bylazar.gamepad.Gamepad {
  public com.bylazar.gamepad.Gamepad(boolean, double, boolean, double, com.bylazar.gamepad.Stick, com.bylazar.gamepad.Stick, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean);
  public com.bylazar.gamepad.Gamepad(boolean, double, boolean, double, com.bylazar.gamepad.Stick, com.bylazar.gamepad.Stick, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final boolean getL1();
  public final void setL1(boolean);
  public final double getL2();
  public final void setL2(double);
  public final boolean getR1();
  public final void setR1(boolean);
  public final double getR2();
  public final void setR2(double);
  public final com.bylazar.gamepad.Stick getLeftStick();
  public final void setLeftStick(com.bylazar.gamepad.Stick);
  public final com.bylazar.gamepad.Stick getRightStick();
  public final void setRightStick(com.bylazar.gamepad.Stick);
  public final boolean getCross();
  public final void setCross(boolean);
  public final boolean getCircle();
  public final void setCircle(boolean);
  public final boolean getSquare();
  public final void setSquare(boolean);
  public final boolean getTriangle();
  public final void setTriangle(boolean);
  public final boolean getDpad_up();
  public final void setDpad_up(boolean);
  public final boolean getDpad_left();
  public final void setDpad_left(boolean);
  public final boolean getDpad_right();
  public final void setDpad_right(boolean);
  public final boolean getDpad_down();
  public final void setDpad_down(boolean);
  public final boolean getTouchpad();
  public final void setTouchpad(boolean);
  public final boolean getOptions();
  public final void setOptions(boolean);
  public final boolean getShare();
  public final void setShare(boolean);
  public final boolean getPs();
  public final void setPs(boolean);
  public final boolean component1();
  public final double component2();
  public final boolean component3();
  public final double component4();
  public final com.bylazar.gamepad.Stick component5();
  public final com.bylazar.gamepad.Stick component6();
  public final boolean component7();
  public final boolean component8();
  public final boolean component9();
  public final boolean component10();
  public final boolean component11();
  public final boolean component12();
  public final boolean component13();
  public final boolean component14();
  public final boolean component15();
  public final boolean component16();
  public final boolean component17();
  public final boolean component18();
  public final com.bylazar.gamepad.Gamepad copy(boolean, double, boolean, double, com.bylazar.gamepad.Stick, com.bylazar.gamepad.Stick, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean);
  public static com.bylazar.gamepad.Gamepad copy.default(com.bylazar.gamepad.Gamepad, boolean, double, boolean, double, com.bylazar.gamepad.Stick, com.bylazar.gamepad.Stick, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, boolean, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.gamepad.Gamepad();
}
```

## class GamepadManager

```java
public final class com.bylazar.gamepad.GamepadManager {
  public com.bylazar.gamepad.GamepadManager();
  public final long getDELETION_INTERVAL();
  public final com.bylazar.gamepad.Gamepad getCurrentState.Gamepad_release();
  public final void setCurrentState.Gamepad_release(com.bylazar.gamepad.Gamepad);
  public final com.bylazar.gamepad.GamepadTimestamps getTimestamps.Gamepad_release();
  public final void setTimestamps.Gamepad_release(com.bylazar.gamepad.GamepadTimestamps);
  public final void update.Gamepad_release(com.bylazar.gamepad.Gamepad);
  public final com.qualcomm.robotcore.hardware.Gamepad asCombinedFTCGamepad(com.qualcomm.robotcore.hardware.Gamepad);
  public final com.qualcomm.robotcore.hardware.Gamepad getAsFTCGamepad();
  public final boolean getL1();
  public final double getL2();
  public final boolean getR1();
  public final double getR2();
  public final boolean getCross();
  public final long getCrossTimestamp();
  public final boolean getCircle();
  public final boolean getSquare();
  public final boolean getTriangle();
  public final boolean getDpadUp();
  public final boolean getDpadLeft();
  public final boolean getDpadRight();
  public final boolean getDpadDown();
  public final boolean getTouchpad();
  public final boolean getOptions();
  public final boolean getShare();
  public final boolean getPs();
  public final double getLeftStickX();
  public final double getLeftStickY();
  public final boolean getLeftStickPressed();
  public final double getRightStickX();
  public final double getRightStickY();
  public final boolean getRightStickPressed();
  public final com.bylazar.gamepad.Stick getLeftStick();
  public final com.bylazar.gamepad.Stick getRightStick();
}
```

## class GamepadPluginConfig

```java
public class com.bylazar.gamepad.GamepadPluginConfig extends com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.gamepad.GamepadPluginConfig();
}
```

## class GamepadTimestamps

```java
public final class com.bylazar.gamepad.GamepadTimestamps {
  public com.bylazar.gamepad.GamepadTimestamps(long, long, long, long, com.bylazar.gamepad.StickTimestamps, com.bylazar.gamepad.StickTimestamps, long, long, long, long, long, long, long, long, long, long, long, long);
  public com.bylazar.gamepad.GamepadTimestamps(long, long, long, long, com.bylazar.gamepad.StickTimestamps, com.bylazar.gamepad.StickTimestamps, long, long, long, long, long, long, long, long, long, long, long, long, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final long getL1();
  public final void setL1(long);
  public final long getL2();
  public final void setL2(long);
  public final long getR1();
  public final void setR1(long);
  public final long getR2();
  public final void setR2(long);
  public final com.bylazar.gamepad.StickTimestamps getLeftStick();
  public final void setLeftStick(com.bylazar.gamepad.StickTimestamps);
  public final com.bylazar.gamepad.StickTimestamps getRightStick();
  public final void setRightStick(com.bylazar.gamepad.StickTimestamps);
  public final long getCross();
  public final void setCross(long);
  public final long getCircle();
  public final void setCircle(long);
  public final long getSquare();
  public final void setSquare(long);
  public final long getTriangle();
  public final void setTriangle(long);
  public final long getDpad_up();
  public final void setDpad_up(long);
  public final long getDpad_left();
  public final void setDpad_left(long);
  public final long getDpad_right();
  public final void setDpad_right(long);
  public final long getDpad_down();
  public final void setDpad_down(long);
  public final long getTouchpad();
  public final void setTouchpad(long);
  public final long getOptions();
  public final void setOptions(long);
  public final long getShare();
  public final void setShare(long);
  public final long getPs();
  public final void setPs(long);
  public final long component1();
  public final long component2();
  public final long component3();
  public final long component4();
  public final com.bylazar.gamepad.StickTimestamps component5();
  public final com.bylazar.gamepad.StickTimestamps component6();
  public final long component7();
  public final long component8();
  public final long component9();
  public final long component10();
  public final long component11();
  public final long component12();
  public final long component13();
  public final long component14();
  public final long component15();
  public final long component16();
  public final long component17();
  public final long component18();
  public final com.bylazar.gamepad.GamepadTimestamps copy(long, long, long, long, com.bylazar.gamepad.StickTimestamps, com.bylazar.gamepad.StickTimestamps, long, long, long, long, long, long, long, long, long, long, long, long);
  public static com.bylazar.gamepad.GamepadTimestamps copy.default(com.bylazar.gamepad.GamepadTimestamps, long, long, long, long, com.bylazar.gamepad.StickTimestamps, com.bylazar.gamepad.StickTimestamps, long, long, long, long, long, long, long, long, long, long, long, long, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.gamepad.GamepadTimestamps();
}
```

## class PanelsGamepad

```java
public final class com.bylazar.gamepad.PanelsGamepad {
  public static final com.bylazar.gamepad.PanelsGamepad INSTANCE;
  public final com.bylazar.gamepad.GamepadManager getFirstManager();
  public final com.bylazar.gamepad.GamepadManager getSecondManager();
}
```

## class Plugin

```java
public final class com.bylazar.gamepad.Plugin extends com.bylazar.panels.plugins.Plugin<com.bylazar.gamepad.GamepadPluginConfig> {
  public static final com.bylazar.gamepad.Plugin INSTANCE;
  public final com.bylazar.gamepad.GamepadManager getFirstManager();
  public final com.bylazar.gamepad.GamepadManager getSecondManager();
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

## class Stick

```java
public final class com.bylazar.gamepad.Stick {
  public com.bylazar.gamepad.Stick(double, double, boolean);
  public com.bylazar.gamepad.Stick(double, double, boolean, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final double getX();
  public final void setX(double);
  public final double getY();
  public final void setY(double);
  public final boolean getValue();
  public final void setValue(boolean);
  public final double component1();
  public final double component2();
  public final boolean component3();
  public final com.bylazar.gamepad.Stick copy(double, double, boolean);
  public static com.bylazar.gamepad.Stick copy.default(com.bylazar.gamepad.Stick, double, double, boolean, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.gamepad.Stick();
}
```

## class StickTimestamps

```java
public final class com.bylazar.gamepad.StickTimestamps {
  public com.bylazar.gamepad.StickTimestamps(long, long, long);
  public com.bylazar.gamepad.StickTimestamps(long, long, long, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final long getX();
  public final void setX(long);
  public final long getY();
  public final void setY(long);
  public final long getValue();
  public final void setValue(long);
  public final long component1();
  public final long component2();
  public final long component3();
  public final com.bylazar.gamepad.StickTimestamps copy(long, long, long);
  public static com.bylazar.gamepad.StickTimestamps copy.default(com.bylazar.gamepad.StickTimestamps, long, long, long, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.gamepad.StickTimestamps();
}
```
