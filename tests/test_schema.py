from ftc_mcp import schema


def _pm(**kw):
    base = dict(
        package="org.x",
        subsystems=[schema.Subsystem(name="Lift", hardware=["liftMotor"])],
        hardware=[schema.Hardware(name="liftMotor", type="DcMotorEx", subsystem="Lift")],
    )
    base.update(kw)
    return schema.ProjectMap(**base)


def test_valid_map_has_no_errors():
    assert schema.validate(_pm()) == []


def test_unknown_hardware_subsystem_flagged():
    pm = _pm(hardware=[schema.Hardware(name="liftMotor", subsystem="Nope")])
    errs = schema.validate(pm)
    assert any("Nope" in e for e in errs)


def test_subsystem_hardware_must_exist():
    pm = _pm(hardware=[])
    assert any("liftMotor" in e for e in schema.validate(pm))


def test_roundtrip_dict():
    pm = _pm(
        teleop=[schema.OpMode(cls="teleOpRED", alliance="RED", base="BaseTeleOp")],
        dataflow=[schema.DataFlow(src="Lift", dst="Lift", via="SubsystemData.h")],
    )
    again = schema.ProjectMap.from_dict(pm.to_dict())
    assert again.teleop[0].cls == "teleOpRED"
    assert again.dataflow[0].via == "SubsystemData.h"


def test_auto_routine_reference_checked():
    pm = _pm(auto=[schema.OpMode(cls="RedAuto", routine="Missing")])
    assert any("Missing" in e for e in schema.validate(pm))
