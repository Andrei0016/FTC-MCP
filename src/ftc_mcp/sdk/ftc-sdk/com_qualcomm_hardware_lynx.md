# `com.qualcomm.hardware.lynx`

_ftc-sdk 11.1.0 — 46 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class LynxAnalogInputController

```java
public class com.qualcomm.hardware.lynx.LynxAnalogInputController extends com.qualcomm.hardware.lynx.LynxController implements com.qualcomm.robotcore.hardware.AnalogInputController {
  public static final java.lang.String TAG = "LynxAnalogInputController";
  public static final int apiPortFirst = 0;
  public static final int apiPortLast = 3;
  protected java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxAnalogInputController(android.content.Context, com.qualcomm.hardware.lynx.LynxModule) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public double getAnalogInputVoltage(int);
  public double getMaxAnalogInputVoltage();
}
```

## class LynxCommExceptionHandler

```java
public class com.qualcomm.hardware.lynx.LynxCommExceptionHandler {
  protected java.lang.String tag;
  protected java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxCommExceptionHandler();
  public com.qualcomm.hardware.lynx.LynxCommExceptionHandler(java.lang.String);
  protected boolean handleException(java.lang.Exception);
  protected void handleSpecificException(java.lang.InterruptedException);
  protected void handleSpecificException(com.qualcomm.robotcore.exception.TargetPositionNotSetException);
  protected void handleSpecificException(java.lang.RuntimeException);
  protected void handleSpecificException(com.qualcomm.hardware.lynx.LynxNackException);
}
```

## class LynxController

```java
public abstract class com.qualcomm.hardware.lynx.LynxController extends com.qualcomm.hardware.lynx.LynxCommExceptionHandler implements com.qualcomm.robotcore.hardware.RobotCoreLynxController,com.qualcomm.robotcore.hardware.Engagable,com.qualcomm.robotcore.hardware.HardwareDeviceHealth,com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback,com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier {
  protected android.content.Context context;
  protected boolean isHardwareInitialized;
  protected boolean isEngaged;
  protected boolean isHooked;
  protected final com.qualcomm.robotcore.util.WeakReferenceSet<com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback> registeredCallbacks;
  protected final com.qualcomm.robotcore.hardware.HardwareDeviceHealthImpl hardwareDeviceHealth;
  protected abstract java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxController(android.content.Context, com.qualcomm.hardware.lynx.LynxModule);
  protected void finishConstruction();
  public synchronized void onModuleStateChange(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier, com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.ARMINGSTATE);
  protected void moduleNowArmedOrPretending();
  protected void moduleNowDisarmed();
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.ARMINGSTATE getArmingState();
  public void registerCallback(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback, boolean);
  public void unregisterCallback(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public synchronized void close();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public abstract java.lang.String getDeviceName();
  public void resetDeviceConfigurationForOpMode();
  protected void initializeHardware() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void floatHardware();
  public void forgetLastKnown();
  protected void setHealthyIfArmed();
  public void setHealthStatus(com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus);
  protected java.util.concurrent.Callable<com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus> getHealthStatusOverride();
  public com.qualcomm.robotcore.hardware.HardwareDeviceHealth.HealthStatus getHealthStatus();
  public void engage();
  public void disengage();
  public boolean isEngaged();
  protected com.qualcomm.hardware.lynx.LynxModuleIntf getModule();
  protected void adjustHookingToMatchEngagement();
  protected void hook();
  protected void unhook();
  protected void doHook();
  protected void doUnhook();
  protected boolean isArmed();
}
```

## class LynxController.PretendLynxModule

```java
public class com.qualcomm.hardware.lynx.LynxController.PretendLynxModule implements com.qualcomm.hardware.lynx.LynxModuleIntf {
  public com.qualcomm.hardware.lynx.LynxController.PretendLynxModule(com.qualcomm.hardware.lynx.LynxController);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getFirmwareVersionString();
  public java.lang.String getNullableFirmwareVersionString();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public <T> T acquireI2cLockWhile(com.qualcomm.hardware.lynx.Supplier<T>) throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException, com.qualcomm.hardware.lynx.LynxNackException;
  public void acquireNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void releaseNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void sendCommand(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException, com.qualcomm.hardware.lynx.LynxUnsupportedCommandException;
  public void retransmit(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void finishedWithMessage(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void resetPingTimer(com.qualcomm.hardware.lynx.commands.LynxMessage);
  public int getModuleAddress();
  public void setAttentionRequired(boolean);
  public com.qualcomm.hardware.lynx.commands.LynxInterface getInterface(java.lang.String);
  public boolean isParent();
  public void validateCommand(com.qualcomm.hardware.lynx.commands.LynxMessage) throws com.qualcomm.hardware.lynx.LynxUnsupportedCommandException;
  public boolean isCommandSupported(java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxCommand>);
  public boolean isOpen();
  public boolean isEngaged();
  public void engage();
  public void disengage();
  public void noteNotResponding();
  public boolean isNotResponding();
  public void attemptFailSafeAndIgnoreErrors();
}
```

## class LynxDcMotorController

```java
public class com.qualcomm.hardware.lynx.LynxDcMotorController extends com.qualcomm.hardware.lynx.LynxController implements com.qualcomm.robotcore.hardware.DcMotorController,com.qualcomm.robotcore.hardware.DcMotorControllerEx {
  public static final int apiMotorFirst = 0;
  public static final int apiMotorLast = 3;
  public static final double apiPowerFirst = -1.0d;
  public static final double apiPowerLast = 1.0d;
  public static final java.lang.String TAG = "LynxMotor";
  protected static boolean DEBUG;
  protected final com.qualcomm.hardware.lynx.LynxDcMotorController.MotorProperties[] motors;
  protected java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxDcMotorController(android.content.Context, com.qualcomm.hardware.lynx.LynxModule) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void initializeHardware() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void doHook();
  protected void doUnhook();
  public void forgetLastKnown();
  public java.lang.String getDeviceName();
  public synchronized void setMotorEnable(int);
  public synchronized void setMotorDisable(int);
  public synchronized boolean isMotorEnabled(int);
  public synchronized void resetDeviceConfigurationForOpMode(int);
  public synchronized com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType getMotorType(int);
  public synchronized void setMotorType(int, com.qualcomm.robotcore.hardware.configuration.typecontainers.MotorConfigurationType);
  protected void rememberPIDParams(int, com.qualcomm.robotcore.hardware.configuration.ExpansionHubMotorControllerParamsState);
  protected void updateMotorParams(int);
  protected int getDefaultMaxMotorSpeed(int);
  public synchronized void setMotorMode(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public synchronized com.qualcomm.robotcore.hardware.DcMotor.RunMode getMotorMode(int);
  protected com.qualcomm.robotcore.hardware.DcMotor.RunMode internalGetPublicMotorMode(int);
  protected com.qualcomm.robotcore.hardware.DcMotor.RunMode internalGetMotorChannelMode(int);
  public synchronized void setMotorPower(int, double);
  public synchronized double getMotorPower(int);
  public synchronized boolean isBusy(int);
  public synchronized void setMotorZeroPowerBehavior(int, com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior);
  public synchronized com.qualcomm.robotcore.hardware.DcMotor.ZeroPowerBehavior getMotorZeroPowerBehavior(int);
  protected synchronized void setMotorPowerFloat(int);
  public synchronized boolean getMotorPowerFloat(int);
  public synchronized void setMotorTargetPosition(int, int);
  public synchronized void setMotorTargetPosition(int, int, int);
  public synchronized int getMotorTargetPosition(int);
  public synchronized int getMotorCurrentPosition(int);
  public synchronized void setMotorVelocity(int, double);
  public synchronized void setMotorVelocity(int, double, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public synchronized double getMotorVelocity(int);
  public synchronized double getMotorVelocity(int, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public void setPIDCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDCoefficients);
  public synchronized void setPIDFCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDFCoefficients);
  protected boolean internalSetPIDFCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode, com.qualcomm.robotcore.hardware.PIDFCoefficients);
  public synchronized com.qualcomm.robotcore.hardware.PIDCoefficients getPIDCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public synchronized com.qualcomm.robotcore.hardware.PIDFCoefficients getPIDFCoefficients(int, com.qualcomm.robotcore.hardware.DcMotor.RunMode);
  public double getMotorCurrent(int, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public double getMotorCurrentAlert(int, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public void setMotorCurrentAlert(int, double, org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public boolean isMotorOverCurrent(int);
  public void floatHardware();
  protected int getModuleAddress();
}
```

