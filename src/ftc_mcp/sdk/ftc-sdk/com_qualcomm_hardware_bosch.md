# `com.qualcomm.hardware.bosch`

_ftc-sdk 11.1.0 — 49 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class BHI260IMU

```java
public class com.qualcomm.hardware.bosch.BHI260IMU extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters<com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.robotcore.hardware.IMU.Parameters> implements com.qualcomm.robotcore.hardware.IMU {
  public static final boolean DIAGNOSTIC_MODE = false;
  public static final boolean DIAGNOSTIC_MODE_FIFO_PARSING = false;
  public static boolean imuIsPresent(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple);
  public static void flashFirmwareIfNecessary(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple);
  public com.qualcomm.hardware.bosch.BHI260IMU(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  protected boolean internalInitialize(com.qualcomm.robotcore.hardware.IMU.Parameters);
  public void resetYaw();
  public org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles getRobotYawPitchRollAngles();
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation getRobotOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion getRobotOrientationAsQuaternion();
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getRobotAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  protected org.firstinspires.ftc.robotcore.external.navigation.Quaternion getRawQuaternion() throws com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException;
  protected org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getRawAngularVelocity();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getFirmwareVersion();
  protected boolean internalInitialize(java.lang.Object);
  public boolean initialize(com.qualcomm.robotcore.hardware.IMU.Parameters);
}
```

## class BHI260IMU.BootStatusFlag

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag FLASH_DETECTED;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag FLASH_VERIFY_DONE;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag FLASH_VERIFY_ERROR;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag NO_FLASH;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag HOST_INTERFACE_READY;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag FIRMWARE_VERIFY_DONE;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag FIRMWARE_VERIFY_ERROR;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag FIRMWARE_HALTED;
  public static com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.BootStatusFlag valueOf(java.lang.String);
}
```

## class BHI260IMU.CommandError

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.CommandError extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.CommandError> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandError INCORRECT_LENGTH;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandError TOO_LONG;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandError PARAM_WRITE_ERROR;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandError PARAM_READ_ERROR;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandError INVALID_COMMAND;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandError INVALID_PARAM;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandError COMMAND_FAILED;
  public static com.qualcomm.hardware.bosch.BHI260IMU.CommandError[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.CommandError valueOf(java.lang.String);
  public static com.qualcomm.hardware.bosch.BHI260IMU.CommandError fromInt(int);
}
```

## class BHI260IMU.CommandFailureException

```java
class com.qualcomm.hardware.bosch.BHI260IMU.CommandFailureException extends java.lang.Exception {
  public com.qualcomm.hardware.bosch.BHI260IMU.CommandFailureException(java.lang.String);
}
```

## class BHI260IMU.CommandType

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.CommandType extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.CommandType> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandType ERASE_FLASH;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandType WRITE_FLASH;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandType BOOT_FLASH;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandType FIFO_FLUSH;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandType CONFIGURE_SENSOR;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandType CHANGE_SENSOR_DYNAMIC_RANGE;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.CommandType CONTROL_FIFO_FORMAT;
  public static com.qualcomm.hardware.bosch.BHI260IMU.CommandType[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.CommandType valueOf(java.lang.String);
  public static com.qualcomm.hardware.bosch.BHI260IMU.CommandType findById(int);
}
```

## class BHI260IMU.Fifo

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.Fifo extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.Fifo> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Fifo WAKE_UP;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Fifo NON_WAKE_UP;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Fifo STATUS_AND_DEBUG;
  public static com.qualcomm.hardware.bosch.BHI260IMU.Fifo[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.Fifo valueOf(java.lang.String);
}
```

