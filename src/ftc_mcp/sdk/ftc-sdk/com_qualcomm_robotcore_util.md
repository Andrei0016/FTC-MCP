# `com.qualcomm.robotcore.util`

_ftc-sdk 11.1.0 — 53 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class AndroidSerialNumberNotFoundException

```java
public class com.qualcomm.robotcore.util.AndroidSerialNumberNotFoundException extends java.lang.Exception {
  public com.qualcomm.robotcore.util.AndroidSerialNumberNotFoundException();
}
```

## class BatteryChecker

```java
public class com.qualcomm.robotcore.util.BatteryChecker {
  public static final java.lang.String TAG = "BatteryChecker";
  protected final java.util.concurrent.ScheduledExecutorService scheduler;
  protected volatile boolean closed;
  protected final com.qualcomm.robotcore.util.BatteryChecker.Monitor monitor;
  protected static final boolean debugBattery = false;
  protected static final int BATTERY_WARN_THRESHOLD = 30;
  public com.qualcomm.robotcore.util.BatteryChecker(com.qualcomm.robotcore.util.BatteryChecker.BatteryWatcher, long);
  public synchronized void startBatteryMonitoring();
  public synchronized void close();
  public void pollBatteryLevel(com.qualcomm.robotcore.util.BatteryChecker.BatteryWatcher);
  protected android.content.Intent registerReceiver(android.content.BroadcastReceiver);
  protected void processBatteryChanged(android.content.Intent);
  protected void logBatteryInfo(int, boolean);
}
```

## class BatteryChecker.BatteryStatus

```java
public class com.qualcomm.robotcore.util.BatteryChecker.BatteryStatus {
  public double percent;
  public boolean isCharging;
  public com.qualcomm.robotcore.util.BatteryChecker.BatteryStatus(double, boolean);
  protected com.qualcomm.robotcore.util.BatteryChecker.BatteryStatus();
  public java.lang.String serialize();
  public static com.qualcomm.robotcore.util.BatteryChecker.BatteryStatus deserialize(java.lang.String);
}
```

## interface BatteryChecker.BatteryWatcher

```java
public interface com.qualcomm.robotcore.util.BatteryChecker.BatteryWatcher {
  public abstract void updateBatteryStatus(com.qualcomm.robotcore.util.BatteryChecker.BatteryStatus);
}
```

## class BatteryChecker.Monitor

```java
public class com.qualcomm.robotcore.util.BatteryChecker.Monitor extends android.content.BroadcastReceiver {
  protected com.qualcomm.robotcore.util.BatteryChecker.Monitor(com.qualcomm.robotcore.util.BatteryChecker);
  public void onReceive(android.content.Context, android.content.Intent);
}
```

## class ClassUtil

```java
public class com.qualcomm.robotcore.util.ClassUtil {
  public static final java.lang.String TAG;
  public com.qualcomm.robotcore.util.ClassUtil();
  public static java.util.List<java.lang.reflect.Constructor> getDeclaredConstructors(java.lang.Class<?>);
  public static boolean inheritsFrom(java.lang.Class, java.lang.Class);
  public static java.lang.reflect.Method getDeclaredMethod(java.lang.Class, java.lang.String, java.lang.Class<?>...);
  public static java.util.List<java.lang.reflect.Method> getAllDeclaredMethods(java.lang.Class);
  public static java.util.List<java.lang.reflect.Method> getLocalDeclaredMethods(java.lang.Class<?>);
  public static java.lang.reflect.Field getDeclaredField(java.lang.Class, java.lang.String);
  public static java.util.List<java.lang.reflect.Field> getAllDeclaredFields(java.lang.Class);
  public static java.util.List<java.lang.reflect.Field> getLocalDeclaredFields(java.lang.Class<?>);
  public static java.lang.Object invoke(java.lang.Object, java.lang.reflect.Method, java.lang.Object...);
  public static boolean searchInheritance(java.lang.Class, org.firstinspires.ftc.robotcore.external.Predicate<java.lang.Class<?>>);
  public static int getStringResId(java.lang.String, java.lang.Class<?>);
  public static java.lang.String decodeStringRes(java.lang.String);
  protected static java.lang.Class findClass(java.lang.String);
  public static long memoryAddressFrom(java.nio.MappedByteBuffer);
}
```

## class ClassUtil.MappedByteBufferInfo

```java
public class com.qualcomm.robotcore.util.ClassUtil.MappedByteBufferInfo {
  public static java.lang.reflect.Field blockField;
  public static java.lang.reflect.Field addressField;
  protected com.qualcomm.robotcore.util.ClassUtil.MappedByteBufferInfo();
}
```

## class ClockWarningSource

```java
public class com.qualcomm.robotcore.util.ClockWarningSource implements com.qualcomm.robotcore.util.GlobalWarningSource,org.firstinspires.ftc.robotcore.internal.network.PeerStatusCallback,android.content.SharedPreferences.OnSharedPreferenceChangeListener {
  public static com.qualcomm.robotcore.util.ClockWarningSource getInstance();
  public void onPossibleRcClockUpdate();
  public void onDsHeartbeatReceived(com.qualcomm.robotcore.robocol.Heartbeat);
  public java.lang.String getGlobalWarning();
  public boolean shouldTriggerWarningSound();
  public void onSharedPreferenceChanged(android.content.SharedPreferences, java.lang.String);
  public void onPeerDisconnected();
  public void suppressGlobalWarning(boolean);
  public void setGlobalWarning(java.lang.String);
  public void clearGlobalWarning();
  public void onPeerConnected();
}
```

## class Device

