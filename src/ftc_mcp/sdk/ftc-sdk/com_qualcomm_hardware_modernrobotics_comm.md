# `com.qualcomm.hardware.modernrobotics.comm`

_ftc-sdk 11.1.0 — 13 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class ModernRoboticsDatagram

```java
public abstract class com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram {
  public static final int CB_HEADER = 5;
  public static final int IB_SYNC_0 = 0;
  public static final int IB_SYNC_1 = 1;
  public static final int IB_FUNCTION = 2;
  public static final int IB_ADDRESS = 3;
  public static final int IB_LENGTH = 4;
  public byte[] data;
  protected com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram(int);
  protected void initialize(int, int);
  public void clearPayload();
  public int getAllocatedPayload();
  public boolean isRead();
  public boolean isWrite();
  public void setRead(int);
  public void setWrite(int);
  public void setRead();
  public void setWrite();
  public int getFunction();
  public void setFunction(int);
  public int getAddress();
  public void setAddress(int);
  public void setPayload(byte[]);
  public int getPayloadLength();
  public void setPayloadLength(int);
  public boolean isFailure();
}
```

## class ModernRoboticsDatagram.AllocationContext

```java
public class com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<DATAGRAM_TYPE extends com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram> {
  protected java.util.concurrent.atomic.AtomicReference<DATAGRAM_TYPE> cacheHeaderOnly0;
  protected java.util.concurrent.atomic.AtomicReference<DATAGRAM_TYPE> cacheHeaderOnly1;
  protected java.util.concurrent.atomic.AtomicReference<DATAGRAM_TYPE> cachedFullInstance0;
  protected java.util.concurrent.atomic.AtomicReference<DATAGRAM_TYPE> cachedFullInstance1;
  public com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext();
}
```

## class ModernRoboticsReaderWriter

```java
public class com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsReaderWriter {
  public static final java.lang.String TAG = "MRReaderWriter";
  public static boolean DEBUG;
  public static int MS_INTER_BYTE_TIMEOUT;
  public static int MS_USB_HUB_LATENCY;
  public static int MS_REQUEST_RESPONSE_TIMEOUT;
  public static int MS_GARBAGE_COLLECTION_SPURT;
  public static int MS_RESYNCH_TIMEOUT;
  public static int MS_FAILURE_WAIT;
  public static int MS_COMM_ERROR_WAIT;
  public static int MS_MAX_TIMEOUT;
  public static int MAX_SEQUENTIAL_USB_ERROR_COUNT;
  public static final java.lang.String COMM_FAILURE_READ = "comm failure read";
  public static final java.lang.String COMM_FAILURE_WRITE = "comm failure write";
  public static final java.lang.String COMM_TIMEOUT_READ = "comm timeout awaiting response (read)";
  public static final java.lang.String COMM_TIMEOUT_WRITE = "comm timeout awaiting response (write)";
  public static final java.lang.String COMM_ERROR_READ = "comm error read";
  public static final java.lang.String COMM_ERROR_WRITE = "comm error write";
  public static final java.lang.String COMM_SYNC_LOST = "comm sync lost";
  public static final java.lang.String COMM_PAYLOAD_ERROR_READ = "comm payload error read";
  public static final java.lang.String COMM_PAYLOAD_ERROR_WRITE = "comm payload error write";
  public static final java.lang.String COMM_TYPE_ERROR_READ = "comm type error read";
  public static final java.lang.String COMM_TYPE_ERROR_WRITE = "comm type error write";
  protected final com.qualcomm.robotcore.hardware.usb.RobotUsbDevice device;
  protected int usbSequentialCommReadErrorCount;
  protected int usbSequentialCommWriteErrorCount;
  protected int usbReadRetryCount;
  protected int usbWriteRetryCount;
  protected int msUsbReadRetryInterval;
  protected int msUsbWriteRetryInterval;
  protected boolean isSynchronized;
  protected org.firstinspires.ftc.robotcore.internal.system.Deadline responseDeadline;
  protected com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest> requestAllocationContext;
  protected com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse> responseAllocationContext;
  public com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsReaderWriter(com.qualcomm.robotcore.hardware.usb.RobotUsbDevice);
  public void throwIfTooManySequentialCommErrors() throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbTooManySequentialErrorsException;
  public void close();
  public void read(boolean, int, byte[], org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException, java.lang.InterruptedException;
  protected void readOnce(int, byte[], org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException, java.lang.InterruptedException;
  public void write(int, byte[]) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException, java.lang.InterruptedException;
  protected void writeOnce(int, byte[]) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException, java.lang.InterruptedException;
  protected com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse readResponse(com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest, org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException, java.lang.InterruptedException;
  protected void readIncomingBytes(byte[], int, int, int, org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow, java.lang.String) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException, java.lang.InterruptedException;
  protected byte readSingleByte(byte[], int, org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow, java.lang.String) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException, java.lang.InterruptedException;
  protected java.lang.String timeoutMessage(java.lang.String, org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbTimeoutException);
  protected void doExceptionBookkeeping();
  protected void logAndRethrowTimeout(org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbTimeoutException, com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest, java.lang.String) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbTimeoutException;
  protected void logAndThrowProtocol(java.lang.String, java.lang.Object...) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbProtocolException;
  protected void logAndThrowProtocol(com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest, com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse, java.lang.String) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbProtocolException;
  protected static java.lang.String bufferToString(byte[]);
}
```

