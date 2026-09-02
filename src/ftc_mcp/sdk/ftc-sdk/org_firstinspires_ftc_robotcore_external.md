# `org.firstinspires.ftc.robotcore.external`

_ftc-sdk 11.1.0 — 33 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class BlocksOpModeCompanion

```java
public abstract class org.firstinspires.ftc.robotcore.external.BlocksOpModeCompanion {
  public static com.qualcomm.robotcore.eventloop.opmode.OpMode opMode;
  public static com.qualcomm.robotcore.eventloop.opmode.LinearOpMode linearOpMode;
  public static com.qualcomm.robotcore.hardware.HardwareMap hardwareMap;
  public static org.firstinspires.ftc.robotcore.external.Telemetry telemetry;
  public static com.qualcomm.robotcore.hardware.Gamepad gamepad1;
  public static com.qualcomm.robotcore.hardware.Gamepad gamepad2;
  public org.firstinspires.ftc.robotcore.external.BlocksOpModeCompanion();
}
```

## class ClassFactory

```java
public abstract class org.firstinspires.ftc.robotcore.external.ClassFactory {
  public org.firstinspires.ftc.robotcore.external.ClassFactory();
  public static org.firstinspires.ftc.robotcore.external.ClassFactory getInstance();
  public abstract org.firstinspires.ftc.robotcore.external.hardware.camera.CameraManager getCameraManager();
  public static org.firstinspires.ftc.robotcore.external.hardware.camera.CameraName createSwitchableCameraNameForAllWebcams(com.qualcomm.robotcore.hardware.HardwareMap);
}
```

## class ClassFactory.InstanceHolder

```java
public class org.firstinspires.ftc.robotcore.external.ClassFactory.InstanceHolder {
  public static org.firstinspires.ftc.robotcore.external.ClassFactory theInstance;
  protected org.firstinspires.ftc.robotcore.external.ClassFactory.InstanceHolder();
}
```

## interface Const

```java
public interface org.firstinspires.ftc.robotcore.external.Const extends java.lang.annotation.Annotation {
}
```

## interface Consumer

```java
public interface org.firstinspires.ftc.robotcore.external.Consumer<T> {
  public abstract void accept(T);
}
```

## interface Event

```java
public interface org.firstinspires.ftc.robotcore.external.Event {
  public abstract java.lang.String getName();
}
```

## interface ExportAprilTagLibraryToBlocks

```java
public interface org.firstinspires.ftc.robotcore.external.ExportAprilTagLibraryToBlocks extends java.lang.annotation.Annotation {
  public abstract int color();
  public abstract java.lang.String heading();
  public abstract java.lang.String comment();
  public abstract java.lang.String tooltip();
  public abstract java.lang.String[] parameterLabels();
  public abstract java.lang.String[] parameterDefaultValues();
}
```

## interface ExportClassToBlocks

```java
public interface org.firstinspires.ftc.robotcore.external.ExportClassToBlocks extends java.lang.annotation.Annotation {
}
```

## interface ExportEnumToBlocks

```java
public interface org.firstinspires.ftc.robotcore.external.ExportEnumToBlocks extends java.lang.annotation.Annotation {
  public abstract int color();
}
```

## interface ExportToBlocks

```java
public interface org.firstinspires.ftc.robotcore.external.ExportToBlocks extends java.lang.annotation.Annotation {
  public abstract int color();
  public abstract java.lang.String heading();
  public abstract java.lang.String comment();
  public abstract java.lang.String tooltip();
  public abstract java.lang.String[] parameterLabels();
  public abstract java.lang.String[] parameterDefaultValues();
}
```

## interface Func

```java
public interface org.firstinspires.ftc.robotcore.external.Func<T> {
  public abstract T value();
}
```

## interface Function

```java
public interface org.firstinspires.ftc.robotcore.external.Function<T, R> {
  public abstract R apply(T);
}
```

## class JavaUtil

