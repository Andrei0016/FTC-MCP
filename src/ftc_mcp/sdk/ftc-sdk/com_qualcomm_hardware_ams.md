# `com.qualcomm.hardware.ams`

_ftc-sdk 11.1.0 — 11 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface AMSColorSensor

```java
public interface com.qualcomm.hardware.ams.AMSColorSensor extends com.qualcomm.robotcore.hardware.ColorSensor,com.qualcomm.robotcore.hardware.NormalizedColorSensor {
  public static final com.qualcomm.robotcore.hardware.I2cAddr AMS_TCS34725_ADDRESS;
  public static final com.qualcomm.robotcore.hardware.I2cAddr AMS_TMD37821_ADDRESS;
  public static final byte AMS_TCS34725_ID = 68;
  public static final byte AMS_TMD37821_ID = 96;
  public static final byte AMS_TMD37823_ID = 105;
  public static final int AMS_COLOR_COMMAND_BIT = 128;
  public static final int AMS_COLOR_COMMAND_TYPE_REPEATED_BYTE = 0;
  public static final int AMS_COLOR_COMMAND_TYPE_AUTO_INCREMENT = 32;
  public static final int AMS_COLOR_COMMAND_TYPE_RESERVED = 512;
  public static final int AMS_COLOR_COMMAND_TYPE_SPECIAL = 544;
  public abstract boolean initialize(com.qualcomm.hardware.ams.AMSColorSensor.Parameters);
  public abstract com.qualcomm.hardware.ams.AMSColorSensor.Parameters getParameters();
  public abstract byte getDeviceID();
  public abstract byte read8(com.qualcomm.hardware.ams.AMSColorSensor.Register);
  public abstract byte[] read(com.qualcomm.hardware.ams.AMSColorSensor.Register, int);
  public abstract void write8(com.qualcomm.hardware.ams.AMSColorSensor.Register, int);
  public abstract void write(com.qualcomm.hardware.ams.AMSColorSensor.Register, byte[]);
}
```

## class AMSColorSensor.Config

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.Config extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.Config> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Config NORMAL;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Config LONG_WAIT;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.Config[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Config valueOf(java.lang.String);
}
```

## class AMSColorSensor.Enable

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.Enable extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.Enable> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable RES7;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable RES6;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable PIEN;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable AIEN;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable WEN;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable PEN;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable AEN;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable PON;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable OFF;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Enable UNKNOWN;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.Enable[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Enable valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.ams.AMSColorSensor.Enable);
  public byte bitOr(byte);
}
```

## class AMSColorSensor.Gain

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.Gain extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.Gain> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Gain UNKNOWN;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Gain GAIN_1;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Gain GAIN_4;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Gain GAIN_16;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Gain GAIN_64;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Gain MASK;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.Gain[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Gain valueOf(java.lang.String);
  public static com.qualcomm.hardware.ams.AMSColorSensor.Gain fromByte(byte);
}
```

## class AMSColorSensor.LEDDrive

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive Percent100;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive Percent50;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive Percent25;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive Percent12_5;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive MASK;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive valueOf(java.lang.String);
}
```

## class AMSColorSensor.Parameters

```java
public class com.qualcomm.hardware.ams.AMSColorSensor.Parameters implements java.lang.Cloneable {
  public int deviceId;
  public com.qualcomm.robotcore.hardware.I2cAddr i2cAddr;
  public com.qualcomm.hardware.ams.AMSColorSensor.Gain gain;
  public int atime;
  public boolean useProximityIfAvailable;
  public int proximityPulseCount;
  public com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive ledDrive;
  public int proximitySaturation;
  public boolean loggingEnabled;
  public java.lang.String loggingTag;
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow readWindow;
  public static int atimeFromMs(float);
  public int integrationCycles();
  public int getMaximumReading();
  public float msAccumulationInterval();
  public com.qualcomm.hardware.ams.AMSColorSensor.Parameters(com.qualcomm.robotcore.hardware.I2cAddr, int);
  public static com.qualcomm.hardware.ams.AMSColorSensor.Parameters createForTCS34725();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Parameters createForTMD37821();
  public com.qualcomm.hardware.ams.AMSColorSensor.Parameters clone();
  public java.lang.Object clone() throws java.lang.CloneNotSupportedException;
}
```

