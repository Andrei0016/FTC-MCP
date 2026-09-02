# `com.qualcomm.hardware.andymark`

_ftc-sdk 11.1.0 — 8 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class AndyMarkColorSensor

```java
public class com.qualcomm.hardware.andymark.AndyMarkColorSensor extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> implements com.qualcomm.robotcore.hardware.ColorRangeSensor, com.qualcomm.robotcore.hardware.DistanceSensor, com.qualcomm.robotcore.hardware.ColorSensor {
  public com.qualcomm.hardware.andymark.AndyMarkColorSensor(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  protected boolean doInitialize();
  public java.lang.String classifyColor();
  public int argb();
  public com.qualcomm.robotcore.hardware.NormalizedRGBA getNormalizedColors();
  public int alpha();
  public double getRawLightDetected();
  public double getLightDetected();
  public double getRawLightDetectedMax();
  public int red();
  public int green();
  public int blue();
  public void enableLed(boolean);
  public void setGain(float);
  public float getGain();
  public double getDistance(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public int getProximity();
  public void setProximityGain(com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain);
  public void setProximityLedPulses(int);
  public void setProximityLedPulseLength(com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength);
  public void configureProximitySettings(com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain, int, com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength);
  public java.lang.String status();
}
```

## class AndyMarkColorSensor.ProximityGain

```java
public final class com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain extends java.lang.Enum<com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain> {
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain GAIN_1X;
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain GAIN_2X;
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain GAIN_4X;
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain GAIN_8X;
  public final int bits;
  public static com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain[] values();
  public static com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityGain valueOf(java.lang.String);
}
```

## class AndyMarkColorSensor.ProximityPulseLength

```java
public final class com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength extends java.lang.Enum<com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength> {
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength LENGTH_4US;
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength LENGTH_8US;
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength LENGTH_16US;
  public static final com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength LENGTH_32US;
  public final int bits;
  public static com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength[] values();
  public static com.qualcomm.hardware.andymark.AndyMarkColorSensor.ProximityPulseLength valueOf(java.lang.String);
}
```

## class AndyMarkIMU

```java
public class com.qualcomm.hardware.andymark.AndyMarkIMU extends com.qualcomm.hardware.bosch.BNO055IMUNew {
  public com.qualcomm.hardware.andymark.AndyMarkIMU(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
}
```

## class AndyMarkIMUOrientationOnRobot

```java
public class com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot implements com.qualcomm.robotcore.hardware.ImuOrientationOnRobot {
  public com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot(com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection, com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection);
  public com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot(org.firstinspires.ftc.robotcore.external.navigation.Orientation);
  public com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot(org.firstinspires.ftc.robotcore.external.navigation.Quaternion);
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuCoordinateSystemOrientationFromPerspectiveOfRobot();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuRotationOffset();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion angularVelocityTransform();
  protected static org.firstinspires.ftc.robotcore.external.navigation.Orientation friendlyApiToOrientation(com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection, com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation zyxOrientation(double, double, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation xyzOrientation(double, double, double);
}
```

## class AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection

```java
public final class com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection extends java.lang.Enum<com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection> {
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection UP;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection DOWN;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection FORWARD;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection BACKWARD;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection LEFT;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection RIGHT;
  public static com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection[] values();
  public static com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.I2cPortFacingDirection valueOf(java.lang.String);
}
```

## class AndyMarkIMUOrientationOnRobot.LogoFacingDirection

```java
public final class com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection extends java.lang.Enum<com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection> {
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection UP;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection DOWN;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection FORWARD;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection BACKWARD;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection LEFT;
  public static final com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection RIGHT;
  public static com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection[] values();
  public static com.qualcomm.hardware.andymark.AndyMarkIMUOrientationOnRobot.LogoFacingDirection valueOf(java.lang.String);
}
```

## class AndyMarkTOF

```java
public class com.qualcomm.hardware.andymark.AndyMarkTOF extends com.qualcomm.hardware.stmicroelectronics.VL53L0X {
  public com.qualcomm.hardware.andymark.AndyMarkTOF(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  public java.lang.String getDeviceName();
}
```
