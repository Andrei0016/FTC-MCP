# `com.qualcomm.hardware.digitalchickenlabs`

_ftc-sdk 11.1.0 — 14 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface OctoQuad

```java
public interface com.qualcomm.hardware.digitalchickenlabs.OctoQuad extends com.qualcomm.robotcore.hardware.HardwareDevice {
  public static final byte OCTOQUAD_CHIP_ID = 81;
  public static final int SUPPORTED_FW_VERSION_MAJ = 3;
  public static final int ENCODER_FIRST = 0;
  public static final int ENCODER_LAST = 7;
  public static final int NUM_ENCODERS = 8;
  public static final int MIN_VELOCITY_MEASUREMENT_INTERVAL_MS = 1;
  public static final int MAX_VELOCITY_MEASUREMENT_INTERVAL_MS = 255;
  public static final int MIN_PULSE_WIDTH_US = 0;
  public static final int MAX_PULSE_WIDTH_US = 65535;
  public abstract byte getChipId();
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.FirmwareVersion getFirmwareVersion();
  public abstract java.lang.String getFirmwareVersionString();
  public abstract void setSingleEncoderDirection(int, com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection);
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection getSingleEncoderDirection(int);
  public abstract void setAllEncoderDirections(boolean[]);
  public abstract void setChannelBankConfig(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig);
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig getChannelBankConfig();
  public abstract void readAllEncoderData(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock);
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock readAllEncoderData();
  public abstract void setCachingMode(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode);
  public abstract void refreshCache();
  public abstract int readSinglePosition_Caching(int);
  public abstract short readSingleVelocity_Caching(int);
  public abstract short readSingleVelocity(int);
  public abstract int readSinglePosition(int);
  public abstract void resetSinglePosition(int);
  public abstract void resetAllPositions();
  public abstract void resetMultiplePositions(boolean[]);
  public abstract void resetMultiplePositions(int...);
  public abstract void setSingleVelocitySampleInterval(int, int);
  public abstract int getSingleVelocitySampleInterval(int);
  public abstract void setAllVelocitySampleIntervals(int);
  public abstract void setSingleChannelPulseWidthParams(int, int, int);
  public abstract void setSingleChannelPulseWidthParams(int, com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelPulseWidthParams);
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelPulseWidthParams getSingleChannelPulseWidthParams(int);
  public abstract void setSingleChannelPulseWidthTracksWrap(int, boolean);
  public abstract boolean getSingleChannelPulseWidthTracksWrap(int);
  public abstract void setAllChannelsPulseWidthTracksWrap(boolean[]);
  public abstract void setLocalizerPortX(int);
  public abstract void setLocalizerPortY(int);
  public abstract void setLocalizerCountsPerMM_X(float);
  public abstract void setLocalizerCountsPerMM_Y(float);
  public abstract void setLocalizerTcpOffsetMM_X(float);
  public abstract void setLocalizerTcpOffsetMM_Y(float);
  public abstract void setLocalizerImuHeadingScalar(float);
  public abstract void setLocalizerVelocityIntervalMS(int);
  public abstract void setAllLocalizerParameters(int, int, float, float, float, float, float, int);
  public abstract void readLocalizerData(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock);
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock readLocalizerData();
  public abstract void readLocalizerDataAndAllEncoderData(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock, com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock);
  public abstract void setLocalizerPose(int, int, float);
  public abstract void setLocalizerHeading(float);
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus getLocalizerStatus();
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis getLocalizerHeadingAxisChoice();
  public abstract void resetLocalizerAndCalibrateIMU();
  public abstract void setI2cRecoveryMode(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode);
  public abstract com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode getI2cRecoveryMode();
  public abstract void saveParametersToFlash();
  public abstract void resetEverything();
}
```

## class OctoQuad.CachingMode

```java
public final class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode MANUAL;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode AUTO;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode valueOf(java.lang.String);
}
```

## class OctoQuad.ChannelBankConfig

```java
public final class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig ALL_QUADRATURE;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig ALL_PULSE_WIDTH;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig BANK1_QUADRATURE_BANK2_PULSE_WIDTH;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig valueOf(java.lang.String);
}
```

## class OctoQuad.ChannelPulseWidthParams

```java
public class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelPulseWidthParams {
  public int min_length_us;
  public int max_length_us;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelPulseWidthParams();
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelPulseWidthParams(int, int);
}
```

## class OctoQuad.EncoderDataBlock

```java
public class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock {
  public int[] positions;
  public short[] velocities;
  public boolean crcOk;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock();
  public boolean isDataValid();
  public void copyTo(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock);
}
```

## class OctoQuad.EncoderDirection

```java
public final class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection FORWARD;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection REVERSE;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection valueOf(java.lang.String);
}
```

## class OctoQuad.FirmwareVersion

```java
public class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.FirmwareVersion {
  public final int maj;
  public final int min;
  public final int eng;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.FirmwareVersion(int, int, int);
  public java.lang.String toString();
}
```

## class OctoQuad.I2cRecoveryMode

```java
public final class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode NONE;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode MODE_1_PERIPH_RST_ON_FRAME_ERR;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode MODE_2_M1_PLUS_SCL_IDLE_ONESHOT_TGL;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode valueOf(java.lang.String);
}
```

