"""Append-to-LOG.md tool."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

LOG_RELPATH = "LOG.md"
_HEADER = "# Change Log\n\nNewest first. One entry per change: the prompt, Claude's reply, and the files touched.\n"


def log_change(
    project_dir: str,
    prompt: str,
    response: str,
    changes: list[str],
    title: str | None = None,
    map_updated: bool = True,
) -> str:
    """Prepend a dated entry to LOG.md."""
    log = Path(project_dir) / LOG_RELPATH
    existing = log.read_text() if log.exists() else _HEADER

    body = existing[len(_HEADER):] if existing.startswith(_HEADER) else ("\n" + existing)

    stamp = datetime.now().strftime("%Y-%m-%dT%H:%M")
    title = title or (prompt.strip().splitlines()[0][:80] if prompt.strip() else "change")
    entry = [
        f"## {stamp} — {title}",
        "",
        f"**Prompt:** {prompt.strip() or '(none)'}",
        "",
        f"**Claude's reply:** {response.strip() or '(none)'}",
        "",
        "**Changed:**",
    ]
    entry += [f"- {c}" for c in changes] or ["- (none)"]
    entry += ["", f"**Map updated:** {'yes' if map_updated else 'no'}", "", ""]

    log.write_text(_HEADER + "\n" + "\n".join(entry) + body)
    return f"Logged '{title}' to {LOG_RELPATH}."
