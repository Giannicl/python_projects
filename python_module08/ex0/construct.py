import os
import sys
import site


def is_virtual_environment() -> bool:

    if "VIRTUAL_ENV" in os.environ:
        return True

    if sys.base_prefix != sys.prefix:
        return True

    return False


def get_virtual_environment_name() -> str:
    virtual_environment = os.environ.get("VIRTUAL_ENV")
    if virtual_environment:
        return os.path.basename(virtual_environment)
    return "None detected"


def get_site_packages_path() -> str:
    return site.getsitepackages()[0]


def display_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {get_virtual_environment_name()}")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate #   On Windows")
    print("\nThen run this program again.")


def display_inside_construct() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {get_virtual_environment_name()}")
    print(f"Environment Path: {os.environ.get('VIRTUAL_ENV', 'Unknown')}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    print(f"{get_site_packages_path()}")


def main() -> None:
    if is_virtual_environment():
        display_inside_construct()
    else:
        display_outside_matrix()


main()
