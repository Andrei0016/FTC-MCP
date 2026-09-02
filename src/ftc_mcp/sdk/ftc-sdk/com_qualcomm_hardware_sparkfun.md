# `com.qualcomm.hardware.sparkfun`

_ftc-sdk 11.1.0 — 8 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class SparkFunLEDStick

```java
public class com.qualcomm.hardware.sparkfun.SparkFunLEDStick extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple> {
  public void setColor(int, int);
  public void setColor(int);
  public void setColors(int[]);
  public void setBrightness(int, int);
  public void setBrightness(int);
  public void turnAllOff();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  protected synchronized boolean doInitialize();
  public java.lang.String getDeviceName();
  public com.qualcomm.hardware.sparkfun.SparkFunLEDStick(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
}
```

## class SparkFunLEDStick.Commands

```java
final class com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands extends java.lang.Enum<com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands> {
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands CHANGE_LED_LENGTH;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_SINGLE_LED_COLOR;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_ALL_LED_COLOR;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_RED_ARRAY;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_GREEN_ARRAY;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_BLUE_ARRAY;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_SINGLE_LED_BRIGHTNESS;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_ALL_LED_BRIGHTNESS;
  public static final com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands WRITE_ALL_LED_OFF;
  public static com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands[] values();
  public static com.qualcomm.hardware.sparkfun.SparkFunLEDStick.Commands valueOf(java.lang.String);
}
```

## class SparkFunOTOS

```java
public class com.qualcomm.hardware.sparkfun.SparkFunOTOS extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> {
  public static final byte DEFAULT_ADDRESS = 23;
  public static final double MIN_SCALAR = 0.872d;
  public static final double MAX_SCALAR = 1.127d;
  protected static final byte REG_PRODUCT_ID = 0;
  protected static final byte REG_HW_VERSION = 1;
  protected static final byte REG_FW_VERSION = 2;
  protected static final byte REG_SCALAR_LINEAR = 4;
  protected static final byte REG_SCALAR_ANGULAR = 5;
  protected static final byte REG_IMU_CALIB = 6;
  protected static final byte REG_RESET = 7;
  protected static final byte REG_SIGNAL_PROCESS = 14;
  protected static final byte REG_SELF_TEST = 15;
  protected static final byte REG_OFF_XL = 16;
  protected static final byte REG_OFF_XH = 17;
  protected static final byte REG_OFF_YL = 18;
  protected static final byte REG_OFF_YH = 19;
  protected static final byte REG_OFF_HL = 20;
  protected static final byte REG_OFF_HH = 21;
  protected static final byte REG_STATUS = 31;
  protected static final byte REG_POS_XL = 32;
  protected static final byte REG_POS_XH = 33;
  protected static final byte REG_POS_YL = 34;
  protected static final byte REG_POS_YH = 35;
  protected static final byte REG_POS_HL = 36;
  protected static final byte REG_POS_HH = 37;
  protected static final byte REG_VEL_XL = 38;
  protected static final byte REG_VEL_XH = 39;
  protected static final byte REG_VEL_YL = 40;
  protected static final byte REG_VEL_YH = 41;
  protected static final byte REG_VEL_HL = 42;
  protected static final byte REG_VEL_HH = 43;
  protected static final byte REG_ACC_XL = 44;
  protected static final byte REG_ACC_XH = 45;
  protected static final byte REG_ACC_YL = 46;
  protected static final byte REG_ACC_YH = 47;
  protected static final byte REG_ACC_HL = 48;
  protected static final byte REG_ACC_HH = 49;
  protected static final byte REG_POS_STD_XL = 50;
  protected static final byte REG_POS_STD_XH = 51;
  protected static final byte REG_POS_STD_YL = 52;
  protected static final byte REG_POS_STD_YH = 53;
  protected static final byte REG_POS_STD_HL = 54;
  protected static final byte REG_POS_STD_HH = 55;
  protected static final byte REG_VEL_STD_XL = 56;
  protected static final byte REG_VEL_STD_XH = 57;
  protected static final byte REG_VEL_STD_YL = 58;
  protected static final byte REG_VEL_STD_YH = 59;
  protected static final byte REG_VEL_STD_HL = 60;
  protected static final byte REG_VEL_STD_HH = 61;
  protected static final byte REG_ACC_STD_XL = 62;
  protected static final byte REG_ACC_STD_XH = 63;
  protected static final byte REG_ACC_STD_YL = 64;
  protected static final byte REG_ACC_STD_YH = 65;
  protected static final byte REG_ACC_STD_HL = 66;
  protected static final byte REG_ACC_STD_HH = 67;
  protected static final byte PRODUCT_ID = 95;
  protected static final double RADIAN_TO_DEGREE = 57.29577951308232d;
  protected static final double DEGREE_TO_RADIAN = 0.017453292519943295d;
  protected static final double METER_TO_INT16 = 3276.8d;
  protected static final double INT16_TO_METER = 3.0517578125E-4d;
  protected static final double MPS_TO_INT16 = 6553.6d;
  protected static final double INT16_TO_MPS = 1.52587890625E-4d;
  protected static final double MPSS_TO_INT16 = 208.83788041787972d;
  protected static final double INT16_TO_MPSS = 0.0047884033203125d;
  protected static final double RAD_TO_INT16 = 10430.378350470453d;
  protected static final double INT16_TO_RAD = 9.587379924285257E-5d;
  protected static final double RPS_TO_INT16 = 938.7340515423407d;
  protected static final double INT16_TO_RPS = 0.0010652644360316954d;
  protected static final double RPSS_TO_INT16 = 10.430378350470454d;
  protected static final double INT16_TO_RPSS = 0.09587379924285257d;
  protected org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit _distanceUnit;
  protected org.firstinspires.ftc.robotcore.external.navigation.AngleUnit _angularUnit;
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS(com.qualcomm.robotcore.hardware.I2cDeviceSynch);
  protected boolean doInitialize();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public boolean begin();
  public boolean isConnected();
  public void getVersionInfo(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Version, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Version);
  public boolean selfTest();
  public boolean calibrateImu();
  public boolean calibrateImu(int, boolean);
  public int getImuCalibrationProgress();
  public org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit getLinearUnit();
  public void setLinearUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.AngleUnit getAngularUnit();
  public void setAngularUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public double getLinearScalar();
  public boolean setLinearScalar(double);
  public double getAngularScalar();
  public boolean setAngularScalar(double);
  public void resetTracking();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.SignalProcessConfig getSignalProcessConfig();
  public void setSignalProcessConfig(com.qualcomm.hardware.sparkfun.SparkFunOTOS.SignalProcessConfig);
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Status getStatus();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D getOffset();
  public void setOffset(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D);
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D getPosition();
  public void setPosition(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D);
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D getVelocity();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D getAcceleration();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D getPositionStdDev();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D getVelocityStdDev();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D getAccelerationStdDev();
  public void getPosVelAcc(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D);
  public void getPosVelAccStdDev(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D);
  public void getPosVelAccAndStdDev(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D);
  protected com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D readPoseRegs(byte, double, double);
  protected void writePoseRegs(byte, com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, double, double);
  protected com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D regsToPose(byte[], double, double);
  protected void poseToRegs(byte[], com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D, double, double);
}
```

