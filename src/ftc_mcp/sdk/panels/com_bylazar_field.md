# `com.bylazar.field`

_panels fullpanels-1.0.12 — 18 types. Signatures are exact (`javap -protected`); see `reference/panels/` for decompiled bodies._

## class Canvas

```java
public final class com.bylazar.field.Canvas {
  public com.bylazar.field.Canvas(com.bylazar.field.FieldPresetParams, java.util.List<com.bylazar.field.Drawable>, java.util.UUID);
  public com.bylazar.field.Canvas(com.bylazar.field.FieldPresetParams, java.util.List, java.util.UUID, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final com.bylazar.field.FieldPresetParams getPreset();
  public final void setPreset(com.bylazar.field.FieldPresetParams);
  public final java.util.List<com.bylazar.field.Drawable> getItems();
  public final void setItems(java.util.List<com.bylazar.field.Drawable>);
  public final java.util.UUID getBgID();
  public final void setBgID(java.util.UUID);
  public final void reset();
  public final void resetOffsets();
  public final com.bylazar.field.FieldPresetParams component1();
  public final java.util.List<com.bylazar.field.Drawable> component2();
  public final java.util.UUID component3();
  public final com.bylazar.field.Canvas copy(com.bylazar.field.FieldPresetParams, java.util.List<com.bylazar.field.Drawable>, java.util.UUID);
  public static com.bylazar.field.Canvas copy.default(com.bylazar.field.Canvas, com.bylazar.field.FieldPresetParams, java.util.List, java.util.UUID, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.field.Canvas();
}
```

## class CanvasRotation

```java
public final class com.bylazar.field.CanvasRotation extends java.lang.Enum<com.bylazar.field.CanvasRotation> {
  public static final com.bylazar.field.CanvasRotation DEG_0;
  public static final com.bylazar.field.CanvasRotation DEG_90;
  public static final com.bylazar.field.CanvasRotation DEG_180;
  public static final com.bylazar.field.CanvasRotation DEG_270;
  public static com.bylazar.field.CanvasRotation[] values();
  public static com.bylazar.field.CanvasRotation valueOf(java.lang.String);
  public static kotlin.enums.EnumEntries<com.bylazar.field.CanvasRotation> getEntries();
}
```

## class Circle

