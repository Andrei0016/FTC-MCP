# `org.firstinspires.ftc.vision.apriltag`

_ftc-sdk 11.1.0 — 15 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class AprilTagCanvasAnnotator

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagCanvasAnnotator {
  public org.firstinspires.ftc.vision.apriltag.AprilTagCanvasAnnotator(org.opencv.core.Mat);
  public void noteDrawParams(float, float);
}
```

## class AprilTagCanvasAnnotator.LinePaint

```java
class org.firstinspires.ftc.vision.apriltag.AprilTagCanvasAnnotator.LinePaint extends android.graphics.Paint {
  public org.firstinspires.ftc.vision.apriltag.AprilTagCanvasAnnotator.LinePaint(int);
}
```

## class AprilTagDetection

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagDetection {
  public final int id;
  public final int hamming;
  public final float decisionMargin;
  public final org.opencv.core.Point center;
  public final org.opencv.core.Point[] corners;
  public final org.firstinspires.ftc.vision.apriltag.AprilTagMetadata metadata;
  public final org.firstinspires.ftc.vision.apriltag.AprilTagPoseFtc ftcPose;
  public final org.firstinspires.ftc.vision.apriltag.AprilTagPoseRaw rawPose;
  public final org.firstinspires.ftc.robotcore.external.navigation.Pose3D robotPose;
  public final long frameAcquisitionNanoTime;
  public org.firstinspires.ftc.vision.apriltag.AprilTagDetection(int, int, float, org.opencv.core.Point, org.opencv.core.Point[], org.firstinspires.ftc.vision.apriltag.AprilTagMetadata, org.firstinspires.ftc.vision.apriltag.AprilTagPoseFtc, org.firstinspires.ftc.vision.apriltag.AprilTagPoseRaw, org.firstinspires.ftc.robotcore.external.navigation.Pose3D, long);
}
```

## class AprilTagGameDatabase

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagGameDatabase {
  public org.firstinspires.ftc.vision.apriltag.AprilTagGameDatabase();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagLibrary getCurrentGameTagLibrary();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagLibrary getCenterStageTagLibrary();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagLibrary getIntoTheDeepTagLibrary();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagLibrary getDecodeTagLibrary();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagLibrary getSampleTagLibrary();
}
```

## class AprilTagLibrary

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagLibrary {
  public org.firstinspires.ftc.vision.apriltag.AprilTagMetadata[] getAllTags();
  public org.firstinspires.ftc.vision.apriltag.AprilTagMetadata lookupTag(int);
}
```

