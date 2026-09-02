# `com.qualcomm.hardware.limelightvision`

_ftc-sdk 11.1.0 — 12 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class LLFieldMap

```java
public class com.qualcomm.hardware.limelightvision.LLFieldMap {
  public com.qualcomm.hardware.limelightvision.LLFieldMap();
  public com.qualcomm.hardware.limelightvision.LLFieldMap(java.util.List<com.qualcomm.hardware.limelightvision.LLFieldMap.Fiducial>, java.lang.String);
  protected com.qualcomm.hardware.limelightvision.LLFieldMap(org.json.JSONObject);
  public java.util.List<com.qualcomm.hardware.limelightvision.LLFieldMap.Fiducial> getFiducials();
  public java.lang.String getType();
  public int getNumberOfTags();
  public boolean isValid();
  protected org.json.JSONObject toJson();
}
```

## class LLFieldMap.Fiducial

```java
public class com.qualcomm.hardware.limelightvision.LLFieldMap.Fiducial {
  public com.qualcomm.hardware.limelightvision.LLFieldMap.Fiducial();
  public com.qualcomm.hardware.limelightvision.LLFieldMap.Fiducial(int, double, java.lang.String, java.util.List<java.lang.Double>, boolean);
  protected com.qualcomm.hardware.limelightvision.LLFieldMap.Fiducial(org.json.JSONObject);
  public int getId();
  public double getSize();
  public java.lang.String getFamily();
  public java.util.List<java.lang.Double> getTransform();
  public boolean isUnique();
  protected org.json.JSONObject toJson();
}
```

## class LLResult

```java
public class com.qualcomm.hardware.limelightvision.LLResult {
  protected com.qualcomm.hardware.limelightvision.LLResult(org.json.JSONObject) throws org.json.JSONException;
  public long getControlHubTimeStamp();
  public long getControlHubTimeStampNanos();
  public long getStaleness();
  public java.util.List<com.qualcomm.hardware.limelightvision.LLResultTypes.BarcodeResult> getBarcodeResults();
  public java.util.List<com.qualcomm.hardware.limelightvision.LLResultTypes.ClassifierResult> getClassifierResults();
  public java.util.List<com.qualcomm.hardware.limelightvision.LLResultTypes.DetectorResult> getDetectorResults();
  public java.util.List<com.qualcomm.hardware.limelightvision.LLResultTypes.FiducialResult> getFiducialResults();
  public java.util.List<com.qualcomm.hardware.limelightvision.LLResultTypes.ColorResult> getColorResults();
  public double getFocusMetric();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getBotpose();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getBotpose_MT2();
  public double[] getStddevMt1();
  public double[] getStddevMt2();
  public int getBotposeTagCount();
  public double getBotposeSpan();
  public double getBotposeAvgDist();
  public double getBotposeAvgArea();
  public double[] getPythonOutput();
  public double getCaptureLatency();
  public java.lang.String getPipelineType();
  public double getTx();
  public double getTy();
  public double getTxNC();
  public double getTyNC();
  public double getTa();
  public int getPipelineIndex();
  public double getTargetingLatency();
  public double getTimestamp();
  public boolean isValid();
  public double getParseLatency();
  protected static org.firstinspires.ftc.robotcore.external.navigation.Pose3D createPose3DRobot(double[]);
  protected static com.qualcomm.hardware.limelightvision.LLResult parse(org.json.JSONObject);
  public java.lang.String toString();
}
```

## class LLResultTypes

```java
public class com.qualcomm.hardware.limelightvision.LLResultTypes {
  public com.qualcomm.hardware.limelightvision.LLResultTypes();
}
```

## class LLResultTypes.BarcodeResult

```java
public class com.qualcomm.hardware.limelightvision.LLResultTypes.BarcodeResult {
  protected com.qualcomm.hardware.limelightvision.LLResultTypes.BarcodeResult(org.json.JSONObject);
  public java.lang.String getFamily();
  public java.lang.String getData();
  public double getTargetXPixels();
  public double getTargetYPixels();
  public double getTargetXDegrees();
  public double getTargetYDegrees();
  public double getTargetXDegreesNoCrosshair();
  public double getTargetYDegreesNoCrosshair();
  public double getTargetArea();
  public java.util.List<java.util.List<java.lang.Double>> getTargetCorners();
}
```

## class LLResultTypes.CalibrationResult

```java
public class com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult {
  public com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult();
  public com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult(java.lang.String, double, double, double, double[], double[]);
  protected com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult(org.json.JSONObject);
  public boolean isValid();
  public java.lang.String getDisplayName();
  public double getResX();
  public double getResY();
  public double getReprojectionError();
  public double[] getCamMatVector();
  public double[] getDistortionCoefficients();
  protected org.json.JSONObject toJson();
}
```

## class LLResultTypes.ClassifierResult