```java
public final class com.bylazar.field.Circle extends com.bylazar.field.Drawable {
  public com.bylazar.field.Circle(double, double, double, com.bylazar.field.Style);
  public final double getX();
  public final double getY();
  public final double getR();
  public final com.bylazar.field.Style getStyle();
  public final double component1();
  public final double component2();
  public final double component3();
  public final com.bylazar.field.Style component4();
  public final com.bylazar.field.Circle copy(double, double, double, com.bylazar.field.Style);
  public static com.bylazar.field.Circle copy.default(com.bylazar.field.Circle, double, double, double, com.bylazar.field.Style, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class Drawable

```java
public abstract class com.bylazar.field.Drawable {
  public final com.bylazar.field.DrawablesTypes getType();
  public final void setType(com.bylazar.field.DrawablesTypes);
  public com.bylazar.field.Drawable(com.bylazar.field.DrawablesTypes, kotlin.jvm.internal.DefaultConstructorMarker);
}
```

## class DrawablesTypes

```java
public final class com.bylazar.field.DrawablesTypes extends java.lang.Enum<com.bylazar.field.DrawablesTypes> {
  public static final com.bylazar.field.DrawablesTypes CIRCLE;
  public static final com.bylazar.field.DrawablesTypes RECTANGLE;
  public static final com.bylazar.field.DrawablesTypes LINE;
  public static final com.bylazar.field.DrawablesTypes IMAGE;
  public static com.bylazar.field.DrawablesTypes[] values();
  public static com.bylazar.field.DrawablesTypes valueOf(java.lang.String);
  public static kotlin.enums.EnumEntries<com.bylazar.field.DrawablesTypes> getEntries();
}
```

## class FieldImage

```java
public final class com.bylazar.field.FieldImage {
  public com.bylazar.field.FieldImage(com.bylazar.field.ImagePreset, com.bylazar.field.ImagePreset);
  public final com.bylazar.field.ImagePreset getLIGHT();
  public final com.bylazar.field.ImagePreset getDARK();
  public final com.bylazar.field.ImagePreset component1();
  public final com.bylazar.field.ImagePreset component2();
  public final com.bylazar.field.FieldImage copy(com.bylazar.field.ImagePreset, com.bylazar.field.ImagePreset);
  public static com.bylazar.field.FieldImage copy.default(com.bylazar.field.FieldImage, com.bylazar.field.ImagePreset, com.bylazar.field.ImagePreset, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class FieldImages

```java
public final class com.bylazar.field.FieldImages {
  public static final com.bylazar.field.FieldImages INSTANCE;
  public final byte[] loadResourceAsBytes(java.lang.String);
  public final java.lang.String loadResourceAsBase64(java.lang.String);
  public final com.bylazar.field.FieldImage getDECODE();
}
```

## class FieldManager

```java
public final class com.bylazar.field.FieldManager {
  public com.bylazar.field.FieldManager();
  public final com.bylazar.field.FieldPluginConfig getConfig();
  public final void setConfig(com.bylazar.field.FieldPluginConfig);
  public final kotlin.jvm.functions.Function1<com.bylazar.field.Canvas, kotlin.Unit> getSendCanvas();
  public final void setSendCanvas(kotlin.jvm.functions.Function1<? super com.bylazar.field.Canvas, kotlin.Unit>);
  public final kotlin.jvm.functions.Function1<java.util.Map<java.util.UUID, java.lang.String>, kotlin.Unit> getSendImages();
  public final void setSendImages(kotlin.jvm.functions.Function1<? super java.util.Map<java.util.UUID, java.lang.String>, kotlin.Unit>);
  public final java.util.Map<java.util.UUID, java.lang.String> getImages();
  public final void setImages(java.util.Map<java.util.UUID, java.lang.String>);
  public final java.util.UUID getDefaultBgID();
  public final void setDefaultBgID(java.util.UUID);
  public final void init();
  public final long getUpdateInterval();
  public final long getLastUpdate();
  public final void setLastUpdate(long);
  public final long getTimeSinceLastUpdate();
  public final boolean getShouldUpdateCanvas();
  public final com.bylazar.field.Canvas getCanvas();
  public final void setCanvas(com.bylazar.field.Canvas);
  public final com.bylazar.field.Canvas getLastCanvas();
  public final void setLastCanvas(com.bylazar.field.Canvas);
  public final double getCursorX();
  public final void setCursorX(double);
  public final double getCursorY();
  public final void setCursorY(double);
  public final double getCursorHeading();
  public final void setCursorHeading(double);
  public final java.lang.String getCurrentFill();
  public final void setCurrentFill(java.lang.String);
  public final java.lang.String getCurrentOutlineFill();
  public final void setCurrentOutlineFill(java.lang.String);
  public final double getCurrentOutlineWidth();
  public final void setCurrentOutlineWidth(double);
  public final com.bylazar.field.Style getCurrentStyle();
  public final void moveCursor(double, double);
  public final void setFill(java.lang.String);
  public final void setOutlineFill(java.lang.String);
  public final void setOutlineWidth(double);
  public final void setOutline(java.lang.String, double);
  public final void setStyle(java.lang.String, java.lang.String, double);
  public final void setStyle(com.bylazar.field.Style);
  public final void clearFill();
  public final void clearOutline();
  public final void clearStyle();
  public final void circle(double);
  public final void line(double, double);
  public final void rect(double, double);
  public final java.util.UUID registerImage(com.bylazar.field.ImagePreset);
  public final java.util.UUID registerBase64Image(java.lang.String);
  public final java.util.UUID registerImage(java.lang.String);
  public final void img(double, double, java.util.UUID);
  public final void setBase64Background(java.lang.String);
  public final void setBackground(java.lang.String);
  public final void setBackground(java.util.UUID);
  public final void setBackground(com.bylazar.field.ImagePreset);
  public final void update();
  public final void setOffsets(com.bylazar.field.FieldPresetParams);
}
```

## class FieldPluginConfig

```java
public class com.bylazar.field.FieldPluginConfig extends com.bylazar.panels.plugins.BasePluginConfig {
  public com.bylazar.field.FieldPluginConfig();
  public long getCanvasUpdateInterval();
  public void setCanvasUpdateInterval(long);
  public com.bylazar.field.ImagePreset getDefaultBg();
  public void setDefaultBg(com.bylazar.field.ImagePreset);
  public java.util.List<com.bylazar.field.FieldPresetParams> getExtraPresets();
  public void setExtraPresets(java.util.List<com.bylazar.field.FieldPresetParams>);
}
```

## class FieldPresetParams

```java
public final class com.bylazar.field.FieldPresetParams {
  public com.bylazar.field.FieldPresetParams(java.lang.String, double, double, com.bylazar.field.CanvasRotation, boolean, boolean, boolean);
  public com.bylazar.field.FieldPresetParams(java.lang.String, double, double, com.bylazar.field.CanvasRotation, boolean, boolean, boolean, int, kotlin.jvm.internal.DefaultConstructorMarker);
  public final java.lang.String getName();
  public final void setName(java.lang.String);
  public final double getOffsetX();
  public final void setOffsetX(double);
  public final double getOffsetY();
  public final void setOffsetY(double);
  public final com.bylazar.field.CanvasRotation getRotation();
  public final void setRotation(com.bylazar.field.CanvasRotation);
  public final boolean getFlipX();
  public final void setFlipX(boolean);
  public final boolean getFlipY();
  public final void setFlipY(boolean);
  public final boolean getReverseXY();
  public final void setReverseXY(boolean);
  public final java.lang.String component1();
  public final double component2();
  public final double component3();
  public final com.bylazar.field.CanvasRotation component4();
  public final boolean component5();
  public final boolean component6();
  public final boolean component7();
  public final com.bylazar.field.FieldPresetParams copy(java.lang.String, double, double, com.bylazar.field.CanvasRotation, boolean, boolean, boolean);
  public static com.bylazar.field.FieldPresetParams copy.default(com.bylazar.field.FieldPresetParams, java.lang.String, double, double, com.bylazar.field.CanvasRotation, boolean, boolean, boolean, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
  public com.bylazar.field.FieldPresetParams();
}
```

## class FieldPresets

```java
public final class com.bylazar.field.FieldPresets {
  public static final com.bylazar.field.FieldPresets INSTANCE;
  public final com.bylazar.field.FieldPresetParams getPANELS();
  public final com.bylazar.field.FieldPresetParams getDEFAULT_FTC();
  public final com.bylazar.field.FieldPresetParams getPEDRO_PATHING();
  public final com.bylazar.field.FieldPresetParams getROAD_RUNNER();
  public final java.util.List<com.bylazar.field.FieldPresetParams> getAllPresets();
}
```

## class Image

```java
public final class com.bylazar.field.Image extends com.bylazar.field.Drawable {
  public com.bylazar.field.Image(double, double, double, double, java.util.UUID);
  public final double getX();
  public final double getY();
  public final double getW();
  public final double getH();
  public final java.util.UUID getId();
  public final double component1();
  public final double component2();
  public final double component3();
  public final double component4();
  public final java.util.UUID component5();
  public final com.bylazar.field.Image copy(double, double, double, double, java.util.UUID);
  public static com.bylazar.field.Image copy.default(com.bylazar.field.Image, double, double, double, double, java.util.UUID, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## interface ImagePreset

```java
public interface com.bylazar.field.ImagePreset {
  public abstract java.lang.String get();
}
```

## class Line

```java
public final class com.bylazar.field.Line extends com.bylazar.field.Drawable {
  public com.bylazar.field.Line(double, double, double, double, com.bylazar.field.Style);
  public final double getX1();
  public final double getY1();
  public final double getX2();
  public final double getY2();
  public final com.bylazar.field.Style getStyle();
  public final double component1();
  public final double component2();
  public final double component3();
  public final double component4();
  public final com.bylazar.field.Style component5();
  public final com.bylazar.field.Line copy(double, double, double, double, com.bylazar.field.Style);
  public static com.bylazar.field.Line copy.default(com.bylazar.field.Line, double, double, double, double, com.bylazar.field.Style, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class PanelsField

```java
public final class com.bylazar.field.PanelsField {
  public static final com.bylazar.field.PanelsField INSTANCE;
  public final com.bylazar.field.FieldManager getField();
  public final com.bylazar.field.FieldPresets getPresets();
  public final java.lang.String getTRANSPARENT();
  public final java.lang.String getWHITE();
  public final java.lang.String getBLACK();
  public final java.lang.String getRED();
  public final java.lang.String getBLUE();
  public final com.bylazar.field.FieldImages getImages();
}
```

## class Plugin

```java
public final class com.bylazar.field.Plugin extends com.bylazar.panels.plugins.Plugin<com.bylazar.field.FieldPluginConfig> {
  public static final com.bylazar.field.Plugin INSTANCE;
  public final com.bylazar.field.FieldManager getManager();
  public final void setManager(com.bylazar.field.FieldManager);
  public void onNewClient(com.bylazar.panels.server.Socket.ClientSocket);
  public void onMessage(com.bylazar.panels.server.Socket.ClientSocket, java.lang.String, java.lang.Object);
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

## class Rectangle

```java
public final class com.bylazar.field.Rectangle extends com.bylazar.field.Drawable {
  public com.bylazar.field.Rectangle(double, double, double, double, com.bylazar.field.Style);
  public final double getX();
  public final double getY();
  public final double getW();
  public final double getH();
  public final com.bylazar.field.Style getStyle();
  public final double component1();
  public final double component2();
  public final double component3();
  public final double component4();
  public final com.bylazar.field.Style component5();
  public final com.bylazar.field.Rectangle copy(double, double, double, double, com.bylazar.field.Style);
  public static com.bylazar.field.Rectangle copy.default(com.bylazar.field.Rectangle, double, double, double, double, com.bylazar.field.Style, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```

## class Style

```java
public final class com.bylazar.field.Style {
  public com.bylazar.field.Style(java.lang.String, java.lang.String, double);
  public final java.lang.String getFill();
  public final java.lang.String getOutlineFill();
  public final double getOutlineWidth();
  public final java.lang.String component1();
  public final java.lang.String component2();
  public final double component3();
  public final com.bylazar.field.Style copy(java.lang.String, java.lang.String, double);
  public static com.bylazar.field.Style copy.default(com.bylazar.field.Style, java.lang.String, java.lang.String, double, int, java.lang.Object);
  public java.lang.String toString();
  public int hashCode();
  public boolean equals(java.lang.Object);
}
```