## class ModernRoboticsRequest

```java
public class com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest extends com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram {
  public static final byte[] syncBytes;
  protected final com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest> allocationContext;
  public static com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest newInstance(com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest>, int);
  public static com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest from(com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest>, byte[]);
  public void close();
  public boolean syncBytesValid();
}
```

## class ModernRoboticsResponse

```java
public class com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse extends com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram {
  public static final byte[] syncBytes;
  protected final com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse> allocationContext;
  public static com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse newInstance(com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse>, int);
  public void close();
  public boolean syncBytesValid();
}
```

## class ModernRoboticsUsbUtil

```java
public class com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsUsbUtil {
  public com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsUsbUtil();
  public static com.qualcomm.robotcore.hardware.usb.RobotUsbDevice openRobotUsbDevice(boolean, com.qualcomm.robotcore.hardware.usb.RobotUsbManager, com.qualcomm.robotcore.util.SerialNumber) throws com.qualcomm.robotcore.exception.RobotCoreException;
  public static byte[] getUsbDeviceHeader(com.qualcomm.robotcore.hardware.usb.RobotUsbDevice) throws org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException;
}
```

## interface ReadWriteRunnable

```java
public interface com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable extends java.lang.Runnable,com.qualcomm.robotcore.eventloop.SyncdDevice {
  public static final int MAX_BUFFER_SIZE = 256;
  public abstract void setCallback(com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.Callback);
  public abstract boolean writeNeeded();
  public abstract void resetWriteNeeded();
  public abstract void write(int, byte[]);
  public abstract void setAcceptingWrites(boolean);
  public abstract boolean getAcceptingWrites();
  public abstract void drainPendingWrites();
  public abstract void suppressReads(boolean);
  public abstract byte[] readFromWriteCache(int, int);
  public abstract byte[] read(int, int);
  public abstract void close();
  public abstract com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableSegment createSegment(int, int, int);
  public abstract void destroySegment(int);
  public abstract com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableSegment getSegment(int);
  public abstract void queueSegmentRead(int);
  public abstract void queueSegmentWrite(int);
  public abstract void executeUsing(java.util.concurrent.ExecutorService);
  public abstract void run();
}
```

## class ReadWriteRunnable.BlockingState

```java
public final class com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.BlockingState extends java.lang.Enum<com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.BlockingState> {
  public static final com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.BlockingState BLOCKING;
  public static final com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.BlockingState WAITING;
  public static com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.BlockingState[] values();
  public static com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.BlockingState valueOf(java.lang.String);
}
```

## interface ReadWriteRunnable.Callback

```java
public interface com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.Callback {
  public abstract void startupComplete() throws java.lang.InterruptedException;
  public abstract void readComplete() throws java.lang.InterruptedException;
  public abstract void writeComplete() throws java.lang.InterruptedException;
  public abstract void shutdownComplete() throws java.lang.InterruptedException;
}
```

## class ReadWriteRunnable.EmptyCallback

```java
public class com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.EmptyCallback implements com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.Callback {
  public com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.EmptyCallback();
  public void startupComplete() throws java.lang.InterruptedException;
  public void readComplete() throws java.lang.InterruptedException;
  public void writeComplete() throws java.lang.InterruptedException;
  public void shutdownComplete() throws java.lang.InterruptedException;
}
```

## class ReadWriteRunnableSegment

```java
public class com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableSegment {
  public com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableSegment(int, int, int);
  public int getKey();
  public int getAddress();
  public void setAddress(int);
  public java.util.concurrent.locks.Lock getReadLock();
  public byte[] getReadBuffer();
  public java.util.concurrent.locks.Lock getWriteLock();
  public byte[] getWriteBuffer();
  public void setRetryOnReadFailure(boolean);
  public boolean getRetryOnReadFailure();
  public org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow getTimeWindow();
  public java.lang.String toString();
}
```

## class ReadWriteRunnableStandard