## class AMSColorSensor.Pers

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.Pers extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.Pers> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_NONE;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_1;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_2;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_3;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_5;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_10;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_15;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_20;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_25;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_30;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_35;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_40;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_45;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_50;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_55;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers CYCLE_60;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Pers UNKNOWN;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.Pers[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Pers valueOf(java.lang.String);
}
```

## class AMSColorSensor.Register

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.Register extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.Register> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register ENABLE;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register ATIME;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register REGISTER2;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register WTIME;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register AILT;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register AIHT;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register PERS;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register CONFIGURATION;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register PPLUSE;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register CONTROL;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register DEVICE_ID;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register STATUS;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register ALPHA;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register RED;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register GREEN;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register BLUE;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register PDATA;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register READ_WINDOW_FIRST;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Register READ_WINDOW_LAST;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.Register[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Register valueOf(java.lang.String);
}
```

## class AMSColorSensor.Status

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.Status extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.Status> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Status PINT;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Status AINT;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Status PVALID;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Status AVALID;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.Status[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Status valueOf(java.lang.String);
}
```

## class AMSColorSensor.Wait

```java
public final class com.qualcomm.hardware.ams.AMSColorSensor.Wait extends java.lang.Enum<com.qualcomm.hardware.ams.AMSColorSensor.Wait> {
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Wait MS_2_4;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Wait MS_204;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Wait MS_614;
  public static final com.qualcomm.hardware.ams.AMSColorSensor.Wait UNKNOWN;
  public final byte bVal;
  public static com.qualcomm.hardware.ams.AMSColorSensor.Wait[] values();
  public static com.qualcomm.hardware.ams.AMSColorSensor.Wait valueOf(java.lang.String);
}
```

## class AMSColorSensorImpl

```java
public abstract class com.qualcomm.hardware.ams.AMSColorSensorImpl extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters<com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.ams.AMSColorSensor.Parameters> implements com.qualcomm.hardware.ams.AMSColorSensor, com.qualcomm.robotcore.hardware.I2cAddrConfig, com.qualcomm.robotcore.hardware.Light {
  public static final java.lang.String TAG = "AMSColorSensorImpl";
  protected com.qualcomm.hardware.ams.AMSColorSensorImpl(com.qualcomm.hardware.ams.AMSColorSensor.Parameters, com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  protected synchronized boolean internalInitialize(com.qualcomm.hardware.ams.AMSColorSensor.Parameters);
  protected void dumpState();
  protected synchronized void enable();
  protected synchronized void disable();
  protected boolean isConnectedAndEnabled();
  protected boolean testBits(byte, byte);
  protected boolean testBits(byte, byte, byte);
  protected boolean testBits(byte, com.qualcomm.hardware.ams.AMSColorSensor.Enable);
  protected boolean testBits(byte, com.qualcomm.hardware.ams.AMSColorSensor.Enable, com.qualcomm.hardware.ams.AMSColorSensor.Enable);
  protected void writeEnable(int);
  protected byte readEnable();
  protected byte readEnableAfterWrite();
  protected void setIntegrationTime(int);
  protected void setProximityPulseCount(int);
  protected boolean is3782();
  protected void setHardwareGain(com.qualcomm.hardware.ams.AMSColorSensor.Gain);
  protected void setPDrive(com.qualcomm.hardware.ams.AMSColorSensor.LEDDrive);
  protected void updateControl(int, int);
  public byte getDeviceID();
  public float getGain();
  public void setGain(float);
  public synchronized int red();
  public synchronized int green();
  public synchronized int blue();
  public synchronized int alpha();
  protected int normalToUnsignedShort(float);
  public synchronized int argb();
  public com.qualcomm.robotcore.hardware.NormalizedRGBA getNormalizedColors();
  public synchronized void enableLed(boolean);
  public boolean isLightOn();
  public synchronized com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public synchronized void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public void resetDeviceConfigurationForOpMode();
  protected int readUnsignedByte(com.qualcomm.hardware.ams.AMSColorSensor.Register);
  protected int readUnsignedShort(com.qualcomm.hardware.ams.AMSColorSensor.Register, java.nio.ByteOrder);
  public synchronized byte read8(com.qualcomm.hardware.ams.AMSColorSensor.Register);
  public synchronized byte[] read(com.qualcomm.hardware.ams.AMSColorSensor.Register, int);
  public synchronized void write8(com.qualcomm.hardware.ams.AMSColorSensor.Register, int);
  public void write(com.qualcomm.hardware.ams.AMSColorSensor.Register, byte[]);
  protected void delay(int);
  protected boolean internalInitialize(java.lang.Object);
  public com.qualcomm.hardware.ams.AMSColorSensor.Parameters getParameters();
  public boolean initialize(com.qualcomm.hardware.ams.AMSColorSensor.Parameters);
}
```