## class OctoQuad.LocalizerDataBlock

```java
public class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock {
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus localizerStatus;
  public boolean crcOk;
  public float heading_rad;
  public short posX_mm;
  public short posY_mm;
  public short velX_mmS;
  public short velY_mmS;
  public float velHeading_radS;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock();
  public boolean isDataValid();
}
```

## class OctoQuad.LocalizerStatus

```java
public final class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus INVALID;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus NOT_INITIALIZED;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus WARMING_UP_IMU;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus CALIBRATING_IMU;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus RUNNING;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus FAULT_NO_IMU;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus valueOf(java.lang.String);
}
```

## class OctoQuad.LocalizerYawAxis

```java
public final class com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis UNDECIDED;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis X;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis X_INV;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis Y;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis Y_INV;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis Z;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis Z_INV;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis valueOf(java.lang.String);
}
```

## class OctoQuadImpl

```java
public class com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple> implements com.qualcomm.hardware.digitalchickenlabs.OctoQuad {
  protected com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode cachingMode;
  protected com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock cachedData;
  protected boolean[] posHasBeenRead;
  protected boolean[] velHasBeenRead;
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  protected boolean doInitialize();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public byte getChipId();
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.FirmwareVersion getFirmwareVersion();
  public java.lang.String getFirmwareVersionString();
  public int readSinglePosition(int);
  public void resetSinglePosition(int);
  public void resetAllPositions();
  public void resetMultiplePositions(boolean[]);
  public void resetMultiplePositions(int...);
  public void setSingleEncoderDirection(int, com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection);
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDirection getSingleEncoderDirection(int);
  public void setAllEncoderDirections(boolean[]);
  public short readSingleVelocity(int);
  public void readAllEncoderData(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock);
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock readAllEncoderData();
  public void setSingleVelocitySampleInterval(int, int);
  public int getSingleVelocitySampleInterval(int);
  public void setAllVelocitySampleIntervals(int);
  public void setSingleChannelPulseWidthParams(int, int, int);
  public void setSingleChannelPulseWidthParams(int, com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelPulseWidthParams);
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelPulseWidthParams getSingleChannelPulseWidthParams(int);
  public void setSingleChannelPulseWidthTracksWrap(int, boolean);
  public boolean getSingleChannelPulseWidthTracksWrap(int);
  public void setAllChannelsPulseWidthTracksWrap(boolean[]);
  public void setLocalizerCountsPerMM_X(float);
  public void setLocalizerCountsPerMM_Y(float);
  public void setLocalizerTcpOffsetMM_X(float);
  public void setLocalizerTcpOffsetMM_Y(float);
  public void setLocalizerImuHeadingScalar(float);
  public void setLocalizerPortX(int);
  public void setLocalizerPortY(int);
  public void setLocalizerVelocityIntervalMS(int);
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerStatus getLocalizerStatus();
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerYawAxis getLocalizerHeadingAxisChoice();
  public void resetLocalizerAndCalibrateIMU();
  public void readLocalizerData(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock);
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock readLocalizerData();
  public void readLocalizerDataAndAllEncoderData(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.LocalizerDataBlock, com.qualcomm.hardware.digitalchickenlabs.OctoQuad.EncoderDataBlock);
  public void setAllLocalizerParameters(int, int, float, float, float, float, float, int);
  public void setLocalizerPose(int, int, float);
  public void setLocalizerHeading(float);
  public void resetEverything();
  public void setChannelBankConfig(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig);
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.ChannelBankConfig getChannelBankConfig();
  public void setI2cRecoveryMode(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode);
  public com.qualcomm.hardware.digitalchickenlabs.OctoQuad.I2cRecoveryMode getI2cRecoveryMode();
  public void saveParametersToFlash();
  public void setCachingMode(com.qualcomm.hardware.digitalchickenlabs.OctoQuad.CachingMode);
  public void refreshCache();
  public int readSinglePosition_Caching(int);
  public short readSingleVelocity_Caching(int);
}
```

## class OctoQuadImpl.Register

```java
final class com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register CHIP_ID;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register FIRMWARE_VERSION_MAJOR;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register FIRMWARE_VERSION_MINOR;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register FIRMWARE_VERSION_ENGINEERING;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND_DAT_0;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND_DAT_1;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND_DAT_2;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND_DAT_3;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND_DAT_4;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND_DAT_5;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register COMMAND_DAT_6;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_YAW_AXIS;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_STATUS;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_VX;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_VY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_VH;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_X;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_Y;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_H;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register LOCALIZER_CRC16;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_0_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_1_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_2_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_3_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_4_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_5_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_6_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_7_POSITION;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_0_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_1_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_2_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_3_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_4_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_5_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_6_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_7_VELOCITY;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register ENCODER_DATA_CRC16;
  public final byte addr;
  public final int length;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.Register valueOf(java.lang.String);
}
```

## class OctoQuadImpl.RegisterType

```java
final class com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType extends java.lang.Enum<com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType> {
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType uint8_t;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType int32_t;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType int16_t;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType uint16_t;
  public static final com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType float32;
  public final int length;
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType[] values();
  public static com.qualcomm.hardware.digitalchickenlabs.OctoQuadImpl.RegisterType valueOf(java.lang.String);
}
```
