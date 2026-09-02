"""Map rendering / validation tools."""

from __future__ import annotations

from pathlib import Path

import yaml

from .. import render, schema


def update_map(project_dir: str) -> str:
    """Validate `map/project-map.yaml` and regenerate every `map/` output."""
    pm = schema.load(project_dir)
    errors = schema.validate(pm, project_dir)
    written = render.write_all(project_dir, pm)

    out = [f"Regenerated: {', '.join(written)}"]
    if errors:
        out.append("")
        out.append(f"⚠️  {len(errors)} map validation issue(s) — fix the YAML:")
        out += [f"  - {e}" for e in errors]
    else:
        out.append("Map is valid.")
    return "\n".join(out)


def render_map(yaml_text: str) -> str:
    """Pure preview: YAML text -> the four generated files, no disk writes."""
    pm = schema.ProjectMap.from_dict(yaml.safe_load(yaml_text) or {})
    errors = schema.validate(pm)
    parts = []
    if errors:
        parts.append("Validation issues:\n" + "\n".join(f"  - {e}" for e in errors) + "\n")
    for rel, content in render.render_all(pm).items():
        parts.append(f"===== {rel} =====\n{content}")
    return "\n".join(parts)
