# `com.bylazar.configurables`

_panels fullpanels-1.0.12 — 8 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class ChangeJson

```java
public final class com.bylazar.configurables.ChangeJson {
  public com.bylazar.configurables.ChangeJson(java.lang.String, java.lang.String);
  public final java.lang.String getId();
  public final void setId(java.lang.String);
  public final java.lang.String getNewValueString();
  public final void setNewValueString(java.lang.String);
}
```

## class ConfigurablesLogger

```java
public final class com.bylazar.configurables.ConfigurablesLogger {
  public static final com.bylazar.configurables.ConfigurablesLogger INSTANCE;
  public final void log(java.lang.String);
  public final void error(java.lang.String);
}
```

## class ConfigurablesPluginConfig

```java
public class com.bylazar.configurables.ConfigurablesPluginConfig extends com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.configurables.ConfigurablesPluginConfig();
}
```

## class GenericTypeJson

```java
public final class com.bylazar.configurables.GenericTypeJson {
  public com.bylazar.configurables.GenericTypeJson(java.lang.String, java.lang.String, java.lang.String, com.bylazar.configurables.variables.BaseTypes, java.lang.String, java.util.List<java.lang.String>, java.util.List<com.bylazar.configurables.GenericTypeJson>);
  public com.bylazar.configurables.GenericTypeJson(java.lang.String, java.lang.String, java.lang.String, com.bylazar.configurables.variables.BaseTypes, java.lang.String, java.util.List, java.util.List, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getId();
  public final void setId(java.lang.String);
  public final java.lang.String getClassName();
  public final void setClassName(java.lang.String);
  public final java.lang.String getFieldName();
  public final void setFieldName(java.lang.String);
  public final com.bylazar.configurables.variables.BaseTypes getType();
  public final void setType(com.bylazar.configurables.variables.BaseTypes);
  public final java.lang.String getValue();
  public final void setValue(java.lang.String);
  public final java.util.List<java.lang.String> getPossibleValues();
  public final void setPossibleValues(java.util.List<java.lang.String>);
  public final java.util.List<com.bylazar.configurables.GenericTypeJson> getCustomValues();
  public final void setCustomValues(java.util.List<com.bylazar.configurables.GenericTypeJson>);
}
```

## class GlobalConfigurables

```java
public final class com.bylazar.configurables.GlobalConfigurables {
  public static final com.bylazar.configurables.GlobalConfigurables INSTANCE;
  public final java.util.List<com.bylazar.configurables.variables.generics.GenericField> getJvmFields();
  public final void setJvmFields(java.util.List<com.bylazar.configurables.variables.generics.GenericField>);
  public final java.util.Map<java.lang.String, com.bylazar.configurables.variables.MyField> getFieldsMap();
  public final void setFieldsMap(java.util.Map<java.lang.String, com.bylazar.configurables.variables.MyField>);
}
```

## class PanelsConfigurables

```java
public final class com.bylazar.configurables.PanelsConfigurables {
  public static final com.bylazar.configurables.PanelsConfigurables INSTANCE;
  public final void refreshClass(java.lang.Object);
}
```

## class Plugin

```java
public final class com.bylazar.configurables.Plugin extends com.bylazar.panels.plugins.Plugin<com.bylazar.configurables.ConfigurablesPluginConfig> {
  public static final com.bylazar.configurables.Plugin INSTANCE;
  public final java.util.Map<java.lang.String, com.bylazar.configurables.variables.MyField> getFieldsMap();
  public final void setFieldsMap(java.util.Map<java.lang.String, com.bylazar.configurables.variables.MyField>);
  public final java.util.List<com.bylazar.panels.reflection.ClassFinder.ClassEntry> getConfigurableClasses();
  public final void setConfigurableClasses(java.util.List<com.bylazar.panels.reflection.ClassFinder.ClassEntry>);
  public final java.util.List<com.bylazar.configurables.GenericTypeJson> getAllFields();
  public final void setAllFields(java.util.List<com.bylazar.configurables.GenericTypeJson>);
  public final java.util.Map<java.lang.String, java.util.List<com.bylazar.configurables.GenericTypeJson>> getAllFieldsMap();
  public final java.util.Map<java.lang.String, java.util.List<com.bylazar.configurables.GenericTypeJson>> getInitialAFieldsMap();
  public final void setInitialAFieldsMap(java.util.Map<java.lang.String, ? extends java.util.List<com.bylazar.configurables.GenericTypeJson>>);
  public void onNewClient(com.bylazar.panels.server.Socket.ClientSocket);
  public void onMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.Object);
  public final void refreshClass(java.lang.String);
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

## class TPair

```java
public class com.bylazar.configurables.TPair<T, V> {
  public com.bylazar.configurables.TPair(kotlin.jvm.functions.Function0<? extends T>, V, java.util.Map<T, V>, kotlin.jvm.functions.Function1<? super com.bylazar.configurables.TPair<T, V>, kotlin.Unit>);
  public com.bylazar.configurables.TPair(kotlin.jvm.functions.Function0, java.lang.Object, java.util.Map, kotlin.jvm.functions.Function1, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final kotlin.jvm.functions.Function0<T> getLambdaProvider();
  public final void setLambdaProvider(kotlin.jvm.functions.Function0<? extends T>);
  public final V getDefaultValue();
  public final void setDefaultValue(V);
  public final java.util.Map<T, V> getStates();
  public final void setStates(java.util.Map<T, V>);
  public final void pair(T, V);
  public final void default(V);
  public final V invoke();
  public final V getStateValue(T);
}
```
