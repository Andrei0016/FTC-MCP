# Panels (bylazar)

`com.bylazar.*` — a live dashboard + telemetry + configurables system (the FTC-Dashboard
successor used in the reference repo). Docs: https://panels.bylazar.com

## Telemetry
```java
import com.bylazar.telemetry.PanelsTelemetry;
import com.bylazar.telemetry.TelemetryManager;

TelemetryManager tm = PanelsTelemetry.INSTANCE.getTelemetry();
tm.addData("key", value);
tm.update(telemetry);   // pass the OpMode's telemetry to also print on the DS
```
`Robot` holds the one `TelemetryManager` and passes it into every `Subsystem.update()`.

## Configurables (live-tunable constants)
```java
import com.bylazar.configurables.annotations.Configurable;
import com.bylazar.configurables.annotations.Sorter;

@Configurable
public class TurretConfig {
    @Sorter(sort = 1) public static double kP = 0.02;   // editable from the dashboard at runtime
}
```
- Only `public static` fields are exposed. `@Sorter(sort = n)` orders them in the UI.
- Rule: every tuned number in the codebase lives in a `@Configurable` config class, never
  inline in subsystem logic.

## Field drawing
The reference repo wraps Panels' canvas in `core/utils/Drawing.java` (`Drawing.init()`,
`Drawing.update(...)`) to draw robot + target poses on the field view.
