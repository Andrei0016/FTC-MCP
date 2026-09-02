# `com.qualcomm.hardware.modernrobotics`

_ftc-sdk 11.1.0 — 17 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class ModernRoboticsAnalogOpticalDistanceSensor

```java
public class com.qualcomm.hardware.modernrobotics.ModernRoboticsAnalogOpticalDistanceSensor implements com.qualcomm.robotcore.hardware.OpticalDistanceSensor,com.qualcomm.robotcore.hardware.AnalogSensor {
  protected static final double apiLevelMin = 0.0d;
  protected static final double apiLevelMax = 1.0d;
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsAnalogOpticalDistanceSensor(com.qualcomm.robotcore.hardware.AnalogInputController, int);
  public java.lang.String toString();
  public double getLightDetected();
  public double getMaxVoltage();
  public double getRawLightDetected();
  public double getRawLightDetectedMax();
  public double readRawVoltage();
  public void enableLed(boolean);
  public java.lang.String status();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```

## class ModernRoboticsI2cColorSensor

```java
public class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> implements com.qualcomm.robotcore.hardware.ColorSensor, com.qualcomm.robotcore.hardware.NormalizedColorSensor, com.qualcomm.robotcore.hardware.SwitchableLight, com.qualcomm.robotcore.hardware.I2cAddrConfig {
  public static final com.qualcomm.robotcore.hardware.I2cAddr ADDRESS_I2C_DEFAULT;
  protected final float colorNormalizationFactor = 1.5258789E-5f;
  protected boolean isLightOn;
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected synchronized boolean doInitialize();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public byte read8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register);
  public void write8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register, byte);
  public int readUnsignedByte(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register);
  public int readUnsignedShort(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register);
  public void writeCommand(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command);
  public java.lang.String toString();
  public int red();
  public int green();
  public int blue();
  public int alpha();
  public int argb();
  public com.qualcomm.robotcore.hardware.NormalizedRGBA getNormalizedColors();
  public float getGain();
  public void setGain(float);
  public synchronized void enableLed(boolean);
  public void enableLight(boolean);
  public synchronized boolean isLightOn();
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public void resetDeviceConfigurationForOpMode();
}
```

## class ModernRoboticsI2cColorSensor.Command

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command ACTIVE_LED;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command PASSIVE_LED;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command HZ50;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command HZ60;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command CALIBRATE_BLACK;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command CALIBRATE_WHITE;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Command valueOf(java.lang.String);
}
```

## class ModernRoboticsI2cColorSensor.Register

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register FIRMWARE_REV;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register MANUFACTURE_CODE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register SENSOR_ID;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register COMMAND;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register COLOR_NUMBER;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register RED;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register GREEN;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register BLUE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register ALPHA;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register COLOR_INDEX;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register RED_INDEX;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register GREEN_INDEX;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register BLUE_INDEX;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register RED_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register GREEN_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register BLUE_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register ALPHA_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register NORMALIZED_RED_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register NORMALIZED_GREEN_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register NORMALIZED_BLUE_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register NORMALIZED_ALPHA_READING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register READ_WINDOW_FIRST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register READ_WINDOW_LAST;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cColorSensor.Register valueOf(java.lang.String);
}
```

## class ModernRoboticsI2cCompassSensor

```java
public class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> implements com.qualcomm.robotcore.hardware.CompassSensor, com.qualcomm.robotcore.hardware.I2cAddrConfig {
  public static final com.qualcomm.robotcore.hardware.I2cAddr ADDRESS_I2C_DEFAULT;
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected void setOptimalReadWindow();
  protected synchronized boolean doInitialize();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public byte read8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register);
  public void write8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register, byte);
  public int readShort(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register);
  public void writeShort(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register, short);
  public void writeCommand(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command);
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command readCommand();
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public org.firstinspires.ftc.robotcore.external.navigation.MagneticFlux getMagneticFlux();
  public double getDirection();
  public java.lang.String status();
  public boolean isCalibrating();
  public boolean calibrationFailed();
  public void setMode(com.qualcomm.robotcore.hardware.CompassSensor.CompassMode);
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
}
```

