# `com.qualcomm.robotcore.hardware`

_ftc-sdk 11.1.0 — 129 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface AccelerationSensor

```java
public interface com.qualcomm.robotcore.hardware.AccelerationSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public abstract java.lang.String status();
}
```

## class AnalogInput

```java
public class com.qualcomm.robotcore.hardware.AnalogInput implements com.qualcomm.robotcore.hardware.HardwareDevice {
  public com.qualcomm.robotcore.hardware.AnalogInput(com.qualcomm.robotcore.hardware.AnalogInputController, int);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public double getVoltage();
  public double getMaxVoltage();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```

## interface AnalogInputController

```java
public interface com.qualcomm.robotcore.hardware.AnalogInputController extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract double getAnalogInputVoltage(int);
  public abstract double getMaxAnalogInputVoltage();
  public abstract com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
}
```

## interface AnalogSensor

```java
public interface com.qualcomm.robotcore.hardware.AnalogSensor {
  public abstract double readRawVoltage();
}
```

## interface Blinker

```java
public interface com.qualcomm.robotcore.hardware.Blinker {
  public abstract void setPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  public abstract java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step> getPattern();
  public abstract void pushPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  public abstract boolean patternStackNotEmpty();
  public abstract boolean popPattern();
  public abstract void setConstant(int);
  public abstract void stopBlinking();
  public abstract int getBlinkerPatternMaxLength();
}
```

## class Blinker.Step

```java
public class com.qualcomm.robotcore.hardware.Blinker.Step {
  protected int color;
  protected int msDuration;
  public com.qualcomm.robotcore.hardware.Blinker.Step();
  public com.qualcomm.robotcore.hardware.Blinker.Step(int, long, java.util.concurrent.TimeUnit);
  public static com.qualcomm.robotcore.hardware.Blinker.Step nullStep();
  public boolean equals(java.lang.Object);
  public boolean equals(com.qualcomm.robotcore.hardware.Blinker.Step);
  public int hashCode();
  public boolean isLit();
  public void setLit(boolean);
  public int getColor();
  public void setColor(int);
  public int getDurationMs();
  public void setDuration(long, java.util.concurrent.TimeUnit);
  public java.lang.String toString();
}
```

## interface CRServo

```java
public interface com.qualcomm.robotcore.hardware.CRServo extends com.qualcomm.robotcore.hardware.DcMotorSimple {
  public abstract com.qualcomm.robotcore.hardware.ServoController getController();
  public abstract int getPortNumber();
}
```

## class CRServoImpl

```java
public class com.qualcomm.robotcore.hardware.CRServoImpl implements com.qualcomm.robotcore.hardware.CRServo {
  protected com.qualcomm.robotcore.hardware.ServoController controller;
  protected int portNumber;
  protected com.qualcomm.robotcore.hardware.DcMotorSimple.Direction direction;
  protected static final double apiPowerMin = -1.0d;
  protected static final double apiPowerMax = 1.0d;
  protected static final double apiServoPositionMin = 0.0d;
  protected static final double apiServoPositionMax = 1.0d;
  public com.qualcomm.robotcore.hardware.CRServoImpl(com.qualcomm.robotcore.hardware.ServoController, int);
  public com.qualcomm.robotcore.hardware.CRServoImpl(com.qualcomm.robotcore.hardware.ServoController, int, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public synchronized void resetDeviceConfigurationForOpMode();
  public void close();
  public com.qualcomm.robotcore.hardware.ServoController getController();
  public int getPortNumber();
  public synchronized void setDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public synchronized com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getDirection();
  public void setPower(double);
  public double getPower();
}
```

## class CRServoImplEx

```java
public class com.qualcomm.robotcore.hardware.CRServoImplEx extends com.qualcomm.robotcore.hardware.CRServoImpl implements com.qualcomm.robotcore.hardware.PwmControl {
  protected com.qualcomm.robotcore.hardware.ServoControllerEx controllerEx;
  public com.qualcomm.robotcore.hardware.CRServoImplEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public com.qualcomm.robotcore.hardware.CRServoImplEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public void setPwmRange(com.qualcomm.robotcore.hardware.PwmControl.PwmRange);
  public com.qualcomm.robotcore.hardware.PwmControl.PwmRange getPwmRange();
  public void setPwmEnable();
  public void setPwmDisable();
  public boolean isPwmEnabled();
}
```

## interface ColorRangeSensor

```java
public interface com.qualcomm.robotcore.hardware.ColorRangeSensor extends com.qualcomm.robotcore.hardware.ColorSensor,com.qualcomm.robotcore.hardware.NormalizedColorSensor,com.qualcomm.robotcore.hardware.DistanceSensor,com.qualcomm.robotcore.hardware.OpticalDistanceSensor,com.qualcomm.robotcore.hardware.LightSensor {
}
```

## interface ColorSensor

```java
public interface com.qualcomm.robotcore.hardware.ColorSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract int red();
  public abstract int green();
  public abstract int blue();
  public abstract int alpha();
  public abstract int argb();
  public abstract void enableLed(boolean);
  public abstract void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public abstract com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
}
```

## interface CompassSensor

```java
public interface com.qualcomm.robotcore.hardware.CompassSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract double getDirection();
  public abstract java.lang.String status();
  public abstract void setMode(com.qualcomm.robotcore.hardware.CompassSensor.CompassMode);
  public abstract boolean calibrationFailed();
}
```

## class CompassSensor.CompassMode

```java
public final class com.qualcomm.robotcore.hardware.CompassSensor.CompassMode extends java.lang.Enum<com.qualcomm.robotcore.hardware.CompassSensor.CompassMode> {
  public static final com.qualcomm.robotcore.hardware.CompassSensor.CompassMode MEASUREMENT_MODE;
  public static final com.qualcomm.robotcore.hardware.CompassSensor.CompassMode CALIBRATION_MODE;
  public static com.qualcomm.robotcore.hardware.CompassSensor.CompassMode[] values();
  public static com.qualcomm.robotcore.hardware.CompassSensor.CompassMode valueOf(java.lang.String);
}
```

## class ControlSystem

```java
public final class com.qualcomm.robotcore.hardware.ControlSystem extends java.lang.Enum<com.qualcomm.robotcore.hardware.ControlSystem> {
  public static final com.qualcomm.robotcore.hardware.ControlSystem REV_HUB;
  public static com.qualcomm.robotcore.hardware.ControlSystem[] values();
  public static com.qualcomm.robotcore.hardware.ControlSystem valueOf(java.lang.String);
}
```

## interface DcMotor

```java
public interface com.qualcomm.robotcore.hardware.DcMotor extends com.qualcomm.robotcore.hardware.DcMotorSimple {
  public abstract com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType getMotorType();
  public abstract void setMotorType(com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType);
  public abstract com.qualcomm.robotcore.hardware.DcMotorController getController();
  public abstract int getPortNumber();
  public abstract void setZeroPowerBehavior(com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior);
  public abstract com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior getZeroPowerBehavior();
  public abstract void setPowerFloat();
  public abstract boolean getPowerFloat();
  public abstract void setTargetPosition(int);
  public abstract int getTargetPosition();
  public abstract boolean isBusy();
  public abstract int getCurrentPosition();
  public abstract void setMode(com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public abstract com.qualcomm.robotcore.hardware.DcMotor.RunMode getMode();
}
```

## class DcMotor.RunMode

```java
public final class com.qualcomm.robotcore.hardware.DcMotor.RunMode extends java.lang.Enum<com.qualcomm.robotcore.hardware.DcMotor.RunMode> {
  public static final com.qualcomm.robotcore.hardware.DcMotor.RunMode RUN_WITHOUT_ENCODER;
  public static final com.qualcomm.robotcore.hardware.DcMotor.RunMode RUN_USING_ENCODER;
  public static final com.qualcomm.robotcore.hardware.DcMotor.RunMode RUN_TO_POSITION;
  public static final com.qualcomm.robotcore.hardware.DcMotor.RunMode STOP_AND_RESET_ENCODER;
  public static final com.qualcomm.robotcore.hardware.DcMotor.RunMode RUN_WITHOUT_ENCODERS;
  public static final com.qualcomm.robotcore.hardware.DcMotor.RunMode RUN_USING_ENCODERS;
  public static final com.qualcomm.robotcore.hardware.DcMotor.RunMode RESET_ENCODERS;
  public static com.qualcomm.robotcore.hardware.DcMotor.RunMode[] values();
  public static com.qualcomm.robotcore.hardware.DcMotor.RunMode valueOf(java.lang.String);
  public com.qualcomm.robotcore.hardware.DcMotor.RunMode migrate();
  public boolean isPIDMode();
}
```

## class DcMotor.ZeroPowerBehavior

```java
public final class com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior extends java.lang.Enum<com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior> {
  public static final com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior UNKNOWN;
  public static final com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior BRAKE;
  public static final com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior FLOAT;
  public static com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior[] values();
  public static com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior valueOf(java.lang.String);
}
```

## interface DcMotorController

```java
public interface com.qualcomm.robotcore.hardware.DcMotorController extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void setMotorType(int, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType);
  public abstract com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType getMotorType(int);
  public abstract void setMotorMode(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public abstract com.qualcomm.robotcore.hardware.DcMotor.RunMode getMotorMode(int);
  public abstract void setMotorPower(int, double);
  public abstract double getMotorPower(int);
  public abstract boolean isBusy(int);
  public abstract void setMotorZeroPowerBehavior(int, com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior);
  public abstract com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior getMotorZeroPowerBehavior(int);
  public abstract boolean getMotorPowerFloat(int);
  public abstract void setMotorTargetPosition(int, int);
  public abstract int getMotorTargetPosition(int);
  public abstract int getMotorCurrentPosition(int);
  public abstract void resetDeviceConfigurationForOpMode(int);
}
```

## interface DcMotorControllerEx

```java
public interface com.qualcomm.robotcore.hardware.DcMotorControllerEx extends com.qualcomm.robotcore.hardware.DcMotorController {
  public abstract void setMotorEnable(int);
  public abstract void setMotorDisable(int);
  public abstract boolean isMotorEnabled(int);
  public abstract void setMotorVelocity(int, double);
  public abstract void setMotorVelocity(int, double, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public abstract double getMotorVelocity(int);
  public abstract double getMotorVelocity(int, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public abstract void setPIDCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDCoefficients);
  public abstract void setPIDFCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDFCoefficients) throws java.lang.UnsupportedOperationException;
  public abstract com.qualcomm.robotcore.hardware.PIDCoefficients getPIDCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public abstract com.qualcomm.robotcore.hardware.PIDFCoefficients getPIDFCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public abstract void setMotorTargetPosition(int, int, int);
  public abstract double getMotorCurrent(int, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public abstract double getMotorCurrentAlert(int, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public abstract void setMotorCurrentAlert(int, double, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public abstract boolean isMotorOverCurrent(int);
}
```

