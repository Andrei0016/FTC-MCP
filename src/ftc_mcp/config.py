"""Runtime configuration, all overridable via environment variables."""

import os

# Starter repo cloned by `create_ftc_project`. Not created yet -> this is a documented
# placeholder. Override with FTC_STARTER_REPO_URL or the tool's `starter_repo_url` arg.
DEFAULT_STARTER_REPO_URL = "https://github.com/Andrei0016/ftc-starter"

# Default team base package used when a project doesn't override it.
DEFAULT_PACKAGE = "org.firstinspires.ftc.teamcode.robot"


def starter_repo_url() -> str:
    return os.environ.get("FTC_STARTER_REPO_URL", DEFAULT_STARTER_REPO_URL)


def default_package() -> str:
    return os.environ.get("FTC_PACKAGE", DEFAULT_PACKAGE)