```java
public class org.firstinspires.ftc.robotcore.external.JavaUtil {
  public org.firstinspires.ftc.robotcore.external.JavaUtil();
  public static java.lang.String inTextGetLetter(java.lang.String, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int);
  public static java.lang.String inTextGetSubstring(java.lang.String, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int);
  public static java.lang.String toTitleCase(java.lang.String);
  public static java.lang.String textTrim(java.lang.String, org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode);
  public static java.lang.String formatNumber(double, int);
  public static java.lang.String formatNumber(double, int, int);
  public static boolean isPrime(double);
  public static double sumOfList(java.util.List);
  public static double minOfList(java.util.List);
  public static double maxOfList(java.util.List);
  public static double averageOfList(java.util.List);
  public static double medianOfList(java.util.List);
  public static java.util.List modesOfList(java.util.List);
  public static double standardDeviationOfList(java.util.List);
  public static java.lang.Object randomItemOfList(java.util.List);
  public static int randomInt(double, double);
  public static java.util.List createListWith(java.lang.Object...);
  public static java.util.List createListWithItemRepeated(java.lang.Object, int);
  public static int listLength(java.lang.Object);
  public static boolean listIsEmpty(java.lang.Object);
  public static java.lang.Object inListGet(java.util.List, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int, boolean);
  public static void inListSet(java.util.List, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int, boolean, java.lang.Object);
  public static java.util.List inListGetSublist(java.util.List, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int);
  public static java.util.List sort(java.util.List, org.firstinspires.ftc.robotcore.external.JavaUtil.SortType, org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection);
  public static java.lang.String makeTextFromList(java.util.List, java.lang.String);
  public static java.lang.String makeTextFromList(double[], java.lang.String);
  public static java.util.List makeListFromText(java.lang.String, java.lang.String);
  public static float colorToHue(int);
  public static float colorToSaturation(int);
  public static float colorToValue(int);
  public static int hsvToColor(float, float, float);
  public static int ahsvToColor(int, float, float, float);
  public static float rgbToHue(int, int, int);
  public static float rgbToSaturation(int, int, int);
  public static float rgbToValue(int, int, int);
  public static java.lang.String colorToText(int);
  public static void showColor(android.content.Context, int);
  public static java.util.List<java.lang.Integer> makeIntegerList(int[]);
  public static int[] makeIntArray(java.util.List<java.lang.Integer>);
  public static double[] makeDoubleArray(java.util.List<java.lang.Double>);
  public static double sumOfList(java.lang.Object[]);
  public static double minOfList(java.lang.Object[]);
  public static double maxOfList(java.lang.Object[]);
  public static double averageOfList(java.lang.Object[]);
  public static double medianOfList(java.lang.Object[]);
  public static java.util.List modesOfList(java.lang.Object[]);
  public static double standardDeviationOfList(java.lang.Object[]);
  public static java.lang.Object randomItemOfList(java.lang.Object[]);
  public static java.lang.Object inListGet(java.lang.Object[], org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int, boolean);
  public static void inListSet(java.lang.Object[], org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int, boolean, java.lang.Object);
  public static java.util.List inListGetSublist(java.lang.Object[], org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int, org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode, int);
  public static java.lang.Object[] sort(java.lang.Object[], org.firstinspires.ftc.robotcore.external.JavaUtil.SortType, org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection);
  public static java.lang.String makeTextFromList(java.lang.Object[], java.lang.String);
}
```

## class JavaUtil.AtMode

```java
public final class org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode> {
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode FIRST;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode LAST;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode FROM_START;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode FROM_END;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode RANDOM;
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode[] values();
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.AtMode valueOf(java.lang.String);
}
```

## class JavaUtil.SortDirection

```java
public final class org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection> {
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection ASCENDING;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection DESCENDING;
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection[] values();
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.SortDirection valueOf(java.lang.String);
}
```

## class JavaUtil.SortType

```java
public final class org.firstinspires.ftc.robotcore.external.JavaUtil.SortType extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.JavaUtil.SortType> {
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.SortType NUMERIC;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.SortType TEXT;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.SortType IGNORE_CASE;
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.SortType[] values();
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.SortType valueOf(java.lang.String);
}
```

## class JavaUtil.TrimMode

```java
public final class org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode> {
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode LEFT;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode RIGHT;
  public static final org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode BOTH;
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode[] values();
  public static org.firstinspires.ftc.robotcore.external.JavaUtil.TrimMode valueOf(java.lang.String);
}
```

## interface NonConst

```java
public interface org.firstinspires.ftc.robotcore.external.NonConst extends java.lang.annotation.Annotation {
}
```

## interface Predicate

```java
public interface org.firstinspires.ftc.robotcore.external.Predicate<T> {
  public abstract boolean test(T);
}
```

## class SignificantMotionDetection

```java
public class org.firstinspires.ftc.robotcore.external.SignificantMotionDetection {
  public org.firstinspires.ftc.robotcore.external.SignificantMotionDetection();
  public void startListening();
  public void stopListening();
  public void registerListener(org.firstinspires.ftc.robotcore.external.SignificantMotionDetection.SignificantMotionDetectionListener);
  protected void notifyListeners();
}
```

## interface SignificantMotionDetection.SignificantMotionDetectionListener

```java
public interface org.firstinspires.ftc.robotcore.external.SignificantMotionDetection.SignificantMotionDetectionListener {
  public abstract void onSignificantMotion();
}
```

## class SignificantMotionDetection.TriggerListener

```java
class org.firstinspires.ftc.robotcore.external.SignificantMotionDetection.TriggerListener extends android.hardware.TriggerEventListener {
  public void onTrigger(android.hardware.TriggerEvent);
}
```

## interface State

```java
public interface org.firstinspires.ftc.robotcore.external.State {
  public abstract void onEnter(org.firstinspires.ftc.robotcore.external.Event);
  public abstract void onExit(org.firstinspires.ftc.robotcore.external.Event);
}
```

## class StateMachine

