"""Scaffold a new subsystem folder (Subsystem + Config) and register it in the map."""

from __future__ import annotations

from pathlib import Path

from .. import schema
from . import mapping

_TMPL_DIR = Path(__file__).parent.parent / "templates" / "subsystem"

_HW_IMPORTS = {
    "DcMotorEx": "com.qualcomm.robotcore.hardware.DcMotorEx",
    "DcMotor": "com.qualcomm.robotcore.hardware.DcMotor",
    "Servo": "com.qualcomm.robotcore.hardware.Servo",
    "CRServo": "com.qualcomm.robotcore.hardware.CRServo",
    "AnalogInput": "com.qualcomm.robotcore.hardware.AnalogInput",
    "DigitalChannel": "com.qualcomm.robotcore.hardware.DigitalChannel",
    "ColorSensor": "com.qualcomm.robotcore.hardware.ColorSensor",
    "DistanceSensor": "com.qualcomm.robotcore.hardware.DistanceSensor",
    "IMU": "com.qualcomm.robotcore.hardware.IMU",
}


def _parse_hw(items: list[str]) -> list[tuple[str, str]]:
    """['liftMotor', 'grip:Servo'] -> [('liftMotor','DcMotorEx'), ('grip','Servo')]"""
    out = []
    for it in items:
        if ":" in it:
            name, typ = it.split(":", 1)
        else:
            name, typ = it, "DcMotorEx"
        out.append((name.strip(), typ.strip()))
    return out


def _fill(tmpl: str, repl: dict[str, str]) -> str:
    for k, v in repl.items():
        tmpl = tmpl.replace(f"<<{k}>>", v)
    return tmpl


def new_subsystem(
    project_dir: str,
    name: str,
    hardware: list[str] | None = None,
    has_states: bool = False,
    summary: str = "",
) -> str:
    name = name[0].upper() + name[1:]
    lname = name[0].lower() + name[1:]
    hw = _parse_hw(hardware or [])
    summary = summary or f"{name} subsystem."

    pm = schema.load(project_dir)
    package = pm.package or "org.firstinspires.ftc.teamcode.robot"

    imports = sorted({_HW_IMPORTS.get(t, f"com.qualcomm.robotcore.hardware.{t}") for _, t in hw})
    hw_imports = "\n".join(f"import {i};" for i in imports)
    hw_fields = "\n".join(f"    private final {t} {n};" for n, t in hw)
    ctor_params = ", ".join(f"{t} {n}" for n, t in hw) or ""
    ctor_body = "\n".join(f"        this.{n} = {n};" for n, t in hw) or "        // no hardware yet"
    state_field = (
        f"    private enum State {{ IDLE, RUNNING }}\n    private State state = State.IDLE;\n"
        if has_states else ""
    )

    repl = {
        "PACKAGE": package,
        "NAME": name,
        "name": lname,
        "SUMMARY": summary,
        "HW_IMPORTS": hw_imports,
        "HW_FIELDS": hw_fields,
        "STATE_FIELD": state_field,
        "CTOR_PARAMS": ctor_params,
        "CTOR_BODY": ctor_body,
    }

    sub_rel = f"TeamCode/src/main/java/{package.replace('.', '/')}/subsystems/{name}"
    root = Path(project_dir)
    (root / sub_rel).mkdir(parents=True, exist_ok=True)

    sub_java = _fill((_TMPL_DIR / "Subsystem.java.tmpl").read_text(), repl)
    cfg_java = _fill((_TMPL_DIR / "SubsystemConfig.java.tmpl").read_text(), repl)
    (root / sub_rel / f"{name}.java").write_text(sub_java)
    (root / sub_rel / f"{name}Config.java").write_text(cfg_java)

    # register in the map
    src_file = f"{sub_rel}/{name}.java"
    cfg_file = f"{sub_rel}/{name}Config.java"
    pm.subsystems = [s for s in pm.subsystems if s.name != name]
    pm.subsystems.append(
        schema.Subsystem(
            name=name, file=src_file, config=cfg_file,
            hardware=[n for n, _ in hw],
            states=["IDLE", "RUNNING"] if has_states else [],
            api=["enable()", "disable()", "isBusy()"],
            summary=summary,
        )
    )
    existing_hw = {h.name for h in pm.hardware}
    for n, t in hw:
        if n not in existing_hw:
            pm.hardware.append(schema.Hardware(name=n, type=t, subsystem=name))
    schema.dump(project_dir, pm)
    map_result = mapping.update_map(project_dir)

    return (
        f"Created:\n  {src_file}\n  {cfg_file}\n\n"
        f"{map_result}\n\n"
        f"Next steps:\n"
        f"  1. Wire {name} into core/Robot.java (field, construct from hardwareMap, call update()).\n"
        f"  2. Add config names to the robot configuration on the Driver Hub: "
        f"{', '.join(n for n, _ in hw) or '(none)'}.\n"
        f"  3. Call log_change with your prompt, reply and this file list."
    )