## class LynxDcMotorController.MotorProperties

```java
public class com.qualcomm.hardware.lynx.LynxDcMotorController.MotorProperties {
  protected com.qualcomm.hardware.lynx.LynxDcMotorController.MotorProperties(com.qualcomm.hardware.lynx.LynxDcMotorController);
}
```

## class LynxDigitalChannelController

```java
public class com.qualcomm.hardware.lynx.LynxDigitalChannelController extends com.qualcomm.hardware.lynx.LynxController implements com.qualcomm.robotcore.hardware.DigitalChannelController {
  public static final java.lang.String TAG = "LynxDigitalChannelController";
  public static final int apiPinFirst = 0;
  public static final int apiPinLast = 7;
  protected final com.qualcomm.hardware.lynx.LynxDigitalChannelController.PinProperties[] pins;
  protected java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxDigitalChannelController(android.content.Context, com.qualcomm.hardware.lynx.LynxModule) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void initializeHardware();
  public void forgetLastKnown();
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public synchronized com.qualcomm.robotcore.hardware.DigitalChannel.Mode getDigitalChannelMode(int);
  public synchronized void setDigitalChannelMode(int, com.qualcomm.robotcore.hardware.DigitalChannel.Mode);
  public void setDigitalChannelMode(int, com.qualcomm.robotcore.hardware.DigitalChannelController.Mode);
  public synchronized boolean getDigitalChannelState(int);
  public synchronized void setDigitalChannelState(int, boolean);
}
```

## class LynxDigitalChannelController.PinProperties

```java
public class com.qualcomm.hardware.lynx.LynxDigitalChannelController.PinProperties {
  protected com.qualcomm.hardware.lynx.LynxDigitalChannelController.PinProperties(com.qualcomm.hardware.lynx.LynxDigitalChannelController);
}
```

## class LynxEmbeddedBNO055IMUNew

```java
public class com.qualcomm.hardware.lynx.LynxEmbeddedBNO055IMUNew extends com.qualcomm.hardware.bosch.BNO055IMUNew {
  public com.qualcomm.hardware.lynx.LynxEmbeddedBNO055IMUNew(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
}
```

## class LynxEmbeddedIMU

```java
public class com.qualcomm.hardware.lynx.LynxEmbeddedIMU extends com.qualcomm.hardware.bosch.BNO055IMUImpl {
  public com.qualcomm.hardware.lynx.LynxEmbeddedIMU(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
}
```

## class LynxFirmwareUpdater

```java
class com.qualcomm.hardware.lynx.LynxFirmwareUpdater {
  public com.qualcomm.hardware.lynx.LynxFirmwareUpdater(com.qualcomm.hardware.lynx.LynxUsbDeviceImpl);
  public org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.LynxFirmwareUpdateResp updateFirmware(org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.FWImage, java.lang.String, org.firstinspires.ftc.robotcore.external.Consumer<org.firstinspires.ftc.robotcore.internal.ui.ProgressParameters>);
  public boolean enterFirmwareUpdateModeControlHub();
}
```

## class LynxI2cColorRangeSensor

```java
public class com.qualcomm.hardware.lynx.LynxI2cColorRangeSensor extends com.qualcomm.hardware.ams.AMSColorSensorImpl implements com.qualcomm.robotcore.hardware.DistanceSensor,com.qualcomm.robotcore.hardware.OpticalDistanceSensor,com.qualcomm.robotcore.hardware.ColorRangeSensor {
  protected static final double apiLevelMin = 0.0d;
  protected static final double apiLevelMax = 1.0d;
  public double aParam;
  public double bParam;
  public double cParam;
  public com.qualcomm.hardware.lynx.LynxI2cColorRangeSensor(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public double getDistance(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  protected double cmFromOptical(int);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public double getLightDetected();
  public double getRawLightDetected();
  public double getRawLightDetectedMax();
  public java.lang.String status();
  public int rawOptical();
}
```

## class LynxI2cDeviceSynch

