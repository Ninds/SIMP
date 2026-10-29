from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sources() -> list[Path]:
    return sorted(ROOT.glob("[0-9][0-9]-*/*/*.tex"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Build every LaTeX document.")
    parser.add_argument("--clean", action="store_true", help="remove LaTeX auxiliaries")
    args = parser.parse_args()
    action = "-C" if args.clean else "-pdf"
    failures: list[Path] = []
    for source in sources():
        command = [
            "latexmk",
            action,
            "-interaction=nonstopmode",
            "-halt-on-error",
            source.name,
        ]
        result = subprocess.run(command, cwd=source.parent, check=False)
        if result.returncode:
            failures.append(source)
    if failures:
        print("Failed:")
        for source in failures:
            print(f"  {source.relative_to(ROOT)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
