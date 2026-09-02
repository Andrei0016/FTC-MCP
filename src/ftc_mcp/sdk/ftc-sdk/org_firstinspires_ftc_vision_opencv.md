# `org.firstinspires.ftc.vision.opencv`

_ftc-sdk 11.1.0 — 20 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class Circle

```java
public class org.firstinspires.ftc.vision.opencv.Circle {
  public org.firstinspires.ftc.vision.opencv.Circle(org.opencv.core.Point, float);
  public org.firstinspires.ftc.vision.opencv.Circle(float, float, float);
  public org.opencv.core.Point getCenter();
  public float getRadius();
  public float getX();
  public float getY();
}
```

## class ColorBlobLocatorProcessor

```java
public abstract class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor implements org.firstinspires.ftc.vision.VisionProcessor {
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor();
  public abstract void addFilter(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobFilter);
  public abstract void removeFilter(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobFilter);
  public abstract void removeAllFilters();
  public abstract void setSort(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobSort);
  public abstract java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob> getBlobs();
}
```

## class ColorBlobLocatorProcessor.Blob

```java
public abstract class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob {
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob();
  public abstract org.opencv.core.MatOfPoint getContour();
  public abstract org.opencv.core.Point[] getContourPoints();
  public abstract org.opencv.core.MatOfPoint2f getContourAsFloat();
  public abstract int getContourArea();
  public abstract double getDensity();
  public abstract double getAspectRatio();
  public abstract org.opencv.core.RotatedRect getBoxFit();
  public abstract double getArcLength();
  public abstract double getCircularity();
  public abstract org.firstinspires.ftc.vision.opencv.Circle getCircle();
}
```

## class ColorBlobLocatorProcessor.BlobCriteria

```java
public final class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria extends java.lang.Enum<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria> {
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria BY_CONTOUR_AREA;
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria BY_DENSITY;
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria BY_ASPECT_RATIO;
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria BY_ARC_LENGTH;
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria BY_CIRCULARITY;
  public static org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria[] values();
  public static org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria valueOf(java.lang.String);
}
```

## class ColorBlobLocatorProcessor.BlobFilter

```java
public class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobFilter {
  public final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria criteria;
  public final double minValue;
  public final double maxValue;
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobFilter(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria, double, double);
}
```

## class ColorBlobLocatorProcessor.BlobSort

```java
public class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobSort {
  public final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria criteria;
  public final com.qualcomm.robotcore.util.SortOrder sortOrder;
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobSort(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria, com.qualcomm.robotcore.util.SortOrder);
}
```

## class ColorBlobLocatorProcessor.Builder

```java
public class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder {
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder();
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setDrawContours(boolean);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setBoxFitColor(int);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setCircleFitColor(int);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setRoiColor(int);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setContourColor(int);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setTargetColorRange(org.firstinspires.ftc.vision.opencv.ColorRange);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setContourMode(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.ContourMode);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setRoi(org.firstinspires.ftc.vision.opencv.ImageRegion);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setBlurSize(int);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setMorphOperationType(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.MorphOperationType);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setErodeSize(int);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Builder setDilateSize(int);
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor build();
}
```

## class ColorBlobLocatorProcessor.ContourMode

```java
public final class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.ContourMode extends java.lang.Enum<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.ContourMode> {
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.ContourMode EXTERNAL_ONLY;
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.ContourMode ALL_FLATTENED_HIERARCHY;
  public static org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.ContourMode[] values();
  public static org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.ContourMode valueOf(java.lang.String);
}
```

## class ColorBlobLocatorProcessor.MorphOperationType

```java
public final class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.MorphOperationType extends java.lang.Enum<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.MorphOperationType> {
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.MorphOperationType OPENING;
  public static final org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.MorphOperationType CLOSING;
  public static org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.MorphOperationType[] values();
  public static org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.MorphOperationType valueOf(java.lang.String);
}
```

## class ColorBlobLocatorProcessor.Util

```java
public class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Util {
  public org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Util();
  public static void filterByCriteria(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria, double, double, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
  public static void sortByCriteria(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobCriteria, com.qualcomm.robotcore.util.SortOrder, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
  public static void filterByArea(double, double, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
  public static void sortByArea(com.qualcomm.robotcore.util.SortOrder, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
  public static void filterByDensity(double, double, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
  public static void sortByDensity(com.qualcomm.robotcore.util.SortOrder, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
  public static void filterByAspectRatio(double, double, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
  public static void sortByAspectRatio(com.qualcomm.robotcore.util.SortOrder, java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob>);
}
```

## class ColorBlobLocatorProcessorImpl

```java
class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessorImpl extends org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor implements org.firstinspires.ftc.vision.VisionProcessor {
  public void init(int, int, org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration);
  public java.lang.Object processFrame(org.opencv.core.Mat, long);
  public void onDrawFrame(android.graphics.Canvas, int, int, float, float, java.lang.Object);
  public void addFilter(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobFilter);
  public void removeFilter(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobFilter);
  public void removeAllFilters();
  public void setSort(org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.BlobSort);
  public java.util.List<org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob> getBlobs();
}
```

