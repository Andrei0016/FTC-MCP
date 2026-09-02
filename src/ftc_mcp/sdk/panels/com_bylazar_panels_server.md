# `com.bylazar.panels.server`

_panels fullpanels-1.0.12 — 4 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class Socket

```java
public final class com.bylazar.panels.server.Socket extends fi.iki.elonen.NanoWSD {
  public com.bylazar.panels.server.Socket(int);
  public fi.iki.elonen.NanoHTTPD.Response serve(fi.iki.elonen.NanoHTTPD.IHTTPSession);
  protected fi.iki.elonen.NanoWSD.WebSocket openWebSocket(fi.iki.elonen.NanoHTTPD.IHTTPSession);
  public final java.util.Set<com.bylazar.panels.server.Socket.ClientSocket> getClients();
  public final void sendStrings(java.lang.String);
  public final void startServer();
  public final void stopServer();
}
```

## class Socket.ClientSocket

```java
public final class com.bylazar.panels.server.Socket.ClientSocket extends fi.iki.elonen.NanoWSD.WebSocket {
  public com.bylazar.panels.server.Socket.ClientSocket(fi.iki.elonen.NanoHTTPD.IHTTPSession);
  public final java.util.List<com.bylazar.panels.server.SocketTask> getTasks();
  public final void sendString.Panels_release(java.lang.String);
  protected void onOpen();
  protected void onClose(fi.iki.elonen.NanoWSD.WebSocketFrame.CloseCode, java.lang.String, boolean);
  protected void onMessage(fi.iki.elonen.NanoWSD.WebSocketFrame);
  protected void onPong(fi.iki.elonen.NanoWSD.WebSocketFrame);
  protected void onException(java.io.IOException);
  public static final java.util.TimerTask access.getPing.p(com.bylazar.panels.server.Socket.ClientSocket);
}
```

## class SocketTask

```java
public abstract class com.bylazar.panels.server.SocketTask {
  public kotlin.jvm.functions.Function1<? super java.lang.String, kotlin.Unit> send;
  public com.bylazar.panels.server.SocketTask();
  public final kotlin.jvm.functions.Function1<java.lang.String, kotlin.Unit> getSend();
  public final void setSend(kotlin.jvm.functions.Function1<? super java.lang.String, kotlin.Unit>);
  public abstract void onOpen();
  public abstract void onClose();
  public abstract void onException();
  public abstract void onMessage(java.lang.String);
  public abstract void onDetailedMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.String, java.lang.Object);
  public void onAdvancedMessage(fi.iki.elonen.NanoWSD.WebSocketFrame);
}
```

## class StaticServer

```java
public final class com.bylazar.panels.server.StaticServer extends fi.iki.elonen.NanoHTTPD {
  public com.bylazar.panels.server.StaticServer(android.content.Context, int, java.lang.String);
  public final fi.iki.elonen.NanoHTTPD.Response getResponse(java.lang.String, java.lang.String, fi.iki.elonen.NanoHTTPD.Response.Status);
  public static fi.iki.elonen.NanoHTTPD.Response getResponse.default(com.bylazar.panels.server.StaticServer, java.lang.String, java.lang.String, fi.iki.elonen.NanoHTTPD.Response.Status, int, java.lang.Object);
  public final java.lang.String sha256Hex(byte[]);
  public final java.lang.String sha256Hex(java.lang.String);
  public final java.lang.String getResponse();
  public final void setResponse(java.lang.String);
  public final java.lang.String getLastSha();
  public final void setLastSha(java.lang.String);
  public final java.util.Map<java.lang.String, java.lang.String> getPluginSvelteSha256();
  public final void prepareData();
  public fi.iki.elonen.NanoHTTPD.Response serve(fi.iki.elonen.NanoHTTPD.IHTTPSession);
  public final void startServer();
  public final void stopServer();
}
```