## interface DcMotorEx

```java
public interface com.qualcomm.robotcore.hardware.DcMotorEx extends com.qualcomm.robotcore.hardware.DcMotor {
  public abstract void setMotorEnable();
  public abstract void setMotorDisable();
  public abstract boolean isMotorEnabled();
  public abstract void setVelocity(double);
  public abstract void setVelocity(double, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public abstract double getVelocity();
  public abstract double getVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public abstract void setPIDCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDCoefficients);
  public abstract void setPIDFCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDFCoefficients) throws java.lang.UnsupportedOperationException;
  public abstract void setVelocityPIDFCoefficients(double, double, double, double);
  public abstract void setPositionPIDFCoefficients(double);
  public abstract com.qualcomm.robotcore.hardware.PIDCoefficients getPIDCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public abstract com.qualcomm.robotcore.hardware.PIDFCoefficients getPIDFCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public abstract void setTargetPositionTolerance(int);
  public abstract int getTargetPositionTolerance();
  public abstract double getCurrent(org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public abstract double getCurrentAlert(org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public abstract void setCurrentAlert(double, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public abstract boolean isOverCurrent();
}
```

## class DcMotorImpl

```java
public class com.qualcomm.robotcore.hardware.DcMotorImpl implements com.qualcomm.robotcore.hardware.DcMotor {
  protected com.qualcomm.robotcore.hardware.DcMotorController controller;
  protected int portNumber;
  protected com.qualcomm.robotcore.hardware.DcMotorSimple.Direction direction;
  protected com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType motorType;
  public com.qualcomm.robotcore.hardware.DcMotorImpl(com.qualcomm.robotcore.hardware.DcMotorController, int);
  public com.qualcomm.robotcore.hardware.DcMotorImpl(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.qualcomm.robotcore.hardware.DcMotorImpl(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
  public com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType getMotorType();
  public void setMotorType(com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType);
  public com.qualcomm.robotcore.hardware.DcMotorController getController();
  public synchronized void setDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getDirection();
  public int getPortNumber();
  public synchronized void setPower(double);
  protected void internalSetPower(double);
  public synchronized double getPower();
  public boolean isBusy();
  public synchronized void setZeroPowerBehavior(com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior);
  public synchronized com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior getZeroPowerBehavior();
  public synchronized void setPowerFloat();
  public synchronized boolean getPowerFloat();
  public synchronized void setTargetPosition(int);
  protected void internalSetTargetPosition(int);
  public synchronized int getTargetPosition();
  public synchronized int getCurrentPosition();
  protected int adjustPosition(int);
  protected double adjustPower(double);
  protected com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getOperationalDirection();
  public synchronized void setMode(com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  protected void internalSetMode(com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public com.qualcomm.robotcore.hardware.DcMotor.RunMode getMode();
}
```

## class DcMotorImplEx

```java
public class com.qualcomm.robotcore.hardware.DcMotorImplEx extends com.qualcomm.robotcore.hardware.DcMotorImpl implements com.qualcomm.robotcore.hardware.DcMotorEx {
  public com.qualcomm.robotcore.hardware.DcMotorImplEx(com.qualcomm.robotcore.hardware.DcMotorController, int);
  public com.qualcomm.robotcore.hardware.DcMotorImplEx(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public com.qualcomm.robotcore.hardware.DcMotorImplEx(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.DcMotorSimple.Direction, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType);
  public void setMotorEnable();
  public void setMotorDisable();
  public boolean isMotorEnabled();
  public synchronized void setVelocity(double);
  public synchronized void setVelocity(double, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public synchronized double getVelocity();
  public synchronized double getVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  protected double adjustAngularRate(double);
  public void setPIDCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDCoefficients);
  public void setPIDFCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDFCoefficients);
  public void setVelocityPIDFCoefficients(double, double, double, double);
  public void setPositionPIDFCoefficients(double);
  public com.qualcomm.robotcore.hardware.PIDCoefficients getPIDCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public com.qualcomm.robotcore.hardware.PIDFCoefficients getPIDFCoefficients(com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public int getTargetPositionTolerance();
  public synchronized void setTargetPositionTolerance(int);
  protected void internalSetTargetPosition(int);
  public double getCurrent(org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public double getCurrentAlert(org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public void setCurrentAlert(double, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public boolean isOverCurrent();
}
```

## interface DcMotorSimple

```java
public interface com.qualcomm.robotcore.hardware.DcMotorSimple extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void setDirection(com.qualcomm.robotcore.hardware.DcMotorSimple.Direction);
  public abstract com.qualcomm.robotcore.hardware.DcMotorSimple.Direction getDirection();
  public abstract void setPower(double);
  public abstract double getPower();
}
```

## class DcMotorSimple.Direction

```java
public final class com.qualcomm.robotcore.hardware.DcMotorSimple.Direction extends java.lang.Enum<com.qualcomm.robotcore.hardware.DcMotorSimple.Direction> {
  public static final com.qualcomm.robotcore.hardware.DcMotorSimple.Direction FORWARD;
  public static final com.qualcomm.robotcore.hardware.DcMotorSimple.Direction REVERSE;
  public static com.qualcomm.robotcore.hardware.DcMotorSimple.Direction[] values();
  public static com.qualcomm.robotcore.hardware.DcMotorSimple.Direction valueOf(java.lang.String);
  public com.qualcomm.robotcore.hardware.DcMotorSimple.Direction inverted();
}
```

## interface DeviceManager

```java
public interface com.qualcomm.robotcore.hardware.DeviceManager {
  public abstract com.qualcomm.robotcore.hardware.ScannedDevices scanForUsbDevices() throws com.qualcomm.robotcore.exception.RobotCoreException;
  public abstract com.qualcomm.robotcore.hardware.DcMotor createDcMotor(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.DcMotor createDcMotorEx(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.Servo createServoEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, java.lang.String, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public abstract com.qualcomm.robotcore.hardware.CRServo createCRServoEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, java.lang.String, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public abstract java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createCustomServoDeviceInstances(com.qualcomm.robotcore.hardware.ServoControllerEx, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public abstract java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createAnalogSensorInstances(com.qualcomm.robotcore.hardware.AnalogInputController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.AnalogSensorConfigurationType);
  public abstract java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createDigitalDeviceInstances(com.qualcomm.robotcore.hardware.DigitalChannelController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.DigitalIoDeviceConfigurationType);
  public abstract com.qualcomm.robotcore.hardware.PWMOutput createPwmOutputDevice(com.qualcomm.robotcore.hardware.PWMOutputController, int, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.I2cDeviceSynch createI2cDeviceSynch(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public abstract java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createI2cDeviceInstances(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, com.qualcomm.robotcore.hardware.configuration.typecontainers.I2cDeviceConfigurationType, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.HardwareDevice createLimelight3A(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, java.net.InetAddress);
  public abstract com.qualcomm.robotcore.hardware.RobotCoreLynxUsbDevice createLynxUsbDevice(com.qualcomm.robotcore.util.SerialNumber, java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName createWebcamName(com.qualcomm.robotcore.util.SerialNumber, java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public abstract com.qualcomm.robotcore.hardware.TouchSensor createMRDigitalTouchSensor(com.qualcomm.robotcore.hardware.DigitalChannelController, int, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.IrSeekerSensor createMRI2cIrSeekerSensorV3(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.GyroSensor createModernRoboticsI2cGyroSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.ColorSensor createAdafruitI2cColorSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.ColorSensor createLynxColorRangeSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.ColorSensor createModernRoboticsI2cColorSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public abstract com.qualcomm.robotcore.hardware.LED createLED(com.qualcomm.robotcore.hardware.DigitalChannelController, int, java.lang.String);
}
```

## class DeviceManager.UsbDeviceType

```java
public final class com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType extends java.lang.Enum<com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType> {
  public static final com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType FTDI_USB_UNKNOWN_DEVICE;
  public static final com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType LYNX_USB_DEVICE;
  public static final com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType WEBCAM;
  public static final com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType ETHERNET_DEVICE;
  public static final com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType UNKNOWN_DEVICE;
  public static com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType[] values();
  public static com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType valueOf(java.lang.String);
  public static com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType from(java.lang.String);
}
```

## interface DigitalChannel

```java
public interface com.qualcomm.robotcore.hardware.DigitalChannel extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract com.qualcomm.robotcore.hardware.DigitalChannel.Mode getMode();
  public abstract void setMode(com.qualcomm.robotcore.hardware.DigitalChannel.Mode);
  public abstract boolean getState();
  public abstract void setState(boolean);
  public abstract void setMode(com.qualcomm.robotcore.hardware.DigitalChannelController.Mode);
}
```

## class DigitalChannel.Mode

```java
public final class com.qualcomm.robotcore.hardware.DigitalChannel.Mode extends java.lang.Enum<com.qualcomm.robotcore.hardware.DigitalChannel.Mode> {
  public static final com.qualcomm.robotcore.hardware.DigitalChannel.Mode INPUT;
  public static final com.qualcomm.robotcore.hardware.DigitalChannel.Mode OUTPUT;
  public static com.qualcomm.robotcore.hardware.DigitalChannel.Mode[] values();
  public static com.qualcomm.robotcore.hardware.DigitalChannel.Mode valueOf(java.lang.String);
}
```

## interface DigitalChannelController

```java
public interface com.qualcomm.robotcore.hardware.DigitalChannelController extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public abstract com.qualcomm.robotcore.hardware.DigitalChannel.Mode getDigitalChannelMode(int);
  public abstract void setDigitalChannelMode(int, com.qualcomm.robotcore.hardware.DigitalChannel.Mode);
  public abstract void setDigitalChannelMode(int, com.qualcomm.robotcore.hardware.DigitalChannelController.Mode);
  public abstract boolean getDigitalChannelState(int);
  public abstract void setDigitalChannelState(int, boolean);
}
```

## class DigitalChannelController.Mode

