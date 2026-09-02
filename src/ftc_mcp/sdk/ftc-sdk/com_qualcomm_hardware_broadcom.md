# `com.qualcomm.hardware.broadcom`

_ftc-sdk 11.1.0 — 13 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface BroadcomColorSensor

```java
public interface com.qualcomm.hardware.broadcom.BroadcomColorSensor extends com.qualcomm.robotcore.hardware.ColorSensor,com.qualcomm.robotcore.hardware.NormalizedColorSensor {
  public static final com.qualcomm.robotcore.hardware.I2cAddr BROADCOM_APDS9151_ADDRESS;
  public static final byte BROADCOM_APDS9151_ID = -62;
  public abstract boolean initialize(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters);
  public abstract com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters getParameters();
  public abstract byte getDeviceID();
  public abstract byte read8(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register);
  public abstract byte[] read(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register, int);
  public abstract void write8(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register, int);
  public abstract void write(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register, byte[]);
}
```

## class BroadcomColorSensor.Gain

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain UNKNOWN;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain GAIN_1;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain GAIN_3;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain GAIN_6;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain GAIN_9;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain GAIN_18;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain valueOf(java.lang.String);
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain fromByte(byte);
}
```

## class BroadcomColorSensor.LEDCurrent

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_2_5mA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_5mA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_10mA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_25mA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_50mA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_75mA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_100mA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent CURRENT_125mA;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.LEDPulseModulation

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation RES0;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation RES1;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation RES2;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation LED_PULSE_60kHz;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation LED_PULSE_70kHz;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation LED_PULSE_80kHz;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation LED_PULSE_90kHz;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation LED_PULSE_100kHz;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.LSMeasurementRate

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R25ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R50ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R100ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R200ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R500ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R1000ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R2000ms_1;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate R2000ms_2;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.LSResolution

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution R20BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution R19BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution R18BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution R17BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution R16BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution R13BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution RES_1;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution RES_2;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.MainControl

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl RES7;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl SAI_PS;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl SAI_LS;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl SW_RESET;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl RES3;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl RGB_MODE;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl LS_EN;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl PS_EN;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl OFF;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainControl);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.MainStatus

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus POWER_ON_STATUS;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus LS_INT_STAT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus LS_DATA_STATUS;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus PS_LOGIC_SIG_STAT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus PS_INT_STAT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus PS_DATA_STAT;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.MainStatus);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.PSMeasurementRate

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate RES;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate R6_25ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate R12_5ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate R25ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate R50ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate R100ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate R200ms;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate R400ms;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.PSResolution

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution R8BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution R9BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution R10BIT;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution R11BIT;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution valueOf(java.lang.String);
  public byte bitOr(com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution);
  public byte bitOr(byte);
}
```

## class BroadcomColorSensor.Parameters

```java
public class com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters implements java.lang.Cloneable {
  public int deviceId;
  public com.qualcomm.robotcore.hardware.I2cAddr i2cAddr;
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain gain;
  public int proximityPulseCount;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution proximityResolution;
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate proximityMeasRate;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution lightSensorResolution;
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate lightSensorMeasRate;
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent ledCurrent;
  public int proximitySaturation;
  public int colorSaturation;
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation pulseModulation;
  public boolean loggingEnabled;
  public java.lang.String loggingTag;
  public com.qualcomm.robotcore.hardware.I2cDeviceSynch.ReadWindow readWindow;
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters(com.qualcomm.robotcore.hardware.I2cAddr, int);
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters createForAPDS9151();
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters clone();
  public java.lang.Object clone() throws java.lang.CloneNotSupportedException;
}
```

## class BroadcomColorSensor.Register

```java
public final class com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register extends java.lang.Enum<com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register> {
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register MAIN_CTRL;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PS_LED;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PS_PULSES;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PS_MEAS_RATE;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_MEAS_RATE;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_GAIN;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PART_ID;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register MAIN_STATUS;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PS_DATA;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_DATA_IR;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_DATA_GREEN;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_DATA_BLUE;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_DATA_RED;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register INT_CFG;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register INT_PST;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PS_THRES_UP;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PS_THRES_LOW;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register PS_CAN;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_THRES_UP;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_THRES_LOW;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register LS_THRES_VAR;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register READ_WINDOW_FIRST;
  public static final com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register READ_WINDOW_LAST;
  public final byte bVal;
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register[] values();
  public static com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register valueOf(java.lang.String);
}
```

## class BroadcomColorSensorImpl

```java
public abstract class com.qualcomm.hardware.broadcom.BroadcomColorSensorImpl extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDeviceWithParameters<com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters> implements com.qualcomm.hardware.broadcom.BroadcomColorSensor, com.qualcomm.robotcore.hardware.I2cAddrConfig, com.qualcomm.robotcore.hardware.Light {
  public static final java.lang.String TAG = "BroadcomColorSensorImpl";
  protected com.qualcomm.hardware.broadcom.BroadcomColorSensorImpl(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters, com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  protected synchronized boolean internalInitialize(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters);
  protected void dumpState();
  protected synchronized void enable();
  protected synchronized void disable();
  protected boolean testBits(byte, byte);
  protected boolean testBits(byte, byte, byte);
  protected byte readMainCtrl();
  protected void setProximityPulseCount(int);
  protected void setHardwareGain(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Gain);
  protected void setPDrive(com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent);
  public byte getDeviceID();
  protected void setLEDParameters(com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDPulseModulation, com.qualcomm.hardware.broadcom.BroadcomColorSensor.LEDCurrent);
  protected void setPSRateAndRes(com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSResolution, com.qualcomm.hardware.broadcom.BroadcomColorSensor.PSMeasurementRate);
  protected void setLSRateAndRes(com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSResolution, com.qualcomm.hardware.broadcom.BroadcomColorSensor.LSMeasurementRate);
  public synchronized int red();
  public synchronized int green();
  public synchronized int blue();
  public synchronized int alpha();
  public synchronized int argb();
  public void setGain(float);
  public float getGain();
  public com.qualcomm.robotcore.hardware.NormalizedRGBA getNormalizedColors();
  public synchronized void enableLed(boolean);
  public boolean isLightOn();
  public synchronized com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public synchronized void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public void resetDeviceConfigurationForOpMode();
  protected int readUnsignedByte(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register);
  protected int readUnsignedShort(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register, java.nio.ByteOrder);
  public synchronized byte read8(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register);
  public synchronized byte[] read(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register, int);
  public synchronized void write8(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register, int);
  public void write(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Register, byte[]);
  protected void delay(int);
  protected boolean internalInitialize(java.lang.Object);
  public com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters getParameters();
  public boolean initialize(com.qualcomm.hardware.broadcom.BroadcomColorSensor.Parameters);
}
```
