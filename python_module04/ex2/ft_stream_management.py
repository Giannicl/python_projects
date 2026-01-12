import sys

def main():
    """ This function takes input from the user
        and writes it to the standard output.
        And it displays an error through the standard error stream"""
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
        archivist_id = input("\nInput Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")
        sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print("\nThree-channel communication test successful.")
    except Exception:
        print(f"ERROR: Communication system failure")

main()
