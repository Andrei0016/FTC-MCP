"""Turn extracted .class trees into per-package API digests.

Called by build.sh:  gen.py <manifest.json> <workdir> <out_sdk_dir>
For each lib: run `javap -protected -constants` on every allowlisted class, capture
the signature block, group by package, write Markdown + a _classes.json index.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

JAVAP = os.environ.get("JAVAP", "javap")

_DROP = re.compile(r"^\s*(Compiled from|descriptor:|Constant pool:|\s*$)")
_CLASS_DECL = re.compile(r"\b(class|interface|enum|@interface|record)\s+([\w.$]+)")


def fqcns_for(lib_classes: Path, include: list[str], exclude: list[str]) -> list[str]:
    out: list[str] = []
    for cf in lib_classes.rglob("*.class"):
        rel = cf.relative_to(lib_classes).with_suffix("")
        fq = str(rel).replace("/", ".")
        if re.search(r"\$\d", fq):  # anonymous / synthetic
            continue
        dotted = fq + "."
        if not any(dotted.startswith(p + ".") or fq == p or fq.startswith(p + ".") for p in include):
            continue
        if any(s in ("." + fq + ".") for s in exclude):
            continue
        out.append(fq)
    return sorted(set(out))


def run_javap(classpath: str, names: list[str]) -> str:
    chunks = []
    for i in range(0, len(names), 150):
        batch = names[i : i + 150]
        r = subprocess.run(
            [JAVAP, "-protected", "-constants", "-classpath", classpath, *batch],
            capture_output=True, text=True,
        )
        chunks.append(r.stdout)
    return "\n".join(chunks)


def split_blocks(javap_out: str) -> list[tuple[str, str, str, str]]:
    """-> list of (fqcn, kind, header_line, body). Splits on top-level class decls."""
    blocks: list[tuple[str, str, str, str]] = []
    cur_header = None
    cur_lines: list[str] = []

    def flush():
        if cur_header is None:
            return
        m = _CLASS_DECL.search(cur_header)
        kind = m.group(1) if m else "class"
        fq = m.group(2) if m else "?"
        body = "\n".join(l for l in cur_lines[1:] if not _DROP.match(l))
        blocks.append((fq, kind, cur_header.strip(), body.rstrip()))

    for line in javap_out.splitlines():
        if _CLASS_DECL.search(line) and not line.startswith(" ") and "{" in line:
            flush()
            cur_header = line
            cur_lines = [line]
        elif cur_header is not None:
            cur_lines.append(line)
    flush()
    return blocks


def header_meta(header: str) -> dict:
    ext = re.search(r"\bextends\s+([\w.$<>, ]+?)(?:\s+implements|\s*\{)", header)
    impl = re.search(r"\bimplements\s+([\w.$<>, ]+?)\s*\{", header)
    return {
        "extends": ext.group(1).strip() if ext else None,
        "implements": [x.strip() for x in impl.group(1).split(",")] if impl else [],
    }


def gen_lib(lib: str, version: str, work: Path, out: Path, include: list[str], exclude: list[str]) -> None:
    classes_dir = work / lib / "classes"
    jars = list((work / lib / "jars").glob("*.jar"))
    classpath = os.pathsep.join(str(j) for j in jars)
    names = fqcns_for(classes_dir, include, exclude)
    if not names:
        print(f"  {lib}: no classes matched"); return

    blocks = split_blocks(run_javap(classpath, names))
    by_pkg: dict[str, list] = {}
    index: dict[str, dict] = {}
    for fq, kind, header, body in blocks:
        pkg = fq.rsplit(".", 1)[0] if "." in fq else "(default)"
        by_pkg.setdefault(pkg, []).append((fq, kind, header, body))
        index[fq] = {"package": pkg, "kind": kind, **header_meta(header)}

    libdir = out / lib
    libdir.mkdir(parents=True, exist_ok=True)
    for f in libdir.glob("*.md"):
        f.unlink()

    for pkg, items in sorted(by_pkg.items()):
        items.sort()
        lines = [f"# `{pkg}`", "", f"_{lib} {version} — {len(items)} types. Signatures are exact "
                 f"(`javap -protected`); see `reference/{lib}/` for decompiled bodies._", ""]
        for fq, kind, header, body in items:
            simple = fq.rsplit(".", 1)[1]
            lines.append(f"## {kind} {simple.replace('$', '.')}")
            lines.append("")
            lines.append("```java")
            lines.append(header.replace("$", "."))
            for bl in body.splitlines():
                if bl.strip() in ("{", "}"):
                    continue
                lines.append(bl.replace("$", "."))
            lines.append("}")
            lines.append("```")
            lines.append("")
        (libdir / (pkg.replace(".", "_") + ".md")).write_text("\n".join(lines))

    idx = [f"# {lib} {version} — API index", "",
           f"{len(index)} team-facing types across {len(by_pkg)} packages. "
           f"Read a package file for exact signatures; use the `sdk_search` / `sdk_class` tools to dig in.", ""]
    for pkg, items in sorted(by_pkg.items()):
        idx.append(f"## `{pkg}`  ·  [{pkg.replace('.', '_')}.md]({pkg.replace('.', '_')}.md)")
        idx.append("")
        for fq, kind, *_ in sorted(items):
            idx.append(f"- {kind} `{fq.rsplit('.', 1)[1]}`")
        idx.append("")
    (libdir / "index.md").write_text("\n".join(idx))
    (libdir / "_classes.json").write_text(json.dumps(index, indent=1, sort_keys=True))
    print(f"  {lib}: {len(index)} types, {len(by_pkg)} packages")


def main() -> None:
    manifest, work, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    m = json.loads(manifest.read_text())
    for lib, cfg in m["libs"].items():
        gen_lib(lib, cfg["version"], work, out, cfg["include_prefixes"], cfg["exclude_substrings"])


if __name__ == "__main__":
    main()
