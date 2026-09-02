# `com.qualcomm.hardware.stmicroelectronics`

_ftc-sdk 11.1.0 — 5 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class VL53L0X

```java
public class com.qualcomm.hardware.stmicroelectronics.VL53L0X extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> implements com.qualcomm.robotcore.hardware.DistanceSensor {
  public static final com.qualcomm.robotcore.hardware.I2cAddr ADDRESS_I2C_DEFAULT;
  protected static final int FAKE_DISTANCE_MM = 65535;
  protected java.lang.String MYTAG;
  protected int io_timeout;
  protected com.qualcomm.robotcore.util.ElapsedTime ioElapsedTime;
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public byte getModelID();
  public double getDistance(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public boolean didTimeoutOccur();
  public com.qualcomm.hardware.stmicroelectronics.VL53L0X(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  protected synchronized boolean doInitialize();
  protected void getSequenceStepEnables(com.qualcomm.hardware.stmicroelectronics.VL53L0X.SequenceStepEnables);
  protected void getSequenceStepTimeouts(com.qualcomm.hardware.stmicroelectronics.VL53L0X.SequenceStepEnables, com.qualcomm.hardware.stmicroelectronics.VL53L0X.SequenceStepTimeouts);
  protected int getVcselPulsePeriod(com.qualcomm.hardware.stmicroelectronics.VL53L0X.vcselPeriodType);
  protected int decodeVcselPeriod(int);
  protected long timeoutMclksToMicroseconds(int, int);
  protected long calcMacroPeriod(int);
  protected boolean setMeasurementTimingBudget(long);
  protected long timeoutMicrosecondsToMclks(long, int);
  protected long encodeTimeout(int);
  protected boolean performSingleRefCalibration(int);
  protected void startContinuous();
  protected void startContinuous(int);
  protected void stopContinuous();
  protected void setTimeout(int);
  protected int getTimeout();
  protected int readRangeContinuousMillimeters();
  protected byte readReg(com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register);
  protected byte readReg(byte);
  protected byte readReg(int);
  protected void writeReg(com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register, byte);
  protected void writeReg(byte, byte);
  protected void writeReg(int, int);
  protected void writeReg(com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register, byte, com.qualcomm.robotcore.hardware.I2cWaitControl);
  protected void writeReg(byte, byte, com.qualcomm.robotcore.hardware.I2cWaitControl);
  protected void writeReg(int, int, com.qualcomm.robotcore.hardware.I2cWaitControl);
  protected int readUnsignedByte(com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register);
  protected void writeShort(com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register, short);
  protected short readShort(com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register);
}
```

## class VL53L0X.Register

```java
public final class com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register extends java.lang.Enum<com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register> {
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSRANGE_START;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_THRESH_HIGH;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_THRESH_LOW;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_SEQUENCE_CONFIG;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_RANGE_CONFIG;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_INTERMEASUREMENT_PERIOD;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_INTERRUPT_CONFIG_GPIO;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GPIO_HV_MUX_ACTIVE_HIGH;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_INTERRUPT_CLEAR;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register RESULT_INTERRUPT_STATUS;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register RESULT_RANGE_STATUS;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register RESULT_CORE_AMBIENT_WINDOW_EVENTS_RTN;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register RESULT_CORE_RANGING_TOTAL_EVENTS_RTN;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register RESULT_CORE_AMBIENT_WINDOW_EVENTS_REF;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register RESULT_CORE_RANGING_TOTAL_EVENTS_REF;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register RESULT_PEAK_SIGNAL_RATE_REF;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register ALGO_PART_TO_PART_RANGE_OFFSET_MM;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register I2C_SLAVE_DEVICE_ADDRESS;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register MSRC_CONFIG_CONTROL;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_MIN_SNR;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_VALID_PHASE_LOW;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_VALID_PHASE_HIGH;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_MIN_COUNT_RATE_RTN_LIMIT;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register FINAL_RANGE_CONFIG_MIN_SNR;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register FINAL_RANGE_CONFIG_VALID_PHASE_LOW;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register FINAL_RANGE_CONFIG_VALID_PHASE_HIGH;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register FINAL_RANGE_CONFIG_MIN_COUNT_RATE_RTN_LIMIT;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_SIGMA_THRESH_HI;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_SIGMA_THRESH_LO;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_VCSEL_PERIOD;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_TIMEOUT_MACROP_HI;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register PRE_RANGE_CONFIG_TIMEOUT_MACROP_LO;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SYSTEM_HISTOGRAM_BIN;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register HISTOGRAM_CONFIG_INITIAL_PHASE_SELECT;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register HISTOGRAM_CONFIG_READOUT_CTRL;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register FINAL_RANGE_CONFIG_VCSEL_PERIOD;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register FINAL_RANGE_CONFIG_TIMEOUT_MACROP_HI;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register FINAL_RANGE_CONFIG_TIMEOUT_MACROP_LO;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register CROSSTALK_COMPENSATION_PEAK_RATE_MCPS;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register MSRC_CONFIG_TIMEOUT_MACROP;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register SOFT_RESET_GO2_SOFT_RESET_N;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register IDENTIFICATION_MODEL_ID;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register IDENTIFICATION_REVISION_ID;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register OSC_CALIBRATE_VAL;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_VCSEL_WIDTH;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_SPAD_ENABLES_REF_0;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_SPAD_ENABLES_REF_1;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_SPAD_ENABLES_REF_2;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_SPAD_ENABLES_REF_3;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_SPAD_ENABLES_REF_4;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_SPAD_ENABLES_REF_5;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register GLOBAL_CONFIG_REF_EN_START_SELECT;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register DYNAMIC_SPAD_NUM_REQUESTED_REF_SPAD;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register DYNAMIC_SPAD_REF_EN_START_OFFSET;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register POWER_MANAGEMENT_GO1_POWER_FORCE;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register VHV_CONFIG_PAD_SCL_SDA__EXTSUP_HV;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register ALGO_PHASECAL_LIM;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register ALGO_PHASECAL_CONFIG_TIMEOUT;
  public int bVal;
  public static com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register[] values();
  public static com.qualcomm.hardware.stmicroelectronics.VL53L0X.Register valueOf(java.lang.String);
}
```

## class VL53L0X.SequenceStepEnables

```java
public class com.qualcomm.hardware.stmicroelectronics.VL53L0X.SequenceStepEnables {
  protected com.qualcomm.hardware.stmicroelectronics.VL53L0X.SequenceStepEnables(com.qualcomm.hardware.stmicroelectronics.VL53L0X);
}
```

## class VL53L0X.SequenceStepTimeouts

```java
public class com.qualcomm.hardware.stmicroelectronics.VL53L0X.SequenceStepTimeouts {
  protected com.qualcomm.hardware.stmicroelectronics.VL53L0X.SequenceStepTimeouts(com.qualcomm.hardware.stmicroelectronics.VL53L0X);
}
```

## class VL53L0X.vcselPeriodType

```java
final class com.qualcomm.hardware.stmicroelectronics.VL53L0X.vcselPeriodType extends java.lang.Enum<com.qualcomm.hardware.stmicroelectronics.VL53L0X.vcselPeriodType> {
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.vcselPeriodType VcselPeriodPreRange;
  public static final com.qualcomm.hardware.stmicroelectronics.VL53L0X.vcselPeriodType VcselPeriodFinalRange;
  public static com.qualcomm.hardware.stmicroelectronics.VL53L0X.vcselPeriodType[] values();
  public static com.qualcomm.hardware.stmicroelectronics.VL53L0X.vcselPeriodType valueOf(java.lang.String);
}
```
