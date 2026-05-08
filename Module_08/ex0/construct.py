#!/usr/bin/env python3

import sys
import os
import site


def is_in_venv() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def get_venv_name() -> str:
    venv_path = os.environ.get("VIRTUAL_ENV", "")
    return os.path.basename(venv_path) if venv_path else ""


def get_site_packages() -> str:
    packages = site.getsitepackages() if hasattr(site, "getsitepackages") else []
    return packages[0] if packages else site.getusersitepackages()


def show_outside_venv() -> None:
    global_packages = get_site_packages()

    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("Global package installation path:")
    print(global_packages)
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print(r"matrix_env\Scripts\activate  # On Windows")
    print()
    print("Then run this program again.")


def show_inside_venv() -> None:
    venv_name = get_venv_name()
    venv_path = os.environ.get("VIRTUAL_ENV", "")
    pkg_path = get_site_packages()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(pkg_path)


def main() -> None:
    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