```java
public abstract class com.qualcomm.hardware.lynx.LynxI2cDeviceSynch extends com.qualcomm.hardware.lynx.LynxController implements com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple,com.qualcomm.robotcore.hardware.I2cDeviceSynchReadHistory {
  public static final java.lang.String TAG = "LynxI2cDeviceSynch";
  protected com.qualcomm.robotcore.hardware.I2cAddr i2cAddr;
  protected int bus;
  protected com.qualcomm.hardware.lynx.LynxUsbUtil.Placeholder<com.qualcomm.robotcore.hardware.TimestampedData> readTimeStampedPlaceholder;
  protected java.lang.String getTag();
  protected com.qualcomm.hardware.lynx.LynxI2cDeviceSynch(android.content.Context, com.qualcomm.hardware.lynx.LynxModule, int);
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public void resetDeviceConfigurationForOpMode();
  public void close();
  public boolean isArmed();
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public void setI2cAddr(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddr();
  public void setUserConfiguredName(java.lang.String);
  public java.lang.String getUserConfiguredName();
  public void setLogging(boolean);
  public boolean getLogging();
  public void setLoggingTag(java.lang.String);
  public java.lang.String getLoggingTag();
  public void setHistoryQueueCapacity(int);
  public int getHistoryQueueCapacity();
  public java.util.concurrent.BlockingQueue<com.qualcomm.robotcore.hardware.TimestampedI2cData> getHistoryQueue();
  public byte[] read(int, int);
  public synchronized byte read8(int);
  public abstract com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int, int);
  public byte[] read(int);
  public synchronized byte read8();
  public synchronized com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int);
  public void write(int, byte[]);
  public synchronized void write8(int, int);
  public synchronized void write8(int, int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public synchronized void write(int, byte[], com.qualcomm.robotcore.hardware.I2cWaitControl);
  public synchronized void write(byte[]);
  public synchronized void write(byte[], com.qualcomm.robotcore.hardware.I2cWaitControl);
  public synchronized void write8(int);
  public synchronized void write8(int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  public synchronized void waitForWriteCompletions(com.qualcomm.robotcore.hardware.I2cWaitControl);
  public void enableWriteCoalescing(boolean);
  public boolean isWriteCoalescingEnabled();
  protected void sendI2cTransaction(com.qualcomm.hardware.lynx.Supplier<? extends com.qualcomm.hardware.lynx.commands.LynxCommand<?>>) throws com.qualcomm.hardware.lynx.LynxNackException, java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException;
  protected <T> T acquireI2cLockWhile(com.qualcomm.hardware.lynx.Supplier<T>) throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException, com.qualcomm.hardware.lynx.LynxNackException;
  protected void internalWaitForWriteCompletions(com.qualcomm.robotcore.hardware.I2cWaitControl);
  protected com.qualcomm.robotcore.hardware.TimestampedData pollForReadResult(com.qualcomm.robotcore.hardware.I2cAddr, int, int);
  public void setBusSpeed(com.qualcomm.hardware.lynx.LynxI2cDeviceSynch.BusSpeed);
}
```

## class LynxI2cDeviceSynch.BusSpeed

```java
public class com.qualcomm.hardware.lynx.LynxI2cDeviceSynch.BusSpeed extends java.lang.Enum<com.qualcomm.hardware.lynx.LynxI2cDeviceSynch.BusSpeed> {
  public static final com.qualcomm.hardware.lynx.LynxI2cDeviceSynch.BusSpeed STANDARD_100K;
  public static final com.qualcomm.hardware.lynx.LynxI2cDeviceSynch.BusSpeed FAST_400K;
  public static com.qualcomm.hardware.lynx.LynxI2cDeviceSynch.BusSpeed[] values();
  public static com.qualcomm.hardware.lynx.LynxI2cDeviceSynch.BusSpeed valueOf(java.lang.String);
  protected com.qualcomm.hardware.lynx.commands.core.LynxI2cConfigureChannelCommand.SpeedCode toSpeedCode();
}
```

## class LynxI2cDeviceSynchV1

```java
public class com.qualcomm.hardware.lynx.LynxI2cDeviceSynchV1 extends com.qualcomm.hardware.lynx.LynxI2cDeviceSynch {
  public com.qualcomm.hardware.lynx.LynxI2cDeviceSynchV1(android.content.Context, com.qualcomm.hardware.lynx.LynxModule, int);
  public synchronized com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int, int);
}
```

## class LynxI2cDeviceSynchV2

```java
public class com.qualcomm.hardware.lynx.LynxI2cDeviceSynchV2 extends com.qualcomm.hardware.lynx.LynxI2cDeviceSynch {
  public com.qualcomm.hardware.lynx.LynxI2cDeviceSynchV2(android.content.Context, com.qualcomm.hardware.lynx.LynxModule, int);
  public synchronized com.qualcomm.robotcore.hardware.TimestampedData readTimeStamped(int, int);
}
```

## class LynxModule

