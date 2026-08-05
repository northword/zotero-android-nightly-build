#!/usr/bin/env python3
"""Sync the build steps in .github/workflows/ci.yml from the upstream
zotero-android android.yml.

Everything between the markers

    # ===== auto-synced from upstream android.yml (managed by scripts/sync_ci.py) =====
    ...
    # ===== end auto-synced =====

is regenerated from upstream, so the environment setup steps (JDK, Python,
setup-* actions) and the bundle build steps stay in sync with upstream.

The following upstream steps are intentionally EXCLUDED because this repo is a
debug-only nightly build without upstream's secrets:
  - the checkout step (this repo checks out the upstream repo explicitly)
  - any step referencing ${{secrets.* }} (PSPDFKit key, keystore, google-services)
  - the Google Play deploy step (publishInternalReleaseBundle)

The rest of ci.yml (triggers, cache check, assembleDebug, upload, release) is
preserved exactly as-is.

Usage:
    python3 scripts/sync_ci.py .github/workflows/ci.yml upstream-android.yml
"""

import sys

STEP_INDENT = "      "
START_MARKER = "# ===== auto-synced from upstream android.yml (managed by scripts/sync_ci.py) ====="
END_MARKER = "# ===== end auto-synced ====="


def is_synced_step(block):
    text = "\n".join(block)
    if "actions/checkout" in text:
        return False
    if "${{secrets." in text:
        return False
    if "publishInternalReleaseBundle" in text:
        return False
    return True


def extract_build_steps(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    blocks = []
    current = None
    for line in lines:
        if line.startswith(STEP_INDENT + "- "):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append(current)

    return [block for block in blocks if is_synced_step(block)]


def splice(ci_lines, steps):
    out = []
    in_section = False
    inserted = False
    for line in ci_lines:
        if line.strip() == START_MARKER:
            in_section = True
            inserted = True
            out.append(line)
            for block in steps:
                out.extend(block)
            continue
        if line.strip() == END_MARKER:
            in_section = False
            out.append(line)
            continue
        if in_section:
            continue
        out.append(line)
    if not inserted:
        raise SystemExit(
            f"START_MARKER not found in ci.yml; cannot auto-sync. "
            f"Expected: {START_MARKER}"
        )
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    ci_path, upstream_path = sys.argv[1], sys.argv[2]

    steps = extract_build_steps(upstream_path)
    with open(ci_path, encoding="utf-8") as f:
        ci_lines = f.read().splitlines()
    new_lines = splice(ci_lines, steps)

    with open(ci_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new_lines) + "\n")
    print(f"Synced {len(steps)} bundle steps from {upstream_path} into {ci_path}.")


if __name__ == "__main__":
    main()
