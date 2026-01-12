def main():
    try:
        print("=== cyber archives - vault security system ===")
        print("\ninitiating secure vault access...")
        print("vault connection established with failsafe protocols")
        print("\nsecure extraction:")
    
        filename = "classified_data.txt"
        filename1 = "security_protocols.txt"
        with open(filename, "r") as file:
            content = file.read()
            print(content)
        print("\nsecure preservation:")
        with open(filename1, "r") as file:
            content = file.read()
            print(content)
        print("vault automatically sealed upon completion")
        print("\nvault automatically sealed upon completion")
    except Exeption as e:
        print(f"ERROR: Vault operation failed - {e}")
    