## class ColorBlobLocatorProcessorImpl.BlobImpl

```java
class org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessorImpl.BlobImpl extends org.firstinspires.ftc.vision.opencv.ColorBlobLocatorProcessor.Blob {
  public org.opencv.core.MatOfPoint getContour();
  public org.opencv.core.Point[] getContourPoints();
  public org.opencv.core.MatOfPoint2f getContourAsFloat();
  public int getContourArea();
  public double getDensity();
  public double getAspectRatio();
  public org.opencv.core.RotatedRect getBoxFit();
  public double getArcLength();
  public double getCircularity();
  public org.firstinspires.ftc.vision.opencv.Circle getCircle();
}
```

## class ColorRange

```java
public class org.firstinspires.ftc.vision.opencv.ColorRange {
  protected final org.firstinspires.ftc.vision.opencv.ColorSpace colorSpace;
  protected final org.opencv.core.Scalar min;
  protected final org.opencv.core.Scalar max;
  public static final org.firstinspires.ftc.vision.opencv.ColorRange BLUE;
  public static final org.firstinspires.ftc.vision.opencv.ColorRange RED;
  public static final org.firstinspires.ftc.vision.opencv.ColorRange YELLOW;
  public static final org.firstinspires.ftc.vision.opencv.ColorRange GREEN;
  public static final org.firstinspires.ftc.vision.opencv.ColorRange ARTIFACT_GREEN;
  public static final org.firstinspires.ftc.vision.opencv.ColorRange ARTIFACT_PURPLE;
  public org.firstinspires.ftc.vision.opencv.ColorRange(org.firstinspires.ftc.vision.opencv.ColorSpace, org.opencv.core.Scalar, org.opencv.core.Scalar);
}
```

## class ColorSpace

```java
public final class org.firstinspires.ftc.vision.opencv.ColorSpace extends java.lang.Enum<org.firstinspires.ftc.vision.opencv.ColorSpace> {
  public static final org.firstinspires.ftc.vision.opencv.ColorSpace YCrCb;
  public static final org.firstinspires.ftc.vision.opencv.ColorSpace HSV;
  public static final org.firstinspires.ftc.vision.opencv.ColorSpace RGB;
  public static org.firstinspires.ftc.vision.opencv.ColorSpace[] values();
  public static org.firstinspires.ftc.vision.opencv.ColorSpace valueOf(java.lang.String);
}
```

## class ImageRegion

```java
public class org.firstinspires.ftc.vision.opencv.ImageRegion {
  public static org.firstinspires.ftc.vision.opencv.ImageRegion asImageCoordinates(int, int, int, int);
  public static org.firstinspires.ftc.vision.opencv.ImageRegion asUnityCenterCoordinates(double, double, double, double);
  public static org.firstinspires.ftc.vision.opencv.ImageRegion entireFrame();
  protected org.opencv.core.Rect asOpenCvRect(int, int);
}
```

## class PredominantColorProcessor

```java
public abstract class org.firstinspires.ftc.vision.opencv.PredominantColorProcessor implements org.firstinspires.ftc.vision.VisionProcessor {
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor();
  public abstract org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Result getAnalysis();
}
```

## class PredominantColorProcessor.Builder

```java
public class org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Builder {
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Builder();
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Builder setRoi(org.firstinspires.ftc.vision.opencv.ImageRegion);
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Builder setSwatches(org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch...);
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor build();
}
```

## class PredominantColorProcessor.Result

```java
public class org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Result {
  public final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch closestSwatch;
  public final int rgb;
  public final int[] RGB;
  public final int[] HSV;
  public final int[] YCrCb;
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Result();
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Result(org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch, int);
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Result(org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch, int, int[], int[], int[]);
}
```

## class PredominantColorProcessor.Swatch

```java
public final class org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch extends java.lang.Enum<org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch> {
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch RED;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch ORANGE;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch YELLOW;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch GREEN;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch ARTIFACT_GREEN;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch CYAN;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch BLUE;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch ARTIFACT_PURPLE;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch PURPLE;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch MAGENTA;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch BLACK;
  public static final org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch WHITE;
  public static org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch[] values();
  public static org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch valueOf(java.lang.String);
  public static org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Swatch valueOf(int);
}
```

## class PredominantColorProcessorImpl

```java
class org.firstinspires.ftc.vision.opencv.PredominantColorProcessorImpl extends org.firstinspires.ftc.vision.opencv.PredominantColorProcessor {
  public void init(int, int, org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration);
  public java.lang.Object processFrame(org.opencv.core.Mat, long);
  public void onDrawFrame(android.graphics.Canvas, int, int, float, float, java.lang.Object);
  public org.firstinspires.ftc.vision.opencv.PredominantColorProcessor.Result getAnalysis();
}
```
