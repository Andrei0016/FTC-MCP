# FTC SDK — the parts you actually use

Docs: https://ftc-docs.firstinspires.org · Javadoc: https://javadoc.io/doc/org.firstinspires.ftc

## OpMode lifecycle
`OpMode` (iterative): `init()` → `init_loop()`* → `start()` → `loop()`* → `stop()`.
`LinearOpMode`: one `runOpMode()` with `waitForStart()` — the reference style uses
iterative `OpMode` for both teleop and auto.

Annotations: `@TeleOp(name=…, group=…)`, `@Autonomous(name=…)`, `@Disabled`.

## Hardware access (in `Robot`'s constructor only)
- `hardwareMap.get(DcMotorEx.class, "name")`, `Servo`, `CRServo`, `AnalogInput`,
  `DigitalChannel`, `RevColorSensorV3`, `Rev2mDistanceSensor`, `IMU`, `Limelight3A`.
- `DcMotorEx`: `setMode(RUN_WITHOUT_ENCODER | STOP_AND_RESET_ENCODER | RUN_USING_ENCODER)`,
  `setZeroPowerBehavior(BRAKE|FLOAT)`, `setDirection`, `setPower`, `getCurrentPosition`,
  `getVelocity`, `setCurrentAlert` / `getCurrent`.
- `Servo`: `setPosition(0..1)`, `scaleRange`. `CRServo`: `setPower`.

## Performance
- `for (LynxModule h : hardwareMap.getAll(LynxModule.class)) h.setBulkCachingMode(AUTO);`
  once in the constructor — turns many reads into one bus transaction.
- `ElapsedTime` for loop dt and timeouts.
- `com.qualcomm.robotcore.util.Range.clip(v, lo, hi)`.

## Gamepad
`gamepad1.left_stick_y` etc.; edge helpers `xWasPressed()`, `dpadUpWasPressed()`,
`rightBumperWasReleased()`; `rumble*`.

## Robot configuration
Names used in `hardwareMap.get(..., "name")` must match the config on the Driver Hub.