```java
public final class com.qualcomm.robotcore.util.Device {
  public static final java.lang.String TAG = "Device";
  public static final java.lang.String MANUFACTURER_REV = "REV Robotics";
  public static final java.lang.String MANUFACTURER_MOTOROLA = "motorola";
  public static final java.lang.String MODEL_E5_PLAY = "moto e5 play";
  public static final java.lang.String MODEL_E5_XT1920DL = "moto e5 (XT1920DL)";
  public static final java.lang.String MODEL_E4 = "Moto E (4)";
  public com.qualcomm.robotcore.util.Device();
  public static com.qualcomm.robotcore.util.Device.LinuxKernelVersion getLinuxKernelVersion();
  public static boolean isMotorola();
  public static boolean isRevDriverHub();
  public static boolean deviceHasBackButton();
  public static boolean phoneImplementsAggressiveWifiScanning();
  public static boolean wifiP2pRemoteChannelChangeWorks();
  public static boolean isRevControlHub();
  public static java.lang.String getSerialNumber() throws com.qualcomm.robotcore.util.AndroidSerialNumberNotFoundException;
  public static java.lang.String getSerialNumberOrUnknown();
}
```

## class Device.LinuxKernelVersion

```java
public class com.qualcomm.robotcore.util.Device.LinuxKernelVersion {
  public final int major;
  public final int minor;
  public final int patch;
  public java.lang.String toString();
}
```

## class DifferentialControlLoopCoefficients

```java
public class com.qualcomm.robotcore.util.DifferentialControlLoopCoefficients {
  public double p;
  public double i;
  public double d;
  public com.qualcomm.robotcore.util.DifferentialControlLoopCoefficients();
  public com.qualcomm.robotcore.util.DifferentialControlLoopCoefficients(double, double, double);
}
```

## class Dimmer

```java
public class com.qualcomm.robotcore.util.Dimmer {
  public static final int DEFAULT_DIM_TIME = 30000;
  public static final int LONG_BRIGHT_TIME = 60000;
  public static final float MAXIMUM_BRIGHTNESS = 1.0f;
  public static final float MINIMUM_BRIGHTNESS = 0.05f;
  public com.qualcomm.robotcore.util.Dimmer(android.app.Activity);
  public com.qualcomm.robotcore.util.Dimmer(long, android.app.Activity);
  public void handleDimTimer();
  public void longBright();
}
```

## class ElapsedTime

```java
public class com.qualcomm.robotcore.util.ElapsedTime {
  public static final long SECOND_IN_NANO = 1000000000l;
  public static final long MILLIS_IN_NANO = 1000000l;
  protected volatile long nsStartTime;
  protected final double resolution;
  public com.qualcomm.robotcore.util.ElapsedTime();
  public com.qualcomm.robotcore.util.ElapsedTime(long);
  public com.qualcomm.robotcore.util.ElapsedTime(com.qualcomm.robotcore.util.ElapsedTime.Resolution);
  protected long nsNow();
  public long now(java.util.concurrent.TimeUnit);
  public void reset();
  public double startTime();
  public long startTimeNanoseconds();
  public double time();
  public long time(java.util.concurrent.TimeUnit);
  public double seconds();
  public double milliseconds();
  public long nanoseconds();
  public com.qualcomm.robotcore.util.ElapsedTime.Resolution getResolution();
  public void log(java.lang.String);
  public java.lang.String toString();
}
```

## class ElapsedTime.Resolution

```java
public final class com.qualcomm.robotcore.util.ElapsedTime.Resolution extends java.lang.Enum<com.qualcomm.robotcore.util.ElapsedTime.Resolution> {
  public static final com.qualcomm.robotcore.util.ElapsedTime.Resolution SECONDS;
  public static final com.qualcomm.robotcore.util.ElapsedTime.Resolution MILLISECONDS;
  public static com.qualcomm.robotcore.util.ElapsedTime.Resolution[] values();
  public static com.qualcomm.robotcore.util.ElapsedTime.Resolution valueOf(java.lang.String);
}
```

## interface GlobalWarningSource

```java
public interface com.qualcomm.robotcore.util.GlobalWarningSource {
  public abstract java.lang.String getGlobalWarning();
  public abstract boolean shouldTriggerWarningSound();
  public abstract void suppressGlobalWarning(boolean);
  public abstract void setGlobalWarning(java.lang.String);
  public abstract void clearGlobalWarning();
}
```

## class ImmersiveMode

```java
public class com.qualcomm.robotcore.util.ImmersiveMode {
  public com.qualcomm.robotcore.util.ImmersiveMode(android.view.View);
  public void hideSystemUI();
}
```

## class IncludedFirmwareFileInfo

```java
public class com.qualcomm.robotcore.util.IncludedFirmwareFileInfo {
  public static final java.lang.String HUMAN_READABLE_FW_VERSION = "1.8.2";
  public static final org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.FWImage FW_IMAGE;
  public com.qualcomm.robotcore.util.IncludedFirmwareFileInfo();
}
```

## class Intents

