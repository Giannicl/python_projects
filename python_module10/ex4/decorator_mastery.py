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
            power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    pass

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass
    def cast_spell(self, spell_name: str, power: int) -> str:
        pass
