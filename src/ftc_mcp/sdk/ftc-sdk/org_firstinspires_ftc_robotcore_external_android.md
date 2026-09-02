# `org.firstinspires.ftc.robotcore.external.android`

_ftc-sdk 11.1.0 — 5 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class AndroidAccelerometer

```java
public class org.firstinspires.ftc.robotcore.external.android.AndroidAccelerometer implements android.hardware.SensorEventListener {
  public org.firstinspires.ftc.robotcore.external.android.AndroidAccelerometer();
  public void onAccuracyChanged(android.hardware.Sensor, int);
  public void onSensorChanged(android.hardware.SensorEvent);
  public void setDistanceUnit(org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit getDistanceUnit();
  public double getX();
  public double getY();
  public double getZ();
  public org.firstinspires.ftc.robotcore.external.navigation.Acceleration getAcceleration();
  public boolean isAvailable();
  public void startListening();
  public void stopListening();
}
```

## class AndroidGyroscope

```java
public class org.firstinspires.ftc.robotcore.external.android.AndroidGyroscope implements android.hardware.SensorEventListener {
  public org.firstinspires.ftc.robotcore.external.android.AndroidGyroscope();
  public void onAccuracyChanged(android.hardware.Sensor, int);
  public void onSensorChanged(android.hardware.SensorEvent);
  public void setAngleUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.AngleUnit getAngleUnit();
  public float getX();
  public float getY();
  public float getZ();
  public org.firstinspires.ftc.robotcore.external.navigation.AngularVelocity getAngularVelocity();
  public boolean isAvailable();
  public void startListening();
  public void stopListening();
}
```

## class AndroidOrientation

```java
public class org.firstinspires.ftc.robotcore.external.android.AndroidOrientation implements android.hardware.SensorEventListener {
  public org.firstinspires.ftc.robotcore.external.android.AndroidOrientation();
  public void onAccuracyChanged(android.hardware.Sensor, int);
  public void onSensorChanged(android.hardware.SensorEvent);
  public void setAngleUnit(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.navigation.AngleUnit getAngleUnit();
  public double getAzimuth();
  public double getPitch();
  public double getRoll();
  public double getAngle();
  public double getMagnitude();
  public boolean isAvailable();
  public void startListening();
  public void stopListening();
}
```

## class AndroidSoundPool

```java
public class org.firstinspires.ftc.robotcore.external.android.AndroidSoundPool {
  public static final java.lang.String RAW_RES_PREFIX = "RawRes:";
  public org.firstinspires.ftc.robotcore.external.android.AndroidSoundPool();
  public void initialize(org.firstinspires.ftc.robotcore.internal.android.SoundPoolIntf);
  public boolean preloadSound(java.lang.String);
  public boolean play(java.lang.String);
  public void stop();
  public float getVolume();
  public void setVolume(float);
  public float getRate();
  public void setRate(float);
  public int getLoop();
  public void setLoop(int);
  public void close();
}
```

## class AndroidTextToSpeech

```java
public class org.firstinspires.ftc.robotcore.external.android.AndroidTextToSpeech {
  public org.firstinspires.ftc.robotcore.external.android.AndroidTextToSpeech();
  public synchronized void initialize();
  public synchronized java.lang.String getStatus();
  public synchronized java.lang.String getLanguageCode();
  public synchronized java.lang.String getCountryCode();
  public synchronized boolean isSpeaking();
  public synchronized void stop();
  public synchronized void setPitch(float);
  public synchronized void setSpeechRate(float);
  public synchronized boolean isLanguageAvailable(java.lang.String);
  public synchronized boolean isLanguageAndCountryAvailable(java.lang.String, java.lang.String);
  public synchronized boolean isLocaleAvailable(java.util.Locale);
  public synchronized void setLanguage(java.lang.String);
  public synchronized void setLanguageAndCountry(java.lang.String, java.lang.String);
  public synchronized void speak(java.lang.String);
  public synchronized void close();
}
```