```java
public final class com.qualcomm.robotcore.util.Intents {
  public static final java.lang.String INTENT_PREFIX = "org.firstinspires.ftc.intent.";
  public static final java.lang.String ACTION_FTC_AP_NAME_CHANGE = "org.firstinspires.ftc.intent.action.FTC_AP_NAME_CHANGE";
  public static final java.lang.String ACTION_FTC_AP_PASSWORD_CHANGE = "org.firstinspires.ftc.intent.action.FTC_AP_PASSWORD_CHANGE";
  public static final java.lang.String ACTION_FTC_AP_CHANNEL_CHANGE = "org.firstinspires.ftc.intent.action.FTC_AP_CHANNEL_CHANGE";
  public static final java.lang.String ACTION_FTC_AP_SETTINGS_CHANGE = "org.firstinspires.ftc.intent.action.FTC_AP_SETTINGS_CHANGE";
  public static final java.lang.String ACTION_FTC_WIFI_FACTORY_RESET = "org.firstinspires.ftc.intent.action.FTC_FACTORY_RESET";
  public static final java.lang.String ACTION_FTC_AP_GET_CURRENT_CHANNEL_INFO = "org.firstinspires.ftc.intent.action.FTC_AP_GET_CURRENT_CHANNEL_INFO";
  public static final java.lang.String ACTION_FTC_AP_NOTIFY_BAND_CHANGE = "org.firstinspires.ftc.intent.action.FTC_AP_NOTIFY_BAND_CHANGE";
  public static final java.lang.String ACTION_FTC_NOTIFY_RC_ALIVE = "org.firstinspires.ftc.intent.action.FTC_NOTIFY_RC_ALIVE";
  public static final java.lang.String EXTRA_AP_PREF = "org.firstinspires.ftc.intent.extra.EXTRA_AP_PREF";
  public static final java.lang.String EXTRA_RC_ALIVE_NOTIFICATION_TIMEOUT_SECONDS = "org.firstinspires.ftc.intent.extra.EXTRA_RC_ALIVE_NOTIFICATION_TIMEOUT_SECONDS";
  public static final java.lang.String EXTRA_AP_NAME = "org.firstinspires.ftc.intent.extra.EXTRA_AP_NAME";
  public static final java.lang.String EXTRA_AP_PASSWORD = "org.firstinspires.ftc.intent.extra.EXTRA_AP_PASSWORD";
  public static final java.lang.String EXTRA_AP_CHANNEL = "org.firstinspires.ftc.intent.extra.EXTRA_AP_CHANNEL";
  public static final java.lang.String EXTRA_AP_BAND = "org.firstinspires.ftc.intent.extra.EXTRA_AP_BAND";
  public static final java.lang.String EXTRA_RESULT_RECEIVER = "org.firstinspires.ftc.intent.extra.RESULT_RECEIVER";
  public static final java.lang.String BUNDLE_KEY_CURRENT_BAND = "current_band";
  public static final java.lang.String BUNDLE_KEY_CURRENT_CHANNEL = "current_channel";
  public static final java.lang.String ANDROID_ACTION_WIFI_AP_STATE_CHANGED = "android.net.wifi.WIFI_AP_STATE_CHANGED";
  public com.qualcomm.robotcore.util.Intents();
}
```

## class LastKnown

```java
public class com.qualcomm.robotcore.util.LastKnown<T> {
  protected T value;
  protected boolean isValid;
  protected com.qualcomm.robotcore.util.ElapsedTime timer;
  protected double msFreshness;
  public com.qualcomm.robotcore.util.LastKnown();
  public com.qualcomm.robotcore.util.LastKnown(double);
  public static <X> com.qualcomm.robotcore.util.LastKnown<X>[] createArray(int);
  public static <X> void invalidateArray(com.qualcomm.robotcore.util.LastKnown<X>[]);
  public void invalidate();
  public boolean isValid();
  public T getValue();
  public T getNonTimedValue();
  public T getRawValue();
  public T setValue(T);
  public boolean isValue(T);
  public boolean updateValue(T);
}
```

## class MovingStatistics

```java
public class com.qualcomm.robotcore.util.MovingStatistics {
  public com.qualcomm.robotcore.util.MovingStatistics(int);
  public int getCount();
  public double getMean();
  public double getVariance();
  public double getStandardDeviation();
  public void clear();
  public void add(double);
}
```

## class Network

```java
public class com.qualcomm.robotcore.util.Network {
  public com.qualcomm.robotcore.util.Network();
  public static java.net.InetAddress getLoopbackAddress();
  public static java.util.ArrayList<java.net.InetAddress> getLocalIpAddresses();
  public static java.util.ArrayList<java.net.InetAddress> getLocalIpAddress(java.lang.String);
  public static java.util.ArrayList<java.net.InetAddress> removeIPv6Addresses(java.util.Collection<java.net.InetAddress>);
  public static java.util.ArrayList<java.net.InetAddress> removeIPv4Addresses(java.util.Collection<java.net.InetAddress>);
  public static java.util.ArrayList<java.net.InetAddress> removeLoopbackAddresses(java.util.Collection<java.net.InetAddress>);
  public static java.util.ArrayList<java.lang.String> getHostAddresses(java.util.Collection<java.net.InetAddress>);
}
```

## class NextLock

```java
public class com.qualcomm.robotcore.util.NextLock {
  protected final java.lang.Object lock;
  protected long count;
  public com.qualcomm.robotcore.util.NextLock();
  public com.qualcomm.robotcore.util.NextLock.Waiter getNextWaiter();
  public void advanceNext();
}
```

## class NextLock.Waiter

```java
public class com.qualcomm.robotcore.util.NextLock.Waiter {
  public void awaitNext() throws java.lang.InterruptedException;
}
```

## class Range

```java
public class com.qualcomm.robotcore.util.Range {
  public static double scale(double, double, double, double, double);
  public static double clip(double, double, double);
  public static float clip(float, float, float);
  public static int clip(int, int, int);
  public static short clip(short, short, short);
  public static byte clip(byte, byte, byte);
  public static void throwIfRangeIsInvalid(double, double, double) throws java.lang.IllegalArgumentException;
  public static void throwIfRangeIsInvalid(int, int, int) throws java.lang.IllegalArgumentException;
}
```

## class ReadWriteFile

