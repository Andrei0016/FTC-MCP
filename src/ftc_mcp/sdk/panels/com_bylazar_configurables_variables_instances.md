# `com.bylazar.configurables.variables.instances`

_panels fullpanels-1.0.12 — 6 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class CustomVariable

```java
public final class com.bylazar.configurables.variables.instances.CustomVariable extends com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.instances.CustomVariable(java.lang.String, java.lang.String, java.util.List<? extends com.bylazar.configurables.variables.generics.GenericVariable>, com.bylazar.configurables.variables.BaseTypes);
  public com.bylazar.configurables.variables.instances.CustomVariable(java.lang.String, java.lang.String, java.util.List, com.bylazar.configurables.variables.BaseTypes, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getFieldName();
  public java.lang.String getClassName();
  public final java.util.List<com.bylazar.configurables.variables.generics.GenericVariable> getValues();
  public final com.bylazar.configurables.variables.BaseTypes getType();
  public final java.lang.String getId();
  public com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```

## class ErrorVariable

```java
public final class com.bylazar.configurables.variables.instances.ErrorVariable extends com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.instances.ErrorVariable(java.lang.String, java.lang.String);
  public java.lang.String getClassName();
  public final java.lang.String getName();
  public com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```

## class JSONErrorVariable

```java
public final class com.bylazar.configurables.variables.instances.JSONErrorVariable extends com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.instances.JSONErrorVariable(java.lang.String, java.lang.String);
  public java.lang.String getClassName();
  public final java.lang.String getName();
  public com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```

## class RecursionReachedVariable

```java
public final class com.bylazar.configurables.variables.instances.RecursionReachedVariable extends com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.instances.RecursionReachedVariable(java.lang.String, java.lang.String);
  public java.lang.String getClassName();
  public final java.lang.String getName();
  public com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```

## class UnknownVariable

```java
public final class com.bylazar.configurables.variables.instances.UnknownVariable extends com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.instances.UnknownVariable(java.lang.String, java.lang.String);
  public java.lang.String getClassName();
  public final java.lang.String getName();
  public com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```

## class UnsupportedVariable

```java
public final class com.bylazar.configurables.variables.instances.UnsupportedVariable extends com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.instances.UnsupportedVariable(java.lang.String, java.lang.String);
  public java.lang.String getClassName();
  public final java.lang.String getName();
  public com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```