```java
public final class com.qualcomm.robotcore.hardware.DigitalChannelController.Mode extends java.lang.Enum<com.qualcomm.robotcore.hardware.DigitalChannelController.Mode> {
  public static final com.qualcomm.robotcore.hardware.DigitalChannelController.Mode INPUT;
  public static final com.qualcomm.robotcore.hardware.DigitalChannelController.Mode OUTPUT;
  public static com.qualcomm.robotcore.hardware.DigitalChannelController.Mode[] values();
  public static com.qualcomm.robotcore.hardware.DigitalChannelController.Mode valueOf(java.lang.String);
  public com.qualcomm.robotcore.hardware.DigitalChannel.Mode migrate();
}
```

## class DigitalChannelImpl

```java
public class com.qualcomm.robotcore.hardware.DigitalChannelImpl implements com.qualcomm.robotcore.hardware.DigitalChannel {
  public com.qualcomm.robotcore.hardware.DigitalChannelImpl(com.qualcomm.robotcore.hardware.DigitalChannelController, int);
  public com.qualcomm.robotcore.hardware.DigitalChannel.Mode getMode();
  public void setMode(com.qualcomm.robotcore.hardware.DigitalChannel.Mode);
  public void setMode(com.qualcomm.robotcore.hardware.DigitalChannelController.Mode);
  public boolean getState();
  public void setState(boolean);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```

## interface DistanceSensor

```java
public interface com.qualcomm.robotcore.hardware.DistanceSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public static final double distanceOutOfRange = 1.7976931348623157E308d;
  public abstract double getDistance(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
}
```

## class EmbeddedControlHubModule

```java
public class com.qualcomm.robotcore.hardware.EmbeddedControlHubModule {
  public static final java.lang.String TAG = "EmbeddedControlHubModule";
  protected static volatile com.qualcomm.robotcore.hardware.RobotCoreLynxModule embeddedLynxModule;
  protected static volatile com.qualcomm.robotcore.hardware.LynxModuleImuType embeddedImuType;
  public com.qualcomm.robotcore.hardware.EmbeddedControlHubModule();
  public static com.qualcomm.robotcore.hardware.RobotCoreLynxModule get();
  public static void set(com.qualcomm.robotcore.hardware.RobotCoreLynxModule);
  public static com.qualcomm.robotcore.hardware.LynxModuleImuType getImuType();
  public static void setImuType(com.qualcomm.robotcore.hardware.LynxModuleImuType);
  public static void clear();
}
```

## interface Engagable

```java
public interface com.qualcomm.robotcore.hardware.Engagable {
  public abstract void disengage();
  public abstract void engage();
  public abstract boolean isEngaged();
}
```

## class Gamepad

```java
public class com.qualcomm.robotcore.hardware.Gamepad extends com.qualcomm.robotcore.robocol.RobocolParsableBase {
  public static final int ID_UNASSOCIATED = -1;
  public static final int ID_SYNTHETIC = -2;
  public volatile com.qualcomm.robotcore.hardware.Gamepad.Type type;
  public volatile float left_stick_x;
  public volatile float left_stick_y;
  public volatile float right_stick_x;
  public volatile float right_stick_y;
  public volatile boolean dpad_up;
  public volatile boolean dpad_down;
  public volatile boolean dpad_left;
  public volatile boolean dpad_right;
  public volatile boolean a;
  public volatile boolean b;
  public volatile boolean x;
  public volatile boolean y;
  public volatile boolean guide;
  public volatile boolean start;
  public volatile boolean back;
  public volatile boolean left_bumper;
  public volatile boolean right_bumper;
  public volatile boolean left_stick_button;
  public volatile boolean right_stick_button;
  public volatile float left_trigger;
  public volatile float right_trigger;
  public static final float DEFAULT_TRIGGER_THRESHOLD = 0.5f;
  public volatile boolean left_trigger_pressed;
  public volatile boolean right_trigger_pressed;
  public volatile boolean circle;
  public volatile boolean cross;
  public volatile boolean triangle;
  public volatile boolean square;
  public volatile boolean share;
  public volatile boolean options;
  public volatile boolean touchpad;
  public volatile boolean touchpad_finger_1;
  public volatile boolean touchpad_finger_2;
  public volatile float touchpad_finger_1_x;
  public volatile float touchpad_finger_1_y;
  public volatile float touchpad_finger_2_x;
  public volatile float touchpad_finger_2_y;
  public volatile boolean ps;
  protected volatile byte user;
  protected volatile byte userForEffects;
  public volatile int id;
  public volatile long timestamp;
  public org.firstinspires.ftc.robotcore.internal.collections.EvictingBlockingQueue<com.qualcomm.robotcore.hardware.Gamepad.LedEffect> ledQueue;
  public static final int LED_DURATION_CONTINUOUS = -1;
  public org.firstinspires.ftc.robotcore.internal.collections.EvictingBlockingQueue<com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect> rumbleQueue;
  public long nextRumbleApproxFinishTime;
  public static final int RUMBLE_DURATION_CONTINUOUS = -1;
  public void setTriggerThreshold(float);
  public float getTriggerThreshold();
  public org.firstinspires.ftc.robotcore.internal.ui.GamepadUser getUser();
  public void setUser(org.firstinspires.ftc.robotcore.internal.ui.GamepadUser);
  public void setUserForEffects(byte);
  public void setGamepadId(int);
  public int getGamepadId();
  public void setTimestamp(long);
  public void refreshTimestamp();
  public com.qualcomm.robotcore.hardware.Gamepad();
  public void copy(com.qualcomm.robotcore.hardware.Gamepad);
  public void reset();
  public com.qualcomm.robotcore.robocol.RobocolParsable.MsgType getRobocolMsgType();
  public byte[] toByteArray();
  public void fromByteArray(byte[]);
  public boolean atRest();
  public com.qualcomm.robotcore.hardware.Gamepad.Type type();
  public java.lang.String toString();
  protected java.lang.String ps4ToString();
  protected java.lang.String genericToString();
  public void setLedColor(double, double, double, int);
  public void runLedEffect(com.qualcomm.robotcore.hardware.Gamepad.LedEffect);
  public void runRumbleEffect(com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect);
  public void rumble(int);
  public void rumble(double, double, int);
  public void stopRumble();
  public void rumbleBlips(int);
  public boolean isRumbling();
  protected void updateButtonAliases();
  public void resetEdgeDetection();
  public boolean dpadUpWasPressed();
  public boolean dpadUpWasReleased();
  public boolean dpadDownWasPressed();
  public boolean dpadDownWasReleased();
  public boolean dpadLeftWasPressed();
  public boolean dpadLeftWasReleased();
  public boolean dpadRightWasPressed();
  public boolean dpadRightWasReleased();
  public boolean aWasPressed();
  public boolean aWasReleased();
  public boolean bWasPressed();
  public boolean bWasReleased();
  public boolean xWasPressed();
  public boolean xWasReleased();
  public boolean yWasPressed();
  public boolean yWasReleased();
  public boolean guideWasPressed();
  public boolean guideWasReleased();
  public boolean startWasPressed();
  public boolean startWasReleased();
  public boolean backWasPressed();
  public boolean backWasReleased();
  public boolean leftBumperWasPressed();
  public boolean leftBumperWasReleased();
  public boolean rightBumperWasPressed();
  public boolean rightBumperWasReleased();
  public boolean leftStickButtonWasPressed();
  public boolean leftStickButtonWasReleased();
  public boolean rightStickButtonWasPressed();
  public boolean rightStickButtonWasReleased();
  public boolean circleWasPressed();
  public boolean circleWasReleased();
  public boolean crossWasPressed();
  public boolean crossWasReleased();
  public boolean triangleWasPressed();
  public boolean triangleWasReleased();
  public boolean squareWasPressed();
  public boolean squareWasReleased();
  public boolean shareWasPressed();
  public boolean shareWasReleased();
  public boolean optionsWasPressed();
  public boolean optionsWasReleased();
  public boolean touchpadWasPressed();
  public boolean touchpadWasReleased();
  public boolean psWasPressed();
  public boolean psWasReleased();
  public boolean leftTriggerWasPressed();
  public boolean leftTriggerWasReleased();
  public boolean rightTriggerWasPressed();
  public boolean rightTriggerWasReleased();
}
```

## class Gamepad.LedEffect

```java
public class com.qualcomm.robotcore.hardware.Gamepad.LedEffect {
  public final java.util.ArrayList<com.qualcomm.robotcore.hardware.Gamepad.LedEffect.Step> steps;
  public final boolean repeating;
  public int user;
  public java.lang.String serialize();
  public static com.qualcomm.robotcore.hardware.Gamepad.LedEffect deserialize(java.lang.String);
}
```

## class Gamepad.LedEffect.Builder

```java
public class com.qualcomm.robotcore.hardware.Gamepad.LedEffect.Builder {
  public com.qualcomm.robotcore.hardware.Gamepad.LedEffect.Builder();
  public com.qualcomm.robotcore.hardware.Gamepad.LedEffect.Builder addStep(double, double, double, int);
  public com.qualcomm.robotcore.hardware.Gamepad.LedEffect.Builder setRepeating(boolean);
  public com.qualcomm.robotcore.hardware.Gamepad.LedEffect build();
}
```

## class Gamepad.LedEffect.Step

```java
public class com.qualcomm.robotcore.hardware.Gamepad.LedEffect.Step {
  public int r;
  public int g;
  public int b;
  public int duration;
  public com.qualcomm.robotcore.hardware.Gamepad.LedEffect.Step();
}
```

## class Gamepad.LegacyType

```java
public final class com.qualcomm.robotcore.hardware.Gamepad.LegacyType extends java.lang.Enum<com.qualcomm.robotcore.hardware.Gamepad.LegacyType> {
  public static final com.qualcomm.robotcore.hardware.Gamepad.LegacyType UNKNOWN;
  public static final com.qualcomm.robotcore.hardware.Gamepad.LegacyType LOGITECH_F310;
  public static final com.qualcomm.robotcore.hardware.Gamepad.LegacyType XBOX_360;
  public static final com.qualcomm.robotcore.hardware.Gamepad.LegacyType SONY_PS4;
  public static com.qualcomm.robotcore.hardware.Gamepad.LegacyType[] values();
  public static com.qualcomm.robotcore.hardware.Gamepad.LegacyType valueOf(java.lang.String);
}
```

## class Gamepad.RumbleEffect

```java
public class com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect {
  public int user;
  public final java.util.ArrayList<com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect.Step> steps;
  public java.lang.String serialize();
  public static com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect deserialize(java.lang.String);
}
```

