# `com.bylazar.panels.server.tasks`

_panels fullpanels-1.0.12 — 2 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class PluginDevTask

```java
public final class com.bylazar.panels.server.tasks.PluginDevTask extends com.bylazar.panels.server.SocketTask {
  public com.bylazar.panels.server.tasks.PluginDevTask();
  public void onOpen();
  public void onException();
  public void onClose();
  public void onMessage(java.lang.String);
  public void onDetailedMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.String, java.lang.Object);
}
```

## class TimeTask

```java
public final class com.bylazar.panels.server.tasks.TimeTask extends com.bylazar.panels.server.SocketTask {
  public com.bylazar.panels.server.tasks.TimeTask();
  public void onOpen();
  public void onException();
  public void onClose();
  public void onMessage(java.lang.String);
  public void onDetailedMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.String, java.lang.Object);
  public final void startSendingTime();
  public final void stopTimer();
}
```
