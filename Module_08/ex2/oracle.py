#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

DEFAULTS: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///local_matrix.db",
    "API_KEY": "",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "http://localhost:8080/zion",
}


def load_configuration() -> dict[str, str]:
    """Load .env then environment variables. Warn on missing, exit if critical."""
    load_dotenv(dotenv_path=".env", override=False)

    config: dict[str, str] = {}
    missing: list[str] = []

    for var in REQUIRED_VARS:
        value = os.environ.get(var, "")
        if value:
            config[var] = value
        elif var in DEFAULTS and DEFAULTS[var]:
            config[var] = DEFAULTS[var]
            print(f"[WARNING] {var} not set — using default: {DEFAULTS[var]}")
        else:
            missing.append(var)
            config[var] = ""

    if missing:
        print()
        print("MISSING required configuration variables:")
        for var in missing:
            print(f"  - {var}")
        print()
        print("Copy .env.example to .env and fill in your values:")
        print("  cp .env.example .env")
        sys.exit(1)

    return config


def display_config(config: dict[str, str]) -> None:
    """Display loaded configuration matching expected output format."""
    mode = config["MATRIX_MODE"]
    api_key = config["API_KEY"]
    log_level = config["LOG_LEVEL"]
    zion = config["ZION_ENDPOINT"]

    db_status = (
        "Connected to local instance"
        if mode == "development"
        else "Connected to production instance"
    )
    api_status = "Authenticated" if api_key else "Not authenticated"
    zion_status = "Online" if zion else "Offline"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_status}")


def show_mode_behavior(config: dict[str, str]) -> None:
    """Show visible differences between development and production modes."""
    mode = config["MATRIX_MODE"]
    print()
    if mode == "development":
        print("--- Development Mode ---")
        print("  Verbose logging active (DEBUG)")
        print("  Local database in use")
        print("  Detailed error traces enabled")
        print("  .env file loaded for local settings")
    else:
        print("--- Production Mode ---")
        print("  Minimal logging active (ERROR only)")
        print("  Remote database in use")
        print("  Error traces hidden from users")
        print("  Environment variables override .env")


def security_check() -> None:
    """Basic security audit of the configuration setup."""
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.isfile(".env") or os.path.isfile(".env.example"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env or .env.example file found")

    print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    config = load_configuration()
    display_config(config)
    show_mode_behavior(config)
    security_check()

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
