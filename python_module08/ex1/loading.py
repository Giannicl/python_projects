import sys
import importlib
from typing import Dict


def check_dependencies() -> Dict:
    required_packages: list = ["pandas", "matplotlib", "requests", "numpy"]
    package_status: dict = {}

    for package in required_packages:
        try:
            import_package = importlib.import_module(package)
            version = import_package.__version__
            package_status[package] = version
        except ImportError:
            package_status[package] = None
        except Exception:
            package_status[package] = "No version attribute available"

    return package_status


def display_dependency_status(package_status: Dict) -> bool:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    all_available: bool = True
    for package in package_status:
        key = package
        value = package_status[key]
        if value:
            print(f"[OK] {key} ({value})", end="")
            if key == "pandas":
                print(" - Data manipulation ready")
            elif key == "requests":
                print(" - Network access ready")
            elif key == "numpy":
                print(" - Numerical computation ready")
            else:
                print(" - Visualization ready")
        else:
            print(f"[MISSING] {package} - Not installed")
            all_available = False

    if not all_available:
        print("\nERROR: Missing required dependencies!")
        print("\nTo install with pip:")
        print(" pip install -r requirements.txt")
        print("\nTo install with Poetry:")
        print(" poetry install")

    return all_available


def create_matrix_visualization() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    time: np.ndarray = np.arange(1000)
    signal: np.ndarray = np.sin(np.linspace(0, 10, 1000)) * 50

    data = pd.DataFrame(
        {
            "Time": time,
            "Signal_Strength": signal,
        }
    )

    plt.figure(figsize=(10, 6))
    plt.plot(data["Time"], data["Signal_Strength"], color="green", alpha=0.7)
    plt.title("Matrix Signal Analysis", fontsize=14, color="green")
    plt.xlabel("Time Units")
    plt.ylabel("Signal Strength")
    plt.grid(True, alpha=0.3)
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    package_status = check_dependencies()

    if not display_dependency_status(package_status):
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    create_matrix_visualization()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
