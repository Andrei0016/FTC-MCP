# `com.qualcomm.hardware`

_ftc-sdk 11.1.0 — 3 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class HardwareDeviceManager

```java
public class com.qualcomm.hardware.HardwareDeviceManager implements com.qualcomm.robotcore.hardware.DeviceManager {
  public static final java.lang.String TAG = "HardwareDeviceManager";
  public static final java.lang.String TAG_USB_SCAN = "USBScan";
  public static final java.lang.Object scanDevicesLock;
  public com.qualcomm.hardware.HardwareDeviceManager(android.content.Context, com.qualcomm.robotcore.eventloop.SyncdDevice.Manager);
  public static com.qualcomm.robotcore.hardware.usb.RobotUsbManager createUsbManager();
  public com.qualcomm.robotcore.hardware.ScannedDevices scanForUsbDevices() throws com.qualcomm.robotcore.exception.RobotCoreException;
  protected void scanForEthernetOverUsbDevices(com.qualcomm.robotcore.hardware.ScannedDevices);
  protected void scanForWebcams(com.qualcomm.robotcore.hardware.ScannedDevices);
  public com.qualcomm.robotcore.hardware.RobotCoreLynxUsbDevice createLynxUsbDevice(com.qualcomm.robotcore.util.SerialNumber, java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public com.qualcomm.robotcore.hardware.DcMotor createDcMotor(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType, java.lang.String);
  public com.qualcomm.robotcore.hardware.DcMotor createDcMotorEx(com.qualcomm.robotcore.hardware.DcMotorController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType, java.lang.String);
  public com.qualcomm.robotcore.hardware.Servo createServoEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, java.lang.String, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public com.qualcomm.robotcore.hardware.CRServo createCRServoEx(com.qualcomm.robotcore.hardware.ServoControllerEx, int, java.lang.String, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createCustomServoDeviceInstances(com.qualcomm.robotcore.hardware.ServoControllerEx, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName createWebcamName(com.qualcomm.robotcore.util.SerialNumber, java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public com.qualcomm.robotcore.hardware.TouchSensor createMRDigitalTouchSensor(com.qualcomm.robotcore.hardware.DigitalChannelController, int, java.lang.String);
  public com.qualcomm.robotcore.hardware.IrSeekerSensor createMRI2cIrSeekerSensorV3(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createAnalogSensorInstances(com.qualcomm.robotcore.hardware.AnalogInputController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.AnalogSensorConfigurationType);
  public java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createDigitalDeviceInstances(com.qualcomm.robotcore.hardware.DigitalChannelController, int, com.qualcomm.robotcore.hardware.configuration.typecontainers.DigitalIoDeviceConfigurationType);
  public com.qualcomm.robotcore.hardware.PWMOutput createPwmOutputDevice(com.qualcomm.robotcore.hardware.PWMOutputController, int, java.lang.String);
  public java.util.List<com.qualcomm.robotcore.hardware.HardwareDevice> createI2cDeviceInstances(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, com.qualcomm.robotcore.hardware.configuration.typecontainers.I2cDeviceConfigurationType, java.lang.String);
  public com.qualcomm.robotcore.hardware.HardwareDevice createLimelight3A(com.qualcomm.robotcore.util.SerialNumber, java.lang.String, java.net.InetAddress);
  public com.qualcomm.robotcore.hardware.ColorSensor createAdafruitI2cColorSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public com.qualcomm.robotcore.hardware.ColorSensor createLynxColorRangeSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public com.qualcomm.robotcore.hardware.ColorSensor createModernRoboticsI2cColorSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public com.qualcomm.robotcore.hardware.GyroSensor createModernRoboticsI2cGyroSensor(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  public com.qualcomm.robotcore.hardware.LED createLED(com.qualcomm.robotcore.hardware.DigitalChannelController, int, java.lang.String);
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch createI2cDeviceSynch(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
  protected com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple createI2cDeviceSynchSimple(com.qualcomm.robotcore.hardware.RobotCoreLynxModule, com.qualcomm.robotcore.hardware.configuration.DeviceConfiguration.I2cChannel, java.lang.String);
}
```

## class HardwareFactory

```java
public class com.qualcomm.hardware.HardwareFactory {
  public static final java.lang.String TAG = "HardwareFactory";
  public com.qualcomm.hardware.HardwareFactory(android.content.Context);
  public com.qualcomm.robotcore.hardware.HardwareMap createHardwareMap(com.qualcomm.robotcore.eventloop.SyncdDevice.Manager, com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void mapControllerConfiguration(com.qualcomm.robotcore.hardware.HardwareMap, com.qualcomm.robotcore.hardware.DeviceManager, com.qualcomm.robotcore.hardware.configuration.ControllerConfiguration) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void setXmlPullParser(org.xmlpull.v1.XmlPullParser);
  public org.xmlpull.v1.XmlPullParser getXmlPullParser();
  public static void noteSerialNumberType(android.content.Context, com.qualcomm.robotcore.util.SerialNumber, java.lang.String);
  public static java.lang.String getDeviceDisplayName(android.content.Context, com.qualcomm.robotcore.util.SerialNumber);
}
```

## class HardwareManualControlOpMode

```java
public abstract class com.qualcomm.hardware.HardwareManualControlOpMode extends com.qualcomm.robotcore.eventloop.opmode.LinearOpMode {
  public com.qualcomm.hardware.HardwareManualControlOpMode();
  public static com.qualcomm.hardware.HardwareManualControlOpMode getInstance();
  protected static void setInstance(com.qualcomm.hardware.HardwareManualControlOpMode);
  public abstract void onLynxModuleAddressChanged(com.qualcomm.hardware.lynx.LynxModule, int, int);
  public abstract void onLynxModuleStatusChanged(com.qualcomm.hardware.lynx.LynxModule, int, int);
}
```
