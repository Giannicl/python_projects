from typing import List


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args):
        result1 = spell1(*args)
        result2 = spell2(*args)

        return(result1, result2)
    return combined

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def multiply(*args):
        result = base_spell(*args)
        return result * multiplier
    return multiply

def conditional_caster(condition: callable, spell: callable) -> callable: 
    def function(*args):
        result = condition(*args)
        if result:
            return spell(*args)
        else:
            return "Spell fizzled"
    return function

def spell_sequence(spells: list[callable]) -> callable:
    def ordered_cast(*args):
        results = []
        for spel in spells:
            results = results + [spel(*args)]
        return results
    return ordered_cast

def main()-> None:
    print("Testing spell combiner...")
    
    def attack(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combined = spell_combiner(attack, heal)
    combined_result = combined("Dragon")
    
    print(f"Combined spell result: {combined_result[0], combined_result[1]}")

    print("\nTesting power amplifier...")

    def base_spell(number: int) -> int:
       return number + 5 
    amplified = power_amplifier(base_spell, 2)
    amplified_result = amplified(10) 
    print(f"Original: 10, Amplified: {amplified_result}")

main()



