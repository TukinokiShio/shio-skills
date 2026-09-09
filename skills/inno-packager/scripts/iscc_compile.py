#!/usr/bin/env python3
"""Compile an Inno Setup script without assuming a machine-specific path."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def resolve_iscc(explicit: str | None) -> str | None:
    if explicit:
        candidate = Path(explicit).expanduser()
        return str(candidate) if candidate.is_file() else None

    on_path = shutil.which("ISCC.exe")
    if on_path:
        return on_path

    roots = [os.environ.get("ProgramFiles"), os.environ.get("ProgramFiles(x86)"), os.environ.get("LOCALAPPDATA")]
    for root in filter(None, roots):
        for relative in (Path("Inno Setup 6") / "ISCC.exe", Path("Programs") / "Inno Setup 6" / "ISCC.exe"):
            candidate = Path(root) / relative
            if candidate.is_file():
                return str(candidate)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile an Inno Setup script")
    parser.add_argument("script", help="Path to the .iss script")
    parser.add_argument("--output", "-O", help="Output directory")
    parser.add_argument("--define", "-D", action="append", default=[], help="NAME or NAME=VALUE")
    parser.add_argument("--iscc", help="Explicit path to ISCC.exe")
    args = parser.parse_args()

    compiler = resolve_iscc(args.iscc)
    if not compiler:
        print("ERROR: ISCC.exe was not found. Install Inno Setup 6, add it to PATH, or pass --iscc.", file=sys.stderr)
        return 1

    script = Path(args.script).expanduser().resolve()
    if not script.is_file():
        print(f"ERROR: Script file not found: {script}", file=sys.stderr)
        return 2

    command = [compiler, str(script)]
    command.extend(f"/D{value}" for value in args.define)
    output_dir = None
    if args.output:
        output_dir = Path(args.output).expanduser().resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        command.append(f"/O{output_dir}")

    print(f"Compiling: {script}")
    print(f"ISCC: {compiler}")
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
    except OSError as exc:
        print(f"ERROR: Could not execute ISCC.exe: {exc}", file=sys.stderr)
        return 3

    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="")
    if result.returncode:
        print(f"Compilation failed with exit code {result.returncode}", file=sys.stderr)
    elif output_dir:
        print(f"Output directory: {output_dir}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
