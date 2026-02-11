def main() -> None:
    """This function demonstrates secure vault
    operations using with statement"""
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
        print("\nInitiating secure vault access...")
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")
        with open("classified_data.txt", "r") as file:
            content = file.read()
            print(content)
        print("\nSECURE PRESERVATION:")
        with open("security_archive.txt", "w") as file:
            file.write("[CLASSIFIED] New security protocols archived")
        with open("security_archive.txt", "r") as file:
            content = file.read()
            print(content)
        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    except Exception:
        print("ERROR: Vault operation failed")


if __name__ == "__main__":
    main()
