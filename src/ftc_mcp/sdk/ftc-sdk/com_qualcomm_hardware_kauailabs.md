# `com.qualcomm.hardware.kauailabs`

_ftc-sdk 11.1.0 — 8 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class NavxMicroNavigationSensor

```java
public class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters<com.qualcomm.robotcore.hardware.I2cDeviceSynch, com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Parameters> implements com.qualcomm.robotcore.hardware.Gyroscope, com.qualcomm.robotcore.hardware.IntegratingGyroscope, com.qualcomm.robotcore.hardware.I2cAddrConfig {
  public final int NAVX_WRITE_COMMAND_BIT = 128;
  protected static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode readMode;
  protected static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow lowerWindow;
  protected static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow upperWindow;
  protected float gyroScaleFactor;
  public static final com.qualcomm.robotcore.hardware.I2cAddr ADDRESS_I2C_DEFAULT;
  protected static com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow newWindow(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register, com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register);
  public com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected void setReadWindow();
  protected boolean internalInitialize(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Parameters);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.usb.RobotUsbDevice.FirmwareVersion getFirmwareVersion();
  protected void ensureReadWindow(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public synchronized com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register, int);
  public byte read8(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register);
  public short readShort(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register);
  public float readSignedHundredthsFloat(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register);
  protected float shortToSignedHundredths(short);
  public void write8(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register, byte);
  public void writeShort(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register, short);
  public boolean isCalibrating();
  public java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularVelocityAxes();
  public java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularOrientationAxes();
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation getAngularOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  protected boolean internalInitialize(java.lang.Object);
}
```

## class NavxMicroNavigationSensor.CalibrationStatus

```java
public final class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus extends java.lang.Enum<com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus> {
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus IMU_CAL_INPROGRESS;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus IMU_CAL_ACCUMULATE;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus IMU_CAL_COMPLETE;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus IMU_CAL_MASK;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus MAG_CAL_COMPLETE;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus BARO_CAL_COMPLETE;
  public byte bVal;
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus[] values();
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.CalibrationStatus valueOf(java.lang.String);
}
```

## class NavxMicroNavigationSensor.IntegrationControl

```java
public final class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl extends java.lang.Enum<com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl> {
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_VEL_X;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_VEL_Y;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_VEL_Z;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_DISP_X;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_DISP_Y;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_DISP_Z;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_YAW;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl RESET_ALL;
  public byte bVal;
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl[] values();
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl valueOf(java.lang.String);
  public byte bitor(com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.IntegrationControl);
  public byte bitor(byte);
}
```

## class NavxMicroNavigationSensor.OpStatus

```java
public final class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus extends java.lang.Enum<com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus> {
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus INITIALIZING;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus SELFTEST_IN_PROGRESS;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus ERROR;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus IMU_AUTOCAL_IN_PROGRESS;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus NORMAL;
  public byte bVal;
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus[] values();
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.OpStatus valueOf(java.lang.String);
}
```

## class NavxMicroNavigationSensor.Parameters

```java
public class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Parameters implements java.lang.Cloneable {
  public int updateRate;
  public com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Parameters();
  public int realizedUpdateRate();
  public com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Parameters clone();
  public java.lang.Object clone() throws java.lang.CloneNotSupportedException;
}
```

## class NavxMicroNavigationSensor.Register

```java
public final class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register extends java.lang.Enum<com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register> {
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register FIRST;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register WHOAMI;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register HW_REV;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register FW_VER_MAJOR;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register FW_VER_MINOR;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register UPDATE_RATE_HZ;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ACCEL_FSR_G;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_FSR_DPS_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_FSR_DPS_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register OP_STATUS;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register CAL_STATUS;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register SELFTEST_STATUS;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register CAPABILITY_FLAGS_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register CAPABILITY_FLAGS_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register SENSOR_STATUS_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register SENSOR_STATUS_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register TIMESTAMP_L_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register TIMESTAMP_L_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register TIMESTAMP_H_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register TIMESTAMP_H_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register YAW_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register YAW_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ROLL_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ROLL_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PITCH_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PITCH_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register HEADING_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register HEADING_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register FUSED_HEADING_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register FUSED_HEADING_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ALTITUDE_I_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ALTITUDE_I_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ALTITUDE_D_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ALTITUDE_D_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register LINEAR_ACC_X_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register LINEAR_ACC_X_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register LINEAR_ACC_Y_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register LINEAR_ACC_Y_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register LINEAR_ACC_Z_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register LINEAR_ACC_Z_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_W_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_W_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_X_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_X_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_Y_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_Y_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_Z_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_Z_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MPU_TEMP_C_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MPU_TEMP_C_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_X_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_X_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_Y_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_Y_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_Z_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register GYRO_Z_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ACC_X_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ACC_X_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ACC_Y_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ACC_Y_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ACC_Z_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register ACC_Z_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MAG_X_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MAG_X_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MAG_Y_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MAG_Y_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MAG_Z_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register MAG_Z_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PRESSURE_IL;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PRESSURE_IH;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PRESSURE_DL;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PRESSURE_DH;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PRESSURE_TEMP_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PRESSURE_TEMP_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register YAW_OFFSET_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register YAW_OFFSET_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_W_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_W_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_X_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_X_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_Y_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_Y_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_Z_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register QUAT_OFFSET_Z_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register INTEGRATION_CTL;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register PAD_UNUSED;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_X_I_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_X_I_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_X_D_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_X_D_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Y_I_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Y_I_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Y_D_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Y_D_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Z_I_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Z_I_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Z_D_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register VEL_Z_D_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_X_I_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_X_I_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_X_D_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_X_D_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Y_I_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Y_I_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Y_D_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Y_D_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Z_I_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Z_I_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Z_D_L;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register DISP_Z_D_H;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register LAST;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register UNKNOWN;
  public byte bVal;
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register[] values();
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register valueOf(java.lang.String);
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.Register fromByte(byte);
}
```

## class NavxMicroNavigationSensor.SelfTestStatus

```java
public final class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus extends java.lang.Enum<com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus> {
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus COMPLETE;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus RESULT_GYRO_PASSED;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus RESULT_ACCEL_PASSED;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus RESULT_MAG_PASSED;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus RESULT_BARO_PASSED;
  public byte bVal;
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus[] values();
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SelfTestStatus valueOf(java.lang.String);
}
```

## class NavxMicroNavigationSensor.SensorStatus

```java
public final class com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus extends java.lang.Enum<com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus> {
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus MOVING;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus YAW_STABLE;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus MAG_DISTURBANCE;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus ALTITUDE_VALID;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus SEALEVEL_PRESS_SET;
  public static final com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus FUSED_HEADING_VALID;
  public byte bVal;
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus[] values();
  public static com.qualcomm.hardware.kauailabs.NavxMicroNavigationSensor.SensorStatus valueOf(java.lang.String);
}
```
