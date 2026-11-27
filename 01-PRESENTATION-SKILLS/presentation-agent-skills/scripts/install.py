#!/usr/bin/env python3
"""Install one or more skills from this repository into an Agent skill directory."""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"


def available_skills() -> list[str]:
    return sorted(
        path.name
        for path in SKILLS_ROOT.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills", nargs="*", help="Skill names to install")
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.home() / ".codex" / "skills",
        help="Destination skill directory (default: ~/.codex/skills)",
    )
    parser.add_argument("--all", action="store_true", help="Install every skill")
    parser.add_argument("--list", action="store_true", help="List bundled skills and exit")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Back up and replace existing skills",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    available = available_skills()

    if args.list:
        for name in available:
            print(name)
        return 0

    selected = available if args.all else args.skills
    if not selected:
        raise SystemExit("Choose one or more skill names, or pass --all.")

    unknown = sorted(set(selected) - set(available))
    if unknown:
        raise SystemExit(f"Unknown skill(s): {', '.join(unknown)}")

    destination_root = args.dest.expanduser().resolve()
    destination_root.mkdir(parents=True, exist_ok=True)
    backup_root = destination_root.parent / f"{destination_root.name}-backups"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    installed = 0
    skipped = 0
    for name in dict.fromkeys(selected):
        source = SKILLS_ROOT / name
        destination = destination_root / name

        if destination.exists() or destination.is_symlink():
            if not args.force:
                print(f"skip: {name} already exists at {destination}")
                skipped += 1
                continue
            backup = backup_root / timestamp / name
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(destination), str(backup))
            print(f"backup: {destination} -> {backup}")

        shutil.copytree(source, destination, symlinks=False)
        print(f"installed: {name} -> {destination}")
        installed += 1

    print(f"done: {installed} installed, {skipped} skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