## class BHI260IMU.HostInterfaceControlFlag

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag ABORT_TRANSFER_CHANNEL_0;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag ABORT_TRANSFER_CHANNEL_1;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag ABORT_TRANSFER_CHANNEL_2;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag ABORT_TRANSFER_CHANNEL_3;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag APPLICATION_PROCESSOR_SUSPENDED;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag RESERVED;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag TIMESTAMP_EVENT_REQUEST;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag ASYNC_STATUS_CHANNEL;
  public static com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.HostInterfaceControlFlag valueOf(java.lang.String);
}
```

## class BHI260IMU.InitException

```java
class com.qualcomm.hardware.bosch.BHI260IMU.InitException extends java.lang.Exception {
}
```

## class BHI260IMU.InterruptStatusFlag

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag HOST_INTERRUPT_ASSERTED;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag WAKE_UP_FIFO_STATUS_1;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag WAKE_UP_FIFO_STATUS_2;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag NON_WAKE_UP_FIFO_STATUS_1;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag NON_WAKE_UP_FIFO_STATUS_2;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag STATUS_STATUS;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag DEBUG_STATUS;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag RESET_OR_FAULT;
  public static com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.InterruptStatusFlag valueOf(java.lang.String);
}
```

## class BHI260IMU.NonSensorEventType

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType DEBUG_DATA;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType TIMESTAMP_SMALL_DELTA;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType TIMESTAMP_LARGE_DELTA;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType TIMESTAMP_FULL;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType META_EVENT;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType FILLER;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType PADDING;
  public static com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType valueOf(java.lang.String);
  public static com.qualcomm.hardware.bosch.BHI260IMU.NonSensorEventType findById(int);
}
```

## class BHI260IMU.Register

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.Register extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.Register> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register COMMAND_INPUT;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register WAKE_UP_FIFO_OUTPUT;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register NON_WAKE_UP_FIFO_OUTPUT;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register STATUS_AND_DEBUG_FIFO_OUTPUT;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register CHIP_CONTROL;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register HOST_INTERFACE_CONTROL;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register HOST_INTERRUPT_CONTROL;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register RESET_REQUEST;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register TIMESTAMP_EVENT_REQUEST;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register HOST_CONTROL;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register HOST_STATUS;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register PRODUCT_IDENTIFIER;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register REVISION_IDENTIFIER;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register ROM_VERSION;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register KERNEL_VERSION;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register USER_VERSION;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register FEATURE_STATUS;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register BOOT_STATUS;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register CHIP_ID;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register INTERRUPT_STATUS;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register ERROR_VALUE;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Register GEN_PURPOSE_READ;
  public static com.qualcomm.hardware.bosch.BHI260IMU.Register[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.Register valueOf(java.lang.String);
}
```

## class BHI260IMU.Sensor

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.Sensor extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.Sensor> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Sensor GAME_ROTATION_VECTOR_WAKE_UP;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Sensor GAME_ROTATION_VECTOR_DATA_HOLDER;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Sensor GAME_ROTATION_VECTOR_GPIO_HANDLER;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Sensor GYROSCOPE_CORRECTED_DATA_HOLDER;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.Sensor GYROSCOPE_CORRECTED_GPIO_HANDLER;
  public static com.qualcomm.hardware.bosch.BHI260IMU.Sensor[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.Sensor valueOf(java.lang.String);
}
```

## class BHI260IMU.StatusAndDebugFifoMode

```java
final class com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoMode extends java.lang.Enum<com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoMode> {
  public static final com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoMode SYNCHRONOUS;
  public static final com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoMode ASYNCHRONOUS;
  public static com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoMode[] values();
  public static com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoMode valueOf(java.lang.String);
}
```

## class BHI260IMU.StatusAndDebugFifoModeManager

```java
class com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoModeManager {
  public void lockStatusAndDebugFifoMode(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BHI260IMU.StatusAndDebugFifoMode);
  public void unlockStatusAndDebugFifoMode();
}
```

## class BHI260IMU.StatusPacket

```java
class com.qualcomm.hardware.bosch.BHI260IMU.StatusPacket {
  public final int statusCode;
  public final byte[] payload;
}
```

## interface BNO055IMU

```java
public interface com.qualcomm.hardware.bosch.BNO055IMU {
  public static final com.qualcomm.robotcore.hardware.I2cAddr I2CADDR_UNSPECIFIED;
  public static final com.qualcomm.robotcore.hardware.I2cAddr I2CADDR_DEFAULT;
  public static final com.qualcomm.robotcore.hardware.I2cAddr I2CADDR_ALTERNATE;
  public abstract boolean initialize(com.qualcomm.hardware.bosch.BNO055IMU.Parameters);
  public abstract com.qualcomm.hardware.bosch.BNO055IMU.Parameters getParameters();
  public abstract void close();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Orientation getAngularOrientation();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Orientation getAngularOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Acceleration getOverallAcceleration();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getAngularVelocity();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Acceleration getLinearAcceleration();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Acceleration getGravity();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Temperature getTemperature();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.MagneticFlux getMagneticFieldStrength();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Quaternion getQuaternionOrientation();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Position getPosition();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Velocity getVelocity();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public abstract void startAccelerationIntegration(org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.Velocity, int);
  public abstract void stopAccelerationIntegration();
  public abstract com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus getSystemStatus();
  public abstract com.qualcomm.hardware.bosch.BNO055IMU.SystemError getSystemError();
  public abstract com.qualcomm.hardware.bosch.BNO055IMU.CalibrationStatus getCalibrationStatus();
  public abstract boolean isSystemCalibrated();
  public abstract boolean isGyroCalibrated();
  public abstract boolean isAccelerometerCalibrated();
  public abstract boolean isMagnetometerCalibrated();
  public abstract com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData readCalibrationData();
  public abstract void writeCalibrationData(com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData);
  public abstract byte read8(com.qualcomm.hardware.bosch.BNO055IMU.Register);
  public abstract byte[] read(com.qualcomm.hardware.bosch.BNO055IMU.Register, int);
  public abstract void write8(com.qualcomm.hardware.bosch.BNO055IMU.Register, int);
  public abstract void write(com.qualcomm.hardware.bosch.BNO055IMU.Register, byte[]);
}
```

## class BNO055IMU.AccelBandwidth

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ7_81;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ15_63;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ31_25;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ62_5;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ125;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ250;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ500;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth HZ1000;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth valueOf(java.lang.String);
}
```