## class SparkFunOTOS.Pose2D

```java
public class com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D {
  public double x;
  public double y;
  public double h;
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D(double, double, double);
  public void set(com.qualcomm.hardware.sparkfun.SparkFunOTOS.Pose2D);
  public java.lang.String toString();
}
```

## class SparkFunOTOS.SelfTestConfig

```java
public class com.qualcomm.hardware.sparkfun.SparkFunOTOS.SelfTestConfig {
  public boolean start;
  public boolean inProgress;
  public boolean pass;
  public boolean fail;
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.SelfTestConfig();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.SelfTestConfig(byte);
  public void set(byte);
  public byte get();
}
```

## class SparkFunOTOS.SignalProcessConfig

```java
public class com.qualcomm.hardware.sparkfun.SparkFunOTOS.SignalProcessConfig {
  public boolean enLut;
  public boolean enAcc;
  public boolean enRot;
  public boolean enVar;
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.SignalProcessConfig();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.SignalProcessConfig(byte);
  public void set(byte);
  public byte get();
}
```

## class SparkFunOTOS.Status

```java
public class com.qualcomm.hardware.sparkfun.SparkFunOTOS.Status {
  public boolean warnTiltAngle;
  public boolean warnOpticalTracking;
  public boolean errorPaa;
  public boolean errorLsm;
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Status();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Status(byte);
  public void set(byte);
  public byte get();
}
```

## class SparkFunOTOS.Version

```java
public class com.qualcomm.hardware.sparkfun.SparkFunOTOS.Version {
  public byte minor;
  public byte major;
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Version();
  public com.qualcomm.hardware.sparkfun.SparkFunOTOS.Version(byte);
  public void set(byte);
  public byte get();
}
```
