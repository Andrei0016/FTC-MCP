# `com.bylazar.panels.json`

_panels fullpanels-1.0.12 — 14 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class Change

```java
public final class com.bylazar.panels.json.Change {
  public com.bylazar.panels.json.Change(com.bylazar.panels.json.ChangeLogType, java.lang.String, java.lang.String);
  public com.bylazar.panels.json.Change(com.bylazar.panels.json.ChangeLogType, java.lang.String, java.lang.String, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final com.bylazar.panels.json.ChangeLogType getType();
  public final java.lang.String getDescription();
  public final java.lang.String getUpgrading();
  public final com.bylazar.panels.json.ChangeLogType component1();
  public final java.lang.String component2();
  public final java.lang.String component3();
  public final com.bylazar.panels.json.Change copy(com.bylazar.panels.json.ChangeLogType, java.lang.String, java.lang.String);
  public static com.bylazar.panels.json.Change copy.default(com.bylazar.panels.json.Change, com.bylazar.panels.json.ChangeLogType, java.lang.String, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.Change();
}
```

## class ChangeLogEntry

```java
public final class com.bylazar.panels.json.ChangeLogEntry {
  public com.bylazar.panels.json.ChangeLogEntry(java.lang.String, java.lang.String, java.util.List<com.bylazar.panels.json.Change>);
  public com.bylazar.panels.json.ChangeLogEntry(java.lang.String, java.lang.String, java.util.List, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getVersion();
  public final java.lang.String getReleaseDate();
  public final java.util.List<com.bylazar.panels.json.Change> getChanges();
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final java.util.List<com.bylazar.panels.json.Change> component3();
  public final com.bylazar.panels.json.ChangeLogEntry copy(java.lang.String, java.lang.String, java.util.List<com.bylazar.panels.json.Change>);
  public static com.bylazar.panels.json.ChangeLogEntry copy.default(com.bylazar.panels.json.ChangeLogEntry, java.lang.String, java.lang.String, java.util.List, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.ChangeLogEntry();
}
```

## class ChangeLogType

```java
public final class com.bylazar.panels.json.ChangeLogType extends java.lang.Enum<com.bylazar.panels.json.ChangeLogType> {
  public static final com.bylazar.panels.json.ChangeLogType ADDED;
  public static final com.bylazar.panels.json.ChangeLogType CHANGED;
  public static final com.bylazar.panels.json.ChangeLogType DEPRECATED;
  public static final com.bylazar.panels.json.ChangeLogType REMOVED;
  public static final com.bylazar.panels.json.ChangeLogType FIXED;
  public static final com.bylazar.panels.json.ChangeLogType DOCS;
  public static final com.bylazar.panels.json.ChangeLogType OTHER;
  public static com.bylazar.panels.json.ChangeLogType[] values();
  public static com.bylazar.panels.json.ChangeLogType valueOf(java.lang.String);
  public static kotlin.enums.EnumEntries<com.bylazar.panels.json.ChangeLogType> getEntries();
}
```

## class PanelsWidget

```java
public final class com.bylazar.panels.json.PanelsWidget {
  public com.bylazar.panels.json.PanelsWidget(java.lang.String, java.lang.String, java.lang.String);
  public com.bylazar.panels.json.PanelsWidget(java.lang.String, java.lang.String, java.lang.String, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getType();
  public final java.lang.String getId();
  public final java.lang.String getFilepath();
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final java.lang.String component3();
  public final com.bylazar.panels.json.PanelsWidget copy(java.lang.String, java.lang.String, java.lang.String);
  public static com.bylazar.panels.json.PanelsWidget copy.default(com.bylazar.panels.json.PanelsWidget, java.lang.String, java.lang.String, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.PanelsWidget();
}
```

## class PluginData