## class BNO055IMU.AccelPowerMode

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode NORMAL;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode SUSPEND;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode LOW1;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode STANDBY;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode LOW2;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode DEEP;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode valueOf(java.lang.String);
}
```

## class BNO055IMU.AccelRange

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.AccelRange extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.AccelRange> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelRange G2;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelRange G4;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelRange G8;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelRange G16;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelRange[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelRange valueOf(java.lang.String);
}
```

## class BNO055IMU.AccelUnit

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.AccelUnit extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.AccelUnit> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelUnit METERS_PERSEC_PERSEC;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AccelUnit MILLI_EARTH_GRAVITY;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelUnit[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.AccelUnit valueOf(java.lang.String);
}
```

## interface BNO055IMU.AccelerationIntegrator

```java
public interface com.qualcomm.hardware.bosch.BNO055IMU.AccelerationIntegrator {
  public abstract void initialize(com.qualcomm.hardware.bosch.BNO055IMU.Parameters, org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.Velocity);
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Position getPosition();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Velocity getVelocity();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public abstract void update(org.firstinspires.ftc.robotcore.external.navigation.Acceleration);
}
```

## class BNO055IMU.AngleUnit

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit DEGREES;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit RADIANS;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit valueOf(java.lang.String);
  public org.firstinspires.ftc.robotcore.external.navigation.AngleUnit toAngleUnit();
  public static com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit fromAngleUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
}
```

## class BNO055IMU.CalibrationData

```java
public class com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData implements java.lang.Cloneable {
  public short dxAccel;
  public short dyAccel;
  public short dzAccel;
  public short dxMag;
  public short dyMag;
  public short dzMag;
  public short dxGyro;
  public short dyGyro;
  public short dzGyro;
  public short radiusAccel;
  public short radiusMag;
  public com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData();
  public java.lang.String serialize();
  public static com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData deserialize(java.lang.String);
  public com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData clone();
  public java.lang.Object clone() throws java.lang.CloneNotSupportedException;
}
```

## class BNO055IMU.CalibrationStatus

```java
public class com.qualcomm.hardware.bosch.BNO055IMU.CalibrationStatus {
  public final byte calibrationStatus;
  public com.qualcomm.hardware.bosch.BNO055IMU.CalibrationStatus(int);
  public java.lang.String toString();
}
```