```java
public class com.qualcomm.hardware.lynx.LynxModule extends com.qualcomm.hardware.lynx.LynxCommExceptionHandler implements com.qualcomm.hardware.lynx.LynxModuleIntf,com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier,com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback,com.qualcomm.robotcore.hardware.Blinker,com.qualcomm.robotcore.hardware.VisuallyIdentifiableHardwareDevice {
  public static final java.lang.String TAG = "LynxModule";
  public static com.qualcomm.hardware.lynx.LynxModule.BlinkerPolicy blinkerPolicy;
  protected static final int msInitialContact = 500;
  protected static final int msKeepAliveTimeout = 2500;
  protected static final byte moduleStatusPersistentBits = 28;
  protected static java.util.Map<java.lang.Integer, com.qualcomm.hardware.lynx.LynxModule.MessageClassAndCtor> standardMessages;
  protected static java.util.Map<java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxCommand>, com.qualcomm.hardware.lynx.LynxModule.MessageClassAndCtor> responseClasses;
  protected com.qualcomm.hardware.lynx.LynxUsbDevice lynxUsbDevice;
  protected java.util.List<com.qualcomm.hardware.lynx.LynxController> controllers;
  protected final java.lang.Object addrAndSerialLock;
  protected int moduleAddress;
  protected com.qualcomm.robotcore.util.SerialNumber moduleSerialNumber;
  protected java.util.concurrent.atomic.AtomicInteger nextMessageNumber;
  protected boolean isParent;
  protected volatile boolean isSystemSynthetic;
  protected volatile boolean isUserModule;
  protected int systemOperationCounter;
  protected boolean isEngaged;
  protected final java.lang.Object engagementLock;
  protected volatile boolean isOpen;
  protected volatile boolean isNotResponding;
  protected final java.lang.Object startStopLock;
  protected final java.util.concurrent.ConcurrentHashMap<java.lang.Integer, com.qualcomm.hardware.lynx.commands.LynxRespondable> unfinishedCommands;
  protected final java.util.concurrent.ConcurrentHashMap<java.lang.Integer, com.qualcomm.hardware.lynx.LynxModule.MessageClassAndCtor> commandClasses;
  protected final java.util.Set<java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxCommand>> supportedCommands;
  protected final java.util.concurrent.ConcurrentHashMap<java.lang.String, com.qualcomm.hardware.lynx.commands.LynxInterface> interfacesQueried;
  protected final java.lang.Object i2cLock;
  protected java.util.ArrayList<com.qualcomm.robotcore.hardware.Blinker.Step> currentSteps;
  protected java.util.Deque<java.util.ArrayList<com.qualcomm.robotcore.hardware.Blinker.Step>> previousSteps;
  protected boolean isVisuallyIdentifying;
  protected java.util.concurrent.ScheduledExecutorService executor;
  protected java.util.concurrent.Future<?> pingFuture;
  protected final java.lang.Object pingFutureLock;
  protected java.util.concurrent.Future<?> moduleStatusFuture;
  protected boolean attentionRequiredPreviously;
  protected int previousModuleStatus;
  protected final java.lang.Object moduleStatusLock;
  protected boolean ftdiResetWatchdogActive;
  protected boolean ftdiResetWatchdogActiveWhenEngaged;
  protected final java.lang.Object bulkCachingLock;
  protected com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode bulkCachingMode;
  protected java.util.Map<java.lang.String, java.util.List<com.qualcomm.hardware.lynx.commands.core.LynxDekaInterfaceCommand<?>>> bulkCachingHistory;
  protected com.qualcomm.hardware.lynx.LynxModule.BulkData lastBulkData;
  protected java.lang.String getTag();
  protected static void addStandardMessage(java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxMessage>);
  protected static void correlateStandardResponse(java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxCommand>);
  public static void correlateResponse(java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxCommand>, java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxResponse>) throws java.lang.NoSuchMethodException;
  public com.qualcomm.hardware.lynx.LynxModule(com.qualcomm.hardware.lynx.LynxUsbDevice, int, boolean, boolean);
  public java.lang.String toString();
  public void close();
  public boolean isOpen();
  public boolean isUserModule();
  public void setUserModule(boolean);
  public boolean isSystemSynthetic();
  public void setSystemSynthetic(boolean);
  public void noteController(com.qualcomm.hardware.lynx.LynxController);
  public int getRevProductNumber();
  public int getModuleAddress();
  public void setNewModuleAddress(int);
  protected byte getNewMessageNumber();
  public void setAttentionRequired(boolean);
  protected void noteDatagramReceived();
  public void noteNotResponding();
  public boolean isNotResponding();
  protected void warnIfClosed();
  protected void stopAttentionRequired();
  protected void sendGetModuleStatusAndProcessResponse(boolean);
  protected void forgetLastKnown();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getFirmwareVersionString();
  public java.lang.String getNullableFirmwareVersionString();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public java.util.List<java.lang.String> getGlobalWarnings();
  public static java.lang.String getHealthStatusWarningMessage(com.qualcomm.robotcore.hardware.HardwareDeviceHealth);
  public com.qualcomm.robotcore.util.SerialNumber getModuleSerialNumber();
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.ARMINGSTATE getArmingState();
  public void registerCallback(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback, boolean);
  public void unregisterCallback(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback);
  public void onModuleStateChange(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier, com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.ARMINGSTATE);
  public void engage();
  public void disengage();
  public boolean isEngaged();
  public void visuallyIdentify(boolean);
  public int getBlinkerPatternMaxLength();
  public void setConstant(int);
  public void stopBlinking();
  public synchronized void setPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  public synchronized java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step> getPattern();
  protected void resendCurrentPattern();
  public synchronized void pushPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  protected void internalPushPattern(java.util.Collection<com.qualcomm.robotcore.hardware.Blinker.Step>);
  public synchronized boolean patternStackNotEmpty();
  public synchronized boolean popPattern();
  public boolean isParent();
  public void pingAndQueryKnownInterfacesAndEtc() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void initializeLEDS();
  protected void initializeDebugLogging() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void pingInitialContact() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void validateCommand(com.qualcomm.hardware.lynx.commands.LynxMessage) throws com.qualcomm.hardware.lynx.LynxUnsupportedCommandException;
  public boolean isCommandSupported(java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxCommand>);
  protected boolean queryInterface(com.qualcomm.hardware.lynx.commands.LynxInterface) throws java.lang.InterruptedException;
  public com.qualcomm.hardware.lynx.commands.LynxInterface getInterface(java.lang.String);
  protected void ping();
  protected void ping(boolean) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, com.qualcomm.hardware.lynx.LynxNackException;
  protected int getMsModulePingInterval();
  public void resetPingTimer(com.qualcomm.hardware.lynx.commands.LynxMessage);
  protected void startPingTimer();
  protected void stopPingTimer(boolean);
  protected void startFtdiResetWatchdog();
  protected void stopFtdiResetWatchdog();
  protected void stopFtdiResetWatchdog(boolean);
  protected void setFtdiResetWatchdog(boolean);
  protected void startExecutor();
  protected void stopExecutor();
  public com.qualcomm.hardware.lynx.LynxModule.BulkData getBulkData();
  public com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode getBulkCachingMode();
  public void setBulkCachingMode(com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode);
  public void clearBulkCache();
  public void failSafe() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, com.qualcomm.hardware.lynx.LynxNackException;
  public void attemptFailSafeAndIgnoreErrors();
  public void enablePhoneCharging(boolean) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, com.qualcomm.hardware.lynx.LynxNackException;
  public boolean isPhoneChargingEnabled() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, com.qualcomm.hardware.lynx.LynxNackException;
  public double getCurrent(org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public double getGpioBusCurrent(org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public double getI2cBusCurrent(org.firstinspires.ftc.robotcore.external.navigation.CurrentUnit);
  public double getInputVoltage(org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit);
  public double getAuxiliaryVoltage(org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit);
  public double getTemperature(org.firstinspires.ftc.robotcore.external.navigation.TempUnit);
  public com.qualcomm.robotcore.hardware.LynxModuleImuType getImuType();
  public void setDebug(com.qualcomm.hardware.lynx.LynxModule.DebugGroup, com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity) throws java.lang.InterruptedException;
  public <T> T acquireI2cLockWhile(com.qualcomm.hardware.lynx.Supplier<T>) throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException, com.qualcomm.hardware.lynx.LynxNackException;
  public void acquireNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void releaseNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void sendCommand(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException, com.qualcomm.hardware.lynx.LynxUnsupportedCommandException;
  public void retransmit(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void finishedWithMessage(com.qualcomm.hardware.lynx.commands.LynxMessage);
  public void pretendFinishExtantCommands() throws java.lang.InterruptedException;
  public void onIncomingDatagramReceived(com.qualcomm.hardware.lynx.commands.LynxDatagram);
  public void abandonUnfinishedCommands();
  protected void nackUnfinishedCommands();
}
```

## interface LynxModule.BlinkerPolicy

```java
public interface com.qualcomm.hardware.lynx.LynxModule.BlinkerPolicy {
  public abstract java.util.List<com.qualcomm.robotcore.hardware.Blinker.Step> getIdlePattern(com.qualcomm.hardware.lynx.LynxModule);
  public abstract java.util.List<com.qualcomm.robotcore.hardware.Blinker.Step> getVisuallyIdentifyPattern(com.qualcomm.hardware.lynx.LynxModule);
}
```

## class LynxModule.BreathingBlinkerPolicy

```java
public class com.qualcomm.hardware.lynx.LynxModule.BreathingBlinkerPolicy implements com.qualcomm.hardware.lynx.LynxModule.BlinkerPolicy {
  public com.qualcomm.hardware.lynx.LynxModule.BreathingBlinkerPolicy();
  public java.util.List<com.qualcomm.robotcore.hardware.Blinker.Step> getIdlePattern(com.qualcomm.hardware.lynx.LynxModule);
  public java.util.List<com.qualcomm.robotcore.hardware.Blinker.Step> getVisuallyIdentifyPattern(com.qualcomm.hardware.lynx.LynxModule);
}
```

## class LynxModule.BulkCachingMode

```java
public final class com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode extends java.lang.Enum<com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode> {
  public static final com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode OFF;
  public static final com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode MANUAL;
  public static final com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode AUTO;
  public static com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode[] values();
  public static com.qualcomm.hardware.lynx.LynxModule.BulkCachingMode valueOf(java.lang.String);
}
```