## class Gamepad.RumbleEffect.Builder

```java
public class com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect.Builder {
  public com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect.Builder();
  public com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect.Builder addStep(double, double, int);
  public com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect build();
}
```

## class Gamepad.RumbleEffect.Step

```java
public class com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect.Step {
  public int large;
  public int small;
  public int duration;
  public com.qualcomm.robotcore.hardware.Gamepad.RumbleEffect.Step();
}
```

## class Gamepad.Type

```java
public final class com.qualcomm.robotcore.hardware.Gamepad.Type extends java.lang.Enum<com.qualcomm.robotcore.hardware.Gamepad.Type> {
  public static final com.qualcomm.robotcore.hardware.Gamepad.Type UNKNOWN;
  public static final com.qualcomm.robotcore.hardware.Gamepad.Type LOGITECH_F310;
  public static final com.qualcomm.robotcore.hardware.Gamepad.Type XBOX_360;
  public static final com.qualcomm.robotcore.hardware.Gamepad.Type SONY_PS4;
  public static final com.qualcomm.robotcore.hardware.Gamepad.Type SONY_PS4_SUPPORTED_BY_KERNEL;
  public static com.qualcomm.robotcore.hardware.Gamepad.Type[] values();
  public static com.qualcomm.robotcore.hardware.Gamepad.Type valueOf(java.lang.String);
}
```

## class GamepadStateChanges

```java
class com.qualcomm.robotcore.hardware.GamepadStateChanges {
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor dpadUp;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor dpadDown;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor dpadLeft;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor dpadRight;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor a;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor b;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor x;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor y;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor guide;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor start;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor back;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor leftBumper;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor rightBumper;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor leftStickButton;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor rightStickButton;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor circle;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor cross;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor triangle;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor square;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor share;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor options;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor touchpad;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor ps;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor leftTrigger;
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor rightTrigger;
  protected void updateAllButtons(com.qualcomm.robotcore.hardware.Gamepad);
}
```

## class GamepadStateChanges.ButtonStateMonitor

```java
public class com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor {
  protected com.qualcomm.robotcore.hardware.GamepadStateChanges.ButtonStateMonitor(com.qualcomm.robotcore.hardware.GamepadStateChanges);
  protected boolean wasPressed();
  protected boolean wasReleased();
}
```

## interface GyroSensor

```java
public interface com.qualcomm.robotcore.hardware.GyroSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void calibrate();
  public abstract boolean isCalibrating();
  public abstract int getHeading();
  public abstract double getRotationFraction();
  public abstract int rawX();
  public abstract int rawY();
  public abstract int rawZ();
  public abstract void resetZAxisIntegrator();
  public abstract java.lang.String status();
}
```

## interface Gyroscope

```java
public interface com.qualcomm.robotcore.hardware.Gyroscope {
  public abstract java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularVelocityAxes();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
}
```

## interface HardwareDevice

```java
public interface com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public abstract java.lang.String getDeviceName();
  public abstract java.lang.String getConnectionInfo();
  public abstract int getVersion();
  public abstract void resetDeviceConfigurationForOpMode();
  public abstract void close();
}
```

## class HardwareDevice.Manufacturer

```java
public final class com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer extends java.lang.Enum<com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer> {
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer Unknown;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer Other;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer Lego;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer HiTechnic;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer ModernRobotics;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer Adafruit;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer Matrix;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer Lynx;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer AMS;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer STMicroelectronics;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer Broadcom;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer DFRobot;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer DigitalChickenLabs;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer SparkFun;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer MaxBotix;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer LimelightVision;
  public static final com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer GoBilda;
  public static com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer[] values();
  public static com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer valueOf(java.lang.String);
}
```

## interface HardwareDeviceCloseOnTearDown

```java
public interface com.qualcomm.robotcore.hardware.HardwareDeviceCloseOnTearDown {
  public abstract void close();
}
```

## interface HardwareDeviceHealth

```java
public interface com.qualcomm.robotcore.hardware.HardwareDeviceHealth {
  public abstract void setHealthStatus(com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus);
  public abstract com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus getHealthStatus();
}
```

## class HardwareDeviceHealth.HealthStatus

```java
public final class com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus extends java.lang.Enum<com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus> {
  public static final com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus UNKNOWN;
  public static final com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus HEALTHY;
  public static final com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus UNHEALTHY;
  public static final com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus CLOSED;
  public static com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus[] values();
  public static com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus valueOf(java.lang.String);
}
```

## class HardwareDeviceHealthImpl

```java
public class com.qualcomm.robotcore.hardware.HardwareDeviceHealthImpl implements com.qualcomm.robotcore.hardware.HardwareDeviceHealth {
  protected java.lang.String tag;
  protected com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus healthStatus;
  protected java.util.concurrent.Callable<com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus> override;
  public com.qualcomm.robotcore.hardware.HardwareDeviceHealthImpl(java.lang.String);
  public com.qualcomm.robotcore.hardware.HardwareDeviceHealthImpl(java.lang.String, java.util.concurrent.Callable<com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus>);
  public void close();
  public void setHealthStatus(com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus);
  public com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus getHealthStatus();
}
```

## class HardwareMap

```java
public class com.qualcomm.robotcore.hardware.HardwareMap implements java.lang.Iterable<com.qualcomm.robotcore.hardware.HardwareDevice> {
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.DcMotorController> dcMotorController;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.DcMotor> dcMotor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.ServoController> servoController;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.Servo> servo;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.CRServo> crservo;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.TouchSensorMultiplexer> touchSensorMultiplexer;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.AnalogInput> analogInput;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.DigitalChannel> digitalChannel;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.OpticalDistanceSensor> opticalDistanceSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.TouchSensor> touchSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.PWMOutput> pwmOutput;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.I2cDevice> i2cDevice;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.I2cDeviceSynch> i2cDeviceSynch;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.ColorSensor> colorSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.LED> led;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.AccelerationSensor> accelerationSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.CompassSensor> compassSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.GyroSensor> gyroSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.IrSeekerSensor> irSeekerSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.LightSensor> lightSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.UltrasonicSensor> ultrasonicSensor;
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<com.qualcomm.robotcore.hardware.VoltageSensor> voltageSensor;
  protected java.util.Map<java.lang.String, java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice>> allDevicesMap;
  protected java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> allDevicesList;
  protected java.util.Map<com.qualcomm.robotcore.hardware.HardwareDevice, java.util.Set<java.lang.String>> deviceNames;
  protected java.util.Map<com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.HardwareDevice> serialNumberMap;
  protected java.util.Map<java.lang.String, java.util.List<com.qualcomm.robotcore.hardware.HardwareMap.DeviceInstancesFromSingleConfigEntry>> devicesWithMultipleDriversMap;
  public final java.util.List<com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<? extends com.qualcomm.robotcore.hardware.HardwareDevice>> allDeviceMappings;
  public final android.content.Context appContext;
  protected final java.lang.Object lock;
  public com.qualcomm.robotcore.hardware.HardwareMap(android.content.Context, com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier);
  public <T> T get(java.lang.Class<? extends T>, java.lang.String);
  public <T> T tryGet(java.lang.Class<? extends T>, java.lang.String);
  public <T> T get(java.lang.Class<? extends T>, com.qualcomm.robotcore.util.SerialNumber);
  public com.qualcomm.robotcore.hardware.HardwareDevice get(java.lang.String);
  public <T> java.util.List<T> getAll(java.lang.Class<? extends T>);
  public java.util.SortedSet<java.lang.String> getAllNames(java.lang.Class<? extends com.qualcomm.robotcore.hardware.HardwareDevice>);
  public void put(java.lang.String, com.qualcomm.robotcore.hardware.HardwareDevice);
  public void put(java.lang.String, java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice>);
  public void put(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, com.qualcomm.robotcore.hardware.HardwareDevice);
  protected void internalPut(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, com.qualcomm.robotcore.hardware.HardwareDevice);
  public boolean remove(java.lang.String, com.qualcomm.robotcore.hardware.HardwareDevice);
  public boolean remove(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, com.qualcomm.robotcore.hardware.HardwareDevice);
  public java.util.Set<java.lang.String> getNamesOf(com.qualcomm.robotcore.hardware.HardwareDevice);
  protected void recordDeviceName(java.lang.String, com.qualcomm.robotcore.hardware.HardwareDevice);
  protected void rebuildDeviceNamesIfNecessary();
  public int size();
  public java.util.Iterator<com.qualcomm.robotcore.hardware.HardwareDevice> iterator();
  public java.lang.Iterable<com.qualcomm.robotcore.hardware.HardwareDevice> unsafeIterable();
  public void logDevices();
}
```

## class HardwareMap.DeviceInstanceHolder

```java
public class com.qualcomm.robotcore.hardware.HardwareMap.DeviceInstanceHolder {
  protected com.qualcomm.robotcore.hardware.HardwareMap.DeviceInstanceHolder(com.qualcomm.robotcore.hardware.HardwareDevice);
}
```

## class HardwareMap.DeviceInstancesFromSingleConfigEntry

```java
public class com.qualcomm.robotcore.hardware.HardwareMap.DeviceInstancesFromSingleConfigEntry {
  protected com.qualcomm.robotcore.hardware.HardwareMap.DeviceInstancesFromSingleConfigEntry(java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice>);
  public boolean warnIfOtherDriverHasBeenRetrieved(com.qualcomm.robotcore.hardware.HardwareDevice, java.lang.String);
}
```

## class HardwareMap.DeviceMapping

```java
public class com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping<DEVICE_TYPE extends com.qualcomm.robotcore.hardware.HardwareDevice> implements java.lang.Iterable<DEVICE_TYPE> {
  public com.qualcomm.robotcore.hardware.HardwareMap.DeviceMapping(java.lang.Class<DEVICE_TYPE>);
  public java.lang.Class<DEVICE_TYPE> getDeviceTypeClass();
  public DEVICE_TYPE cast(java.lang.Object);
  public DEVICE_TYPE get(java.lang.String);
  public void put(java.lang.String, DEVICE_TYPE);
  public void put(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, DEVICE_TYPE);
  protected void internalPut(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, DEVICE_TYPE);
  public void putLocal(java.lang.String, DEVICE_TYPE);
  public boolean contains(java.lang.String);
  public boolean remove(java.lang.String);
  public boolean remove(com.qualcomm.robotcore.util.SerialNumber, java.lang.String);
  public java.util.Iterator<DEVICE_TYPE> iterator();
  public java.util.Set<java.util.Map.Entry<java.lang.String, DEVICE_TYPE>> entrySet();
  public int size();
}
```

