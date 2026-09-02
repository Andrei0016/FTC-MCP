# `com.bylazar.configurables.variables`

_panels fullpanels-1.0.12 — 9 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class BaseTypes

```java
public final class com.bylazar.configurables.variables.BaseTypes extends java.lang.Enum<com.bylazar.configurables.variables.BaseTypes> {
  public static final com.bylazar.configurables.variables.BaseTypes INT;
  public static final com.bylazar.configurables.variables.BaseTypes LONG;
  public static final com.bylazar.configurables.variables.BaseTypes DOUBLE;
  public static final com.bylazar.configurables.variables.BaseTypes STRING;
  public static final com.bylazar.configurables.variables.BaseTypes BOOLEAN;
  public static final com.bylazar.configurables.variables.BaseTypes FLOAT;
  public static final com.bylazar.configurables.variables.BaseTypes ENUM;
  public static final com.bylazar.configurables.variables.BaseTypes UNKNOWN;
  public static final com.bylazar.configurables.variables.BaseTypes UNSUPPORTED;
  public static final com.bylazar.configurables.variables.BaseTypes RECURSION_REACHED;
  public static final com.bylazar.configurables.variables.BaseTypes JSON_ERROR;
  public static final com.bylazar.configurables.variables.BaseTypes ERROR;
  public static final com.bylazar.configurables.variables.BaseTypes CUSTOM;
  public static final com.bylazar.configurables.variables.BaseTypes ARRAY;
  public static final com.bylazar.configurables.variables.BaseTypes LIST;
  public static final com.bylazar.configurables.variables.BaseTypes MAP;
  public static final com.bylazar.configurables.variables.BaseTypes GENERIC;
  public static final com.bylazar.configurables.variables.BaseTypes GENERIC_NO_ANNOTATION;
  public static com.bylazar.configurables.variables.BaseTypes[] values();
  public static com.bylazar.configurables.variables.BaseTypes valueOf(java.lang.String);
  public static kotlin.enums.EnumEntries<com.bylazar.configurables.variables.BaseTypes> getEntries();
}
```

## class ConvertValueKt

```java
public final class com.bylazar.configurables.variables.ConvertValueKt {
  public static final java.lang.Object convertValue(java.lang.String, com.bylazar.configurables.variables.BaseTypes, java.lang.Object[]);
}
```

## class ConvertValueKt.WhenMappings

```java
public final class com.bylazar.configurables.variables.ConvertValueKt.WhenMappings {
  public static final int[] .EnumSwitchMapping.0;
}
```

## class MyField

```java
public final class com.bylazar.configurables.variables.MyField extends com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.MyField(java.lang.String, java.lang.Class<?>, boolean, kotlin.jvm.functions.Function1<java.lang.Object, ? extends java.lang.Object>, kotlin.jvm.functions.Function2<java.lang.Object, java.lang.Object, kotlin.Unit>, java.lang.reflect.Type, java.lang.reflect.Field, com.bylazar.configurables.variables.MyField, java.lang.String);
  public com.bylazar.configurables.variables.MyField(java.lang.String, java.lang.Class, boolean, kotlin.jvm.functions.Function1, kotlin.jvm.functions.Function2, java.lang.reflect.Type, java.lang.reflect.Field, com.bylazar.configurables.variables.MyField, java.lang.String, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getName();
  public final java.lang.Class<?> getType();
  public final boolean isAccessible();
  public final void setAccessible(boolean);
  public final kotlin.jvm.functions.Function1<java.lang.Object, java.lang.Object> getGet();
  public final void setGet(kotlin.jvm.functions.Function1<java.lang.Object, ? extends java.lang.Object>);
  public final kotlin.jvm.functions.Function2<java.lang.Object, java.lang.Object, kotlin.Unit> getSet();
  public final void setSet(kotlin.jvm.functions.Function2<java.lang.Object, java.lang.Object, kotlin.Unit>);
  public final java.lang.reflect.Type getGenericType();
  public final void setGenericType(java.lang.reflect.Type);
  public final java.lang.reflect.Field getRef();
  public final com.bylazar.configurables.variables.MyField getParentField();
  public java.lang.String getClassName();
  public final com.bylazar.configurables.variables.BaseTypes getMyType();
  public final java.util.List<java.lang.String> getPossibleValues();
  public final java.lang.String getId();
  public final java.lang.Object getValue(int);
  public static java.lang.Object getValue.default(com.bylazar.configurables.variables.MyField, int, int, java.lang.Object);
  public final boolean setValue(java.lang.String);
  public final boolean setValue(java.lang.Object);
  public com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```

## class MyField.WhenMappings

```java
public final class com.bylazar.configurables.variables.MyField.WhenMappings {
  public static final int[] .EnumSwitchMapping.0;
}
```

## class MyFieldKt

```java
public final class com.bylazar.configurables.variables.MyFieldKt {
  public static final com.bylazar.configurables.variables.MyField convertToMyField(java.lang.reflect.Field);
  public static final com.bylazar.configurables.variables.MyField convertToMyField(com.bylazar.configurables.variables.MyField, com.bylazar.configurables.variables.MyField, java.lang.String);
}
```

## class ProcessValueKt

```java
public final class com.bylazar.configurables.variables.ProcessValueKt {
  public static final int MAX_RECURSION_DEPTH = 64;
  public static final com.bylazar.configurables.variables.generics.GenericVariable processValue(int, java.lang.String, com.bylazar.configurables.variables.BaseTypes, com.bylazar.configurables.variables.MyField, com.bylazar.configurables.variables.MyField, java.util.List<java.lang.String>);
  public static com.bylazar.configurables.variables.generics.GenericVariable processValue.default(int, java.lang.String, com.bylazar.configurables.variables.BaseTypes, com.bylazar.configurables.variables.MyField, com.bylazar.configurables.variables.MyField, java.util.List, int, java.lang.Object);
}
```

## class RecursionDetectedException

```java
public final class com.bylazar.configurables.variables.RecursionDetectedException extends java.lang.RuntimeException {
  public com.bylazar.configurables.variables.RecursionDetectedException(java.lang.String);
  public final java.lang.String getFieldName();
}
```

## class TypesKt

```java
public final class com.bylazar.configurables.variables.TypesKt {
  public static final com.bylazar.configurables.variables.BaseTypes getType(java.lang.Class<?>, com.bylazar.configurables.variables.MyField, com.bylazar.configurables.variables.MyField);
  public static com.bylazar.configurables.variables.BaseTypes getType.default(java.lang.Class, com.bylazar.configurables.variables.MyField, com.bylazar.configurables.variables.MyField, int, java.lang.Object);
}
```
