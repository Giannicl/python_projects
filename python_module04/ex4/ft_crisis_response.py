

def crisis_handler(filename):
    """ This function tries to access a file
    and handles the errors"""
    try:        
        with open(filename, 'r') as file:
            content = file.read()
            print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...") 
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Crisis handled, security maintained")
    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"\ncrisis alert: attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print(f"\ncrisis alert: attempting access to '{filename}'...")
        print(f"RESPONSE: Unexpected system malfunction")
        print("STATUS: Crisis handled, failsafe activated")

def main():
    """ This function calls the crisis_handler function with
    with several files"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    crisis_handler("./lost_archive.txt")
    crisis_handler("./classified_data.txt")
    crisis_handler("./standard_archive.txt")
    print("\nnAll crisis scenarios handled successfully. Archives secure.")

main()