```java
public class com.qualcomm.robotcore.util.ReadWriteFile {
  public static final java.lang.String TAG = "ReadWriteFile";
  protected static java.nio.charset.Charset charset;
  public com.qualcomm.robotcore.util.ReadWriteFile();
  public static java.lang.String readFileOrThrow(java.io.File) throws java.io.IOException;
  public static java.lang.String readFile(java.io.File);
  public static byte[] readBytes(org.firstinspires.ftc.robotcore.internal.network.RobotCoreCommandList.FWImage);
  public static byte[] readAssetBytes(java.io.File);
  public static byte[] readFileBytes(java.io.File);
  public static byte[] readAssetBytesOrThrow(java.io.File) throws java.io.IOException;
  public static byte[] readRawResourceBytesOrThrow(int) throws java.io.IOException;
  public static byte[] readFileBytesOrThrow(java.io.File) throws java.io.IOException;
  protected static byte[] readBytesOrThrow(int, java.io.InputStream) throws java.io.IOException;
  public static void writeFile(java.io.File, java.lang.String);
  public static void writeFileOrThrow(java.io.File, java.lang.String) throws java.io.IOException;
  public static void writeFileOrThrow(java.io.File, java.lang.String, java.lang.String) throws java.io.IOException;
  public static void writeFile(java.io.File, java.lang.String, java.lang.String);
  public static void ensureAllChangesAreCommitted(java.io.File);
  public static void ensureChangesAreCommitted(java.io.File);
  public static void updateFileRequiringCommit(java.io.File, java.lang.String);
}
```

## class RobotLog

```java
public class com.qualcomm.robotcore.util.RobotLog {
  public static final java.lang.String OPMODE_START_TAG = "******************** START - OPMODE %s ********************";
  public static final java.lang.String OPMODE_STOP_TAG = "******************** STOP - OPMODE %s ********************";
  public static final java.lang.String TAG = "RobotCore";
  public static void processTimeSynch(long, long, long, long);
  public static void setMsTimeOffset(double);
  public static long getRemoteTime();
  public static long getRemoteTime(long);
  public static long getLocalTime(long);
  public static void a(java.lang.String, java.lang.Object...);
  public static void a(java.lang.String);
  public static void aa(java.lang.String, java.lang.String, java.lang.Object...);
  public static void aa(java.lang.String, java.lang.String);
  public static void aa(java.lang.String, java.lang.Throwable, java.lang.String, java.lang.Object...);
  public static void aa(java.lang.String, java.lang.Throwable, java.lang.String);
  public static void v(java.lang.String, java.lang.Object...);
  public static void v(java.lang.String);
  public static void vv(java.lang.String, java.lang.String, java.lang.Object...);
  public static void vv(java.lang.String, java.lang.String);
  public static void vv(java.lang.String, java.lang.Throwable, java.lang.String, java.lang.Object...);
  public static void vv(java.lang.String, java.lang.Throwable, java.lang.String);
  public static void d(java.lang.String, java.lang.Object...);
  public static void d(java.lang.String);
  public static void dd(java.lang.String, java.lang.String, java.lang.Object...);
  public static void dd(java.lang.String, java.lang.String);
  public static void dd(java.lang.String, java.lang.Throwable, java.lang.String, java.lang.Object...);
  public static void dd(java.lang.String, java.lang.Throwable, java.lang.String);
  public static void i(java.lang.String, java.lang.Object...);
  public static void i(java.lang.String);
  public static void ii(java.lang.String, java.lang.String, java.lang.Object...);
  public static void ii(java.lang.String, java.lang.String);
  public static void ii(java.lang.String, java.lang.Throwable, java.lang.String, java.lang.Object...);
  public static void ii(java.lang.String, java.lang.Throwable, java.lang.String);
  public static void w(java.lang.String, java.lang.Object...);
  public static void w(java.lang.String);
  public static void ww(java.lang.String, java.lang.String, java.lang.Object...);
  public static void ww(java.lang.String, java.lang.String);
  public static void ww(java.lang.String, java.lang.Throwable, java.lang.String, java.lang.Object...);
  public static void ww(java.lang.String, java.lang.Throwable, java.lang.String);
  public static void e(java.lang.String, java.lang.Object...);
  public static void e(java.lang.String);
  public static void ee(java.lang.String, java.lang.String, java.lang.Object...);
  public static void ee(java.lang.String, java.lang.String);
  public static void ee(java.lang.String, java.lang.Throwable, java.lang.String, java.lang.Object...);
  public static void ee(java.lang.String, java.lang.Throwable, java.lang.String);
  public static void internalLog(int, java.lang.String, java.lang.String);
  public static void internalLog(int, java.lang.String, java.lang.Throwable, java.lang.String);
  public static void logExceptionHeader(java.lang.Exception, java.lang.String, java.lang.Object...);
  public static void logExceptionHeader(java.lang.String, java.lang.Exception, java.lang.String, java.lang.Object...);
  public static void logStacktrace(java.lang.Throwable);
  public static void logStackTrace(java.lang.Throwable);
  public static void logStackTrace(java.lang.Thread, java.lang.String, java.lang.Object...);
  public static void logStackTrace(java.lang.Thread, java.lang.StackTraceElement[]);
  public static void logStackTrace(java.lang.String, java.lang.Throwable);
  public static void logAndThrow(java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException;
  public static boolean setGlobalErrorMsg(java.lang.String);
  public static void setGlobalErrorMsg(java.lang.String, java.lang.Object...);
  public static void addGlobalWarningMessage(java.lang.String);
  public static void addGlobalWarningMessage(java.lang.String, java.lang.Object...);
  public static void registerGlobalWarningSource(com.qualcomm.robotcore.util.GlobalWarningSource);
  public static void unregisterGlobalWarningSource(com.qualcomm.robotcore.util.GlobalWarningSource);
  public static void setGlobalErrorMsg(com.qualcomm.robotcore.exception.RobotCoreException, java.lang.String);
  public static void setGlobalErrorMsgAndThrow(com.qualcomm.robotcore.exception.RobotCoreException, java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException;
  public static void setGlobalErrorMsg(java.lang.RuntimeException, java.lang.String);
  public static void setGlobalErrorMsgAndThrow(java.lang.RuntimeException, java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException;
  public static java.lang.String getGlobalErrorMsg();
  public static void setGlobalErrorMsgSticky(boolean);
  public static com.qualcomm.robotcore.util.RobotLog.GlobalWarningMessage getGlobalWarningMessage();
  public static void setGlobalWarningMsgSticky(boolean);
  public static java.lang.String combineGlobalWarnings(java.util.List<java.lang.String>);
  public static boolean hasGlobalErrorMsg();
  public static boolean hasGlobalWarningMsg();
  public static void clearGlobalErrorMsg();
  public static void clearGlobalWarningMsg();
  public static void onApplicationStart();
  protected static synchronized void writeLogcatToDisk(android.content.Context, int);
  public static void startMatchLogging(android.content.Context, java.lang.String, int) throws com.qualcomm.robotcore.exception.RobotCoreException;
  public static synchronized void stopMatchLogging();
  public static java.lang.String getLogFilename();
  public static java.lang.String getLogFilename(android.content.Context);
  protected static void pruneMatchLogsIfNecessary();
  public static java.lang.String getMatchLogFilename(android.content.Context, java.lang.String, int);
  public static java.util.List<java.io.File> getExtantLogFiles(android.content.Context);
  public static synchronized void cancelWriteLogcatToDisk();
  public static void logAppInfo();
  public static void logDeviceInfo();
  public static void logBytes(java.lang.String, java.lang.String, byte[], int);
  public static void logBytes(java.lang.String, java.lang.String, byte[], int, int);
}
```