```java
public final class com.bylazar.panels.json.PluginData {
  public com.bylazar.panels.json.PluginData(java.util.List<com.bylazar.panels.json.PluginInfo>, java.util.List<com.bylazar.panels.json.PluginDetails>);
  public final java.util.List<com.bylazar.panels.json.PluginInfo> getPlugins();
  public final void setPlugins(java.util.List<com.bylazar.panels.json.PluginInfo>);
  public final java.util.List<com.bylazar.panels.json.PluginDetails> getSkippedPlugins();
  public final void setSkippedPlugins(java.util.List<com.bylazar.panels.json.PluginDetails>);
  public final java.util.List<com.bylazar.panels.json.PluginInfo> component1();
  public final java.util.List<com.bylazar.panels.json.PluginDetails> component2();
  public final com.bylazar.panels.json.PluginData copy(java.util.List<com.bylazar.panels.json.PluginInfo>, java.util.List<com.bylazar.panels.json.PluginDetails>);
  public static com.bylazar.panels.json.PluginData copy.default(com.bylazar.panels.json.PluginData, java.util.List, java.util.List, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class PluginDetails

```java
public final class com.bylazar.panels.json.PluginDetails {
  public com.bylazar.panels.json.PluginDetails(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List<com.bylazar.panels.json.PanelsWidget>, java.lang.String, java.util.List<com.bylazar.panels.json.Template>, java.util.List<java.lang.String>, java.util.List<com.bylazar.panels.json.ChangeLogEntry>);
  public com.bylazar.panels.json.PluginDetails(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List, java.lang.String, java.util.List, java.util.List, java.util.List, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getId();
  public final java.lang.String getName();
  public final java.lang.String getLetterName();
  public final java.lang.String getDescription();
  public final java.lang.String getWebsiteURL();
  public final java.lang.String getMavenURL();
  public final java.lang.String getPackageString();
  public final java.lang.String getVersion();
  public final java.lang.String getPluginsCoreVersion();
  public final java.lang.String getAuthor();
  public final java.util.List<com.bylazar.panels.json.PanelsWidget> getComponents();
  public final java.lang.String getManager();
  public final java.util.List<com.bylazar.panels.json.Template> getTemplates();
  public final java.util.List<java.lang.String> getIncludedPluginsIDs();
  public final java.util.List<com.bylazar.panels.json.ChangeLogEntry> getChangelog();
  public java.lang.String toString();
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final java.lang.String component3();
  public final java.lang.String component4();
  public final java.lang.String component5();
  public final java.lang.String component6();
  public final java.lang.String component7();
  public final java.lang.String component8();
  public final java.lang.String component9();
  public final java.lang.String component10();
  public final java.util.List<com.bylazar.panels.json.PanelsWidget> component11();
  public final java.lang.String component12();
  public final java.util.List<com.bylazar.panels.json.Template> component13();
  public final java.util.List<java.lang.String> component14();
  public final java.util.List<com.bylazar.panels.json.ChangeLogEntry> component15();
  public final com.bylazar.panels.json.PluginDetails copy(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List<com.bylazar.panels.json.PanelsWidget>, java.lang.String, java.util.List<com.bylazar.panels.json.Template>, java.util.List<java.lang.String>, java.util.List<com.bylazar.panels.json.ChangeLogEntry>);
  public static com.bylazar.panels.json.PluginDetails copy.default(com.bylazar.panels.json.PluginDetails, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.util.List, java.lang.String, java.util.List, java.util.List, java.util.List, int, java.lang.Object);
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.PluginDetails();
}
```

## class PluginInfo

```java
public final class com.bylazar.panels.json.PluginInfo {
  public com.bylazar.panels.json.PluginInfo(com.bylazar.panels.json.PluginDetails, java.lang.Object);
  public final com.bylazar.panels.json.PluginDetails getDetails();
  public final void setDetails(com.bylazar.panels.json.PluginDetails);
  public final java.lang.Object getConfig();
  public final void setConfig(java.lang.Object);
  public final com.bylazar.panels.json.PluginDetails component1();
  public final java.lang.Object component2();
  public final com.bylazar.panels.json.PluginInfo copy(com.bylazar.panels.json.PluginDetails, java.lang.Object);
  public static com.bylazar.panels.json.PluginInfo copy.default(com.bylazar.panels.json.PluginInfo, com.bylazar.panels.json.PluginDetails, java.lang.Object, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class SocketMessage

```java
public final class com.bylazar.panels.json.SocketMessage {
  public static final com.bylazar.panels.json.SocketMessage.Companion Companion;
  public com.bylazar.panels.json.SocketMessage(java.lang.String, java.lang.String, java.lang.Object);
  public final java.lang.String getPluginID();
  public final java.lang.String getMessageID();
  public final java.lang.Object getData();
  public final java.lang.String toJson();
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final java.lang.Object component3();
  public final com.bylazar.panels.json.SocketMessage copy(java.lang.String, java.lang.String, java.lang.Object);
  public static com.bylazar.panels.json.SocketMessage copy.default(com.bylazar.panels.json.SocketMessage, java.lang.String, java.lang.String, java.lang.Object, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public static final com.google.gson.Gson access.getGson.cp();
}
```

## class SocketMessage.Companion

```java
public final class com.bylazar.panels.json.SocketMessage.Companion {
  public final com.google.gson.Gson getGson();
  public final com.bylazar.panels.json.SocketMessage fromJson(java.lang.String);
  public final <T> T convertData(java.lang.Object);
  public com.bylazar.panels.json.SocketMessage.Companion(kotlin.jvm.internal.DefaultConstructorMarker);
}
```

## class Template

```java
public final class com.bylazar.panels.json.Template {
  public com.bylazar.panels.json.Template(java.lang.String, java.util.List<com.bylazar.panels.json.TemplateWidgetGroup>, java.util.List<com.bylazar.panels.json.TemplateNavlet>);
  public com.bylazar.panels.json.Template(java.lang.String, java.util.List, java.util.List, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getName();
  public final java.util.List<com.bylazar.panels.json.TemplateWidgetGroup> getWidgets();
  public final java.util.List<com.bylazar.panels.json.TemplateNavlet> getNavlets();
  public final java.lang.String component1();
  public final java.util.List<com.bylazar.panels.json.TemplateWidgetGroup> component2();
  public final java.util.List<com.bylazar.panels.json.TemplateNavlet> component3();
  public final com.bylazar.panels.json.Template copy(java.lang.String, java.util.List<com.bylazar.panels.json.TemplateWidgetGroup>, java.util.List<com.bylazar.panels.json.TemplateNavlet>);
  public static com.bylazar.panels.json.Template copy.default(com.bylazar.panels.json.Template, java.lang.String, java.util.List, java.util.List, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.Template();
}
```

## class TemplateNavlet

```java
public final class com.bylazar.panels.json.TemplateNavlet {
  public com.bylazar.panels.json.TemplateNavlet(java.lang.String, java.lang.String);
  public com.bylazar.panels.json.TemplateNavlet(java.lang.String, java.lang.String, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getPluginID();
  public final java.lang.String getNavletID();
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final com.bylazar.panels.json.TemplateNavlet copy(java.lang.String, java.lang.String);
  public static com.bylazar.panels.json.TemplateNavlet copy.default(com.bylazar.panels.json.TemplateNavlet, java.lang.String, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.TemplateNavlet();
}
```

## class TemplateWidget

```java
public final class com.bylazar.panels.json.TemplateWidget {
  public com.bylazar.panels.json.TemplateWidget(java.lang.String, java.lang.String);
  public com.bylazar.panels.json.TemplateWidget(java.lang.String, java.lang.String, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getPluginID();
  public final java.lang.String getWidgetID();
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final com.bylazar.panels.json.TemplateWidget copy(java.lang.String, java.lang.String);
  public static com.bylazar.panels.json.TemplateWidget copy.default(com.bylazar.panels.json.TemplateWidget, java.lang.String, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.TemplateWidget();
}
```

## class TemplateWidgetGroup

```java
public final class com.bylazar.panels.json.TemplateWidgetGroup {
  public com.bylazar.panels.json.TemplateWidgetGroup(java.util.List<com.bylazar.panels.json.TemplateWidget>, int, int, int, int);
  public com.bylazar.panels.json.TemplateWidgetGroup(java.util.List, int, int, int, int, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.util.List<com.bylazar.panels.json.TemplateWidget> getWidgets();
  public final int getX();
  public final int getY();
  public final int getW();
  public final int getH();
  public final java.util.List<com.bylazar.panels.json.TemplateWidget> component1();
  public final int component2();
  public final int component3();
  public final int component4();
  public final int component5();
  public final com.bylazar.panels.json.TemplateWidgetGroup copy(java.util.List<com.bylazar.panels.json.TemplateWidget>, int, int, int, int);
  public static com.bylazar.panels.json.TemplateWidgetGroup copy.default(com.bylazar.panels.json.TemplateWidgetGroup, java.util.List, int, int, int, int, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.panels.json.TemplateWidgetGroup();
}
```

## class TimeData

```java
public final class com.bylazar.panels.json.TimeData {
  public com.bylazar.panels.json.TimeData(java.lang.String);
  public final java.lang.String getTime();
  public final java.lang.String component1();
  public final com.bylazar.panels.json.TimeData copy(java.lang.String);
  public static com.bylazar.panels.json.TimeData copy.default(com.bylazar.panels.json.TimeData, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```
