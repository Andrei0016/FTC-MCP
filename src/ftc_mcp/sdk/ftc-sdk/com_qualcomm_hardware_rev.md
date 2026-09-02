# `com.qualcomm.hardware.rev`

_ftc-sdk 11.1.0 — 14 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class Rev2mDistanceSensor

```java
public class com.qualcomm.hardware.rev.Rev2mDistanceSensor extends com.qualcomm.hardware.stmicroelectronics.VL53L0X {
  public com.qualcomm.hardware.rev.Rev2mDistanceSensor(com.qualcomm.robotcore.hardware.I2cDeviceSynch, boolean);
  public java.lang.String getDeviceName();
}
```

## class Rev9AxisImu

```java
public class com.qualcomm.hardware.rev.Rev9AxisImu extends com.qualcomm.hardware.bosch.BNO055IMUNew {
  public com.qualcomm.hardware.rev.Rev9AxisImu(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
}
```

## class Rev9AxisImuOrientationOnRobot

```java
public class com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot extends com.qualcomm.hardware.rev.RevImuOrientationOnRobot {
  public com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot(com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection, com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection);
  public com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot(org.firstinspires.ftc.robotcore.external.navigation.Orientation);
  public com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot(org.firstinspires.ftc.robotcore.external.navigation.Quaternion);
  protected static org.firstinspires.ftc.robotcore.external.navigation.Orientation friendlyApiToOrientation(com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection, com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation zyxOrientation(double, double, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation xyzOrientation(double, double, double);
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion angularVelocityTransform();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuRotationOffset();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuCoordinateSystemOrientationFromPerspectiveOfRobot();
}
```

## class Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection

```java
public final class com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection extends java.lang.Enum<com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection> {
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection UP;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection DOWN;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection FORWARD;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection BACKWARD;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection LEFT;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection RIGHT;
  public static com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection[] values();
  public static com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.I2cPortFacingDirection valueOf(java.lang.String);
}
```

## class Rev9AxisImuOrientationOnRobot.LogoFacingDirection

```java
public final class com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection extends java.lang.Enum<com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection> {
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection UP;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection DOWN;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection FORWARD;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection BACKWARD;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection LEFT;
  public static final com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection RIGHT;
  public static com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection[] values();
  public static com.qualcomm.hardware.rev.Rev9AxisImuOrientationOnRobot.LogoFacingDirection valueOf(java.lang.String);
}
```

## class RevBlinkinLedDriver

```java
public class com.qualcomm.hardware.rev.RevBlinkinLedDriver implements com.qualcomm.robotcore.hardware.HardwareDevice {
  protected static final java.lang.String TAG = "RevBlinkinLedDriver";
  protected static final double PULSE_WIDTH_INCREMENTOR = 5.0E-4d;
  protected static final double BASE_SERVO_POSITION = 0.2525d;
  protected static final int PATTERN_OFFSET = 10;
  protected com.qualcomm.robotcore.hardware.ServoControllerEx controller;
  public com.qualcomm.hardware.rev.RevBlinkinLedDriver(com.qualcomm.robotcore.hardware.ServoControllerEx, int);
  public void setPattern(com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```

## class RevBlinkinLedDriver.BlinkinPattern

```java
public final class com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern extends java.lang.Enum<com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern> {
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RAINBOW_RAINBOW_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RAINBOW_PARTY_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RAINBOW_OCEAN_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RAINBOW_LAVA_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RAINBOW_FOREST_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RAINBOW_WITH_GLITTER;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CONFETTI;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SHOT_RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SHOT_BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SHOT_WHITE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SINELON_RAINBOW_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SINELON_PARTY_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SINELON_OCEAN_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SINELON_LAVA_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SINELON_FOREST_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BEATS_PER_MINUTE_RAINBOW_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BEATS_PER_MINUTE_PARTY_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BEATS_PER_MINUTE_OCEAN_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BEATS_PER_MINUTE_LAVA_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BEATS_PER_MINUTE_FOREST_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern FIRE_MEDIUM;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern FIRE_LARGE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern TWINKLES_RAINBOW_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern TWINKLES_PARTY_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern TWINKLES_OCEAN_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern TWINKLES_LAVA_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern TWINKLES_FOREST_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern COLOR_WAVES_RAINBOW_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern COLOR_WAVES_PARTY_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern COLOR_WAVES_OCEAN_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern COLOR_WAVES_LAVA_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern COLOR_WAVES_FOREST_PALETTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern LARSON_SCANNER_RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern LARSON_SCANNER_GRAY;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern LIGHT_CHASE_RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern LIGHT_CHASE_BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern LIGHT_CHASE_GRAY;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern HEARTBEAT_RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern HEARTBEAT_BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern HEARTBEAT_WHITE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern HEARTBEAT_GRAY;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BREATH_RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BREATH_BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BREATH_GRAY;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern STROBE_RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern STROBE_BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern STROBE_GOLD;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern STROBE_WHITE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_END_TO_END_BLEND_TO_BLACK;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_LARSON_SCANNER;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_LIGHT_CHASE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_HEARTBEAT_SLOW;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_HEARTBEAT_MEDIUM;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_HEARTBEAT_FAST;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_BREATH_SLOW;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_BREATH_FAST;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_SHOT;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_STROBE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_END_TO_END_BLEND_TO_BLACK;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_LARSON_SCANNER;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_LIGHT_CHASE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_HEARTBEAT_SLOW;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_HEARTBEAT_MEDIUM;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_HEARTBEAT_FAST;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_BREATH_SLOW;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_BREATH_FAST;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_SHOT;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP2_STROBE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_SPARKLE_1_ON_2;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_SPARKLE_2_ON_1;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_COLOR_GRADIENT;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_BEATS_PER_MINUTE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_END_TO_END_BLEND_1_TO_2;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_END_TO_END_BLEND;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_NO_BLENDING;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_TWINKLES;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_COLOR_WAVES;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern CP1_2_SINELON;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern HOT_PINK;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern DARK_RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RED;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern RED_ORANGE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern ORANGE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern GOLD;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern YELLOW;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern LAWN_GREEN;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern LIME;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern DARK_GREEN;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern GREEN;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BLUE_GREEN;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern AQUA;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern SKY_BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern DARK_BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BLUE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BLUE_VIOLET;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern VIOLET;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern WHITE;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern GRAY;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern DARK_GRAY;
  public static final com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern BLACK;
  public static com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern[] values();
  public static com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern valueOf(java.lang.String);
  public static com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern fromNumber(int);
  public com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern next();
  public com.qualcomm.hardware.rev.RevBlinkinLedDriver.BlinkinPattern previous();
}
```