## class RobotLog.GlobalWarningMessage

```java
public class com.qualcomm.robotcore.util.RobotLog.GlobalWarningMessage {
  public final java.lang.String message;
  public final boolean deservesWarningSound;
  public com.qualcomm.robotcore.util.RobotLog.GlobalWarningMessage(java.lang.String, boolean);
}
```

## class RobotLog.LoggingThread

```java
public class com.qualcomm.robotcore.util.RobotLog.LoggingThread extends java.lang.Thread {
  public void run(java.lang.String);
  public void kill();
}
```

## class RollingAverage

```java
public class com.qualcomm.robotcore.util.RollingAverage {
  public static final int DEFAULT_SIZE = 100;
  public com.qualcomm.robotcore.util.RollingAverage();
  public com.qualcomm.robotcore.util.RollingAverage(int);
  public int size();
  public void resize(int);
  public void addNumber(int);
  public int getAverage();
  public void reset();
}
```

## class RunShellCommand

```java
public class com.qualcomm.robotcore.util.RunShellCommand {
  public com.qualcomm.robotcore.util.RunShellCommand();
  public void enableLogging(boolean);
  public com.qualcomm.robotcore.util.RunShellCommand.ProcessResult run(java.lang.String);
  public com.qualcomm.robotcore.util.RunShellCommand.ProcessResult runAsRoot(java.lang.String);
  public void commitSeppuku();
  public static void killSpawnedProcess(java.lang.String, java.lang.String) throws com.qualcomm.robotcore.exception.RobotCoreException;
  public static int getSpawnedProcessPid(java.lang.String, java.lang.String);
}
```

## class RunShellCommand.ProcessResult

```java
public final class com.qualcomm.robotcore.util.RunShellCommand.ProcessResult {
  public int getReturnCode();
  public java.lang.String getOutput();
  public boolean equals(java.lang.Object);
  public int hashCode();
}
```

## class SerialNumber

```java
public abstract class com.qualcomm.robotcore.util.SerialNumber implements java.io.Serializable {
  protected static final java.lang.String fakePrefix = "FakeUSB:";
  protected static final java.lang.String vendorProductPrefix = "VendorProduct:";
  protected static final java.lang.String lynxModulePrefix = "ExpHub:";
  protected static final java.lang.String embedded = "(embedded)";
  protected static final java.lang.String ethernetOverUsbPrefix = "EthernetOverUsb:";
  protected final java.lang.String serialNumberString;
  protected static final java.util.HashMap<java.lang.String, java.lang.String> deviceDisplayNames;
  protected com.qualcomm.robotcore.util.SerialNumber(java.lang.String);
  public static com.qualcomm.robotcore.util.SerialNumber createFake();
  public static com.qualcomm.robotcore.util.SerialNumber createEmbedded();
  public static com.qualcomm.robotcore.util.SerialNumber fromString(java.lang.String);
  public static com.qualcomm.robotcore.util.SerialNumber fromStringOrNull(java.lang.String);
  public static com.qualcomm.robotcore.util.SerialNumber fromUsbOrNull(java.lang.String);
  public static com.qualcomm.robotcore.util.SerialNumber fromVidPid(int, int, java.lang.String);
  public boolean isVendorProduct();
  public boolean isFake();
  public boolean isUsb();
  public boolean isEmbedded();
  public java.lang.String getString();
  public com.qualcomm.robotcore.util.SerialNumber getScannableDeviceSerialNumber();
  public boolean matches(java.lang.Object);
  public boolean equals(java.lang.Object);
  public boolean equals(java.lang.String);
  public int hashCode();
  public static void noteSerialNumberType(com.qualcomm.robotcore.util.SerialNumber, java.lang.String);
  public static java.lang.String getDeviceDisplayName(com.qualcomm.robotcore.util.SerialNumber);
}
```