```java
public class org.firstinspires.ftc.robotcore.external.StateMachine {
  protected org.firstinspires.ftc.robotcore.external.State currentState;
  protected java.util.HashMap<org.firstinspires.ftc.robotcore.external.State, java.util.ArrayList<org.firstinspires.ftc.robotcore.external.StateTransition>> stateGraph;
  protected java.util.ArrayList<org.firstinspires.ftc.robotcore.external.Event> maskList;
  public org.firstinspires.ftc.robotcore.external.StateMachine();
  protected void start(org.firstinspires.ftc.robotcore.external.State);
  public void addTransition(org.firstinspires.ftc.robotcore.external.StateTransition);
  public org.firstinspires.ftc.robotcore.external.State consumeEvent(org.firstinspires.ftc.robotcore.external.Event);
  public void maskEvent(org.firstinspires.ftc.robotcore.external.Event);
  public void unMaskEvent(org.firstinspires.ftc.robotcore.external.Event);
  protected org.firstinspires.ftc.robotcore.external.State transition(org.firstinspires.ftc.robotcore.external.Event);
  public java.lang.String toString();
}
```

## class StateTransition

```java
public class org.firstinspires.ftc.robotcore.external.StateTransition {
  protected org.firstinspires.ftc.robotcore.external.State from;
  protected org.firstinspires.ftc.robotcore.external.Event event;
  protected org.firstinspires.ftc.robotcore.external.State to;
  public org.firstinspires.ftc.robotcore.external.StateTransition(org.firstinspires.ftc.robotcore.external.State, org.firstinspires.ftc.robotcore.external.Event, org.firstinspires.ftc.robotcore.external.State);
  public java.lang.String toString();
}
```

## interface Supplier

```java
public interface org.firstinspires.ftc.robotcore.external.Supplier<T> {
  public abstract T get();
}
```

## interface Telemetry

```java
public interface org.firstinspires.ftc.robotcore.external.Telemetry {
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, java.lang.Object...);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.Object);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public abstract boolean removeItem(org.firstinspires.ftc.robotcore.external.Telemetry.Item);
  public abstract void clear();
  public abstract void clearAll();
  public abstract java.lang.Object addAction(java.lang.Runnable);
  public abstract boolean removeAction(java.lang.Object);
  public abstract void speak(java.lang.String);
  public abstract void speak(java.lang.String, java.lang.String, java.lang.String);
  public abstract boolean update();
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Line addLine();
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Line addLine(java.lang.String);
  public abstract boolean removeLine(org.firstinspires.ftc.robotcore.external.Telemetry.Line);
  public abstract boolean isAutoClear();
  public abstract void setAutoClear(boolean);
  public abstract int getMsTransmissionInterval();
  public abstract void setMsTransmissionInterval(int);
  public abstract java.lang.String getItemSeparator();
  public abstract void setItemSeparator(java.lang.String);
  public abstract java.lang.String getCaptionValueSeparator();
  public abstract void setCaptionValueSeparator(java.lang.String);
  public abstract void setDisplayFormat(org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat);
  public default void setNumDecimalPlaces(int, int);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Log log();
}
```

## class Telemetry.DisplayFormat

```java
public final class org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat> {
  public static final org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat CLASSIC;
  public static final org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat MONOSPACE;
  public static final org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat HTML;
  public static org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat[] values();
  public static org.firstinspires.ftc.robotcore.external.Telemetry.DisplayFormat valueOf(java.lang.String);
}
```

## interface Telemetry.Item

```java
public interface org.firstinspires.ftc.robotcore.external.Telemetry.Item {
  public abstract java.lang.String getCaption();
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item setCaption(java.lang.String);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item setValue(java.lang.String, java.lang.Object...);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item setValue(java.lang.Object);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item setValue(org.firstinspires.ftc.robotcore.external.Func<T>);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item setValue(java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item setRetained(java.lang.Boolean);
  public abstract boolean isRetained();
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, java.lang.Object...);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.Object);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
}
```

## interface Telemetry.Line

```java
public interface org.firstinspires.ftc.robotcore.external.Telemetry.Line {
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, java.lang.Object...);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.Object);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
  public abstract <T> org.firstinspires.ftc.robotcore.external.Telemetry.Item addData(java.lang.String, java.lang.String, org.firstinspires.ftc.robotcore.external.Func<T>);
}
```

## interface Telemetry.Log

```java
public interface org.firstinspires.ftc.robotcore.external.Telemetry.Log {
  public abstract int getCapacity();
  public abstract void setCapacity(int);
  public abstract org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder getDisplayOrder();
  public abstract void setDisplayOrder(org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder);
  public abstract void add(java.lang.String);
  public abstract void add(java.lang.String, java.lang.Object...);
  public abstract void clear();
}
```

## class Telemetry.Log.DisplayOrder

```java
public final class org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder extends java.lang.Enum<org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder> {
  public static final org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder NEWEST_FIRST;
  public static final org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder OLDEST_FIRST;
  public static org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder[] values();
  public static org.firstinspires.ftc.robotcore.external.Telemetry.Log.DisplayOrder valueOf(java.lang.String);
}
```

## interface ThrowingCallable

```java
public interface org.firstinspires.ftc.robotcore.external.ThrowingCallable<VALUE, EXCEPTION extends java.lang.Throwable> {
  public abstract VALUE call() throws EXCEPTION;
}
```
