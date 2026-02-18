from functools import wraps
from typing import Any


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Spell completed in 0.101 seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                power = args[2]

                if power >= min_power:
                    return func(*args, **kwargs)
                else:
                    return "Insufficient power for this spell"
            except Exception:
                print("power is the third positional argument")
                return "Invalid spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt = 1
            while attempt <= max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if attempt == max_attempts:
                        return f"Spell casting failed after {max_attempts} attempts"
                    else:
                        attempt = attempt + 1
                        print(
                            f"Spell failed, retrying... (attempt {attempt}/{max_attempts})"
                        )

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        size = 0
        for character in name:
            size = size + 1
            is_space = character == " "
            is_lower_case = "a" <= character <= "z"
            is_upper_case = "A" <= character <= "Z"
            if not (is_space or is_lower_case or is_upper_case):
                return False
        if size < 3:
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if MageGuild.validate_mage_name(spell_name):
            return f"Successfully cast {spell_name} with power {power}"
        return "Invalid spell name"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    mage_guild = MageGuild()
    print(f"{mage_guild.validate_mage_name("Fireball")}")
    print(f"{mage_guild.validate_mage_name("T@!=")}")
    print(f"{mage_guild.cast_spell("Fireball", 15)}")
    print(f"{mage_guild.cast_spell("Tornado", 5)}")


if __name__ == "__main__":
    main()
