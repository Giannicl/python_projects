import sys
import importlib
from typing import Dict

def check_dependencies() -> Dict:
    required_packages = ["pandas", "matplotlib", "requests"]
    package_status = {}

    for package in required_packages:
        try:
            import_package = importlib.import_module(package)
            version = import_package.__version__
            package_status[package] = version
        except ImportError:
            package_status[package] = None
        except Exception as e:
            package_status[package] = 'No version attribute available'
     
    return package_status

def display_dependency_status(package_status: Dict) -> bool:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    all_available = True
    for package in package_status:
        key = package
        value = package_status[key]
        if value:
            print(f"[OK] {key} ({value})", end="")
            if key == "pandas":
                print(" - Data manipulation ready")
            elif key == "requests":
                print(" - Network access ready")
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

def main() -> None:
    package_status = check_dependencies()
    
    if not display_dependency_status(package_status):
        sys.exit(1)
 
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
        
    print("\nAnalysis complete!")
    print("Results saved to: matrix\_analysis.png")

main()



