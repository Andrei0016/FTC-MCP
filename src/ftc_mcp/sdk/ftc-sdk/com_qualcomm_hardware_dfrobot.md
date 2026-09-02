# `com.qualcomm.hardware.dfrobot`

_ftc-sdk 11.1.0 — 4 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class HuskyLens

```java
public class com.qualcomm.hardware.dfrobot.HuskyLens extends com.qualcomm.robotcore.hardware.I2cDeviceSynchDevice<com.qualcomm.robotcore.hardware.I2cDeviceSynch> {
  protected final int DEFAULT_I2C_ADDR = 50;
  public com.qualcomm.hardware.dfrobot.HuskyLens(com.qualcomm.robotcore.hardware.I2cDeviceSynch);
  public com.qualcomm.robotcore.hardware.HardwareDevice.Manufacturer getManufacturer();
  protected synchronized boolean doInitialize();
  public java.lang.String getDeviceName();
  public boolean knock();
  public void selectAlgorithm(com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm);
  public com.qualcomm.hardware.dfrobot.HuskyLens.Block[] blocks();
  public com.qualcomm.hardware.dfrobot.HuskyLens.Block[] blocks(int);
  public com.qualcomm.hardware.dfrobot.HuskyLens.Arrow[] arrows();
  public com.qualcomm.hardware.dfrobot.HuskyLens.Arrow[] arrows(int);
  protected byte[] readInfo();
  protected com.qualcomm.hardware.dfrobot.HuskyLens.Block[] readBlocksResponse();
  protected com.qualcomm.hardware.dfrobot.HuskyLens.Arrow[] readArrowsResponse();
  protected void sendCommand(byte);
  protected void sendCommandWithData(byte, byte, byte);
}
```

## class HuskyLens.Algorithm

```java
public final class com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm extends java.lang.Enum<com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm> {
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm FACE_RECOGNITION;
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm OBJECT_TRACKING;
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm OBJECT_RECOGNITION;
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm LINE_TRACKING;
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm COLOR_RECOGNITION;
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm TAG_RECOGNITION;
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm OBJECT_CLASSIFICATION;
  public static final com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm NONE;
  public byte bVal;
  public static com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm[] values();
  public static com.qualcomm.hardware.dfrobot.HuskyLens.Algorithm valueOf(java.lang.String);
}
```

## class HuskyLens.Arrow

```java
public class com.qualcomm.hardware.dfrobot.HuskyLens.Arrow {
  public final int x_origin;
  public final int y_origin;
  public final int x_target;
  public final int y_target;
  public final int id;
  public com.qualcomm.hardware.dfrobot.HuskyLens.Arrow(com.qualcomm.hardware.dfrobot.HuskyLens, byte[]);
  public java.lang.String toString();
}
```

## class HuskyLens.Block

```java
public class com.qualcomm.hardware.dfrobot.HuskyLens.Block {
  public final int x;
  public final int y;
  public final int width;
  public final int height;
  public final int top;
  public final int left;
  public final int id;
  public com.qualcomm.hardware.dfrobot.HuskyLens.Block(com.qualcomm.hardware.dfrobot.HuskyLens, byte[]);
  public java.lang.String toString();
}
```