```java
public class com.qualcomm.hardware.limelightvision.LLResultTypes.ClassifierResult {
  protected com.qualcomm.hardware.limelightvision.LLResultTypes.ClassifierResult(org.json.JSONObject);
  public java.lang.String getClassName();
  public int getClassId();
  public double getConfidence();
}
```

## class LLResultTypes.ColorResult

```java
public class com.qualcomm.hardware.limelightvision.LLResultTypes.ColorResult {
  protected com.qualcomm.hardware.limelightvision.LLResultTypes.ColorResult(org.json.JSONObject);
  public java.util.List<java.util.List<java.lang.Double>> getTargetCorners();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getCameraPoseTargetSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getRobotPoseFieldSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getRobotPoseTargetSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getTargetPoseCameraSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getTargetPoseRobotSpace();
  public double getTargetArea();
  public double getTargetXPixels();
  public double getTargetYPixels();
  public double getTargetXDegrees();
  public double getTargetYDegrees();
  public double getTargetXDegreesNoCrosshair();
  public double getTargetYDegreesNoCrosshair();
}
```

## class LLResultTypes.DetectorResult

```java
public class com.qualcomm.hardware.limelightvision.LLResultTypes.DetectorResult {
  protected com.qualcomm.hardware.limelightvision.LLResultTypes.DetectorResult(org.json.JSONObject);
  public java.lang.String getClassName();
  public int getClassId();
  public double getConfidence();
  public java.util.List<java.util.List<java.lang.Double>> getTargetCorners();
  public double getTargetArea();
  public double getTargetXPixels();
  public double getTargetYPixels();
  public double getTargetXDegrees();
  public double getTargetYDegrees();
  public double getTargetXDegreesNoCrosshair();
  public double getTargetYDegreesNoCrosshair();
}
```

## class LLResultTypes.FiducialResult

```java
public class com.qualcomm.hardware.limelightvision.LLResultTypes.FiducialResult {
  protected com.qualcomm.hardware.limelightvision.LLResultTypes.FiducialResult(org.json.JSONObject);
  public int getFiducialId();
  public java.lang.String getFamily();
  public java.util.List<java.util.List<java.lang.Double>> getTargetCorners();
  public double getSkew();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getCameraPoseTargetSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getRobotPoseFieldSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getRobotPoseTargetSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getTargetPoseCameraSpace();
  public org.firstinspires.ftc.robotcore.external.navigation.Pose3D getTargetPoseRobotSpace();
  public double getTargetArea();
  public double getTargetXPixels();
  public double getTargetYPixels();
  public double getTargetXDegrees();
  public double getTargetYDegrees();
  public double getTargetXDegreesNoCrosshair();
  public double getTargetYDegreesNoCrosshair();
}
```

## class LLStatus

```java
public class com.qualcomm.hardware.limelightvision.LLStatus {
  public com.qualcomm.hardware.limelightvision.LLStatus();
  protected com.qualcomm.hardware.limelightvision.LLStatus(org.json.JSONObject);
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion getCameraQuat();
  public int getCid();
  public double getCpu();
  public double getFinalYaw();
  public double getFps();
  public int getHwType();
  public java.lang.String getName();
  public int getPipeImgCount();
  public int getPipelineIndex();
  public java.lang.String getPipelineType();
  public double getRam();
  public int getSnapshotMode();
  public double getTemp();
  public java.lang.String toString();
}
```

## class Limelight3A

```java
public class com.qualcomm.hardware.limelightvision.Limelight3A implements com.qualcomm.robotcore.hardware.HardwareDevice {
  public com.qualcomm.hardware.limelightvision.Limelight3A(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, java.net.InetAddress);
  public synchronized void start();
  public synchronized void pause();
  public synchronized void stop();
  public boolean isRunning();
  public synchronized void setPollRateHz(int);
  public long getTimeSinceLastUpdate();
  public boolean isConnected();
  public com.qualcomm.hardware.limelightvision.LLResult getLatestResult();
  public com.qualcomm.hardware.limelightvision.LLStatus getStatus();
  public boolean reloadPipeline();
  public boolean pipelineSwitch(int);
  public boolean captureSnapshot(java.lang.String);
  public boolean deleteSnapshots();
  public boolean deleteSnapshot(java.lang.String);
  public boolean updatePythonInputs(double, double, double, double, double, double, double, double);
  public boolean updatePythonInputs(double[]);
  public boolean updateRobotOrientation(double);
  public boolean uploadPipeline(java.lang.String, java.lang.Integer);
  public boolean uploadFieldmap(com.qualcomm.hardware.limelightvision.LLFieldMap, java.lang.Integer);
  public boolean uploadPython(java.lang.String, java.lang.Integer);
  public com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult getCalDefault();
  public com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult getCalFile();
  public com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult getCalEEPROM();
  public com.qualcomm.hardware.limelightvision.LLResultTypes.CalibrationResult getCalLatest();
  public void shutdown();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```