## class RevColorSensorV3

```java
public class com.qualcomm.hardware.rev.RevColorSensorV3 extends com.qualcomm.hardware.broadcom.BroadcomColorSensorImpl implements com.qualcomm.robotcore.hardware.DistanceSensor,com.qualcomm.robotcore.hardware.OpticalDistanceSensor,com.qualcomm.robotcore.hardware.ColorRangeSensor {
  protected static final double apiLevelMin = 0.0d;
  protected static final double apiLevelMax = 1.0d;
  public com.qualcomm.hardware.rev.RevColorSensorV3(com.qualcomm.robotcore.hardware.I2cDeviceSynchSimple, boolean);
  public java.lang.String getDeviceName();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public double getLightDetected();
  public double getRawLightDetected();
  public double getRawLightDetectedMax();
  public java.lang.String status();
  public double getDistance(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  protected double inFromOptical(int);
  public int rawOptical();
}
```

## class RevHubOrientationOnRobot

```java
public class com.qualcomm.hardware.rev.RevHubOrientationOnRobot extends com.qualcomm.hardware.rev.RevImuOrientationOnRobot {
  public com.qualcomm.hardware.rev.RevHubOrientationOnRobot(com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection, com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection);
  public com.qualcomm.hardware.rev.RevHubOrientationOnRobot(org.firstinspires.ftc.robotcore.external.navigation.Orientation);
  public com.qualcomm.hardware.rev.RevHubOrientationOnRobot(org.firstinspires.ftc.robotcore.external.navigation.Quaternion);
  protected static org.firstinspires.ftc.robotcore.external.navigation.Orientation friendlyApiToOrientation(com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection, com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation zyxOrientation(double, double, double);
  public static org.firstinspires.ftc.robotcore.external.navigation.Orientation xyzOrientation(double, double, double);
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion angularVelocityTransform();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuRotationOffset();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuCoordinateSystemOrientationFromPerspectiveOfRobot();
}
```

## class RevHubOrientationOnRobot.LogoFacingDirection

```java
public final class com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection extends java.lang.Enum<com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection> {
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection UP;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection DOWN;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection FORWARD;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection BACKWARD;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection LEFT;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection RIGHT;
  public static com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection[] values();
  public static com.qualcomm.hardware.rev.RevHubOrientationOnRobot.LogoFacingDirection valueOf(java.lang.String);
}
```

## class RevHubOrientationOnRobot.UsbFacingDirection

```java
public final class com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection extends java.lang.Enum<com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection> {
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection UP;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection DOWN;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection FORWARD;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection BACKWARD;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection LEFT;
  public static final com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection RIGHT;
  public static com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection[] values();
  public static com.qualcomm.hardware.rev.RevHubOrientationOnRobot.UsbFacingDirection valueOf(java.lang.String);
}
```

## class RevImuOrientationOnRobot

```java
abstract class com.qualcomm.hardware.rev.RevImuOrientationOnRobot implements com.qualcomm.robotcore.hardware.ImuOrientationOnRobot {
  protected com.qualcomm.hardware.rev.RevImuOrientationOnRobot(org.firstinspires.ftc.robotcore.external.navigation.Quaternion);
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuCoordinateSystemOrientationFromPerspectiveOfRobot();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion imuRotationOffset();
  public org.firstinspires.ftc.robotcore.external.navigation.Quaternion angularVelocityTransform();
}
```

## interface RevSPARKMini

```java
public interface com.qualcomm.hardware.rev.RevSPARKMini {
}
```

## class RevTouchSensor

```java
public class com.qualcomm.hardware.rev.RevTouchSensor implements com.qualcomm.robotcore.hardware.TouchSensor {
  public com.qualcomm.hardware.rev.RevTouchSensor(com.qualcomm.robotcore.hardware.DigitalChannelController, int);
  public double getValue();
  public boolean isPressed();
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  public java.lang.String getDeviceName();
  public java.lang.String getConnectionInfo();
  public int getVersion();
  public void resetDeviceConfigurationForOpMode();
  public void close();
}
```
