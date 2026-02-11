def crisis_handler(filename: str) -> None:
    """This function tries to access a file
    and handles the errors"""
    try:
        print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...")
        with open(filename, "r") as file:
            content = file.read()
            print(f'SUCCESS: Archive recovered - "{content}"')
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system malfunction")
        print("STATUS: Crisis handled, failsafe activated")


def main() -> None:
    """This function calls the crisis_handler function with
    with several files"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
