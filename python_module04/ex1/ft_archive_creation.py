def main():
    """ This function writes to a file and checks if it is saved correctly"""
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        filename = "new_discovery.txt"
        print(f"\nInitializing new storage unit: {filename}")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        file = open(filename, "w")
        file.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
        file.write("{[}ENTRY 002{]} Efficiency increased by 347%\n")
        file.write("{[}ENTRY 003{]} Archived by Data Archivist trainee\n")
        file.close()
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except FileNotFoundError:     
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception: 
        print("ERROR: Archive creation failed")


main()
