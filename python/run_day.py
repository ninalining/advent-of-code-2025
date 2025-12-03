#!/usr/bin/env python3
"""
Dispatch script to run a specific Advent of Code Python solution.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    """Run the specified day's solution script."""
    day_arg = sys.argv[1] if len(sys.argv) > 1 else "01"
    day = day_arg.zfill(2)

    script_path = Path(__file__).parent / f"day{day}" / f"day{day}.py"
    if not script_path.exists():
        print(f"No Python solution found for day {day}. Expected file: {script_path}")
        return 1

    result = subprocess.run([sys.executable, str(script_path)], check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