## class I2cAddr

```java
public final class com.qualcomm.robotcore.hardware.I2cAddr {
  public com.qualcomm.robotcore.hardware.I2cAddr(int);
  public static com.qualcomm.robotcore.hardware.I2cAddr zero();
  public static com.qualcomm.robotcore.hardware.I2cAddr create7bit(int);
  public static com.qualcomm.robotcore.hardware.I2cAddr create8bit(int);
  public int get8Bit();
  public int get7Bit();
}
```

## interface I2cAddrConfig

```java
public interface com.qualcomm.robotcore.hardware.I2cAddrConfig extends com.qualcomm.robotcore.hardware.I2cAddressableDevice {
  public abstract void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
}
```

## interface I2cAddressableDevice

```java
public interface com.qualcomm.robotcore.hardware.I2cAddressableDevice {
  public abstract com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
}
```

## interface I2cDevice

```java
public interface com.qualcomm.robotcore.hardware.I2cDevice extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void enableI2cReadMode(com.qualcomm.robotcore.hardware.I2cAddr, int, int);
  public abstract void enableI2cWriteMode(com.qualcomm.robotcore.hardware.I2cAddr, int, int);
  public abstract boolean isI2cPortInReadMode();
  public abstract boolean isI2cPortInWriteMode();
  public abstract void readI2cCacheFromController();
  public abstract void writeI2cCacheToController();
  public abstract void writeI2cPortFlagOnlyToController();
  public abstract void setI2cPortActionFlag();
  public abstract boolean isI2cPortActionFlagSet();
  public abstract void clearI2cPortActionFlag();
  public abstract byte[] getI2cReadCache();
  public abstract org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow getI2cReadCacheTimeWindow();
  public abstract java.util.concurrent.locks.Lock getI2cReadCacheLock();
  public abstract byte[] getI2cWriteCache();
  public abstract java.util.concurrent.locks.Lock getI2cWriteCacheLock();
  public abstract byte[] getCopyOfReadBuffer();
  public abstract byte[] getCopyOfWriteBuffer();
  public abstract void copyBufferIntoWriteBuffer(byte[]);
  public abstract int getMaxI2cWriteLatency();
  public abstract boolean isArmed();
  public abstract void readI2cCacheFromModule();
  public abstract void writeI2cCacheToModule();
  public abstract void writeI2cPortFlagOnlyToModule();
}
```

## interface I2cDeviceSynch

```java
public interface com.qualcomm.robotcore.hardware.I2cDeviceSynch extends com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple,com.qualcomm.robotcore.hardware.Engagable {
  public abstract void setReadWindow(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public abstract com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow getReadWindow();
  public abstract void ensureReadWindow(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public abstract com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int, int, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public abstract void setHeartbeatInterval(int);
  public abstract int getHeartbeatInterval();
  public abstract void setHeartbeatAction(com.qualcomm.robotcore.hardware.I2cDeviceSynch.HeartbeatAction);
  public abstract com.qualcomm.robotcore.hardware.I2cDeviceSynch.HeartbeatAction getHeartbeatAction();
}
```

## class I2cDeviceSynch.HeartbeatAction

```java
public class com.qualcomm.robotcore.hardware.I2cDeviceSynch.HeartbeatAction {
  public final boolean rereadLastRead;
  public final boolean rewriteLastWritten;
  public final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow heartbeatReadWindow;
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.HeartbeatAction(boolean, boolean, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
}
```

## class I2cDeviceSynch.ReadMode

```java
public final class com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode extends java.lang.Enum<com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode> {
  public static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode REPEAT;
  public static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode BALANCED;
  public static final com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode ONLY_ONCE;
  public static com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode[] values();
  public static com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode valueOf(java.lang.String);
}
```

## class I2cDeviceSynch.ReadWindow

```java
public class com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow {
  public static final int READ_REGISTER_COUNT_MAX = 26;
  public static final int WRITE_REGISTER_COUNT_MAX = 26;
  public int getRegisterFirst();
  public int getRegisterMax();
  public int getRegisterCount();
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode getReadMode();
  public boolean hasWindowBeenUsedForRead();
  public void noteWindowUsedForRead();
  public boolean canBeUsedToRead();
  public boolean mayInitiateSwitchToReadMode();
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow(int, int, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadMode);
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow readableCopy();
  public boolean sameAsIncludingMode(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public boolean contains(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public boolean containsWithSameMode(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public boolean contains(int, int);
}
```

## class I2cDeviceSynchDevice

```java
public abstract class com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<DEVICE_CLIENT extends com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple> implements com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback, com.qualcomm.robotcore.hardware.HardwareDevice {
  protected DEVICE_CLIENT deviceClient;
  protected boolean deviceClientIsOwned;
  protected boolean isInitialized;
  protected com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice(DEVICE_CLIENT, boolean);
  protected void registerArmingStateCallback(boolean);
  protected void engage();
  protected void disengage();
  public DEVICE_CLIENT getDeviceClient();
  public void onModuleStateChange(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier, com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.ARMINGSTATE);
  protected synchronized void initializeIfNecessary();
  public synchronized boolean initialize();
  protected abstract boolean doInitialize();
  public void resetDeviceConfigurationForOpMode();
  public void close();
  public int getVersion();
  public java.lang.String getConnectionInfo();
}
```

## class I2cDeviceSynchDeviceWithParameters

```java
public abstract class com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters<DEVICE_CLIENT extends com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, PARAMETERS> extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<DEVICE_CLIENT> {
  protected volatile PARAMETERS parameters;
  protected final PARAMETERS defaultParameters;
  protected com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters(DEVICE_CLIENT, boolean, PARAMETERS);
  public PARAMETERS getParameters();
  protected synchronized boolean doInitialize();
  public void resetDeviceConfigurationForOpMode();
  public boolean initialize(PARAMETERS);
  protected abstract boolean internalInitialize(PARAMETERS);
}
```

## class I2cDeviceSynchImplOnSimple

```java
public class com.qualcomm.robotcore.hardware.I2cDeviceSynchImplOnSimple extends com.qualcomm.robotcore.hardware.I2cDeviceSynchReadHistoryImpl implements com.qualcomm.robotcore.hardware.I2cDeviceSynch {
  protected com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple i2cDeviceSynchSimple;
  protected com.qualcomm.robotcore.hardware.I2cDeviceSynchReadHistory i2cDeviceSynchSimpleHistory;
  protected boolean isSimpleOwned;
  protected int iregReadLast;
  protected int cregReadLast;
  protected int iregWriteLast;
  protected byte[] rgbWriteLast;
  protected boolean isHooked;
  protected boolean isEngaged;
  protected boolean isClosing;
  protected int msHeartbeatInterval;
  protected com.qualcomm.robotcore.hardware.I2cDeviceSynch.HeartbeatAction heartbeatAction;
  protected java.util.concurrent.ScheduledExecutorService heartbeatExecutor;
  protected final java.lang.Object engagementLock;
  protected final java.lang.Object concurrentClientLock;
  public com.qualcomm.robotcore.hardware.I2cDeviceSynchImplOnSimple(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public void setUserConfiguredName(java.lang.String);
  public java.lang.String getUserConfiguredName();
  public void setLogging(boolean);
  public boolean getLogging();
  public void setLoggingTag(java.lang.String);
  public java.lang.String getLoggingTag();
  public void engage();
  protected void hook();
  protected void adjustHooking();
  public boolean isEngaged();
  public boolean isArmed();
  public void disengage();
  protected void unhook();
  public void setHeartbeatInterval(int);
  public int getHeartbeatInterval();
  public void setHeartbeatAction(com.qualcomm.robotcore.hardware.I2cDeviceSynch.HeartbeatAction);
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.HeartbeatAction getHeartbeatAction();
  public void setReadWindow(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow getReadWindow();
  public void ensureReadWindow(com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int, int, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow, com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
  public void setHealthStatus(com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus);
  public com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus getHealthStatus();
  public java.util.concurrent.BlockingQueue<com.qualcomm.robotcore.hardware.TimestampedI2cData> getHistoryQueue();
  public void setHistoryQueueCapacity(int);
  public int getHistoryQueueCapacity();
  public void addToHistoryQueue(com.qualcomm.robotcore.hardware.TimestampedI2cData);
  protected boolean isOpenForReading();
  protected boolean isOpenForWriting();
  protected boolean newReadsAndWritesAllowed();
  public com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple getSimple();
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public void setI2cAddr(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddr();
  public byte read8();
  public synchronized byte read8(int);
  public byte[] read(int);
  public byte[] read(int, int);
  public com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int);
  public com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int, int);
  public void write8(int);
  public void write8(int, int);
  public void write8(int, int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public void write8(int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public void write(int, byte[]);
  public void write(byte[]);
  public void write(int, byte[], com.qualcomm.robotcore.hardware.I2cWaitControl);
  public void write(byte[], com.qualcomm.robotcore.hardware.I2cWaitControl);
  public void waitForWriteCompletions(com.qualcomm.robotcore.hardware.I2cWaitControl);
  public void enableWriteCoalescing(boolean);
  public boolean isWriteCoalescingEnabled();
}
```

## interface I2cDeviceSynchReadHistory

```java
public interface com.qualcomm.robotcore.hardware.I2cDeviceSynchReadHistory {
  public abstract void setHistoryQueueCapacity(int);
  public abstract int getHistoryQueueCapacity();
  public abstract java.util.concurrent.BlockingQueue<com.qualcomm.robotcore.hardware.TimestampedI2cData> getHistoryQueue();
}
```

## class I2cDeviceSynchReadHistoryImpl

```java
public class com.qualcomm.robotcore.hardware.I2cDeviceSynchReadHistoryImpl implements com.qualcomm.robotcore.hardware.I2cDeviceSynchReadHistory {
  protected final java.lang.Object historyQueueLock;
  protected java.util.concurrent.BlockingQueue<com.qualcomm.robotcore.hardware.TimestampedI2cData> historyQueue;
  protected int historyQueueCapacity;
  public com.qualcomm.robotcore.hardware.I2cDeviceSynchReadHistoryImpl();
  public java.util.concurrent.BlockingQueue<com.qualcomm.robotcore.hardware.TimestampedI2cData> getHistoryQueue();
  public void setHistoryQueueCapacity(int);
  public int getHistoryQueueCapacity();
  public void addToHistoryQueue(com.qualcomm.robotcore.hardware.TimestampedI2cData);
}
```

