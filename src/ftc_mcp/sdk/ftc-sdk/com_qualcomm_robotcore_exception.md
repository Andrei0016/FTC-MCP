# `com.qualcomm.robotcore.exception`

_ftc-sdk 11.1.0 — 4 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class DuplicateNameException

```java
public class com.qualcomm.robotcore.exception.DuplicateNameException extends java.lang.RuntimeException {
  public com.qualcomm.robotcore.exception.DuplicateNameException(java.lang.String);
  public com.qualcomm.robotcore.exception.DuplicateNameException(java.lang.String, java.lang.Object...);
}
```

## class RobotCoreException

```java
public class com.qualcomm.robotcore.exception.RobotCoreException extends java.lang.Exception {
  public com.qualcomm.robotcore.exception.RobotCoreException(java.lang.String);
  public com.qualcomm.robotcore.exception.RobotCoreException(java.lang.String, java.lang.Throwable);
  public com.qualcomm.robotcore.exception.RobotCoreException(java.lang.String, java.lang.Object...);
  public static com.qualcomm.robotcore.exception.RobotCoreException createChained(java.lang.Exception, java.lang.String, java.lang.Object...);
}
```

## class RobotProtocolException

```java
public class com.qualcomm.robotcore.exception.RobotProtocolException extends java.lang.Exception {
  public com.qualcomm.robotcore.exception.RobotProtocolException(java.lang.String);
  public com.qualcomm.robotcore.exception.RobotProtocolException(java.lang.String, java.lang.Object...);
}
```

## class TargetPositionNotSetException

```java
public class com.qualcomm.robotcore.exception.TargetPositionNotSetException extends java.lang.RuntimeException {
  public com.qualcomm.robotcore.exception.TargetPositionNotSetException();
}
```