## class LynxModule.BulkData

```java
public class com.qualcomm.hardware.lynx.LynxModule.BulkData {
  public boolean getDigitalChannelState(int);
  public int getMotorCurrentPosition(int);
  public int getMotorVelocity(int);
  public boolean isMotorBusy(int);
  public boolean isMotorOverCurrent(int);
  public double getAnalogInputVoltage(int);
  public double getAnalogInputVoltage(int, org.firstinspires.ftc.robotcore.external.navigation.VoltageUnit);
  public boolean isFake();
}
```

## class LynxModule.CountModuleAddressBlinkerPolicy

```java
public class com.qualcomm.hardware.lynx.LynxModule.CountModuleAddressBlinkerPolicy extends com.qualcomm.hardware.lynx.LynxModule.BreathingBlinkerPolicy {
  public com.qualcomm.hardware.lynx.LynxModule.CountModuleAddressBlinkerPolicy();
  public java.util.List<com.qualcomm.robotcore.hardware.Blinker.Step> getIdlePattern(com.qualcomm.hardware.lynx.LynxModule);
}
```

## class LynxModule.DebugGroup

```java
public final class com.qualcomm.hardware.lynx.LynxModule.DebugGroup extends java.lang.Enum<com.qualcomm.hardware.lynx.LynxModule.DebugGroup> {
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup NONE;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup MAIN;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup TOHOST;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup FROMHOST;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup ADC;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup PWMSERVO;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup MODULELED;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup DIGITALIO;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup I2C;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup MOTOR0;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup MOTOR1;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup MOTOR2;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugGroup MOTOR3;
  public final byte bVal;
  public static com.qualcomm.hardware.lynx.LynxModule.DebugGroup[] values();
  public static com.qualcomm.hardware.lynx.LynxModule.DebugGroup valueOf(java.lang.String);
  public static com.qualcomm.hardware.lynx.LynxModule.DebugGroup fromInt(int);
}
```

## class LynxModule.DebugVerbosity

```java
public final class com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity extends java.lang.Enum<com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity> {
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity OFF;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity LOW;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity MEDIUM;
  public static final com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity HIGH;
  public final byte bVal;
  public static com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity[] values();
  public static com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity valueOf(java.lang.String);
  public static com.qualcomm.hardware.lynx.LynxModule.DebugVerbosity fromInt(int);
}
```

## class LynxModule.MessageClassAndCtor

```java
public class com.qualcomm.hardware.lynx.LynxModule.MessageClassAndCtor {
  public java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxMessage> clazz;
  public java.lang.reflect.Constructor<? extends com.qualcomm.hardware.lynx.commands.LynxMessage> ctor;
  protected com.qualcomm.hardware.lynx.LynxModule.MessageClassAndCtor();
  public void assignCtor() throws java.lang.NoSuchMethodException;
}
```

## interface LynxModuleIntf

```java
public interface com.qualcomm.hardware.lynx.LynxModuleIntf extends com.qualcomm.robotcore.hardware.RobotCoreLynxModule,com.qualcomm.robotcore.hardware.HardwareDevice,com.qualcomm.robotcore.hardware.Engagable {
  public abstract <T> T acquireI2cLockWhile(com.qualcomm.hardware.lynx.Supplier<T>) throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException, com.qualcomm.hardware.lynx.LynxNackException;
  public abstract void acquireNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public abstract void releaseNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public abstract void validateCommand(com.qualcomm.hardware.lynx.commands.LynxMessage) throws com.qualcomm.hardware.lynx.LynxUnsupportedCommandException;
  public abstract boolean isCommandSupported(java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxCommand>);
  public abstract boolean isOpen();
  public abstract void sendCommand(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException, com.qualcomm.hardware.lynx.LynxUnsupportedCommandException;
  public abstract void resetPingTimer(com.qualcomm.hardware.lynx.commands.LynxMessage);
  public abstract void retransmit(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public abstract void finishedWithMessage(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public abstract void setAttentionRequired(boolean);
  public abstract void noteNotResponding();
  public abstract boolean isNotResponding();
  public abstract com.qualcomm.hardware.lynx.commands.LynxInterface getInterface(java.lang.String);
}
```

## class LynxModuleWarningManager

```java
public class com.qualcomm.hardware.lynx.LynxModuleWarningManager {
  public com.qualcomm.hardware.lynx.LynxModuleWarningManager();
  public static com.qualcomm.hardware.lynx.LynxModuleWarningManager getInstance();
  public void init(com.qualcomm.robotcore.eventloop.opmode.OpModeManagerImpl, com.qualcomm.robotcore.hardware.HardwareMap);
  public void reportModuleUnresponsive(com.qualcomm.hardware.lynx.LynxModule);
  public void reportModuleReset(com.qualcomm.hardware.lynx.LynxModule);
  public void reportModuleLowBattery(com.qualcomm.hardware.lynx.LynxModule);
}
```

## class LynxModuleWarningManager.ConditionStatus

```java
abstract class com.qualcomm.hardware.lynx.LynxModuleWarningManager.ConditionStatus {
}
```

## class LynxModuleWarningManager.LowBatteryStatus

```java
class com.qualcomm.hardware.lynx.LynxModuleWarningManager.LowBatteryStatus extends com.qualcomm.hardware.lynx.LynxModuleWarningManager.ConditionStatus {
}
```

## class LynxModuleWarningManager.LynxModuleWarningSource

```java
class com.qualcomm.hardware.lynx.LynxModuleWarningManager.LynxModuleWarningSource implements com.qualcomm.robotcore.util.GlobalWarningSource {
  public java.lang.String getGlobalWarning();
  public boolean shouldTriggerWarningSound();
  public void suppressGlobalWarning(boolean);
  public void clearGlobalWarning();
  public void setGlobalWarning(java.lang.String);
}
```

## class LynxModuleWarningManager.UnresponsiveStatus

```java
class com.qualcomm.hardware.lynx.LynxModuleWarningManager.UnresponsiveStatus extends com.qualcomm.hardware.lynx.LynxModuleWarningManager.ConditionStatus {
}
```

## class LynxModuleWarningManager.WarningManagerOpModeListener

```java
class com.qualcomm.hardware.lynx.LynxModuleWarningManager.WarningManagerOpModeListener implements com.qualcomm.robotcore.eventloop.opmode.OpModeManagerNotifier.Notifications {
  public void onOpModePreInit(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePreStart(com.qualcomm.robotcore.eventloop.opmode.OpMode);
  public void onOpModePostStop(com.qualcomm.robotcore.eventloop.opmode.OpMode);
}
```

## class LynxNackException