## interface I2cDeviceSynchSimple

```java
public interface com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple extends com.qualcomm.robotcore.hardware.HardwareDevice,com.qualcomm.robotcore.hardware.HardwareDeviceHealth,com.qualcomm.robotcore.hardware.I2cAddrConfig,com.qualcomm.robotcore.hardware.RobotConfigNameable {
  public abstract byte read8();
  public abstract byte read8(int);
  public abstract byte[] read(int);
  public abstract byte[] read(int, int);
  public abstract com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int);
  public abstract com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int, int);
  public abstract void write8(int);
  public abstract void write8(int, int);
  public abstract void write(byte[]);
  public abstract void write(int, byte[]);
  public abstract void write8(int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public abstract void write8(int, int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public abstract void write(byte[], com.qualcomm.robotcore.hardware.I2cWaitControl);
  public abstract void write(int, byte[], com.qualcomm.robotcore.hardware.I2cWaitControl);
  public abstract void waitForWriteCompletions(com.qualcomm.robotcore.hardware.I2cWaitControl);
  public abstract void enableWriteCoalescing(boolean);
  public abstract boolean isWriteCoalescingEnabled();
  public abstract boolean isArmed();
  public abstract void setI2cAddr(com.qualcomm.robotcore.hardware.I2cAddr);
  public abstract com.qualcomm.robotcore.hardware.I2cAddr getI2cAddr();
  public abstract void setLogging(boolean);
  public abstract boolean getLogging();
  public abstract void setLoggingTag(java.lang.String);
  public abstract java.lang.String getLoggingTag();
}
```

## class I2cWaitControl

```java
public final class com.qualcomm.robotcore.hardware.I2cWaitControl extends java.lang.Enum<com.qualcomm.robotcore.hardware.I2cWaitControl> {
  public static final com.qualcomm.robotcore.hardware.I2cWaitControl NONE;
  public static final com.qualcomm.robotcore.hardware.I2cWaitControl ATOMIC;
  public static final com.qualcomm.robotcore.hardware.I2cWaitControl WRITTEN;
  public static com.qualcomm.robotcore.hardware.I2cWaitControl[] values();
  public static com.qualcomm.robotcore.hardware.I2cWaitControl valueOf(java.lang.String);
}
```

## class I2cWarningManager

```java
public class com.qualcomm.robotcore.hardware.I2cWarningManager implements com.qualcomm.robotcore.util.GlobalWarningSource {
  public com.qualcomm.robotcore.hardware.I2cWarningManager();
  public static void notifyProblemI2cDevice(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple);
  public static void removeProblemI2cDevice(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple);
  public static void suppressNewProblemDeviceWarningsWhile(java.lang.Runnable);
  public static void suppressNewProblemDeviceWarnings(boolean);
  public static void clearI2cWarnings();
  public java.lang.String getGlobalWarning();
  public boolean shouldTriggerWarningSound();
  public void suppressGlobalWarning(boolean);
  public void setGlobalWarning(java.lang.String);
  public void clearGlobalWarning();
}
```

## interface IMU

```java
public interface com.qualcomm.robotcore.hardware.IMU extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract boolean initialize(com.qualcomm.robotcore.hardware.IMU.Parameters);
  public abstract void resetYaw();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles getRobotYawPitchRollAngles();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Orientation getRobotOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Quaternion getRobotOrientationAsQuaternion();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getRobotAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
}
```

## class IMU.Parameters

```java
public class com.qualcomm.robotcore.hardware.IMU.Parameters {
  public com.qualcomm.robotcore.hardware.ImuOrientationOnRobot imuOrientationOnRobot;
  public com.qualcomm.robotcore.hardware.IMU.Parameters(com.qualcomm.robotcore.hardware.ImuOrientationOnRobot);
  public com.qualcomm.robotcore.hardware.IMU.Parameters copy();
}
```

## interface ImuOrientationOnRobot

```java
public interface com.qualcomm.robotcore.hardware.ImuOrientationOnRobot {
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuCoordinateSystemOrientationFromPerspectiveOfRobot();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuRotationOffset();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Quaternion angularVelocityTransform();
}
```

## interface IntegratingGyroscope

```java
public interface com.qualcomm.robotcore.hardware.IntegratingGyroscope extends com.qualcomm.robotcore.hardware.Gyroscope,com.qualcomm.robotcore.hardware.OrientationSensor {
}
```

## interface IrSeekerSensor

```java
public interface com.qualcomm.robotcore.hardware.IrSeekerSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void setSignalDetectedThreshold(double);
  public abstract double getSignalDetectedThreshold();
  public abstract void setMode(com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode);
  public abstract com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode getMode();
  public abstract boolean signalDetected();
  public abstract double getAngle();
  public abstract double getStrength();
  public abstract com.qualcomm.robotcore.hardware.IrSeekerSensor.IrSeekerIndividualSensor[] getIndividualSensors();
  public abstract void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public abstract com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
}
```

## class IrSeekerSensor.IrSeekerIndividualSensor

```java
public class com.qualcomm.robotcore.hardware.IrSeekerSensor.IrSeekerIndividualSensor {
  public com.qualcomm.robotcore.hardware.IrSeekerSensor.IrSeekerIndividualSensor();
  public com.qualcomm.robotcore.hardware.IrSeekerSensor.IrSeekerIndividualSensor(double, double);
  public double getSensorAngle();
  public double getSensorStrength();
  public java.lang.String toString();
}
```

## class IrSeekerSensor.Mode

```java
public final class com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode extends java.lang.Enum<com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode> {
  public static final com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode MODE_600HZ;
  public static final com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode MODE_1200HZ;
  public static com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode[] values();
  public static com.qualcomm.robotcore.hardware.IrSeekerSensor.Mode valueOf(java.lang.String);
}
```

## class LED

```java
public class com.qualcomm.robotcore.hardware.LED implements com.qualcomm.robotcore.hardware.HardwareDevice,com.qualcomm.robotcore.hardware.SwitchableLight {
  public com.qualcomm.robotcore.hardware.LED(com.qualcomm.robotcore.hardware.DigitalChannelController, int);
  public void enable(boolean);
  public boolean isLightOn();
  public void enableLight(boolean);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
  public void on();
  public void off();
}
```

## interface Light

```java
public interface com.qualcomm.robotcore.hardware.Light {
  public abstract boolean isLightOn();
}
```

## class LightBlinker

```java
public class com.qualcomm.robotcore.hardware.LightBlinker implements com.qualcomm.robotcore.hardware.Blinker {
  public static final java.lang.String TAG = "LightBlinker";
  protected final com.qualcomm.robotcore.hardware.SwitchableLight light;
  protected java.util.ArrayList<com.qualcomm.robotcore.hardware.Blinker.Step> currentSteps;
  protected java.util.Deque<java.util.ArrayList<com.qualcomm.robotcore.hardware.Blinker.Step>> previousSteps;
  protected java.util.concurrent.ScheduledFuture<?> future;
  protected int nextStep;
  public com.qualcomm.robotcore.hardware.LightBlinker(com.qualcomm.robotcore.hardware.SwitchableLight);
  public void setConstant(int);
  public void stopBlinking();
  public int getBlinkerPatternMaxLength();
  public synchronized void pushPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  public synchronized boolean patternStackNotEmpty();
  public synchronized boolean popPattern();
  public synchronized void setPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  protected boolean isCurrentPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  public synchronized java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step> getPattern();
  protected synchronized void scheduleNext();
  protected synchronized void stop();
}
```

## class LightMultiplexor

```java
public class com.qualcomm.robotcore.hardware.LightMultiplexor implements com.qualcomm.robotcore.hardware.SwitchableLight {
  protected static final java.util.Set<com.qualcomm.robotcore.hardware.LightMultiplexor> extantMultiplexors;
  protected final com.qualcomm.robotcore.hardware.SwitchableLight target;
  protected int enableCount;
  public static synchronized com.qualcomm.robotcore.hardware.LightMultiplexor forLight(com.qualcomm.robotcore.hardware.SwitchableLight);
  protected com.qualcomm.robotcore.hardware.LightMultiplexor(com.qualcomm.robotcore.hardware.SwitchableLight);
  public boolean isLightOn();
  public synchronized void enableLight(boolean);
}
```

## interface LightSensor

```java
public interface com.qualcomm.robotcore.hardware.LightSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract double getLightDetected();
  public abstract double getRawLightDetected();
  public abstract double getRawLightDetectedMax();
  public abstract void enableLed(boolean);
  public abstract java.lang.String status();
}
```

## class LynxModuleDescription

```java
public class com.qualcomm.robotcore.hardware.LynxModuleDescription {
  public final int address;
  public final boolean isParent;
  public final boolean isUserModule;
  public final boolean isSystemSynthetic;
}
```

## class LynxModuleDescription.Builder

```java
public class com.qualcomm.robotcore.hardware.LynxModuleDescription.Builder {
  public com.qualcomm.robotcore.hardware.LynxModuleDescription.Builder(int, boolean);
  public com.qualcomm.robotcore.hardware.LynxModuleDescription.Builder setUserModule();
  public com.qualcomm.robotcore.hardware.LynxModuleDescription.Builder setSystemSynthetic();
  public com.qualcomm.robotcore.hardware.LynxModuleDescription build();
}
```

## class LynxModuleImuType

```java
public final class com.qualcomm.robotcore.hardware.LynxModuleImuType extends java.lang.Enum<com.qualcomm.robotcore.hardware.LynxModuleImuType> {
  public static final com.qualcomm.robotcore.hardware.LynxModuleImuType UNKNOWN;
  public static final com.qualcomm.robotcore.hardware.LynxModuleImuType NONE;
  public static final com.qualcomm.robotcore.hardware.LynxModuleImuType BNO055;
  public static final com.qualcomm.robotcore.hardware.LynxModuleImuType BHI260;
  public static com.qualcomm.robotcore.hardware.LynxModuleImuType[] values();
  public static com.qualcomm.robotcore.hardware.LynxModuleImuType valueOf(java.lang.String);
  public java.lang.String toString();
}
```

## class LynxModuleMeta

