"""Access to the generated SDK reference under ftc_mcp/sdk/.

Digests (exact `javap` signatures + class index) ship with the package. The full
CFR-decompiled source under <repo>/reference/ is optional (gitignored, produced by
tools/gen_reference/build.sh) and used only when present locally.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

_SDK = Path(__file__).parent.parent / "sdk"
LIBS = ("ftc-sdk", "pedro-pathing", "panels")


def _lib_dir(lib: str) -> Path:
    if lib not in LIBS:
        raise ValueError(f"unknown lib '{lib}'. Options: {', '.join(LIBS)}")
    return _SDK / lib


def list_libs() -> str:
    out = ["# SDK reference", "", "Generated from the artifacts pinned in "
           "`tools/gen_reference/manifest.json` (Pedro Pathing Quickstart versions).", ""]
    for lib in LIBS:
        idx = _lib_dir(lib) / "_classes.json"
        n = len(json.loads(idx.read_text())) if idx.exists() else 0
        out.append(f"- **{lib}** — {n} team-facing types. "
                   f"Index: `ftc://sdk/{lib}`. Packages: `ftc://sdk/{lib}/<package>`.")
    out.append("")
    out.append("Tools: `sdk_search(query)` to find a class/method, "
               "`sdk_class(fqcn)` for one type's full signature block.")
    return "\n".join(out)


def lib_index(lib: str) -> str:
    p = _lib_dir(lib) / "index.md"
    if not p.exists():
        raise ValueError(f"no index for {lib} — run tools/gen_reference/build.sh")
    return p.read_text()


def package_digest(lib: str, package: str) -> str:
    fname = package.replace(".", "_") + ".md"
    p = _lib_dir(lib) / fname
    if not p.exists():
        raise ValueError(f"no package '{package}' in {lib}. See ftc://sdk/{lib} for the list.")
    return p.read_text()


def _all_digest_files() -> list[tuple[str, Path]]:
    return [(lib, f) for lib in LIBS for f in sorted(_lib_dir(lib).glob("*.md"))
            if f.name != "index.md"]


def search(query: str, lib: str = "") -> str:
    """Case-insensitive substring search across every signature line."""
    libs = [lib] if lib else list(LIBS)
    for l in libs:
        if l not in LIBS:
            raise ValueError(f"unknown lib '{l}'")
    rx = re.compile(re.escape(query), re.I)
    hits: list[str] = []
    kind, name = "", ""
    for l, f in _all_digest_files():
        if lib and l != lib:
            continue
        pkg = f.stem.replace("_", ".")
        for line in f.read_text().splitlines():
            if line.startswith("## "):
                parts = line[3:].strip().split(" ", 1)
                kind, name = (parts + [""])[:2] if len(parts) == 2 else ("class", parts[0])
                if rx.search(name):
                    hits.append(f"[{l}] {kind} {pkg}.{name}")
            elif (line.startswith("  ") or line.startswith("public ")) and rx.search(line):
                sig = line.strip()
                if sig:
                    hits.append(f"[{l}] {pkg}.{name} ({kind})\n    {sig}")
            if len(hits) >= 200:
                hits.append("… (truncated at 200; narrow the query or pass lib=)")
                return "\n".join(hits)
    return "\n".join(hits) if hits else f"No matches for '{query}'" + (f" in {lib}" if lib else "")


def find_class(fqcn: str) -> tuple[str, str] | None:
    """-> (lib, package) for a fully-qualified class name, or None."""
    for lib in LIBS:
        idx = _lib_dir(lib) / "_classes.json"
        if not idx.exists():
            continue
        data = json.loads(idx.read_text())
        if fqcn in data:
            return lib, data[fqcn]["package"]
        # allow simple name
        matches = [k for k in data if k.rsplit(".", 1)[-1] == fqcn]
        if len(matches) == 1:
            return lib, data[matches[0]]["package"]
    return None


def class_block(fqcn: str) -> str:
    found = find_class(fqcn)
    if not found:
        return f"'{fqcn}' not found. Try sdk_search('{fqcn.rsplit('.', 1)[-1]}')."
    lib, package = found
    simple = fqcn.rsplit(".", 1)[-1]
    text = package_digest(lib, package)
    # slice out the "## ... <simple>" section
    lines = text.splitlines()
    want = simple.replace("$", ".")
    start = next((i for i, x in enumerate(lines)
                  if x.startswith("## ") and x.rstrip().split(" ")[-1] == want), None)
    if start is None:
        return f"{fqcn} is in {lib}/{package} but no signature block was found."
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    block = "\n".join(lines[start:end]).rstrip()

    src = _decompiled_source_path(lib, fqcn)
    footer = f"\n\n_Decompiled source: `{src}`_" if src else (
        "\n\n_(Full decompiled body not available locally — run "
        "`tools/gen_reference/build.sh` to produce `reference/`.)_")
    return f"{block}\n\n_Package digest: `ftc://sdk/{lib}/{package}`_{footer}"


def _decompiled_source_path(lib: str, fqcn: str) -> str | None:
    top = fqcn.split(".")[0]  # 'com'
    rel = fqcn.replace(".", "/") + ".java"
    for base in (_SDK.parent.parent.parent / "reference" / lib,):  # <repo>/reference/<lib>
        cand = base / rel
        if cand.exists():
            return str(cand)
    return None