```java
public class com.qualcomm.hardware.lynx.LynxNackException extends java.lang.Exception {
  public com.qualcomm.hardware.lynx.LynxNackException(com.qualcomm.hardware.lynx.commands.LynxRespondable, java.lang.String);
  public com.qualcomm.hardware.lynx.LynxNackException(com.qualcomm.hardware.lynx.commands.LynxRespondable, java.lang.String, java.lang.Object...);
  public com.qualcomm.robotcore.exception.RobotCoreException wrap();
  public com.qualcomm.hardware.lynx.commands.LynxRespondable getCommand();
  public com.qualcomm.hardware.lynx.commands.standard.LynxNack getNack();
}
```

## class LynxPwmOutputController

```java
public class com.qualcomm.hardware.lynx.LynxPwmOutputController extends com.qualcomm.hardware.lynx.LynxController implements com.qualcomm.robotcore.hardware.PWMOutputController,com.qualcomm.robotcore.hardware.PWMOutputControllerEx {
  public static final java.lang.String TAG = "LynxPwmOutputController";
  public static final int apiPortFirst = 0;
  public static final int apiPortLast = 3;
  protected com.qualcomm.robotcore.util.LastKnown<java.lang.Integer>[] lastKnownOutputTimes;
  protected com.qualcomm.robotcore.util.LastKnown<java.lang.Integer>[] lastKnownPulseWidthPeriods;
  protected java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxPwmOutputController(android.content.Context, com.qualcomm.hardware.lynx.LynxModule) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void initializeHardware();
  public void floatHardware();
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public synchronized void setPulseWidthOutputTime(int, int);
  public synchronized void setPulseWidthPeriod(int, int);
  public synchronized int getPulseWidthOutputTime(int);
  public synchronized int getPulseWidthPeriod(int);
  public synchronized void setPwmEnable(int);
  public synchronized void setPwmDisable(int);
  public synchronized boolean isPwmEnabled(int);
}
```

## class LynxServoController

```java
public class com.qualcomm.hardware.lynx.LynxServoController extends com.qualcomm.hardware.lynx.LynxController implements com.qualcomm.robotcore.hardware.ServoController,com.qualcomm.robotcore.hardware.ServoControllerEx {
  public static final java.lang.String TAG = "LynxServoController";
  public static final int apiServoFirst = 0;
  public static final int apiServoLast = 5;
  public static final double apiPositionFirst = 0.0d;
  public static final double apiPositionLast = 1.0d;
  protected final com.qualcomm.robotcore.util.LastKnown<java.lang.Double>[] lastKnownCommandedPosition;
  protected final com.qualcomm.robotcore.util.LastKnown<java.lang.Boolean>[] lastKnownEnabled;
  protected com.qualcomm.robotcore.hardware.PwmControl.PwmRange[] pwmRanges;
  protected com.qualcomm.robotcore.hardware.PwmControl.PwmRange[] defaultPwmRanges;
  protected java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxServoController(android.content.Context, com.qualcomm.hardware.lynx.LynxModule) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void initializeHardware();
  public void floatHardware();
  public void forgetLastKnown();
  public java.lang.String getDeviceName();
  public synchronized void pwmEnable();
  public synchronized void pwmDisable();
  public synchronized com.qualcomm.robotcore.hardware.ServoController.PwmStatus getPwmStatus();
  public synchronized void setServoPwmEnable(int);
  public synchronized void setServoPwmDisable(int);
  public synchronized boolean isServoPwmEnabled(int);
  public void setServoType(int, com.qualcomm.robotcore.hardware.configuration.typecontainers.ServoConfigurationType);
  public synchronized void setServoPosition(int, double);
  public synchronized double getServoPosition(int);
  public synchronized void setServoPwmRange(int, com.qualcomm.robotcore.hardware.PwmControl.PwmRange);
  public synchronized com.qualcomm.robotcore.hardware.PwmControl.PwmRange getServoPwmRange(int);
}
```

## class LynxUnsupportedCommandException

```java
public class com.qualcomm.hardware.lynx.LynxUnsupportedCommandException extends java.lang.Exception {
  public com.qualcomm.hardware.lynx.LynxUnsupportedCommandException(com.qualcomm.hardware.lynx.LynxModule, com.qualcomm.hardware.lynx.commands.LynxMessage);
  public int getCommandNumber();
  public java.lang.Class<? extends com.qualcomm.hardware.lynx.commands.LynxMessage> getClazz();
  public com.qualcomm.hardware.lynx.LynxModuleIntf getLynxModule();
}
```

## interface LynxUsbDevice

```java
public interface com.qualcomm.hardware.lynx.LynxUsbDevice extends com.qualcomm.robotcore.hardware.usb.RobotUsbModule,com.qualcomm.robotcore.util.GlobalWarningSource,com.qualcomm.robotcore.hardware.RobotCoreLynxUsbDevice,com.qualcomm.robotcore.hardware.HardwareDevice,com.qualcomm.robotcore.eventloop.SyncdDevice,com.qualcomm.robotcore.hardware.Engagable {
  public abstract com.qualcomm.robotcore.hardware.usb.RobotUsbDevice getRobotUsbDevice();
  public abstract boolean isSystemSynthetic();
  public abstract void setSystemSynthetic(boolean);
  public abstract void failSafe();
  public abstract void changeModuleAddress(com.qualcomm.hardware.lynx.LynxModule, int, java.lang.Runnable);
  public abstract com.qualcomm.hardware.lynx.LynxModule getOrAddModule(com.qualcomm.robotcore.hardware.LynxModuleDescription) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public abstract void removeConfiguredModule(com.qualcomm.hardware.lynx.LynxModule);
  public abstract void noteMissingModule(int, java.lang.String);
  public abstract void performSystemOperationOnParentModule(int, org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  public abstract void performSystemOperationOnConnectedModule(int, int, org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  public abstract com.qualcomm.hardware.lynx.LynxUsbDevice.SystemOperationHandle keepConnectedModuleAliveForSystemOperations(int, int) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public abstract com.qualcomm.robotcore.hardware.LynxModuleMetaList discoverModules(boolean) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public abstract void acquireNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public abstract void releaseNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public abstract void transmit(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public abstract boolean setupControlHubEmbeddedModule() throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException;
  public abstract com.qualcomm.hardware.lynx.LynxUsbDeviceImpl getDelegationTarget();
  public abstract org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.LynxFirmwareUpdateResp updateFirmware(org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.FWImage, java.lang.String, org.firstinspires.ftc.robotcore.external.Consumer<org.firstinspires.ftc.robotcore.internal.ui.ProgressParameters>);
}
```

## class LynxUsbDevice.SystemOperationHandle