## class BNO055IMU.GyroBandwidth

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ523;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ230;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ116;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ47;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ23;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ12;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ64;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth HZ32;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth valueOf(java.lang.String);
}
```

## class BNO055IMU.GyroPowerMode

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode NORMAL;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode FAST;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode DEEP;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode SUSPEND;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode ADVANCED;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode valueOf(java.lang.String);
}
```

## class BNO055IMU.GyroRange

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.GyroRange extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.GyroRange> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroRange DPS2000;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroRange DPS1000;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroRange DPS500;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroRange DPS250;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.GyroRange DPS125;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.GyroRange[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.GyroRange valueOf(java.lang.String);
}
```

## class BNO055IMU.MagOpMode

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode LOW;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode REGULAR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode ENHANCED;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode HIGH;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode valueOf(java.lang.String);
}
```

## class BNO055IMU.MagPowerMode

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode NORMAL;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode SLEEP;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode SUSPEND;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode FORCE;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode valueOf(java.lang.String);
}
```

## class BNO055IMU.MagRate

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.MagRate extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.MagRate> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ2;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ6;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ8;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ10;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ15;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ20;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ25;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.MagRate HZ30;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.MagRate[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.MagRate valueOf(java.lang.String);
}
```

## class BNO055IMU.Parameters

```java
public class com.qualcomm.hardware.bosch.BNO055IMU.Parameters implements java.lang.Cloneable {
  public com.qualcomm.robotcore.hardware.I2cAddr i2cAddr;
  public com.qualcomm.hardware.bosch.BNO055IMU.SensorMode mode;
  public boolean useExternalCrystal;
  public com.qualcomm.hardware.bosch.BNO055IMU.TempUnit temperatureUnit;
  public com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit angleUnit;
  public com.qualcomm.hardware.bosch.BNO055IMU.AccelUnit accelUnit;
  public com.qualcomm.hardware.bosch.BNO055IMU.PitchMode pitchMode;
  public com.qualcomm.hardware.bosch.BNO055IMU.AccelRange accelRange;
  public com.qualcomm.hardware.bosch.BNO055IMU.AccelBandwidth accelBandwidth;
  public com.qualcomm.hardware.bosch.BNO055IMU.AccelPowerMode accelPowerMode;
  public com.qualcomm.hardware.bosch.BNO055IMU.GyroRange gyroRange;
  public com.qualcomm.hardware.bosch.BNO055IMU.GyroBandwidth gyroBandwidth;
  public com.qualcomm.hardware.bosch.BNO055IMU.GyroPowerMode gyroPowerMode;
  public com.qualcomm.hardware.bosch.BNO055IMU.MagRate magRate;
  public com.qualcomm.hardware.bosch.BNO055IMU.MagOpMode magOpMode;
  public com.qualcomm.hardware.bosch.BNO055IMU.MagPowerMode magPowerMode;
  public com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData calibrationData;
  public java.lang.String calibrationDataFile;
  public com.qualcomm.hardware.bosch.BNO055IMU.AccelerationIntegrator accelerationIntegrationAlgorithm;
  public boolean loggingEnabled;
  public java.lang.String loggingTag;
  public com.qualcomm.hardware.bosch.BNO055IMU.Parameters();
  public com.qualcomm.hardware.bosch.BNO055IMU.Parameters clone();
  public java.lang.Object clone() throws java.lang.CloneNotSupportedException;
}
```