## class SerialNumber.GsonTypeAdapter

```java
class com.qualcomm.robotcore.util.SerialNumber.GsonTypeAdapter extends com.google.gson.TypeAdapter<com.qualcomm.robotcore.util.SerialNumber> {
  public void write(com.google.gson.stream.JsonWriter, com.qualcomm.robotcore.util.SerialNumber) throws java.io.IOException;
  public com.qualcomm.robotcore.util.SerialNumber read(com.google.gson.stream.JsonReader) throws java.io.IOException;
  public java.lang.Object read(com.google.gson.stream.JsonReader) throws java.io.IOException;
  public void write(com.google.gson.stream.JsonWriter, java.lang.Object) throws java.io.IOException;
}
```

## class ShortHash

```java
public class com.qualcomm.robotcore.util.ShortHash {
  public static final long MAX_NUMBER = 9007199254740992l;
  public com.qualcomm.robotcore.util.ShortHash();
  public com.qualcomm.robotcore.util.ShortHash(java.lang.String);
  public com.qualcomm.robotcore.util.ShortHash(java.lang.String, int);
  public com.qualcomm.robotcore.util.ShortHash(java.lang.String, int, java.lang.String);
  public java.lang.String encode(long);
  public int getAlphabetLength();
  public java.lang.String getVersion();
}
```

## class SoftwareVersionWarningSource

```java
public class com.qualcomm.robotcore.util.SoftwareVersionWarningSource implements com.qualcomm.robotcore.util.GlobalWarningSource,org.firstinspires.ftc.robotcore.internal.network.PeerStatusCallback,android.content.SharedPreferences.OnSharedPreferenceChangeListener {
  public static com.qualcomm.robotcore.util.SoftwareVersionWarningSource getInstance();
  public void onReceivedPeerDiscoveryFromCurrentPeer(com.qualcomm.robotcore.robocol.PeerDiscovery);
  public void onReceivedDriverHubOsVersionCode(int);
  public java.lang.String getGlobalWarning();
  public boolean shouldTriggerWarningSound();
  public void onPeerDisconnected();
  public void onSharedPreferenceChanged(android.content.SharedPreferences, java.lang.String);
  public void suppressGlobalWarning(boolean);
  public void setGlobalWarning(java.lang.String);
  public void clearGlobalWarning();
  public void onPeerConnected();
}
```

## class SoftwareVersionWarningSource.MismatchedAppsDetail

```java
class com.qualcomm.robotcore.util.SoftwareVersionWarningSource.MismatchedAppsDetail {
}
```

## class SortOrder

```java
public final class com.qualcomm.robotcore.util.SortOrder extends java.lang.Enum<com.qualcomm.robotcore.util.SortOrder> {
  public static final com.qualcomm.robotcore.util.SortOrder ASCENDING;
  public static final com.qualcomm.robotcore.util.SortOrder DESCENDING;
  public static com.qualcomm.robotcore.util.SortOrder[] values();
  public static com.qualcomm.robotcore.util.SortOrder valueOf(java.lang.String);
}
```

## class Statistics

```java
public class com.qualcomm.robotcore.util.Statistics {
  public com.qualcomm.robotcore.util.Statistics();
  public int getCount();
  public double getMean();
  public double getVariance();
  public double getStandardDeviation();
  public void clear();
  public void add(double);
  public void remove(double);
}
```

## class ThreadPool

```java
public class com.qualcomm.robotcore.util.ThreadPool {
  public static final java.lang.String TAG = "ThreadPool";
  public com.qualcomm.robotcore.util.ThreadPool();
  public static java.util.concurrent.ExecutorService getDefault();
  public static java.util.concurrent.ExecutorService getDefaultSerial();
  public static java.util.concurrent.ScheduledExecutorService getDefaultScheduler();
  public static java.util.concurrent.ExecutorService newSingleThreadExecutor(java.lang.String);
  public static java.util.concurrent.ExecutorService newFixedThreadPool(int, java.lang.String);
  public static java.util.concurrent.ExecutorService newCachedThreadPool(java.lang.String);
  public static com.qualcomm.robotcore.util.ThreadPool.RecordingScheduledExecutor newScheduledExecutor(int, java.lang.String);
  public static int getTID(java.lang.Thread);
  public static int getTID(long);
  public static boolean awaitTermination(java.util.concurrent.ExecutorService, long, java.util.concurrent.TimeUnit, java.lang.String) throws java.lang.InterruptedException;
  public static void awaitTerminationOrExitApplication(java.util.concurrent.ExecutorService, long, java.util.concurrent.TimeUnit, java.lang.String, java.lang.String);
  public static boolean awaitFuture(java.util.concurrent.Future, long, java.util.concurrent.TimeUnit);
  public static void cancelFutureOrExitApplication(java.util.concurrent.Future, long, java.util.concurrent.TimeUnit, java.lang.String, java.lang.String);
  public static void exitApplication(java.lang.String, java.lang.String);
  public static void logThreadLifeCycle(java.lang.String, java.lang.Runnable);
  protected static java.lang.Throwable retrieveUserException(java.lang.Runnable, java.lang.Throwable);
}
```

## interface ThreadPool.ContainerOfThreads

```java
public interface com.qualcomm.robotcore.util.ThreadPool.ContainerOfThreads extends java.lang.Iterable<java.lang.Thread> {
  public abstract void setNameRootForThreads(java.lang.String);
  public abstract void setPriorityForThreads(java.lang.Integer);
  public abstract void noteNewThread(java.lang.Thread);
  public abstract void noteFinishedThread(java.lang.Thread);
}
```

## class ThreadPool.ContainerOfThreadsRecorder