```java
public class com.qualcomm.hardware.lynx.LynxUsbDevice.SystemOperationHandle {
  protected final com.qualcomm.hardware.lynx.LynxUsbDeviceImpl lynxUsb;
  protected final com.qualcomm.hardware.lynx.LynxModule module;
  protected final com.qualcomm.hardware.lynx.LynxModule parentModule;
  protected volatile boolean closed;
  protected com.qualcomm.hardware.lynx.LynxUsbDevice.SystemOperationHandle(com.qualcomm.hardware.lynx.LynxUsbDeviceImpl, com.qualcomm.hardware.lynx.LynxModule, com.qualcomm.hardware.lynx.LynxModule);
  public void performSystemOperation(org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  public void close();
  public com.qualcomm.robotcore.util.SerialNumber getLynxModuleSerialNumber();
  public boolean wrapsModule(com.qualcomm.hardware.lynx.LynxModule);
  public boolean wrapsSameModule(com.qualcomm.hardware.lynx.LynxUsbDevice.SystemOperationHandle);
}
```

## class LynxUsbDeviceDelegate

```java
public class com.qualcomm.hardware.lynx.LynxUsbDeviceDelegate implements com.qualcomm.hardware.lynx.LynxUsbDevice,com.qualcomm.robotcore.hardware.HardwareDeviceCloseOnTearDown {
  public static java.lang.String TAG;
  protected com.qualcomm.hardware.lynx.LynxUsbDeviceImpl delegate;
  protected boolean releaseOnClose;
  protected boolean isOpen;
  public com.qualcomm.hardware.lynx.LynxUsbDeviceDelegate(com.qualcomm.hardware.lynx.LynxUsbDeviceImpl);
  public com.qualcomm.hardware.lynx.LynxUsbDeviceImpl getDelegationTarget();
  public synchronized void close();
  protected void assertOpen();
  public void disengage();
  public void engage();
  public boolean isEngaged();
  public com.qualcomm.robotcore.hardware.usb.RobotUsbDevice getRobotUsbDevice();
  public boolean isSystemSynthetic();
  public void setSystemSynthetic(boolean);
  public void failSafe();
  public void lockNetworkLockAcquisitions();
  public void setThrowOnNetworkLockAcquisition(boolean);
  public void changeModuleAddress(com.qualcomm.hardware.lynx.LynxModule, int, java.lang.Runnable);
  public void noteMissingModule(int, java.lang.String);
  public void performSystemOperationOnParentModule(int, org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  public void performSystemOperationOnConnectedModule(int, int, org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  public com.qualcomm.hardware.lynx.LynxUsbDevice.SystemOperationHandle keepConnectedModuleAliveForSystemOperations(int, int) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public com.qualcomm.hardware.lynx.LynxModule getOrAddModule(com.qualcomm.robotcore.hardware.LynxModuleDescription) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void removeConfiguredModule(com.qualcomm.hardware.lynx.LynxModule);
  public com.qualcomm.robotcore.hardware.LynxModuleMetaList discoverModules(boolean) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void acquireNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void releaseNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void transmit(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public boolean setupControlHubEmbeddedModule() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.LynxFirmwareUpdateResp updateFirmware(org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.FWImage, java.lang.String, org.firstinspires.ftc.robotcore.external.Consumer<org.firstinspires.ftc.robotcore.internal.ui.ProgressParameters>);
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public void resetDeviceConfigurationForOpMode();
  public com.qualcomm.robotcore.eventloop.SyncdDevice.ShutdownReason getShutdownReason();
  public void setOwner(com.qualcomm.robotcore.hardware.usb.RobotUsbModule);
  public com.qualcomm.robotcore.hardware.usb.RobotUsbModule getOwner();
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.ARMINGSTATE getArmingState();
  public void registerCallback(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback, boolean);
  public void unregisterCallback(com.qualcomm.robotcore.hardware.usb.RobotArmingStateNotifier.Callback);
  public void arm() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void pretend() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void armOrPretend() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void disarm() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public java.lang.String getGlobalWarning();
  public boolean shouldTriggerWarningSound();
  public void suppressGlobalWarning(boolean);
  public void setGlobalWarning(java.lang.String);
  public void clearGlobalWarning();
}
```

## class LynxUsbDeviceImpl

