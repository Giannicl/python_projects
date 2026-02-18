from typing import Callable, List, Tuple


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args):
        result1: Callable = spell1(*args)
        result2: Callable = spell2(*args)

        return (result1, result2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiply(*args):
        result: int = base_spell(*args)
        return result * multiplier

    return multiply


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def function(*args):
        result: Callable = condition(*args)
        if result:
            return spell(*args)
        else:
            return "Spell fizzled"

    return function


def spell_sequence(spells: list[Callable]) -> Callable:
    def ordered_cast(*args):
        results: List = []
        for spel in spells:
            results: List = results + [spel(*args)]
        return results

    return ordered_cast


def main() -> None:
    print("Testing spell combiner...")

    def attack(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combined: Callable = spell_combiner(attack, heal)
    combined_result: Tuple[str, str] = combined("Dragon")

    print(f"Combined spell result: {combined_result[0], combined_result[1]}")

    print("\nTesting power amplifier...")

    def base_spell(number: int) -> int:
        return number + 5

    amplified: Callable = power_amplifier(base_spell, 2)
    amplified_result: int = amplified(10)
    print(f"Original: 10, Amplified: {amplified_result}")


if __name__ == "__main__":
    main()
