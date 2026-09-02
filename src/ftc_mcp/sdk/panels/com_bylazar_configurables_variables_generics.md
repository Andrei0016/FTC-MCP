# `com.bylazar.configurables.variables.generics`

_panels fullpanels-1.0.12 — 2 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class GenericField

```java
public final class com.bylazar.configurables.variables.generics.GenericField {
  public com.bylazar.configurables.variables.generics.GenericField(java.lang.String, java.lang.reflect.Field);
  public final java.lang.String getClassName();
  public final void setClassName(java.lang.String);
  public final java.lang.reflect.Field getReference();
  public final void setReference(java.lang.reflect.Field);
  public final com.bylazar.configurables.variables.BaseTypes getType();
  public final com.bylazar.configurables.variables.generics.GenericVariable getValue();
  public final boolean isNull();
  public final java.lang.String getName();
  public final void debug();
  public final com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```

## class GenericVariable

```java
public abstract class com.bylazar.configurables.variables.generics.GenericVariable {
  public com.bylazar.configurables.variables.generics.GenericVariable(java.lang.String);
  public java.lang.String getClassName();
  public abstract com.bylazar.configurables.GenericTypeJson getToJsonType();
}
```
