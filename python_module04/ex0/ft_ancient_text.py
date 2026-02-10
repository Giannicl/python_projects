def main() -> None:
    """This function opens, reads and closes a text file"""
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        filename = "ancient_fragment.txt"
        print(f"Accessing Storage Vault: {filename}")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
