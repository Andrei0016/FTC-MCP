# `com.bylazar.panels.reflection`

_panels fullpanels-1.0.12 — 3 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class ClassFinder

```java
public final class com.bylazar.panels.reflection.ClassFinder {
  public static final com.bylazar.panels.reflection.ClassFinder INSTANCE;
  public final java.util.Set<java.lang.String> getDEFAULT_IGNORED_PACKAGES();
  public final java.lang.String getApkPath();
  public final void setApkPath(java.lang.String);
  public final java.util.List<com.bylazar.panels.reflection.ClassFinder.ClassEntry> getAllClasses();
  public final void setAllClasses(java.util.List<com.bylazar.panels.reflection.ClassFinder.ClassEntry>);
  public final void init(java.lang.String);
  public final java.util.List<com.bylazar.panels.reflection.ClassFinder.ClassEntry> findClasses(kotlin.jvm.functions.Function1<? super java.lang.Class<?>, java.lang.Boolean>);
  public static java.util.List findClasses.default(com.bylazar.panels.reflection.ClassFinder, kotlin.jvm.functions.Function1, int, java.lang.Object);
}
```

## class ClassFinder.ClassEntry

```java
public final class com.bylazar.panels.reflection.ClassFinder.ClassEntry {
  public com.bylazar.panels.reflection.ClassFinder.ClassEntry(java.lang.String);
  public final java.lang.String getClassName();
  public final java.lang.String component1();
  public final com.bylazar.panels.reflection.ClassFinder.ClassEntry copy(java.lang.String);
  public static com.bylazar.panels.reflection.ClassFinder.ClassEntry copy.default(com.bylazar.panels.reflection.ClassFinder.ClassEntry, java.lang.String, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class DexUtilsKt

```java
public final class com.bylazar.panels.reflection.DexUtilsKt {
  public static final java.util.List<java.lang.String> extractClassNamesFromDex(java.nio.ByteBuffer);
}
```
