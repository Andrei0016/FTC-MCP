# `org.firstinspires.ftc.ftccommon.external`

_ftc-sdk 11.1.0 — 8 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface OnCreate

```java
public interface org.firstinspires.ftc.ftccommon.external.OnCreate extends java.lang.annotation.Annotation {
}
```

## interface OnCreateEventLoop

```java
public interface org.firstinspires.ftc.ftccommon.external.OnCreateEventLoop extends java.lang.annotation.Annotation {
}
```

## interface OnCreateMenu

```java
public interface org.firstinspires.ftc.ftccommon.external.OnCreateMenu extends java.lang.annotation.Annotation {
}
```

## interface OnDestroy

```java
public interface org.firstinspires.ftc.ftccommon.external.OnDestroy extends java.lang.annotation.Annotation {
}
```

## interface RobotStateMonitor

```java
public interface org.firstinspires.ftc.ftccommon.external.RobotStateMonitor {
  public abstract void updateRobotState(com.qualcomm.robotcore.robot.RobotState);
  public abstract void updateRobotStatus(com.qualcomm.robotcore.robot.RobotStatus);
  public abstract void updatePeerStatus(org.firstinspires.ftc.robotcore.internal.network.PeerStatus);
  public abstract void updateNetworkStatus(org.firstinspires.ftc.robotcore.internal.network.NetworkStatus, java.lang.String);
  public abstract void updateErrorMessage(java.lang.String);
  public abstract void updateWarningMessage(com.qualcomm.robotcore.util.RobotLog.GlobalWarningMessage);
}
```

## class SoundPlayingRobotMonitor

```java
public class org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor implements org.firstinspires.ftc.ftccommon.external.RobotStateMonitor {
  public static boolean DEBUG;
  protected android.content.Context context;
  protected com.qualcomm.robotcore.robot.RobotState robotState;
  protected com.qualcomm.robotcore.robot.RobotStatus robotStatus;
  protected org.firstinspires.ftc.robotcore.internal.network.NetworkStatus networkStatus;
  protected org.firstinspires.ftc.robotcore.internal.network.PeerStatus peerStatus;
  protected java.lang.String errorMessage;
  protected java.lang.String warningMessageString;
  protected org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound lastSoundPlayed;
  protected java.util.concurrent.atomic.AtomicInteger runningsInFlight;
  public static int soundConnect;
  public static int soundDisconnect;
  public static int soundRunning;
  public static int soundWarning;
  public static int soundError;
  public org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor();
  public org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor(android.content.Context);
  public static void prefillSoundCache();
  protected void playConnect();
  protected void playDisconnect();
  protected void playRunning();
  protected void playWarning();
  protected void playError();
  public synchronized void updateRobotState(com.qualcomm.robotcore.robot.RobotState);
  public synchronized void updateRobotStatus(com.qualcomm.robotcore.robot.RobotStatus);
  public void updatePeerStatus(org.firstinspires.ftc.robotcore.internal.network.PeerStatus);
  public synchronized void updateNetworkStatus(org.firstinspires.ftc.robotcore.internal.network.NetworkStatus, java.lang.String);
  public synchronized void updateErrorMessage(java.lang.String);
  public synchronized void updateWarningMessage(com.qualcomm.robotcore.util.RobotLog.GlobalWarningMessage);
  protected void playSound(org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound, int);
  protected void playSound(org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound, int, org.firstinspires.ftc.robotcore.external.function.Consumer<java.lang.Integer>, java.lang.Runnable);
}
```

## class SoundPlayingRobotMonitor.Sound

```java
public final class org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound extends java.lang.Enum<org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound> {
  public static final org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound None;
  public static final org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound Connect;
  public static final org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound Disconnect;
  public static final org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound Running;
  public static final org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound Warning;
  public static final org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound Error;
  public static org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound[] values();
  public static org.firstinspires.ftc.ftccommon.external.SoundPlayingRobotMonitor.Sound valueOf(java.lang.String);
}
```

## interface WebHandlerRegistrar

```java
public interface org.firstinspires.ftc.ftccommon.external.WebHandlerRegistrar extends java.lang.annotation.Annotation {
}
```