## class ModernRoboticsI2cCompassSensor.Command

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command NORMAL;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command CALIBRATE_IRON;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command ACCEL_NULL_X;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command ACCEL_NULL_Y;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command ACCEL_NULL_Z;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command ACCEL_GAIN_ADJUST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command MEASURE_TILT_UP;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command MEASURE_TILT_DOWN;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command WRITE_EEPROM;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command CALIBRATION_FAILED;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command UNKNOWN;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command valueOf(java.lang.String);
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Command fromByte(byte);
}
```

## class ModernRoboticsI2cCompassSensor.Register

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register READ_WINDOW_FIRST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register FIRMWARE_REV;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MANUFACTURE_CODE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register SENSOR_ID;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register COMMAND;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register HEADING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register ACCELX;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register ACCELY;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register ACCELZ;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAGX;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAGY;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAGZ;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register READ_WINDOW_LAST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register ACCELX_OFFSET;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register ACCELY_OFFSET;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register ACCELZ_OFFSET;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAGX_OFFSET;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAGY_OFFSET;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAGZ_OFFSET;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAG_TILT_COEFF;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register ACCEL_SCALE_COEFF;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAG_SCALE_COEFF_X;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register MAG_SCALE_COEFF_Y;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register UNKNOWN;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cCompassSensor.Register valueOf(java.lang.String);
}
```

## class ModernRoboticsI2cGyro

```java
public class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> implements com.qualcomm.robotcore.hardware.GyroSensor, com.qualcomm.robotcore.hardware.Gyroscope, com.qualcomm.robotcore.hardware.IntegratingGyroscope, com.qualcomm.robotcore.hardware.I2cAddrConfig {
  public static final com.qualcomm.robotcore.hardware.I2cAddr ADDRESS_I2C_DEFAULT;
  protected float degreesPerSecondPerDigit;
  protected com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode headingMode;
  protected float degreesPerZAxisTick;
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected void setOptimalReadWindow();
  protected synchronized boolean doInitialize();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public byte read8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register);
  public void write8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register, byte);
  public short readShort(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register);
  public void writeShort(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register, short);
  public void writeCommand(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command);
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command readCommand();
  public java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularVelocityAxes();
  public java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularOrientationAxes();
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.Orientation getAngularOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public synchronized void setHeadingMode(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode);
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode getHeadingMode();
  public int rawX();
  public int rawY();
  public int rawZ();
  public int getZAxisOffset();
  public void setZAxisOffset(short);
  public int getZAxisScalingCoefficient();
  public void setZAxisScalingCoefficient(int);
  public int getIntegratedZValue();
  public synchronized int getHeading();
  protected int truncate(float);
  protected float normalize0359(float);
  protected float degreesZFromIntegratedZ(int);
  public void resetZAxisIntegrator();
  public java.lang.String status();
  public void calibrate();
  public boolean isCalibrating();
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public double getRotationFraction();
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode getMeasurementMode();
  protected void notSupported();
}
```

## class ModernRoboticsI2cGyro.Command

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command NORMAL;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command CALIBRATE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command RESET_Z_AXIS;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command WRITE_EEPROM;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command UNKNOWN;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command valueOf(java.lang.String);
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Command fromByte(byte);
}
```

## class ModernRoboticsI2cGyro.HeadingMode

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode HEADING_CARTESIAN;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode HEADING_CARDINAL;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.HeadingMode valueOf(java.lang.String);
}
```

## class ModernRoboticsI2cGyro.MeasurementMode

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode GYRO_CALIBRATION_PENDING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode GYRO_CALIBRATING;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode GYRO_NORMAL;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.MeasurementMode valueOf(java.lang.String);
}
```

## class ModernRoboticsI2cGyro.Register

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register READ_WINDOW_FIRST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register FIRMWARE_REV;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register MANUFACTURE_CODE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register SENSOR_ID;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register COMMAND;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register HEADING_DATA;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register INTEGRATED_Z_VALUE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register RAW_X_VAL;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register RAW_Y_VAL;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register RAW_Z_VAL;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register Z_AXIS_OFFSET;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register Z_AXIS_SCALE_COEF;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register READ_WINDOW_LAST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register UNKNOWN;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register valueOf(java.lang.String);
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cGyro.Register fromByte(byte);
}
```

## class ModernRoboticsI2cIrSeekerSensorV3