```java
public class com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableStandard implements com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable {
  public static final java.lang.String TAG = "ReadWriteRunnable";
  protected final byte[] localDeviceReadCache;
  protected final byte[] localDeviceWriteCache;
  protected java.util.Map<java.lang.Integer, com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableSegment> segments;
  protected java.util.concurrent.ConcurrentLinkedQueue<java.lang.Integer> segmentReadQueue;
  protected java.util.concurrent.ConcurrentLinkedQueue<java.lang.Integer> segmentWriteQueue;
  protected final android.content.Context context;
  protected final com.qualcomm.robotcore.util.SerialNumber serialNumber;
  protected com.qualcomm.robotcore.hardware.usb.RobotUsbDevice robotUsbDevice;
  protected com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsReaderWriter usbHandler;
  protected int startAddress;
  protected int monitorLength;
  protected boolean pruneBufferAfterRead;
  protected volatile boolean fullWriteNeeded;
  protected int ibActiveFirst;
  protected byte[] activeBuffer;
  protected org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow activeBufferTimeWindow;
  protected java.util.concurrent.CountDownLatch runningInterlock;
  protected volatile boolean running;
  protected volatile com.qualcomm.robotcore.eventloop.SyncdDevice.ShutdownReason shutdownReason;
  protected volatile boolean shutdownComplete;
  protected final java.lang.Object acceptingWritesLock;
  protected volatile boolean acceptingWrites;
  protected volatile boolean suppressReads;
  protected final java.lang.Object readSupressionLock;
  protected com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.Callback callback;
  protected com.qualcomm.robotcore.hardware.usb.RobotUsbModule owner;
  protected final boolean debugLogging;
  protected static boolean DEBUG_SEGMENTS;
  public com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableStandard(android.content.Context, com.qualcomm.robotcore.util.SerialNumber, com.qualcomm.robotcore.hardware.usb.RobotUsbDevice, int, int, boolean);
  public void setCallback(com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnable.Callback);
  public void setOwner(com.qualcomm.robotcore.hardware.usb.RobotUsbModule);
  public com.qualcomm.robotcore.hardware.usb.RobotUsbModule getOwner();
  public boolean writeNeeded();
  public void resetWriteNeeded();
  public void write(int, byte[]);
  public void suppressReads(boolean);
  public byte[] readFromWriteCache(int, int);
  public byte[] read(int, int);
  public void executeUsing(java.util.concurrent.ExecutorService);
  public void close();
  public com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableSegment createSegment(int, int, int);
  public void destroySegment(int);
  public com.qualcomm.hardware.modernrobotics.comm.ReadWriteRunnableSegment getSegment(int);
  public void queueSegmentRead(int);
  public void queueSegmentWrite(int);
  protected void awaitRunning();
  protected void setFullActive();
  protected boolean isFullActive();
  protected void setSuffixActive();
  public void run();
  protected void doReadCycle() throws java.lang.InterruptedException, org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException;
  protected void doWriteCycle() throws java.lang.InterruptedException, org.firstinspires.ftc.robotcore.internal.usb.exception.RobotUsbException;
  public com.qualcomm.robotcore.eventloop.SyncdDevice.ShutdownReason getShutdownReason();
  public void drainPendingWrites();
  public void setAcceptingWrites(boolean);
  public boolean getAcceptingWrites();
  protected void dumpBuffers(java.lang.String, byte[]);
  protected void queueIfNotAlreadyQueued(int, java.util.concurrent.ConcurrentLinkedQueue<java.lang.Integer>);
}
```

## class RobotUsbDevicePretendModernRobotics

```java
public class com.qualcomm.hardware.modernrobotics.comm.RobotUsbDevicePretendModernRobotics implements com.qualcomm.robotcore.hardware.usb.RobotUsbDevice {
  protected com.qualcomm.robotcore.hardware.usb.RobotUsbDevice.FirmwareVersion firmwareVersion;
  protected org.firstinspires.ftc.robotcore.internal.collections.CircularByteBuffer circularByteBuffer;
  protected org.firstinspires.ftc.robotcore.internal.collections.MarkedItemQueue markedItemQueue;
  protected boolean interruptRequested;
  protected com.qualcomm.robotcore.util.SerialNumber serialNumber;
  protected com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType deviceType;
  protected boolean debugRetainBuffers;
  protected com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsRequest> requestAllocationContext;
  protected com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsDatagram.AllocationContext<com.qualcomm.hardware.modernrobotics.comm.ModernRoboticsResponse> responseAllocationContext;
  public com.qualcomm.hardware.modernrobotics.comm.RobotUsbDevicePretendModernRobotics(com.qualcomm.robotcore.util.SerialNumber);
  public com.qualcomm.robotcore.util.SerialNumber getSerialNumber();
  public java.lang.String getProductName();
  public void setDeviceType(com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType);
  public com.qualcomm.robotcore.hardware.DeviceManager.UsbDeviceType getDeviceType();
  public void close();
  public boolean isOpen();
  public boolean isAttached();
  public void setDebugRetainBuffers(boolean);
  public boolean getDebugRetainBuffers();
  public void logRetainedBuffers(long, long, java.lang.String, java.lang.String, java.lang.Object...);
  public void setBaudRate(int);
  public void setDataCharacteristics(byte, byte, byte);
  public void setLatencyTimer(int);
  public void setBreak(boolean);
  public void skipToLikelyUsbPacketStart();
  public boolean mightBeAtUsbPacketStart();
  public void write(byte[]);
  public int read(byte[], int, int, long, org.firstinspires.ftc.robotcore.internal.hardware.TimeWindow);
  public void resetAndFlushBuffers();
  public com.qualcomm.robotcore.hardware.usb.RobotUsbDevice.FirmwareVersion getFirmwareVersion();
  public void setFirmwareVersion(com.qualcomm.robotcore.hardware.usb.RobotUsbDevice.FirmwareVersion);
  public void requestReadInterrupt(boolean);
  public com.qualcomm.robotcore.hardware.usb.RobotUsbDevice.USBIdentifiers getUsbIdentifiers();
}
```