## class BNO055IMU.PitchMode

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.PitchMode extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.PitchMode> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.PitchMode WINDOWS;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.PitchMode ANDROID;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.PitchMode[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.PitchMode valueOf(java.lang.String);
}
```

## class BNO055IMU.Register

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.Register extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.Register> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register PAGE_ID;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register CHIP_ID;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_ID;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_ID;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_ID;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SW_REV_ID_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SW_REV_ID_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register BL_REV_ID;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_DATA_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_DATA_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_DATA_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_DATA_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_DATA_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_DATA_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_DATA_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_DATA_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_DATA_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_DATA_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_DATA_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_DATA_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_DATA_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_DATA_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_DATA_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_DATA_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_DATA_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_DATA_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register EUL_H_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register EUL_H_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register EUL_R_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register EUL_R_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register EUL_P_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register EUL_P_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_W_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_W_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register QUA_DATA_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register LIA_DATA_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register LIA_DATA_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register LIA_DATA_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register LIA_DATA_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register LIA_DATA_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register LIA_DATA_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRV_DATA_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRV_DATA_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRV_DATA_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRV_DATA_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRV_DATA_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRV_DATA_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register TEMP;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register CALIB_STAT;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SELFTEST_RESULT;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register INTR_STAT;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SYS_CLK_STAT;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SYS_STAT;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SYS_ERR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register UNIT_SEL;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register DATA_SELECT;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register OPR_MODE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register PWR_MODE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SYS_TRIGGER;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register TEMP_SOURCE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register AXIS_MAP_CONFIG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register AXIS_MAP_SIGN;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_0_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_0_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_1_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_1_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_2_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_2_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_3_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_3_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_4_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_4_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_5_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_5_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_6_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_6_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_7_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_7_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_8_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register SIC_MATRIX_8_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_OFFSET_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_OFFSET_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_OFFSET_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_OFFSET_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_OFFSET_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_OFFSET_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_OFFSET_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_OFFSET_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_OFFSET_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_OFFSET_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_OFFSET_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_OFFSET_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_OFFSET_X_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_OFFSET_X_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_OFFSET_Y_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_OFFSET_Y_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_OFFSET_Z_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_OFFSET_Z_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_RADIUS_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_RADIUS_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_RADIUS_LSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_RADIUS_MSB;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_CONFIG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register MAG_CONFIG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_CONFIG_0;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_CONFIG_1;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_SLEEP_CONFIG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GYR_SLEEP_CONFIG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register INT_MSK;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register INT_EN;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_AM_THRES;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_INT_SETTINGS;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_HG_DURATION;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_HG_THRES;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_NM_THRES;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register ACC_NM_SET;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_INT_SETTING;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_HR_X_SET;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_DUR_X;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_HR_Y_SET;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_DUR_Y;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_HR_Z_SET;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_DUR_Z;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_AM_THRES;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register GRYO_AM_SET;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register UNIQUE_ID_FIRST;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.Register UNIQUE_ID_LAST;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.Register[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.Register valueOf(java.lang.String);
}
```

## class BNO055IMU.SensorMode

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.SensorMode extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.SensorMode> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode CONFIG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode ACCONLY;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode MAGONLY;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode GYRONLY;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode ACCMAG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode ACCGYRO;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode MAGGYRO;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode AMG;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode IMU;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode COMPASS;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode M4G;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode NDOF_FMC_OFF;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode NDOF;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SensorMode DISABLED;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.SensorMode[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.SensorMode valueOf(java.lang.String);
  public boolean isFusionMode();
  public static com.qualcomm.hardware.bosch.BNO055IMU.SensorMode fromByte(byte);
}
```

## class BNO055IMU.SystemError

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.SystemError extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.SystemError> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError UNKNOWN;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError NO_ERROR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError PERIPHERAL_INITIALIZATION_ERROR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError SYSTEM_INITIALIZATION_ERROR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError SELF_TEST_FAILED;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError REGISTER_MAP_OUT_OF_RANGE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError REGISTER_MAP_ADDRESS_OUT_OF_RANGE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError REGISTER_MAP_WRITE_ERROR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError LOW_POWER_MODE_NOT_AVAILABLE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError ACCELEROMETER_POWER_MODE_NOT_AVAILABLE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError FUSION_CONFIGURATION_ERROR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemError SENSOR_CONFIGURATION_ERROR;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.SystemError[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.SystemError valueOf(java.lang.String);
  public static com.qualcomm.hardware.bosch.BNO055IMU.SystemError from(int);
}
```

