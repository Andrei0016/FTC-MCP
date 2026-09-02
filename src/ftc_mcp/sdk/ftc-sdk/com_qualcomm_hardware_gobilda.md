# `com.qualcomm.hardware.gobilda`

_ftc-sdk 11.1.0 — 9 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class GoBildaPinpointDriver

```java
public class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple> {
  public com.qualcomm.hardware.gobilda.GoBildaPinpointDriver(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  protected synchronized boolean doInitialize();
  public java.lang.String getDeviceName();
  public void update();
  public void update(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ReadData);
  public void setBulkReadScope(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register...);
  public void setErrorDetectionType(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType);
  public void setOffsets(double, double, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public void recalibrateIMU();
  public void resetPosAndIMU();
  public void setEncoderDirections(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection, com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection);
  public void setEncoderResolution(com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods);
  public void setEncoderResolution(double, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public void setYawScalar(double);
  public void setPosition(org.firstinspires.ftc.robotcore.external.navigation.Pose2D);
  public void setPosX(double, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public void setPosY(double, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public void setHeading(double, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public int getDeviceID();
  public int getDeviceVersion();
  public float getYawScalar();
  public com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus getDeviceStatus();
  public int getLoopTime();
  public double getFrequency();
  public int getEncoderX();
  public int getEncoderY();
  public double getPosX(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getPosY(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getHeading(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public double getHeading(org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit);
  public double getVelX(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getVelY(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getHeadingVelocity(org.firstinspires.ftc.robotcore.external.navigation.UnnormalizedAngleUnit);
  public float getXOffset(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public float getYOffset(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.Pose2D getPosition();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion getQuaternion();
  public double getPitch(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public double getRoll(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
}
```

## class GoBildaPinpointDriver.DeviceControl

```java
final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl RECALIBRATE_IMU;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl RESET_POS_AND_IMU;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl SET_X_ENCODER_REVERSED;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl SET_X_ENCODER_FORWARD;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl SET_Y_ENCODER_REVERSED;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl SET_Y_ENCODER_FORWARD;
  public final int value;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceControl valueOf(java.lang.String);
}
```

## class GoBildaPinpointDriver.DeviceStatus

```java
public final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus NOT_READY;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus READY;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus CALIBRATING;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus FAULT_X_POD_NOT_DETECTED;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus FAULT_Y_POD_NOT_DETECTED;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus FAULT_NO_PODS_DETECTED;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus FAULT_IMU_RUNAWAY;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus FAULT_BAD_READ;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.DeviceStatus valueOf(java.lang.String);
}
```

## class GoBildaPinpointDriver.EncoderDirection

```java
public final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection FORWARD;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection REVERSED;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.EncoderDirection valueOf(java.lang.String);
}
```

## class GoBildaPinpointDriver.ErrorDetectionType

```java
public final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType NONE;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType CRC;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType LOCAL_TEST;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ErrorDetectionType valueOf(java.lang.String);
}
```

## class GoBildaPinpointDriver.GoBildaOdometryPods

```java
public final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods goBILDA_SWINGARM_POD;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods goBILDA_4_BAR_POD;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.GoBildaOdometryPods valueOf(java.lang.String);
}
```

## class GoBildaPinpointDriver.ReadData

```java
public final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ReadData extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ReadData> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ReadData ONLY_UPDATE_HEADING;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ReadData[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.ReadData valueOf(java.lang.String);
}
```

## class GoBildaPinpointDriver.Register

```java
public final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register DEVICE_ID;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register DEVICE_VERSION;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register DEVICE_STATUS;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register DEVICE_CONTROL;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register LOOP_TIME;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register X_ENCODER_VALUE;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register Y_ENCODER_VALUE;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register X_POSITION;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register Y_POSITION;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register H_ORIENTATION;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register X_VELOCITY;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register Y_VELOCITY;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register H_VELOCITY;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register MM_PER_TICK;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register X_POD_OFFSET;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register Y_POD_OFFSET;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register YAW_SCALAR;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register BULK_READ;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register QUATERNION_W;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register QUATERNION_X;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register QUATERNION_Y;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register QUATERNION_Z;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register PITCH;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register ROLL;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register SET_BULK_READ;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.Register valueOf(java.lang.String);
}
```

## class GoBildaPinpointDriver.RegisterType

```java
final class com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType extends java.lang.Enum<com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType> {
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType INT32;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType FLOAT;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType GENERIC;
  public static final com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType BULK;
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType[] values();
  public static com.qualcomm.hardware.gobilda.GoBildaPinpointDriver.RegisterType valueOf(java.lang.String);
}
```
