#!/usr/bin/env bash
# Regenerate the SDK reference (API digests + decompiled source) from the pinned
# artifacts in manifest.json. Needs: bash, curl, unzip, a JDK 11+ (javap), python3.
#
#   tools/gen_reference/build.sh
#
# Outputs:
#   src/ftc_mcp/sdk/<lib>/*.md       committed API digests (exact signatures)
#   reference/<lib>/                 CFR-decompiled source (gitignored, for deep dives)
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
CACHE="$HERE/.cache"
WORK="$CACHE/work"
mkdir -p "$CACHE" "$WORK"

# ── locate a JDK ───────────────────────────────────────────────────────────
if [ -z "${JAVA_HOME:-}" ] || [ ! -x "${JAVA_HOME:-}/bin/javap" ]; then
  if [ -x /usr/libexec/java_home ]; then JAVA_HOME="$(/usr/libexec/java_home 2>/dev/null || true)"; fi
fi
if [ -z "${JAVA_HOME:-}" ] || [ ! -x "$JAVA_HOME/bin/javap" ]; then
  echo "No JDK found. Set JAVA_HOME to a JDK 11+ (macOS: brew install --cask temurin)." >&2
  exit 1
fi
JAVAP="$JAVA_HOME/bin/javap"
JAVA="$JAVA_HOME/bin/java"
echo "JDK: $($JAVA -version 2>&1 | head -1)"

fetch() {  # url -> cached file path on stdout
  local url="$1"
  local dest="$CACHE/$(basename "$url")"
  [ -f "$dest" ] || curl -sSL -o "$dest" "$url"
  echo "$dest"
}

CFR_URL="$(sed -n 's/.*"cfr":[[:space:]]*"\([^"]*\)".*/\1/p' "$HERE/manifest.json")"
CFR="$(fetch "$CFR_URL")"

# ── per-lib: download, extract class jars, decompile ───────────────────────
python3 -c '
import json, sys
m = json.load(open(sys.argv[1]))
for lib, cfg in m["libs"].items():
    print(lib, cfg["version"], *cfg["artifacts"], sep="\t")
' "$HERE/manifest.json" | while IFS=$'\t' read -r lib version rest; do
  echo "=== $lib ($version) ==="
  libwork="$WORK/$lib"; rm -rf "$libwork"; mkdir -p "$libwork/jars" "$libwork/classes"
  for url in $rest; do
    art="$(fetch "$url")"
    case "$art" in
      *.aar) tmp="$(mktemp -d)"; unzip -oq "$art" -d "$tmp"; cp "$tmp/classes.jar" "$libwork/jars/$(basename "${art%.aar}").jar"; rm -rf "$tmp" ;;
      *.jar) cp "$art" "$libwork/jars/$(basename "$art")" ;;
    esac
  done
  # explode all class files onto one tree (for FQCN discovery)
  for j in "$libwork"/jars/*.jar; do (cd "$libwork/classes" && unzip -oq "$j" '*.class' || true); done
  # decompile every jar -> reference/<lib>/
  refdir="$ROOT/reference/$lib"; rm -rf "$refdir"; mkdir -p "$refdir"
  for j in "$libwork"/jars/*.jar; do
    "$JAVA" -jar "$CFR" "$j" --outputdir "$refdir" --caseinsensitivefs true --silent true 2>/dev/null || true
  done
  echo "  decompiled -> reference/$lib/"
done

# ── generate digests ──────────────────────────────────────────────────────
JAVAP="$JAVAP" python3 "$HERE/gen.py" "$HERE/manifest.json" "$WORK" "$ROOT/src/ftc_mcp/sdk"
echo "Done. Digests in src/ftc_mcp/sdk/, decompiled source in reference/ (gitignored)."
