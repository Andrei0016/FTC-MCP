# `com.qualcomm.hardware.maxbotix`

_ftc-sdk 11.1.0 — 1 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class MaxSonarI2CXL

```java
public class com.qualcomm.hardware.maxbotix.MaxSonarI2CXL extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> {
  protected static final byte DEFAULT_I2C_ADDR = -32;
  protected static final byte CHANGE_I2C_ADDR_UNLOCK_1 = -86;
  protected static final byte CHANGE_I2C_ADDR_UNLOCK_2 = -91;
  protected static final byte CMD_PING = 81;
  protected static final byte NUM_RANGE_BYTES = 2;
  protected static int DEFAULT_SONAR_PROPAGATION_DELAY_MS;
  protected double lastDistance;
  protected long lastPingTime;
  public com.qualcomm.hardware.maxbotix.MaxSonarI2CXL(com.qualcomm.robotcore.hardware.I2cDeviceSynch);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  protected synchronized boolean doInitialize();
  public java.lang.String getDeviceName();
  protected void ping();
  protected double getRangingResult(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getDistanceSync(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getDistanceSync(int, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getDistanceAsync(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public double getDistanceAsync(int, org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public void setI2cAddress(com.qualcomm.robotcore.hardware.I2cAddr);
  public com.qualcomm.robotcore.hardware.I2cAddr getI2cAddress();
  public void writeI2cAddrToSensorEEPROM(byte);
}
```
