# `com.pedropathing.util`

_pedro-pathing 2.1.2 — 4 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class FiniteRunAction

```java
public class com.pedropathing.util.FiniteRunAction implements com.pedropathing.paths.callbacks.PathCallback {
  public com.pedropathing.util.FiniteRunAction(com.pedropathing.paths.callbacks.PathCallback);
  public com.pedropathing.util.FiniteRunAction(com.pedropathing.paths.callbacks.PathCallback, int);
  public boolean isCompleted();
  public boolean hasBeenRunOnce();
  public boolean run();
  public void reset();
  public void complete();
  public boolean isReady();
  public void initialize();
  public boolean isInitialized();
  public int getPathIndex();
}
```

## class NanoTimer

```java
public class com.pedropathing.util.NanoTimer {
  public com.pedropathing.util.NanoTimer();
  public void resetTimer();
  public long getElapsedTime();
  public double getElapsedTime(java.util.concurrent.TimeUnit);
  public double getElapsedTimeSeconds();
}
```

## class PoseHistory

```java
public class com.pedropathing.util.PoseHistory {
  public com.pedropathing.util.PoseHistory(com.pedropathing.localization.PoseTracker);
  public void update();
  public double[] getXPositionsArray();
  public double[] getYPositionsArray();
}
```

## class Timer

```java
public class com.pedropathing.util.Timer {
  public com.pedropathing.util.Timer();
  public void resetTimer();
  public long getElapsedTime();
  public double getElapsedTimeSeconds();
}
```