```java
class com.qualcomm.robotcore.util.ThreadPool.ContainerOfThreadsRecorder implements com.qualcomm.robotcore.util.ThreadPool.ContainerOfThreads {
  public void setNameRootForThreads(java.lang.String);
  public void setPriorityForThreads(java.lang.Integer);
  public void noteNewThread(java.lang.Thread);
  public void noteFinishedThread(java.lang.Thread);
  protected void logThread(java.lang.Thread, java.lang.String);
  public java.util.Iterator<java.lang.Thread> iterator();
}
```

## class ThreadPool.RecordingScheduledExecutor

```java
public class com.qualcomm.robotcore.util.ThreadPool.RecordingScheduledExecutor extends com.qualcomm.robotcore.util.ThreadPool.ContainerOfThreadsRecorder implements java.util.concurrent.ScheduledExecutorService {
  protected java.util.concurrent.ScheduledThreadPoolExecutor executor;
  public void setKeepAliveTime(long, java.util.concurrent.TimeUnit);
  public void allowCoreThreadTimeOut(boolean);
  public void execute(java.lang.Runnable);
  public void shutdown();
  public java.util.List<java.lang.Runnable> shutdownNow();
  public boolean isShutdown();
  public boolean isTerminated();
  public boolean awaitTermination(long, java.util.concurrent.TimeUnit) throws java.lang.InterruptedException;
  public <T> java.util.concurrent.Future<T> submit(java.util.concurrent.Callable<T>);
  public <T> java.util.concurrent.Future<T> submit(java.lang.Runnable, T);
  public java.util.concurrent.Future<?> submit(java.lang.Runnable);
  public <T> java.util.List<java.util.concurrent.Future<T>> invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException;
  public <T> java.util.List<java.util.concurrent.Future<T>> invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>, long, java.util.concurrent.TimeUnit) throws java.lang.InterruptedException;
  public <T> T invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException, java.util.concurrent.ExecutionException;
  public <T> T invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>, long, java.util.concurrent.TimeUnit) throws java.lang.InterruptedException, java.util.concurrent.ExecutionException, java.util.concurrent.TimeoutException;
  public java.util.concurrent.ScheduledFuture<?> schedule(java.lang.Runnable, long, java.util.concurrent.TimeUnit);
  public <V> java.util.concurrent.ScheduledFuture<V> schedule(java.util.concurrent.Callable<V>, long, java.util.concurrent.TimeUnit);
  public java.util.concurrent.ScheduledFuture<?> scheduleAtFixedRate(java.lang.Runnable, long, long, java.util.concurrent.TimeUnit);
  public java.util.concurrent.ScheduledFuture<?> scheduleWithFixedDelay(java.lang.Runnable, long, long, java.util.concurrent.TimeUnit);
  public java.util.Iterator iterator();
  public void noteFinishedThread(java.lang.Thread);
  public void noteNewThread(java.lang.Thread);
  public void setPriorityForThreads(java.lang.Integer);
  public void setNameRootForThreads(java.lang.String);
}
```

## class ThreadPool.RecordingThreadPool

```java
public class com.qualcomm.robotcore.util.ThreadPool.RecordingThreadPool extends com.qualcomm.robotcore.util.ThreadPool.ContainerOfThreadsRecorder implements java.util.concurrent.ExecutorService {
  public void execute(java.lang.Runnable);
  public void shutdown();
  public java.util.List<java.lang.Runnable> shutdownNow();
  public boolean isShutdown();
  public boolean isTerminated();
  public boolean awaitTermination(long, java.util.concurrent.TimeUnit) throws java.lang.InterruptedException;
  public <T> java.util.concurrent.Future<T> submit(java.util.concurrent.Callable<T>);
  public <T> java.util.concurrent.Future<T> submit(java.lang.Runnable, T);
  public java.util.concurrent.Future<?> submit(java.lang.Runnable);
  public <T> java.util.List<java.util.concurrent.Future<T>> invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException;
  public <T> java.util.List<java.util.concurrent.Future<T>> invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>, long, java.util.concurrent.TimeUnit) throws java.lang.InterruptedException;
  public <T> T invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException, java.util.concurrent.ExecutionException;
  public <T> T invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>, long, java.util.concurrent.TimeUnit) throws java.lang.InterruptedException, java.util.concurrent.ExecutionException, java.util.concurrent.TimeoutException;
  public java.util.Iterator iterator();
  public void noteFinishedThread(java.lang.Thread);
  public void noteNewThread(java.lang.Thread);
  public void setPriorityForThreads(java.lang.Integer);
  public void setNameRootForThreads(java.lang.String);
}
```

## class ThreadPool.Singleton

```java
public class com.qualcomm.robotcore.util.ThreadPool.Singleton<T> {
  public static int INFINITE_TIMEOUT;
  public com.qualcomm.robotcore.util.ThreadPool.Singleton();
  public void setService(java.util.concurrent.ExecutorService);
  public void reset();
  public com.qualcomm.robotcore.util.ThreadPool.SingletonResult<T> submit(int, java.lang.Runnable);
  public com.qualcomm.robotcore.util.ThreadPool.SingletonResult<T> submit(java.lang.Runnable);
  public com.qualcomm.robotcore.util.ThreadPool.SingletonResult<T> submit(int, java.util.concurrent.Callable<T>);
  public com.qualcomm.robotcore.util.ThreadPool.SingletonResult<T> submit(java.util.concurrent.Callable<T>);
  public com.qualcomm.robotcore.util.ThreadPool.SingletonResult<T> getResult();
  public T await(long) throws java.lang.InterruptedException;
  public T await() throws java.lang.InterruptedException;
}
```

