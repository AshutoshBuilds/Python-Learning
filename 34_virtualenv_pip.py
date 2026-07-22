"""
Lesson 34: Virtual Environments and pip
=======================================
Commerce focus: Keep project dependencies isolated (pandas, matplotlib, etc.).
"""

import platform
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# CONCEPT
# ---------------------------------------------------------------------------
# A virtual environment (venv) is a private Python folder with its own pip
# packages — avoids version conflicts between school projects and work tools.
#
# Windows commands (run in PowerShell or CMD from project folder):
#
#   python -m venv .venv          # create venv named .venv
#   .venv\Scripts\activate      # activate (prompt shows (.venv))
#   pip install pandas matplotlib
#   pip freeze > requirements.txt   # save installed versions
#   deactivate                    # leave venv
#
# On another PC:
#   python -m venv .venv
#   .venv\Scripts\activate
#   pip install -r requirements.txt
#
# pip installs packages from PyPI (Python Package Index).
# Always activate venv before pip install so packages land in the project.
# ---------------------------------------------------------------------------

EXAMPLE_REQUIREMENTS = """\
# requirements.txt — pin versions for reproducible installs
pandas>=2.0
matplotlib>=3.8
openpyxl>=3.1
requests>=2.31
"""


def main() -> None:
    # LIVE DEMOS
    print("LIVE DEMO — Your Python environment")
    print(f"  Python version : {sys.version.split()[0]}")
    print(f"  Executable     : {sys.executable}")
    print(f"  Platform       : {platform.system()} {platform.release()}")
    print(f"  Project folder : {Path(__file__).parent.resolve()}")

    print("\nLIVE DEMO — sys.path (where Python looks for modules)")
    for i, entry in enumerate(sys.path[:6], start=1):
        print(f"  {i}. {entry}")
    if len(sys.path) > 6:
        print(f"  ... and {len(sys.path) - 6} more entries")

    in_venv = hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix
    print(f"\n  Running inside venv? {'Yes' if in_venv else 'No (system Python)'}")

    print("\nLIVE DEMO — Example requirements.txt snippet")
    print(EXAMPLE_REQUIREMENTS)

    print("Quick reference — Windows venv workflow:")
    print("  1. cd Python-Course")
    print("  2. python -m venv .venv")
    print("  3. .venv\\Scripts\\activate")
    print("  4. pip install -r requirements.txt")

    # -----------------------------------------------------------------------
    # EXERCISES — solutions in comments
    # -----------------------------------------------------------------------
    # 1) Create a venv in this folder and verify sys.prefix changes after activate.
    # 2) Run `pip list` and note which packages are installed.
    #
    # Solution 1:
    #   Before activate: in_venv is False
    #   After activate:  in_venv is True, executable points to .venv\Scripts\python
    #
    # Solution 2:
    #   pip list | findstr pandas   (Windows)
    # -----------------------------------------------------------------------

    # MINI CHALLENGE
    # Create requirements.txt with only pandas and matplotlib, install them
    # in a fresh venv, and run lesson 31 to confirm matplotlib works.


if __name__ == "__main__":
    main()
