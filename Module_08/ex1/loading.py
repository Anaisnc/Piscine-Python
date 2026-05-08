#!/usr/bin/env python3

import sys
import importlib


PACKAGES: list[tuple[str, str, bool]] = [
    ("pandas", "Data manipulation ready", True),
    ("numpy", "Numerical computation ready", True),
    ("requests", "Network access ready", False),
    ("matplotlib", "Visualization ready", True),
]


def check_package(name: str) -> str | None:
    try:
        mod = importlib.import_module(name)
        version: str = getattr(mod, "__version__", "unknown")
        return version
    except ImportError:
        return None


def check_dependencies() -> bool:
    """Check packages and print status. Return True if all required ones are OK."""
    print("Checking dependencies:")
    all_ok = True

    for name, description, required in PACKAGES:
        version = check_package(name)
        if version:
            print(f"[OK] {name} ({version}) - {description}")
        elif required:
            print(f"[MISSING] {name} - {description}")
            all_ok = False

    return all_ok


def show_install_instructions() -> None:
    print()
    print("Some required dependencies are missing.")
    print()
    print("--- Install with pip ---")
    print("  pip install -r requirements.txt")
    print()
    print("--- Install with Poetry ---")
    print("  poetry install")
    print("  poetry run python loading.py")


def compare_managers() -> None:
    """Show the differences between pip and Poetry."""
    print()
    print("--- Dependency Manager Comparison ---")
    print("pip    :")
    print("  - Uses requirements.txt")
    print("  - No automatic lockfile (use pip freeze > requirements.txt)")
    print("  - Manual virtual environment management required")
    print("  - Install: pip install -r requirements.txt")
    print()
    print("Poetry :")
    print("  - Uses pyproject.toml + auto-generated poetry.lock")
    print("  - Automatic dependency resolution and conflict detection")
    print("  - Built-in virtual environment management")
    print("  - Install: poetry install")
    print("-------------------------------------")


def run_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print()
    print("Analyzing Matrix data...")

    rng = np.random.default_rng(seed=42)
    n_points = 1000
    print(f"Processing {n_points} data points...")

    time_steps = np.arange(n_points)
    signal = rng.normal(loc=0.0, scale=1.0, size=n_points).cumsum()
    noise = rng.uniform(low=-0.5, high=0.5, size=n_points)
    anomalies = (
        (rng.random(size=n_points) > 0.97).astype(float)
        * rng.choice([-5, 5], size=n_points)
    )

    df = pd.DataFrame({
        "time": time_steps,
        "signal": signal,
        "noise": noise,
        "anomaly": anomalies,
    })
    df["combined"] = df["signal"] + df["noise"] + df["anomaly"]

    print("Generating visualization...")

    fig, axes = plt.subplots(2, 1, figsize=(12, 6))
    fig.suptitle("Matrix Data Analysis", fontsize=14)

    axes[0].plot(
        df["time"], df["signal"],
        color="green", linewidth=0.8, label="Signal"
    )
    axes[0].set_title("Raw Matrix Signal")
    axes[0].set_ylabel("Amplitude")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    anomaly_mask = df["anomaly"] != 0
    axes[1].plot(
        df["time"], df["combined"],
        color="cyan", linewidth=0.5, label="Combined"
    )
    axes[1].scatter(
        df.loc[anomaly_mask, "time"],
        df.loc[anomaly_mask, "combined"],
        color="red", s=10, label="Anomalies", zorder=5,
    )
    axes[1].set_title("Combined Signal with Anomalies")
    axes[1].set_ylabel("Amplitude")
    axes[1].set_xlabel("Time step")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    output_file = "matrix_analysis.png"
    plt.savefig(output_file, dpi=100)
    plt.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    all_ok = check_dependencies()

    if not all_ok:
        show_install_instructions()
        sys.exit(1)

    run_analysis()
    compare_managers()


if __name__ == "__main__":
    main()