## class ThreadPool.SingletonResult

```java
public class com.qualcomm.robotcore.util.ThreadPool.SingletonResult<T> {
  public com.qualcomm.robotcore.util.ThreadPool.SingletonResult(int, com.qualcomm.robotcore.util.ThreadPool.Singleton<T>, java.util.concurrent.Future<T>);
  public void setFuture(java.util.concurrent.Future<T>);
  public T await(long) throws java.lang.InterruptedException;
  public T await() throws java.lang.InterruptedException;
}
```

## interface ThreadPool.ThreadBorrowable

```java
public interface com.qualcomm.robotcore.util.ThreadPool.ThreadBorrowable {
  public abstract boolean canBorrowThread(java.lang.Thread);
}
```

## class ThreadPool.ThreadFactoryImpl

```java
class com.qualcomm.robotcore.util.ThreadPool.ThreadFactoryImpl implements java.util.concurrent.ThreadFactory {
  public java.lang.Thread newThread(java.lang.Runnable);
}
```

## class TypeConversion

```java
public class com.qualcomm.robotcore.util.TypeConversion {
  public static byte[] shortToByteArray(short);
  public static byte[] shortToByteArray(short, java.nio.ByteOrder);
  public static byte[] intToByteArray(int);
  public static byte[] intToByteArray(int, java.nio.ByteOrder);
  public static byte[] longToByteArray(long);
  public static byte[] longToByteArray(long, java.nio.ByteOrder);
  public static short byteArrayToShort(byte[]);
  public static short byteArrayToShort(byte[], java.nio.ByteOrder);
  public static short byteArrayToShort(byte[], int, java.nio.ByteOrder);
  public static int byteArrayToInt(byte[]);
  public static int byteArrayToInt(byte[], java.nio.ByteOrder);
  public static long byteArrayToLong(byte[]);
  public static long byteArrayToLong(byte[], java.nio.ByteOrder);
  public static int unsignedByteToInt(byte);
  public static int unsignedShortToInt(short);
  public static double unsignedByteToDouble(byte);
  public static long unsignedIntToLong(int);
  public static byte[] stringToUtf8(java.lang.String);
  public static int doubleToFixedInt(double, int);
  public static double doubleFromFixed(int, int);
  public static long doubleToFixedLong(double, int);
  public static double doubleFromFixed(long, int);
  public static java.lang.String utf8ToString(byte[]);
  public static boolean toBoolean(java.lang.Boolean);
  public static boolean toBoolean(java.lang.Boolean, boolean);
}
```

## class Util

```java
public class com.qualcomm.robotcore.util.Util {
  public static java.lang.String ASCII_RECORD_SEPARATOR;
  public static final java.lang.String LOWERCASE_ALPHA_NUM_CHARACTERS = "0123456789qwertyuiopasdfghjklzxcvbnm";
  public com.qualcomm.robotcore.util.Util();
  public static java.lang.String getRandomString(int, java.lang.String);
  public static void sortFilesByName(java.io.File[]);
  public static void updateTextView(android.widget.TextView, java.lang.String);
  public static byte[] concatenateByteArrays(byte[], byte[]);
  public static byte[] concatenateByteArrays(byte[], byte[], byte[]);
  public static boolean isPrefixOf(java.lang.String, java.lang.String);
  public static boolean isGoodString(java.lang.String);
  public static void forEachInFolder(java.io.File, boolean, org.firstinspires.ftc.robotcore.external.Predicate<java.io.File>) throws java.io.FileNotFoundException;
  public static boolean teamNumberMatch(java.lang.String, java.lang.String);
}
```

## class Version

```java
public class com.qualcomm.robotcore.util.Version {
  public static final java.lang.String LIBRARY_VERSION = "developer_build";
  public com.qualcomm.robotcore.util.Version();
  public static java.lang.String getLibraryVersion();
}
```

## class WeakReferenceSet

```java
public class com.qualcomm.robotcore.util.WeakReferenceSet<E> implements java.util.Set<E> {
  public com.qualcomm.robotcore.util.WeakReferenceSet();
  public boolean add(E);
  public boolean remove(java.lang.Object);
  public boolean contains(java.lang.Object);
  public boolean addAll(java.util.Collection<? extends E>);
  public void clear();
  public boolean containsAll(java.util.Collection<?>);
  public boolean isEmpty();
  public int size();
  public java.lang.Object[] toArray();
  public java.util.Iterator<E> iterator();
  public boolean removeAll(java.util.Collection<?>);
  public boolean retainAll(java.util.Collection<?>);
  public java.lang.Object[] toArray(java.lang.Object[]);
}
```

## interface WebHandlerManager

```java
public interface com.qualcomm.robotcore.util.WebHandlerManager {
  public abstract com.qualcomm.robotcore.util.WebServer getWebServer();
  public abstract void register(java.lang.String, org.firstinspires.ftc.robotcore.internal.webserver.WebHandler);
  public abstract org.firstinspires.ftc.robotcore.internal.webserver.WebHandler getRegistered(java.lang.String);
  public abstract void registerObserver(java.lang.String, org.firstinspires.ftc.robotcore.internal.webserver.WebObserver);
}
```

## interface WebServer

```java
public interface com.qualcomm.robotcore.util.WebServer {
  public abstract com.qualcomm.robotcore.util.WebHandlerManager getWebHandlerManager();
  public abstract boolean wasStarted();
  public abstract void start();
  public abstract void stop();
  public abstract org.firstinspires.ftc.robotcore.internal.webserver.RobotControllerWebInfo getConnectionInformation();
  public abstract org.firstinspires.ftc.robotcore.internal.webserver.websockets.WebSocketManager getWebSocketManager();
}
```
