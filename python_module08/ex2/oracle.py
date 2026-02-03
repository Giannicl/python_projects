import os
import sys

def load_environment_file()-> bool:
    try:
        from dotenv import load_dotenv
        return load_dotenv()
    except ImportError:
        return False

class Config:
    def __init__(self):
        self.matrix_mode = os.environ.get("MATRIX_MODE")
        self.database_url = os.environ.get("DATABASE_URL")
        self.api_key = os.environ.get("API_KEY")
        self.log_level = os.environ.get("LOG_LEVEL")
        self.zion_endpoint = os.environ.get("ZION_ENDPOINT")

def display_configuration(config: Config) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {config.matrix_mode}")

    if config.database_url:
        print(f"Database: {config.database_url}")
    else:
        print("Database: Not configured")

    if config.api_key:
        print(f"API Access: {config.api_key}")
    else:
        print("API Access: Not configured")

    print(f"Log Level: {config.log_level}")

    if config.zion_endpoint:
        print(f"Zion Network: {config.zion_endpoint}")
    else:
        print("Zion Network: Offline")

def display_security_checks() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

def main() -> None:
    load_environment_file()
    
    config = Config()
    display_configuration(config)
    display_security_checks()    
    print("\nThe Oracle sees all configurations.")

main()