## class BNO055IMU.SystemStatus

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus UNKNOWN;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus IDLE;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus SYSTEM_ERROR;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus INITIALIZING_PERIPHERALS;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus SYSTEM_INITIALIZATION;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus SELF_TEST;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus RUNNING_FUSION;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus RUNNING_NO_FUSION;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus valueOf(java.lang.String);
  public static com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus from(int);
  public java.lang.String toShortString();
}
```

## class BNO055IMU.TempUnit

```java
public final class com.qualcomm.hardware.bosch.BNO055IMU.TempUnit extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMU.TempUnit> {
  public static final com.qualcomm.hardware.bosch.BNO055IMU.TempUnit CELSIUS;
  public static final com.qualcomm.hardware.bosch.BNO055IMU.TempUnit FARENHEIT;
  public final byte bVal;
  public static com.qualcomm.hardware.bosch.BNO055IMU.TempUnit[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMU.TempUnit valueOf(java.lang.String);
  public org.firstinspires.ftc.robotcore.external.navigation.TempUnit toTempUnit();
  public static com.qualcomm.hardware.bosch.BNO055IMU.TempUnit fromTempUnit(org.firstinspires.ftc.robotcore.external.navigation.TempUnit);
}
```

## class BNO055IMUImpl

```java
public abstract class com.qualcomm.hardware.bosch.BNO055IMUImpl extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters<com.qualcomm.robotcore.hardware.I2cDeviceSynch, com.qualcomm.hardware.bosch.BNO055IMU.Parameters> implements com.qualcomm.hardware.bosch.BNO055IMU, com.qualcomm.robotcore.hardware.Gyroscope, com.qualcomm.robotcore.hardware.IntegratingGyroscope, com.qualcomm.robotcore.hardware.I2cAddrConfig, com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications {
  protected final java.lang.Object dataLock;
  protected com.qualcomm.hardware.bosch.BNO055IMU.AccelerationIntegrator accelerationAlgorithm;
  protected final java.lang.Object startStopLock;
  protected java.util.concurrent.ExecutorService accelerationMananger;
  protected float delayScale;
  protected static final int msAwaitChipId = 2000;
  protected static final int msAwaitSelfTest = 2000;
  protected static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode readMode;
  protected static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow lowerWindow;
  protected static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow upperWindow;
  protected static final int msExtra = 50;
  public static final byte bCHIP_ID_VALUE = -96;
  public static boolean imuIsPresent(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  protected static com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow newWindow(com.qualcomm.hardware.bosch.BNO055IMU.Register, com.qualcomm.hardware.bosch.BNO055IMU.Register);
  protected void throwIfNotInitialized();
  public com.qualcomm.hardware.bosch.BNO055IMUImpl(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected static com.qualcomm.hardware.bosch.BNO055IMU.Parameters disabledParameters();
  public void resetDeviceConfigurationForOpMode();
  public void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public boolean internalInitialize(com.qualcomm.hardware.bosch.BNO055IMU.Parameters);
  protected boolean internalInitializeOnce(com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus);
  protected void setSensorMode(com.qualcomm.hardware.bosch.BNO055IMU.SensorMode);
  public synchronized com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus getSystemStatus();
  public synchronized com.qualcomm.hardware.bosch.BNO055IMU.SystemError getSystemError();
  public synchronized com.qualcomm.hardware.bosch.BNO055IMU.CalibrationStatus getCalibrationStatus();
  public void close();
  public abstract java.lang.String getDeviceName();
  public abstract com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularVelocityAxes();
  public java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularOrientationAxes();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation getAngularOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public synchronized boolean isSystemCalibrated();
  public synchronized boolean isGyroCalibrated();
  public synchronized boolean isAccelerometerCalibrated();
  public synchronized boolean isMagnetometerCalibrated();
  public com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData readCalibrationData();
  public void writeCalibrationData(com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData);
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Temperature getTemperature();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.MagneticFlux getMagneticFieldStrength();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Acceleration getOverallAcceleration();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Acceleration getLinearAcceleration();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Acceleration getGravity();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getAngularVelocity();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Orientation getAngularOrientation();
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Quaternion getQuaternionOrientation();
  protected float getAngularScale();
  protected float getAccelerationScale();
  protected float getMetersAccelerationScale();
  protected float getFluxScale();
  protected com.qualcomm.hardware.bosch.BNO055IMUImpl.VectorData getVector(com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR, float);
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public org.firstinspires.ftc.robotcore.external.navigation.Velocity getVelocity();
  public org.firstinspires.ftc.robotcore.external.navigation.Position getPosition();
  public void startAccelerationIntegration(org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.Velocity, int);
  public void stopAccelerationIntegration();
  public synchronized byte read8(com.qualcomm.hardware.bosch.BNO055IMU.Register);
  public synchronized byte[] read(com.qualcomm.hardware.bosch.BNO055IMU.Register, int);
  protected short readShort(com.qualcomm.hardware.bosch.BNO055IMU.Register);
  public void write8(com.qualcomm.hardware.bosch.BNO055IMU.Register, int);
  public void write8(com.qualcomm.hardware.bosch.BNO055IMU.Register, int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public void write(com.qualcomm.hardware.bosch.BNO055IMU.Register, byte[]);
  public void write(com.qualcomm.hardware.bosch.BNO055IMU.Register, byte[], com.qualcomm.robotcore.hardware.I2cWaitControl);
  protected void writeShort(com.qualcomm.hardware.bosch.BNO055IMU.Register, short);
  protected void waitForWriteCompletions();
  protected java.lang.String getLoggingTag();
  protected void log_v(java.lang.String, java.lang.Object...);
  protected void log_d(java.lang.String, java.lang.Object...);
  protected void log_w(java.lang.String, java.lang.Object...);
  protected void log_e(java.lang.String, java.lang.Object...);
  protected void ensureReadWindow(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  protected void delayExtra(int);
  protected void delayLoreExtra(int);
  protected void delayLore(int);
  protected void delay(int);
  protected void enterConfigModeFor(java.lang.Runnable);
  protected <T> T enterConfigModeFor(org.firstinspires.ftc.robotcore.external.Func<T>);
  public boolean internalInitialize(java.lang.Object);
  public com.qualcomm.hardware.bosch.BNO055IMU.Parameters getParameters();
  public boolean initialize(com.qualcomm.hardware.bosch.BNO055IMU.Parameters);
}
```

## class BNO055IMUImpl.AccelerationManager

```java
class com.qualcomm.hardware.bosch.BNO055IMUImpl.AccelerationManager implements java.lang.Runnable {
  protected final int msPollInterval;
  protected static final long nsPerMs = 1000000l;
  public void run();
}
```

## class BNO055IMUImpl.ImuNotInitializedException

```java
public class com.qualcomm.hardware.bosch.BNO055IMUImpl.ImuNotInitializedException extends java.lang.RuntimeException {
  public com.qualcomm.hardware.bosch.BNO055IMUImpl.ImuNotInitializedException();
}
```

## class BNO055IMUImpl.POWER_MODE

```java
final class com.qualcomm.hardware.bosch.BNO055IMUImpl.POWER_MODE extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMUImpl.POWER_MODE> {
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.POWER_MODE NORMAL;
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.POWER_MODE LOWPOWER;
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.POWER_MODE SUSPEND;
  protected byte value;
  public static com.qualcomm.hardware.bosch.BNO055IMUImpl.POWER_MODE[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMUImpl.POWER_MODE valueOf(java.lang.String);
  public byte getValue();
}
```

## class BNO055IMUImpl.VECTOR

```java
final class com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR extends java.lang.Enum<com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR> {
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR ACCELEROMETER;
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR MAGNETOMETER;
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR GYROSCOPE;
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR EULER;
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR LINEARACCEL;
  public static final com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR GRAVITY;
  protected byte value;
  public static com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR[] values();
  public static com.qualcomm.hardware.bosch.BNO055IMUImpl.VECTOR valueOf(java.lang.String);
  public byte getValue();
}
```

## class BNO055IMUImpl.VectorData

```java
public class com.qualcomm.hardware.bosch.BNO055IMUImpl.VectorData {
  public com.qualcomm.robotcore.hardware.TimestampedData data;
  public float scale;
  protected java.nio.ByteBuffer buffer;
  public com.qualcomm.hardware.bosch.BNO055IMUImpl.VectorData(com.qualcomm.robotcore.hardware.TimestampedData, float);
  public float next();
}
```

## class BNO055IMUNew

```java
public abstract class com.qualcomm.hardware.bosch.BNO055IMUNew extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters<com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.robotcore.hardware.IMU.Parameters> implements com.qualcomm.robotcore.hardware.IMU {
  public com.qualcomm.hardware.bosch.BNO055IMUNew(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public com.qualcomm.hardware.bosch.BNO055IMUNew(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean, com.qualcomm.robotcore.hardware.I2cAddr);
  protected boolean internalInitialize(com.qualcomm.robotcore.hardware.IMU.Parameters);
  public void resetYaw();
  public org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles getRobotYawPitchRollAngles();
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation getRobotOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion getRobotOrientationAsQuaternion();
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getRobotAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public abstract java.lang.String getDeviceName();
  public abstract com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  protected boolean internalInitialize(java.lang.Object);
  public boolean initialize(com.qualcomm.robotcore.hardware.IMU.Parameters);
}
```

## class BNO055IMUNew.Parameters

```java
public class com.qualcomm.hardware.bosch.BNO055IMUNew.Parameters extends com.qualcomm.robotcore.hardware.IMU.Parameters {
  public com.qualcomm.robotcore.hardware.I2cAddr i2cAddr;
  public com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData calibrationData;
  public java.lang.String calibrationDataFile;
  public com.qualcomm.hardware.bosch.BNO055IMUNew.Parameters(com.qualcomm.robotcore.hardware.ImuOrientationOnRobot);
  public com.qualcomm.hardware.bosch.BNO055IMUNew.Parameters copy();
  public com.qualcomm.robotcore.hardware.IMU.Parameters copy();
}
```

## class BNO055Util

```java
public class com.qualcomm.hardware.bosch.BNO055Util {
  public com.qualcomm.hardware.bosch.BNO055Util();
  public static void sharedInit(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.Parameters) throws com.qualcomm.hardware.bosch.BNO055Util.InitException;
  public static boolean imuIsPresent(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public static com.qualcomm.hardware.bosch.BNO055IMU.SystemStatus getSystemStatus(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, java.lang.String);
  public static void writeCalibrationData(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.CalibrationData);
  public static void setSensorMode(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.SensorMode);
  public static com.qualcomm.hardware.bosch.BNO055IMU.SensorMode getSensorMode(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple);
  public static org.firstinspires.ftc.robotcore.external.navigation.Quaternion getRawQuaternion(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple) throws com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException;
  public static org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getRawAngularVelocity(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public static float getAngularScale(com.qualcomm.hardware.bosch.BNO055IMU.AngleUnit);
  public static byte read8(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.Register);
  public static byte[] read(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.Register, int);
  public static void write8(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.Register, int);
  public static void write8(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.Register, int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public static void write(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.Register, byte[]);
  public static void writeShort(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.bosch.BNO055IMU.Register, short);
}
```

## class BNO055Util.InitException

```java
public class com.qualcomm.hardware.bosch.BNO055Util.InitException extends java.lang.Exception {
  public com.qualcomm.hardware.bosch.BNO055Util.InitException(java.lang.String);
}
```

## class JustLoggingAccelerationIntegrator

```java
public class com.qualcomm.hardware.bosch.JustLoggingAccelerationIntegrator implements com.qualcomm.hardware.bosch.BNO055IMU.AccelerationIntegrator {
  public com.qualcomm.hardware.bosch.JustLoggingAccelerationIntegrator();
  public void initialize(com.qualcomm.hardware.bosch.BNO055IMU.Parameters, org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.Velocity);
  public org.firstinspires.ftc.robotcore.external.navigation.Position getPosition();
  public org.firstinspires.ftc.robotcore.external.navigation.Velocity getVelocity();
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public void update(org.firstinspires.ftc.robotcore.external.navigation.Acceleration);
}
```

## class NaiveAccelerationIntegrator

```java
public class com.qualcomm.hardware.bosch.NaiveAccelerationIntegrator implements com.qualcomm.hardware.bosch.BNO055IMU.AccelerationIntegrator {
  public org.firstinspires.ftc.robotcore.external.navigation.Position getPosition();
  public org.firstinspires.ftc.robotcore.external.navigation.Velocity getVelocity();
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public void initialize(com.qualcomm.hardware.bosch.BNO055IMU.Parameters, org.firstinspires.ftc.robotcore.external.navigation.Position, org.firstinspires.ftc.robotcore.external.navigation.Velocity);
  public void update(org.firstinspires.ftc.robotcore.external.navigation.Acceleration);
}
```