```java
public class com.qualcomm.robotcore.hardware.LynxModuleMeta {
  protected final int moduleAddress;
  protected final boolean isParent;
  protected com.qualcomm.robotcore.hardware.LynxModuleImuType imuType;
  protected java.lang.Integer revProductNumber;
  public com.qualcomm.robotcore.hardware.LynxModuleMeta(int, boolean);
  public com.qualcomm.robotcore.hardware.LynxModuleMeta(com.qualcomm.robotcore.hardware.LynxModuleMeta);
  public int getModuleAddress();
  public boolean isParent();
  public synchronized com.qualcomm.robotcore.hardware.LynxModuleImuType imuType();
  public synchronized void setImuType(com.qualcomm.robotcore.hardware.LynxModuleImuType);
  public synchronized int revProductNumber();
  public synchronized void setRevProductNumber(int);
  public synchronized java.lang.String toString();
}
```

## class LynxModuleMetaList

```java
public class com.qualcomm.robotcore.hardware.LynxModuleMetaList implements java.lang.Iterable<com.qualcomm.robotcore.hardware.LynxModuleMeta> {
  public com.qualcomm.robotcore.util.SerialNumber serialNumber;
  public com.qualcomm.robotcore.hardware.LynxModuleMeta[] modules;
  public com.qualcomm.robotcore.hardware.LynxModuleMetaList(com.qualcomm.robotcore.util.SerialNumber);
  public com.qualcomm.robotcore.hardware.LynxModuleMetaList(com.qualcomm.robotcore.util.SerialNumber, java.util.Collection<com.qualcomm.robotcore.hardware.LynxModuleMeta>);
  public java.util.Iterator<com.qualcomm.robotcore.hardware.LynxModuleMeta> iterator();
  public com.qualcomm.robotcore.hardware.LynxModuleMeta getParent();
  protected com.qualcomm.robotcore.hardware.LynxModuleMetaList flatten();
  public java.lang.String toSerializationString();
  public static com.qualcomm.robotcore.hardware.LynxModuleMetaList fromSerializationString(java.lang.String);
  public java.lang.String toString();
}
```

## class MotorControlAlgorithm

```java
public final class com.qualcomm.robotcore.hardware.MotorControlAlgorithm extends java.lang.Enum<com.qualcomm.robotcore.hardware.MotorControlAlgorithm> {
  public static final com.qualcomm.robotcore.hardware.MotorControlAlgorithm Unknown;
  public static final com.qualcomm.robotcore.hardware.MotorControlAlgorithm LegacyPID;
  public static final com.qualcomm.robotcore.hardware.MotorControlAlgorithm PIDF;
  public static com.qualcomm.robotcore.hardware.MotorControlAlgorithm[] values();
  public static com.qualcomm.robotcore.hardware.MotorControlAlgorithm valueOf(java.lang.String);
}
```

## interface NormalizedColorSensor

```java
public interface com.qualcomm.robotcore.hardware.NormalizedColorSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract com.qualcomm.robotcore.hardware.NormalizedRGBA getNormalizedColors();
  public abstract float getGain();
  public abstract void setGain(float);
}
```

## class NormalizedRGBA

```java
public class com.qualcomm.robotcore.hardware.NormalizedRGBA {
  public float red;
  public float green;
  public float blue;
  public float alpha;
  public com.qualcomm.robotcore.hardware.NormalizedRGBA();
  public int toColor();
}
```

## interface OpticalDistanceSensor

```java
public interface com.qualcomm.robotcore.hardware.OpticalDistanceSensor extends com.qualcomm.robotcore.hardware.LightSensor {
}
```

## interface OrientationSensor

```java
public interface com.qualcomm.robotcore.hardware.OrientationSensor {
  public abstract java.util.Set<org.firstinspires.ftc.robotcore.external.navigation.Axis> getAngularOrientationAxes();
  public abstract org.firstinspires.ftc.robotcore.external.navigation.Orientation getAngularOrientation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
}
```

## class PIDCoefficients

```java
public class com.qualcomm.robotcore.hardware.PIDCoefficients {
  public double p;
  public double i;
  public double d;
  public java.lang.String toString();
  public com.qualcomm.robotcore.hardware.PIDCoefficients();
  public com.qualcomm.robotcore.hardware.PIDCoefficients(double, double, double);
}
```

## class PIDFCoefficients

```java
public class com.qualcomm.robotcore.hardware.PIDFCoefficients {
  public double p;
  public double i;
  public double d;
  public double f;
  public com.qualcomm.robotcore.hardware.MotorControlAlgorithm algorithm;
  public java.lang.String toString();
  public com.qualcomm.robotcore.hardware.PIDFCoefficients();
  public com.qualcomm.robotcore.hardware.PIDFCoefficients(double, double, double, double, com.qualcomm.robotcore.hardware.MotorControlAlgorithm);
  public com.qualcomm.robotcore.hardware.PIDFCoefficients(double, double, double, double);
  public com.qualcomm.robotcore.hardware.PIDFCoefficients(com.qualcomm.robotcore.hardware.PIDFCoefficients);
  public com.qualcomm.robotcore.hardware.PIDFCoefficients(com.qualcomm.robotcore.hardware.PIDCoefficients);
}
```

## interface PWMOutput

```java
public interface com.qualcomm.robotcore.hardware.PWMOutput extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void setPulseWidthOutputTime(int);
  public abstract int getPulseWidthOutputTime();
  public abstract void setPulseWidthPeriod(int);
  public abstract int getPulseWidthPeriod();
}
```

## interface PWMOutputController

```java
public interface com.qualcomm.robotcore.hardware.PWMOutputController extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public abstract void setPulseWidthOutputTime(int, int);
  public abstract void setPulseWidthPeriod(int, int);
  public abstract int getPulseWidthOutputTime(int);
  public abstract int getPulseWidthPeriod(int);
}
```

## interface PWMOutputControllerEx

```java
public interface com.qualcomm.robotcore.hardware.PWMOutputControllerEx {
  public abstract void setPwmEnable(int);
  public abstract void setPwmDisable(int);
  public abstract boolean isPwmEnabled(int);
}
```

## interface PWMOutputEx

```java
public interface com.qualcomm.robotcore.hardware.PWMOutputEx {
  public abstract void setPwmEnable();
  public abstract void setPwmDisable();
  public abstract boolean isPwmEnabled();
}
```

## class PWMOutputImpl

```java
public class com.qualcomm.robotcore.hardware.PWMOutputImpl implements com.qualcomm.robotcore.hardware.PWMOutput {
  protected com.qualcomm.robotcore.hardware.PWMOutputController controller;
  protected int port;
  public com.qualcomm.robotcore.hardware.PWMOutputImpl(com.qualcomm.robotcore.hardware.PWMOutputController, int);
  public void setPulseWidthOutputTime(int);
  public int getPulseWidthOutputTime();
  public void setPulseWidthPeriod(int);
  public int getPulseWidthPeriod();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```

## class PWMOutputImplEx

```java
public class com.qualcomm.robotcore.hardware.PWMOutputImplEx extends com.qualcomm.robotcore.hardware.PWMOutputImpl implements com.qualcomm.robotcore.hardware.PWMOutputEx {
  public com.qualcomm.robotcore.hardware.PWMOutputImplEx(com.qualcomm.robotcore.hardware.PWMOutputController, int);
  public void setPwmEnable();
  public void setPwmDisable();
  public boolean isPwmEnabled();
}
```

## interface PwmControl

```java
public interface com.qualcomm.robotcore.hardware.PwmControl {
  public abstract void setPwmRange(com.qualcomm.robotcore.hardware.PwmControl.PwmRange);
  public abstract com.qualcomm.robotcore.hardware.PwmControl.PwmRange getPwmRange();
  public abstract void setPwmEnable();
  public abstract void setPwmDisable();
  public abstract boolean isPwmEnabled();
}
```

## class PwmControl.PwmRange

```java
public class com.qualcomm.robotcore.hardware.PwmControl.PwmRange {
  public static final double usFrameDefault = 20000.0d;
  public static final double usPulseUpperDefault = 2400.0d;
  public static final double usPulseLowerDefault = 600.0d;
  public static final com.qualcomm.robotcore.hardware.PwmControl.PwmRange defaultRange;
  public final double usPulseLower;
  public final double usPulseUpper;
  public final double usFrame;
  public com.qualcomm.robotcore.hardware.PwmControl.PwmRange(double, double);
  public com.qualcomm.robotcore.hardware.PwmControl.PwmRange(double, double, double);
  public boolean equals(java.lang.Object);
  public int hashCode();
}
```

## class QuaternionBasedImuHelper

```java
public class com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper {
  public static org.firstinspires.ftc.robotcore.external.navigation.Quaternion quaternionFromZAxisRotation(float, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper(com.qualcomm.robotcore.hardware.ImuOrientationOnRobot);
  public synchronized void resetYaw(java.lang.String, org.firstinspires.ftc.robotcore.external.function.ThrowingSupplier<org.firstinspires.ftc.robotcore.external.navigation.Quaternion, com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException>, int);
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Quaternion getRobotOrientationAsQuaternionOrThrow(org.firstinspires.ftc.robotcore.external.function.ThrowingSupplier<org.firstinspires.ftc.robotcore.external.navigation.Quaternion, com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException>, boolean) throws com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException;
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Quaternion getRobotOrientationAsQuaternion(java.lang.String, org.firstinspires.ftc.robotcore.external.function.ThrowingSupplier<org.firstinspires.ftc.robotcore.external.navigation.Quaternion, com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException>, boolean);
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.YawPitchRollAngles getRobotYawPitchRollAngles(java.lang.String, org.firstinspires.ftc.robotcore.external.function.ThrowingSupplier<org.firstinspires.ftc.robotcore.external.navigation.Quaternion, com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException>);
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.Orientation getRobotOrientation(java.lang.String, org.firstinspires.ftc.robotcore.external.function.ThrowingSupplier<org.firstinspires.ftc.robotcore.external.navigation.Quaternion, com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException>, org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public synchronized org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getRobotAngularVelocity(org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public synchronized void setImuOrientationOnRobot(com.qualcomm.robotcore.hardware.ImuOrientationOnRobot);
}
```

## class QuaternionBasedImuHelper.FailedToRetrieveQuaternionException

```java
public class com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException extends java.lang.Exception {
  public com.qualcomm.robotcore.hardware.QuaternionBasedImuHelper.FailedToRetrieveQuaternionException();
}
```

## interface RobotConfigNameable

```java
public interface com.qualcomm.robotcore.hardware.RobotConfigNameable extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void setUserConfiguredName(java.lang.String);
  public abstract java.lang.String getUserConfiguredName();
}
```

