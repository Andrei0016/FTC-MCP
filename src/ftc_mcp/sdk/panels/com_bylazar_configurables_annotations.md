# `com.bylazar.configurables.annotations`

_panels fullpanels-1.0.12 — 4 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## interface Configurable

```java
public interface com.bylazar.configurables.annotations.Configurable extends java.lang.annotation.Annotation {
}
```

## interface GenericValue

```java
public interface com.bylazar.configurables.annotations.GenericValue extends java.lang.annotation.Annotation {
  public abstract java.lang.Class<?> tParam();
  public abstract java.lang.Class<?> vParam();
}
```

## interface IgnoreConfigurable

```java
public interface com.bylazar.configurables.annotations.IgnoreConfigurable extends java.lang.annotation.Annotation {
}
```

## interface Sorter

```java
public interface com.bylazar.configurables.annotations.Sorter extends java.lang.annotation.Annotation {
  public abstract int sort();
}
```
