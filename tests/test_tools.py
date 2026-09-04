import subprocess

import pytest

from ftc_mcp.tools import changelog, mapping, project, subsystem


@pytest.fixture
def proj(tmp_path):
    # Force the skeleton fallback with an unreachable repo.
    out = project.create_ftc_project(
        str(tmp_path), team_package="org.demo.robot",
        starter_repo_url="file:///nonexistent/repo.git", project_name="Demo",
    )
    assert "FTC project ready" in out
    return tmp_path


def test_project_scaffold(proj):
    assert (proj / "map/project-map.yaml").exists()
    assert (proj / "map/MAP.md").exists()
    assert (proj / "LOG.md").exists()
    assert (proj / ".claude/agents/plan-critic.md").exists()
    assert (proj / ".claude/agents/plan-pro-advocate.md").exists()
    assert (proj / "CLAUDE.md").read_text().count("org.demo.robot")
    assert (proj / "TeamCode/src/main/java/org/demo/robot/core/Robot.java").exists()


def test_new_subsystem_registers_and_renders(proj):
    out = subsystem.new_subsystem(str(proj), "lift", hardware=["liftMotor", "grip:Servo"],
                                  has_states=True, summary="Two-stage lift.")
    assert "Lift.java" in out
    lift = proj / "TeamCode/src/main/java/org/demo/robot/subsystems/Lift/Lift.java"
    assert lift.exists() and "implements Subsystem" in lift.read_text()
    map_md = (proj / "map/MAP.md").read_text()
    assert "Lift" in map_md and "liftMotor" in map_md
    assert "Map is valid." in mapping.update_map(str(proj))


@pytest.mark.parametrize("name", ["Drivetrain", "drive", "Chassis", "swerve"])
def test_new_subsystem_refuses_drivetrain(proj, name):
    with pytest.raises(ValueError, match="Pedro Follower"):
        subsystem.new_subsystem(str(proj), name)


def test_log_change_prepends(proj):
    changelog.log_change(str(proj), "add lift", "added Lift subsystem",
                         ["subsystems/Lift/Lift.java — new"])
    changelog.log_change(str(proj), "tweak", "changed power", ["LiftConfig.java — power"])
    text = (proj / "LOG.md").read_text()
    assert text.index("tweak") < text.index("add lift")  # newest first


def test_render_map_pure(proj):
    yaml_text = (proj / "map/project-map.yaml").read_text()
    out = mapping.render_map(yaml_text)
    assert "map/overview.mmd" in out and "flowchart TD" in out