```java
public class com.qualcomm.hardware.lynx.LynxUsbDeviceImpl extends org.firstinspires.ftc.robotcore.internal.hardware.usb.ArmableUsbDevice implements com.qualcomm.hardware.lynx.LynxUsbDevice {
  public static final java.lang.String TAG = "LynxUsb";
  public static boolean DEBUG_LOG_MESSAGES;
  public static boolean DEBUG_LOG_DATAGRAMS;
  public static boolean DEBUG_LOG_DATAGRAMS_FINISH;
  public static boolean DEBUG_LOG_DATAGRAMS_LOCK;
  protected static final com.qualcomm.robotcore.util.WeakReferenceSet<com.qualcomm.hardware.lynx.LynxUsbDeviceImpl> extantDevices;
  protected static final com.qualcomm.hardware.lynx.LynxCommExceptionHandler exceptionHandler;
  protected final java.util.concurrent.ConcurrentHashMap<java.lang.Integer, com.qualcomm.hardware.lynx.LynxModule> knownModules;
  protected final java.util.concurrent.ConcurrentHashMap<java.lang.Integer, com.qualcomm.hardware.lynx.LynxModule> knownModulesChanging;
  protected final java.util.concurrent.ConcurrentHashMap<java.lang.Integer, com.qualcomm.robotcore.hardware.LynxModuleMeta> discoveredModules;
  protected final java.util.concurrent.ConcurrentHashMap<java.lang.Integer, java.lang.String> missingModules;
  protected final com.qualcomm.hardware.lynx.MessageKeyedLock networkTransmissionLock;
  protected java.util.concurrent.ExecutorService incomingDatagramPoller;
  protected boolean resetAttempted;
  protected boolean hasShutdownAbnormally;
  protected boolean isSystemSynthetic;
  protected boolean isEngaged;
  protected boolean wasPollingWhenEngaged;
  protected final java.lang.Object engageLock;
  protected final java.lang.Object sysOpStartStopLock;
  protected final java.util.Set<java.lang.Object> runningSysOpTrackers;
  protected final com.qualcomm.hardware.lynx.LynxFirmwareUpdater lynxFirmwareUpdater;
  protected static final int cbusNReset = 1;
  protected static final int cbusNProg = 2;
  protected static final int cbusMask = 3;
  protected static final int cbusNeitherAsserted = 3;
  protected static final int cbusBothAsserted = 0;
  protected static final int cbusProgAsserted = 1;
  protected static final int cbusResetAsserted = 2;
  protected static final int msNetworkTransmissionLockAcquisitionTimeMax = 500;
  protected static final int msCbusWiggle = 75;
  protected static final int msResetRecovery = 200;
  protected static final java.lang.String SEPARATOR = " / ";
  protected java.lang.String getTag();
  public static org.firstinspires.ftc.robotcore.internal.hardware.usb.ArmableUsbDevice.OpenRobotUsbDevice createUsbOpener(com.qualcomm.robotcore.hardware.usb.RobotUsbManager, com.qualcomm.robotcore.util.SerialNumber);
  protected com.qualcomm.hardware.lynx.LynxUsbDeviceImpl(android.content.Context, com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.eventloop.SyncdDevice.Manager, com.qualcomm.robotcore.hardware.usb.RobotUsbManager);
  public static com.qualcomm.hardware.lynx.LynxUsbDevice findOrCreateAndArm(android.content.Context, com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.eventloop.SyncdDevice.Manager, com.qualcomm.robotcore.hardware.usb.RobotUsbManager) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public com.qualcomm.hardware.lynx.LynxUsbDeviceImpl getDelegationTarget();
  public boolean isSystemSynthetic();
  public void setSystemSynthetic(boolean);
  protected void doClose();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public void resetDeviceConfigurationForOpMode();
  public int getVersion();
  public com.qualcomm.robotcore.eventloop.SyncdDevice.ShutdownReason getShutdownReason();
  protected boolean hasShutdownAbnormally();
  public void setOwner(com.qualcomm.robotcore.hardware.usb.RobotUsbModule);
  public com.qualcomm.robotcore.hardware.usb.RobotUsbModule getOwner();
  public synchronized void engage();
  public synchronized void disengage();
  public synchronized boolean isEngaged();
  protected void doPretend();
  protected void armDevice(com.qualcomm.robotcore.hardware.usb.RobotUsbDevice) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void disarmDevice() throws java.lang.InterruptedException;
  protected void doCloseFromArmed() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void doCloseFromOther() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  protected void closeModules();
  public void failSafe();
  protected java.util.Collection<com.qualcomm.hardware.lynx.LynxModule> getKnownModules();
  protected com.qualcomm.hardware.lynx.LynxModule findKnownModule(int);
  public java.util.List<java.lang.String> getAllModuleFirmwareVersions();
  public void changeModuleAddress(com.qualcomm.hardware.lynx.LynxModule, int, java.lang.Runnable);
  public void noteMissingModule(int, java.lang.String);
  protected java.lang.String composeGlobalWarning();
  public com.qualcomm.hardware.lynx.LynxModule getOrAddModule(com.qualcomm.robotcore.hardware.LynxModuleDescription) throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException;
  public void removeConfiguredModule(com.qualcomm.hardware.lynx.LynxModule);
  public void performSystemOperationOnParentModule(int, org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  public void performSystemOperationOnConnectedModule(int, int, org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  protected void internalPerformSysOp(com.qualcomm.hardware.lynx.LynxModule, com.qualcomm.hardware.lynx.LynxModule, org.firstinspires.ftc.robotcore.external.Consumer<com.qualcomm.hardware.lynx.LynxModule>, int, java.util.concurrent.TimeUnit) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException, java.util.concurrent.TimeoutException;
  protected void internalCloseLynxModuleIfUnused(com.qualcomm.hardware.lynx.LynxModule);
  public com.qualcomm.hardware.lynx.LynxUsbDevice.SystemOperationHandle keepConnectedModuleAliveForSystemOperations(int, int) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public com.qualcomm.robotcore.hardware.LynxModuleMetaList discoverModules(boolean) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public boolean setupControlHubEmbeddedModule() throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException;
  protected void onLynxDiscoveryResponseReceived(com.qualcomm.hardware.lynx.commands.LynxDatagram);
  protected void pingAndQueryKnownInterfaces() throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public void lockNetworkLockAcquisitions();
  public void setThrowOnNetworkLockAcquisition(boolean);
  protected void resetNetworkTransmissionLock() throws java.lang.InterruptedException;
  public void acquireNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void releaseNetworkTransmissionLock(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  protected void startPollingForIncomingDatagrams();
  protected boolean stopPollingForIncomingDatagrams();
  protected void startRegularPinging();
  public void transmit(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  protected void shutdownAbnormally();
  protected void pretendFinishExtantCommands() throws java.lang.InterruptedException;
  protected void abandonUnfinishedCommands();
  protected static com.qualcomm.robotcore.hardware.usb.ftdi.RobotUsbDeviceFtdi accessCBus(com.qualcomm.robotcore.hardware.usb.RobotUsbDevice);
  public static void resetDevice(com.qualcomm.robotcore.hardware.usb.RobotUsbDevice);
  public org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.LynxFirmwareUpdateResp updateFirmware(org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.FWImage, java.lang.String, org.firstinspires.ftc.robotcore.external.Consumer<org.firstinspires.ftc.robotcore.internal.ui.ProgressParameters>);
}
```

## class LynxUsbDeviceImpl.IncomingDatagramPoller

```java
class com.qualcomm.hardware.lynx.LynxUsbDeviceImpl.IncomingDatagramPoller implements java.lang.Runnable {
  public void run();
}
```

## class LynxUsbUtil

```java
public class com.qualcomm.hardware.lynx.LynxUsbUtil {
  public com.qualcomm.hardware.lynx.LynxUsbUtil();
  public static com.qualcomm.robotcore.hardware.usb.RobotUsbDevice openUsbDevice(boolean, com.qualcomm.robotcore.hardware.usb.RobotUsbManager, com.qualcomm.robotcore.util.SerialNumber) throws com.qualcomm.robotcore.exception.RobotCoreException;
  public static <T> T makePlaceholderValue(T);
}
```

## class LynxUsbUtil.Placeholder

```java
public class com.qualcomm.hardware.lynx.LynxUsbUtil.Placeholder<T> {
  public com.qualcomm.hardware.lynx.LynxUsbUtil.Placeholder(java.lang.String, java.lang.String, java.lang.Object...);
  public synchronized void reset();
  public synchronized T log(T);
}
```

## class LynxVoltageSensor

```java
public class com.qualcomm.hardware.lynx.LynxVoltageSensor extends com.qualcomm.hardware.lynx.LynxController implements com.qualcomm.robotcore.hardware.VoltageSensor {
  public static final java.lang.String TAG = "LynxVoltageSensor";
  protected java.lang.String getTag();
  public com.qualcomm.hardware.lynx.LynxVoltageSensor(android.content.Context, com.qualcomm.hardware.lynx.LynxModule) throws com.qualcomm.robotcore.exception.RobotCoreException, java.lang.InterruptedException;
  public java.lang.String getDeviceName();
  public double getVoltage();
}
```

## class MessageKeyedLock

```java
public class com.qualcomm.hardware.lynx.MessageKeyedLock {
  public com.qualcomm.hardware.lynx.MessageKeyedLock(java.lang.String);
  public com.qualcomm.hardware.lynx.MessageKeyedLock(java.lang.String, int);
  public void reset() throws java.lang.InterruptedException;
  public void acquire(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void release(com.qualcomm.hardware.lynx.commands.LynxMessage) throws java.lang.InterruptedException;
  public void lockAcquisitions();
  public void throwOnLockAcquisitions(boolean);
}
```

## interface Supplier

```java
public interface com.qualcomm.hardware.lynx.Supplier<T> {
  public abstract T get() throws java.lang.InterruptedException, com.qualcomm.robotcore.exception.RobotCoreException, com.qualcomm.hardware.lynx.LynxNackException;
}
```