## interface RobotCoreLynxController

```java
public interface com.qualcomm.robotcore.hardware.RobotCoreLynxController extends com.qualcomm.robotcore.hardware.HardwareDevice {
}
```

## interface RobotCoreLynxModule

```java
public interface com.qualcomm.robotcore.hardware.RobotCoreLynxModule extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract int getModuleAddress();
  public abstract com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public abstract java.lang.String getFirmwareVersionString();
  public abstract java.lang.String getNullableFirmwareVersionString();
  public abstract boolean isParent();
  public abstract void attemptFailSafeAndIgnoreErrors();
}
```

## interface RobotCoreLynxUsbDevice

```java
public interface com.qualcomm.robotcore.hardware.RobotCoreLynxUsbDevice {
  public abstract void failSafe();
  public abstract void lockNetworkLockAcquisitions();
  public abstract void setThrowOnNetworkLockAcquisition(boolean);
  public abstract com.qualcomm.robotcore.hardware.LynxModuleMetaList discoverModules(boolean) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public abstract void close();
}
```

## class ScannedDevices

```java
public class com.qualcomm.robotcore.hardware.ScannedDevices {
  public static final java.lang.String TAG = "ScannedDevices";
  protected final java.lang.Object lock;
  protected java.lang.String errorMessage;
  protected java.util.Map<com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType> map;
  public com.qualcomm.robotcore.hardware.ScannedDevices(com.qualcomm.robotcore.hardware.ScannedDevices);
  public com.qualcomm.robotcore.hardware.ScannedDevices();
  public void setErrorMessage(java.lang.String);
  public java.lang.String getErrorMessage();
  public int size();
  public com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType put(com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType);
  public com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType get(com.qualcomm.robotcore.util.SerialNumber);
  public boolean containsKey(com.qualcomm.robotcore.util.SerialNumber);
  public java.util.Set<com.qualcomm.robotcore.util.SerialNumber> keySet();
  public java.util.Set<java.util.Map.Entry<com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType>> entrySet();
  public com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType remove(com.qualcomm.robotcore.util.SerialNumber);
  protected static com.google.gson.Gson newGson();
  public java.lang.String toSerializationString();
  public static com.qualcomm.robotcore.hardware.ScannedDevices fromSerializationString(java.lang.String);
}
```

## class ScannedDevices.MapAdapter

```java
public class com.qualcomm.robotcore.hardware.ScannedDevices.MapAdapter extends com.google.gson.TypeAdapter<java.util.Map<com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType>> {
  protected com.qualcomm.robotcore.hardware.ScannedDevices.MapAdapter();
  public void write(com.google.gson.stream.JsonWriter, java.util.Map<com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType>) throws java.io.IOException;
  public java.util.Map<com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType> read(com.google.gson.stream.JsonReader) throws java.io.IOException;
  public java.lang.Object read(com.google.gson.stream.JsonReader) throws java.io.IOException;
  public void write(com.google.gson.stream.JsonWriter, java.lang.Object) throws java.io.IOException;
}
```

## interface Servo

```java
public interface com.qualcomm.robotcore.hardware.Servo extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public static final double MIN_POSITION = 0.0d;
  public static final double MAX_POSITION = 1.0d;
  public abstract com.qualcomm.robotcore.hardware.ServoController getController();
  public abstract int getPortNumber();
  public abstract void setDirection(com.qualcomm.robotcore.hardware.Servo.Direction);
  public abstract com.qualcomm.robotcore.hardware.Servo.Direction getDirection();
  public abstract void setPosition(double);
  public abstract double getPosition();
  public abstract void scaleRange(double, double);
}
```

## class Servo.Direction

```java
public final class com.qualcomm.robotcore.hardware.Servo.Direction extends java.lang.Enum<com.qualcomm.robotcore.hardware.Servo.Direction> {
  public static final com.qualcomm.robotcore.hardware.Servo.Direction FORWARD;
  public static final com.qualcomm.robotcore.hardware.Servo.Direction REVERSE;
  public static com.qualcomm.robotcore.hardware.Servo.Direction[] values();
  public static com.qualcomm.robotcore.hardware.Servo.Direction valueOf(java.lang.String);
}
```

## interface ServoController

```java
public interface com.qualcomm.robotcore.hardware.ServoController extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract void pwmEnable();
  public abstract void pwmDisable();
  public abstract com.qualcomm.robotcore.hardware.ServoController.PwmStatus getPwmStatus();
  public abstract void setServoPosition(int, double);
  public abstract double getServoPosition(int);
}
```

## class ServoController.PwmStatus

```java
public final class com.qualcomm.robotcore.hardware.ServoController.PwmStatus extends java.lang.Enum<com.qualcomm.robotcore.hardware.ServoController.PwmStatus> {
  public static final com.qualcomm.robotcore.hardware.ServoController.PwmStatus ENABLED;
  public static final com.qualcomm.robotcore.hardware.ServoController.PwmStatus DISABLED;
  public static final com.qualcomm.robotcore.hardware.ServoController.PwmStatus MIXED;
  public static com.qualcomm.robotcore.hardware.ServoController.PwmStatus[] values();
  public static com.qualcomm.robotcore.hardware.ServoController.PwmStatus valueOf(java.lang.String);
}
```

## interface ServoControllerEx

```java
public interface com.qualcomm.robotcore.hardware.ServoControllerEx extends com.qualcomm.robotcore.hardware.ServoController {
  public abstract void setServoPwmRange(int, com.qualcomm.robotcore.hardware.PwmControl.PwmRange);
  public abstract com.qualcomm.robotcore.hardware.PwmControl.PwmRange getServoPwmRange(int);
  public abstract void setServoPwmEnable(int);
  public abstract void setServoPwmDisable(int);
  public abstract boolean isServoPwmEnabled(int);
  public abstract void setServoType(int, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
}
```

## class ServoImpl

```java
public class com.qualcomm.robotcore.hardware.ServoImpl implements com.qualcomm.robotcore.hardware.Servo {
  protected com.qualcomm.robotcore.hardware.ServoController controller;
  protected int portNumber;
  protected com.qualcomm.robotcore.hardware.Servo.Direction direction;
  protected double limitPositionMin;
  protected double limitPositionMax;
  public com.qualcomm.robotcore.hardware.ServoImpl(com.qualcomm.robotcore.hardware.ServoController, int);
  public com.qualcomm.robotcore.hardware.ServoImpl(com.qualcomm.robotcore.hardware.ServoController, int, com.qualcomm.robotcore.hardware.Servo.Direction);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public synchronized void resetDeviceConfigurationForOpMode();
  public void close();
  public com.qualcomm.robotcore.hardware.ServoController getController();
  public synchronized void setDirection(com.qualcomm.robotcore.hardware.Servo.Direction);
  public com.qualcomm.robotcore.hardware.Servo.Direction getDirection();
  public int getPortNumber();
  public synchronized void setPosition(double);
  protected void internalSetPosition(double);
  public synchronized double getPosition();
  public synchronized void scaleRange(double, double);
}
```

## class ServoImplEx

```java
public class com.qualcomm.robotcore.hardware.ServoImplEx extends com.qualcomm.robotcore.hardware.ServoImpl implements com.qualcomm.robotcore.hardware.PwmControl {
  protected com.qualcomm.robotcore.hardware.ServoControllerEx controllerEx;
  public com.qualcomm.robotcore.hardware.ServoImplEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public com.qualcomm.robotcore.hardware.ServoImplEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, com.qualcomm.robotcore.hardware.Servo.Direction, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public void setPwmRange(com.qualcomm.robotcore.hardware.PwmControl.PwmRange);
  public com.qualcomm.robotcore.hardware.PwmControl.PwmRange getPwmRange();
  public void setPwmEnable();
  public void setPwmDisable();
  public boolean isPwmEnabled();
}
```

## interface SwitchableLight

```java
public interface com.qualcomm.robotcore.hardware.SwitchableLight extends com.qualcomm.robotcore.hardware.Light {
  public abstract void enableLight(boolean);
}
```

## class TimestampedData

```java
public class com.qualcomm.robotcore.hardware.TimestampedData {
  public byte[] data;
  public long nanoTime;
  public com.qualcomm.robotcore.hardware.TimestampedData();
}
```

## class TimestampedI2cData

```java
public class com.qualcomm.robotcore.hardware.TimestampedI2cData extends com.qualcomm.robotcore.hardware.TimestampedData {
  public com.qualcomm.robotcore.hardware.I2cAddr i2cAddr;
  public int register;
  public com.qualcomm.robotcore.hardware.TimestampedI2cData();
  public static com.qualcomm.robotcore.hardware.TimestampedI2cData makeFakeData(com.qualcomm.robotcore.hardware.I2cAddr, int, int);
}
```

## interface TouchSensor

```java
public interface com.qualcomm.robotcore.hardware.TouchSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract double getValue();
  public abstract boolean isPressed();
}
```

## interface TouchSensorMultiplexer

```java
public interface com.qualcomm.robotcore.hardware.TouchSensorMultiplexer extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract boolean isTouchSensorPressed(int);
  public abstract int getSwitches();
}
```

## class USBAccessibleLynxModule

```java
public final class com.qualcomm.robotcore.hardware.USBAccessibleLynxModule {
  protected com.qualcomm.robotcore.util.SerialNumber serialNumber;
  protected int moduleAddress;
  protected java.lang.String firmwareVersionString;
  protected java.lang.String formattedFirmwareVersionString;
  public com.qualcomm.robotcore.hardware.USBAccessibleLynxModule(com.qualcomm.robotcore.util.SerialNumber);
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public void setSerialNumber(com.qualcomm.robotcore.util.SerialNumber);
  public int getModuleAddress();
  public void setModuleAddress(int);
  public java.lang.String getFirmwareVersionString();
  public java.lang.String getFinishedFirmwareVersionString();
  public void setFirmwareVersionString(java.lang.String);
}
```

## interface UltrasonicSensor

```java
public interface com.qualcomm.robotcore.hardware.UltrasonicSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract double getUltrasonicLevel();
  public abstract java.lang.String status();
}
```

## interface VisuallyIdentifiableHardwareDevice

```java
public interface com.qualcomm.robotcore.hardware.VisuallyIdentifiableHardwareDevice {
  public abstract void visuallyIdentify(boolean);
}
```

## interface VoltageSensor

```java
public interface com.qualcomm.robotcore.hardware.VoltageSensor extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public abstract double getVoltage();
}
```
