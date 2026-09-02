from ftc_mcp import render, schema


def _pm():
    return schema.ProjectMap(
        package="org.x",
        subsystems=[
            schema.Subsystem(name="Turret", hardware=["turretMotor"],
                             depends_on=["PIDF"], api=["aimAt(pose)"], summary="Aims."),
        ],
        hardware=[schema.Hardware(name="turretMotor", subsystem="Turret")],
        actions=[schema.Action(name="SHOOT", entrypoint="Robot.shoot()",
                               sequence="OPENING -> SHOOTING -> CLOSING", touches=["Turret"])],
        teleop=[schema.OpMode(cls="teleOpRED", alliance="RED", base="BaseTeleOp")],
        dataflow=[schema.DataFlow(src="Turret", dst="Turret", via="SubsystemData.goal")],
    )


def test_overview_lists_nodes():
    out = render.overview_mmd(_pm())
    assert out.startswith("flowchart TD")
    assert "Turret" in out and "turretMotor" in out and "teleOpRED" in out


def test_actions_statediagram():
    out = render.actions_mmd(_pm())
    assert "stateDiagram-v2" in out
    assert "OPENING --> SHOOTING" in out


def test_map_md_embeds_mermaid():
    md = render.map_md(_pm())
    assert "```mermaid" in md
    assert "## Subsystems" in md and "aimAt(pose)" in md


def test_render_all_keys():
    assert set(render.render_all(_pm())) == {
        "map/overview.mmd", "map/actions.mmd", "map/dataflow.mmd", "map/MAP.md",
    }