```java
public class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3 extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> implements com.qualcomm.robotcore.hardware.IrSeekerSensor, com.qualcomm.robotcore.hardware.I2cAddrConfig {
  public static final com.qualcomm.robotcore.hardware.I2cAddr ADDRESS_I2C_DEFAULT;
  public static final double MAX_SENSOR_STRENGTH = 255.0d;
  protected com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode mode;
  protected double signalDetectedThreshold;
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected void setOptimalReadWindow();
  protected boolean doInitialize();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public int getVersion();
  public byte read8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register);
  public void write8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register, byte);
  protected short readShort(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register);
  public java.lang.String toString();
  public synchronized void setSignalDetectedThreshold(double);
  public double getSignalDetectedThreshold();
  public synchronized void setMode(com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode);
  public com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode getMode();
  public boolean signalDetected();
  public synchronized double getAngle();
  public synchronized double getStrength();
  public synchronized com.qualcomm.robotcore.hardware.IrSeekerSensor.IrSeekerIndividualSensor[] getIndividualSensors();
  public synchronized void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
}
```

## class ModernRoboticsI2cIrSeekerSensorV3.Register

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register READ_WINDOW_FIRST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register FIRMWARE_REV;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register MANUFACTURE_CODE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register SENSOR_ID;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register UNUSED;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register DIR_DATA_1200;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register SIGNAL_STRENTH_1200;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register DIR_DATA_600;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register SIGNAL_STRENTH_600;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register LEFT_SIDE_DATA_1200;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register RIGHT_SIDE_DATA_1200;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register LEFT_SIDE_DATA_600;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register RIGHT_SIDE_DATA_600;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register READ_WINDOW_LAST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register UNKNOWN;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cIrSeekerSensorV3.Register valueOf(java.lang.String);
}
```

## class ModernRoboticsI2cRangeSensor

```java
public class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> implements com.qualcomm.robotcore.hardware.DistanceSensor, com.qualcomm.robotcore.hardware.OpticalDistanceSensor, com.qualcomm.robotcore.hardware.I2cAddrConfig {
  public static final com.qualcomm.robotcore.hardware.I2cAddr ADDRESS_I2C_DEFAULT;
  protected static final double apiLevelMin = 0.0d;
  protected static final double apiLevelMax = 1.0d;
  public double aParam;
  public double bParam;
  public double cParam;
  public double dParam;
  public int rawOpticalMinValid;
  protected static final int cmUltrasonicMax = 255;
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected void setOptimalReadWindow();
  protected synchronized boolean doInitialize();
  public double getDistance(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  protected double cmFromOptical(int);
  public double cmUltrasonic();
  public double cmOptical();
  public double getLightDetected();
  public double getRawLightDetected();
  public double getRawLightDetectedMax();
  public void enableLed(boolean);
  public java.lang.String status();
  public int rawUltrasonic();
  public int rawOptical();
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public byte read8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register);
  public void write8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register, byte);
  public void write8(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register, byte, com.qualcomm.robotcore.hardware.I2cWaitControl);
  protected int readUnsignedByte(com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register);
}
```

## class ModernRoboticsI2cRangeSensor.Register

```java
public final class com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register> {
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register FIRST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register FIRMWARE_REV;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register MANUFACTURE_CODE;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register SENSOR_ID;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register ULTRASONIC;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register OPTICAL;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register LAST;
  public static final com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register UNKNOWN;
  public byte bVal;
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register[] values();
  public static com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor.Register valueOf(java.lang.String);
}
```

## class ModernRoboticsTouchSensor

```java
public class com.qualcomm.hardware.modernrobotics.ModernRoboticsTouchSensor implements com.qualcomm.robotcore.hardware.TouchSensor {
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsTouchSensor(com.qualcomm.robotcore.hardware.DigitalChannelController, int);
  public com.qualcomm.hardware.modernrobotics.ModernRoboticsTouchSensor(com.qualcomm.robotcore.hardware.AnalogInputController, int);
  public boolean isDigital();
  public boolean isAnalog();
  public double getAnalogVoltageThreshold();
  public void setAnalogVoltageThreshold(double);
  public java.lang.String toString();
  public double getValue();
  public boolean isPressed();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```
