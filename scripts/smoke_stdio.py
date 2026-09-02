"""Minimal stdio smoke test: boot the server, list its tools/resources/prompts,
and call update_map on a throwaway project. No external deps.

    python scripts/smoke_stdio.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _rpc(proc: subprocess.Popen, method: str, params: dict | None = None, id_: int | None = 1):
    msg = {"jsonrpc": "2.0", "method": method}
    if id_ is not None:
        msg["id"] = id_
    if params is not None:
        msg["params"] = params
    proc.stdin.write(json.dumps(msg) + "\n")
    proc.stdin.flush()
    if id_ is None:
        return None
    return json.loads(proc.stdout.readline())


def main() -> int:
    proc = subprocess.Popen(
        [sys.executable, "-m", "ftc_mcp"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True,
        cwd=REPO,
    )
    try:
        init = _rpc(proc, "initialize", {
            "protocolVersion": "2024-11-05", "capabilities": {},
            "clientInfo": {"name": "smoke", "version": "0"},
        })
        print("server:", init["result"]["serverInfo"])
        _rpc(proc, "notifications/initialized", id_=None)

        tools = _rpc(proc, "tools/list", id_=2)["result"]["tools"]
        print("tools:", [t["name"] for t in tools])
        prompts = _rpc(proc, "prompts/list", id_=3)["result"]["prompts"]
        print("prompts:", [p["name"] for p in prompts])

        guide = _rpc(proc, "resources/read", {"uri": "ftc://guide/architecture"}, id_=4)
        assert "Subsystem" in guide["result"]["contents"][0]["text"]
        print("resource ftc://guide/architecture: OK")

        with tempfile.TemporaryDirectory() as d:
            res = _rpc(proc, "tools/call", {
                "name": "create_ftc_project",
                "arguments": {"target_dir": d, "team_package": "org.smoke.robot",
                              "starter_repo_url": "file:///nonexistent.git"},
            }, id_=5)
            text = res["result"]["content"][0]["text"]
            assert "FTC project ready" in text, text
            assert (Path(d) / "map/MAP.md").exists()
            print("create_ftc_project (skeleton fallback): OK")

        print("\nALL GOOD")
        return 0
    finally:
        proc.terminate()


if __name__ == "__main__":
    raise SystemExit(main())
