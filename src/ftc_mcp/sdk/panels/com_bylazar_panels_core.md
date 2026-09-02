# `com.bylazar.panels.core`

_panels fullpanels-1.0.12 — 3 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class OpModeHandler

```java
public final class com.bylazar.panels.core.OpModeHandler {
  public static final com.bylazar.panels.core.OpModeHandler INSTANCE;
  public static com.qualcomm.robotcore.eventloop.opmode.OpModeManager manager;
  public final com.qualcomm.robotcore.eventloop.opmode.OpModeManager getManager();
  public final void setManager(com.qualcomm.robotcore.eventloop.opmode.OpModeManager);
  public final void init(com.qualcomm.robotcore.eventloop.opmode.OpModeManager);
  public final void registerOpMode();
}
```

## class PreferencesHandler

```java
public final class com.bylazar.panels.core.PreferencesHandler {
  public static final com.bylazar.panels.core.PreferencesHandler INSTANCE;
  public static final java.lang.String PREF_FILE_NAME = "FTControl Panels";
  public static final java.lang.String KEY_AUTO_ENABLE = "autoEnable";
  public final void init(android.content.Context);
  public final boolean isEnabled();
  public final void setEnabled(boolean);
}
```

## class TextHandler

```java
public final class com.bylazar.panels.core.TextHandler {
  public static final com.bylazar.panels.core.TextHandler INSTANCE;
  public final void injectText();
  public final void updateText();
  public final void removeText();
}
```
