#!/usr/bin/env python3
"""
Ren'Py Script Hygiene & Formatter
Safely cleans up trailing whitespaces, converts tab characters to 4 spaces,
ensures single newline at EOF, and validates syntax with Ren'Py lint.
"""

import os
import sys
import argparse
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME_DIR = os.path.join(PROJECT_ROOT, "game")

IGNORED_FILES = {
    "_mcp_bridge.rpy",
    "mcp_bridge.rpy",
}

IGNORED_DIRS = {
    "cache",
    "saves",
    "_mcp",
}


def get_rpy_files(target_dir):
    rpy_files = []
    for root, dirs, files in os.walk(target_dir):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith(".")]
        for f in sorted(files):
            if f.endswith(".rpy") and f not in IGNORED_FILES:
                rpy_files.append(os.path.join(root, f))
    return rpy_files


def format_file(file_path, check_only=False):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    new_lines = []
    modified = False

    for line in lines:
        # Convert tabs to 4 spaces (Ren'Py standard)
        expanded_line = line.replace("\t", "    ")
        # Strip trailing whitespaces
        cleaned_line = expanded_line.rstrip()
        if cleaned_line != line:
            modified = True
        new_lines.append(cleaned_line)

    # Ensure single newline at end of file if not empty
    new_content = "\n".join(new_lines)
    if new_content and not new_content.endswith("\n"):
        new_content += "\n"

    if new_content != content:
        modified = True

    if modified and not check_only:
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)

    return modified


def main():
    parser = argparse.ArgumentParser(description="Clean and format Ren'Py (.rpy) script files.")
    parser.add_argument("--check", action="store_true", help="Only check for formatting issues without modifying files.")
    parser.add_argument("--lint", action="store_true", help="Run Ren'Py SDK lint after formatting.")
    args = parser.parse_args()

    files = get_rpy_files(GAME_DIR)
    modified_count = 0

    print(f"Scanning {len(files)} Ren'Py files in game/...")

    for file_path in files:
        rel_path = os.path.relpath(file_path, PROJECT_ROOT)
        was_modified = format_file(file_path, check_only=args.check)
        if was_modified:
            modified_count += 1
            status = "[NEEDS CLEANUP]" if args.check else "[CLEANED]"
            print(f"  {status} {rel_path}")

    if args.check:
        if modified_count > 0:
            print(f"\nFound {modified_count} file(s) with trailing spaces or tab issues.")
            sys.exit(1)
        else:
            print("\nAll Ren'Py files are clean and properly formatted.")
    else:
        print(f"\nSuccessfully cleaned {modified_count} file(s).")

    if args.lint:
        sdk_path = os.path.expanduser("~/Documents/renpy-8.5.3-sdk/renpy.sh")
        if os.path.exists(sdk_path):
            print("\nRunning Ren'Py lint to verify syntax integrity...")
            result = subprocess.run([sdk_path, PROJECT_ROOT, "lint"])
            if result.returncode != 0:
                print("Ren'Py lint detected errors!", file=sys.stderr)
                sys.exit(result.returncode)
            print("Ren'Py lint passed successfully!")


if __name__ == "__main__":
    main()