## class AprilTagLibrary.Builder

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagLibrary.Builder {
  public org.firstinspires.ftc.vision.apriltag.AprilTagLibrary.Builder();
  public org.firstinspires.ftc.vision.apriltag.AprilTagLibrary.Builder setAllowOverwrite(boolean);
  public org.firstinspires.ftc.vision.apriltag.AprilTagLibrary.Builder addTag(org.firstinspires.ftc.vision.apriltag.AprilTagMetadata);
  public org.firstinspires.ftc.vision.apriltag.AprilTagLibrary.Builder addTag(int, java.lang.String, double, org.firstinspires.ftc.robotcore.external.matrices.VectorF, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, org.firstinspires.ftc.robotcore.external.navigation.Quaternion);
  public org.firstinspires.ftc.vision.apriltag.AprilTagLibrary.Builder addTag(int, java.lang.String, double, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public org.firstinspires.ftc.vision.apriltag.AprilTagLibrary.Builder addTags(org.firstinspires.ftc.vision.apriltag.AprilTagLibrary);
  public org.firstinspires.ftc.vision.apriltag.AprilTagLibrary build();
}
```

## class AprilTagMetadata

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagMetadata {
  public final int id;
  public final double tagsize;
  public final java.lang.String name;
  public final org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit distanceUnit;
  public final org.firstinspires.ftc.robotcore.external.matrices.VectorF fieldPosition;
  public final org.firstinspires.ftc.robotcore.external.navigation.Quaternion fieldOrientation;
  public org.firstinspires.ftc.vision.apriltag.AprilTagMetadata(int, java.lang.String, double, org.firstinspires.ftc.robotcore.external.matrices.VectorF, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, org.firstinspires.ftc.robotcore.external.navigation.Quaternion);
  public org.firstinspires.ftc.vision.apriltag.AprilTagMetadata(int, java.lang.String, double, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
}
```

## class AprilTagPoseFtc

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagPoseFtc {
  public final double x;
  public final double y;
  public final double z;
  public final double yaw;
  public final double pitch;
  public final double roll;
  public final double range;
  public final double bearing;
  public final double elevation;
  public org.firstinspires.ftc.vision.apriltag.AprilTagPoseFtc(double, double, double, double, double, double, double, double, double);
}
```

## class AprilTagPoseRaw

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagPoseRaw {
  public final double x;
  public final double y;
  public final double z;
  public final org.firstinspires.ftc.robotcore.external.matrices.MatrixF R;
  public org.firstinspires.ftc.vision.apriltag.AprilTagPoseRaw(double, double, double, org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
}
```

## class AprilTagProcessor

```java
public abstract class org.firstinspires.ftc.vision.apriltag.AprilTagProcessor implements org.firstinspires.ftc.vision.VisionProcessor {
  public static final int THREADS_DEFAULT = 3;
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagProcessor easyCreateWithDefaults();
  public abstract void setDecimation(float);
  public abstract void setPoseSolver(org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver);
  public abstract int getPerTagAvgPoseSolveTime();
  public abstract java.util.ArrayList<org.firstinspires.ftc.vision.apriltag.AprilTagDetection> getDetections();
  public abstract java.util.ArrayList<org.firstinspires.ftc.vision.apriltag.AprilTagDetection> getFreshDetections();
}
```

## class AprilTagProcessor.Builder

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder {
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder();
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setCameraPose(org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setLensIntrinsics(double, double, double, double);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setSuppressCalibrationWarnings(boolean);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setTagFamily(org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setTagLibrary(org.firstinspires.ftc.vision.apriltag.AprilTagLibrary);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setOutputUnits(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setDrawAxes(boolean);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setDrawCubeProjection(boolean);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setDrawTagOutline(boolean);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setDrawTagID(boolean);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.Builder setNumThreads(int);
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessor build();
}
```

## class AprilTagProcessor.PoseSolver

```java
public final class org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver extends java.lang.Enum<org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver> {
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver APRILTAG_BUILTIN;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver OPENCV_ITERATIVE;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver OPENCV_SOLVEPNP_EPNP;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver OPENCV_IPPE;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver OPENCV_IPPE_SQUARE;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver OPENCV_SQPNP;
  public static org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver[] values();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver valueOf(java.lang.String);
}
```

## class AprilTagProcessor.TagFamily

```java
public final class org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily extends java.lang.Enum<org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily> {
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily TAG_36h11;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily TAG_25h9;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily TAG_16h5;
  public static final org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily TAG_standard41h12;
  public static org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily[] values();
  public static org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily valueOf(java.lang.String);
}
```

## class AprilTagProcessorImpl

```java
public class org.firstinspires.ftc.vision.apriltag.AprilTagProcessorImpl extends org.firstinspires.ftc.vision.apriltag.AprilTagProcessor {
  public static final java.lang.String TAG = "AprilTagProcessorImpl";
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessorImpl(org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix, double, double, double, double, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, org.firstinspires.ftc.vision.apriltag.AprilTagLibrary, boolean, boolean, boolean, boolean, org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.TagFamily, int, boolean);
  protected void finalize();
  public void init(int, int, org.firstinspires.ftc.robotcore.internal.camera.calibration.CameraCalibration);
  public java.lang.Object processFrame(org.opencv.core.Mat, long);
  public void onDrawFrame(android.graphics.Canvas, int, int, float, float, java.lang.Object);
  public void setDecimation(float);
  public void setPoseSolver(org.firstinspires.ftc.vision.apriltag.AprilTagProcessor.PoseSolver);
  public int getPerTagAvgPoseSolveTime();
  public java.util.ArrayList<org.firstinspires.ftc.vision.apriltag.AprilTagDetection> getDetections();
  public java.util.ArrayList<org.firstinspires.ftc.vision.apriltag.AprilTagDetection> getFreshDetections();
}
```

## class AprilTagProcessorImpl.Pose

```java
class org.firstinspires.ftc.vision.apriltag.AprilTagProcessorImpl.Pose {
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessorImpl.Pose();
  public org.firstinspires.ftc.vision.apriltag.AprilTagProcessorImpl.Pose(org.opencv.core.Mat, org.opencv.core.Mat);
}
```
