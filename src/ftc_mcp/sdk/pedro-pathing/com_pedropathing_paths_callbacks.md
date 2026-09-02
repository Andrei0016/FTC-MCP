# `com.pedropathing.paths.callbacks`

_pedro-pathing 2.1.2 — 4 types. Signatures are exact (`javap -protected`); see `reference/pedro-pathing/` for decompiled bodies._

## class ParametricCallback

```java
public class com.pedropathing.paths.callbacks.ParametricCallback implements com.pedropathing.paths.callbacks.PathCallback {
  public com.pedropathing.paths.callbacks.ParametricCallback(int, double, com.pedropathing.follower.Follower, java.lang.Runnable);
  public boolean run();
  public boolean isReady();
  public int getPathIndex();
  public double getStartCondition();
}
```

## interface PathCallback

```java
public interface com.pedropathing.paths.callbacks.PathCallback {
  public abstract boolean run();
  public abstract boolean isReady();
  public default void initialize();
  public default void reset();
  public default boolean isCompleted();
  public abstract int getPathIndex();
}
```

## class PoseCallback

```java
public class com.pedropathing.paths.callbacks.PoseCallback implements com.pedropathing.paths.callbacks.PathCallback {
  public com.pedropathing.paths.callbacks.PoseCallback(com.pedropathing.follower.Follower, int, com.pedropathing.geometry.Pose, java.lang.Runnable, double, com.pedropathing.geometry.Curve);
  public boolean run();
  public boolean isReady();
  public int getPathIndex();
}
```

## class TemporalCallback

```java
public class com.pedropathing.paths.callbacks.TemporalCallback implements com.pedropathing.paths.callbacks.PathCallback {
  public com.pedropathing.paths.callbacks.TemporalCallback(int, double, java.lang.Runnable);
  public boolean run();
  public boolean isReady();
  public void initialize();
  public int getPathIndex();
  public double getStartCondition();
}
```
