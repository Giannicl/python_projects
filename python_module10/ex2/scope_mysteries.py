from typing import Any


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count = count + 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def power_up(amount: int) -> int:
        nonlocal power
        power = power + amount
        return power

    return power_up


def enchantment_factory(enchantment_type: str) -> callable:
    def apply(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return apply


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall,
    }


def main():
    print("Testing mage counter...")
    mage_counter1 = mage_counter()
    counter = mage_counter1()

    print(f"Call 1: {counter}")
    print(f"Call 2: {counter}")
    print(f"Call 3: {counter}")
    print("\nTesting enchantment factory...")
    enchantment_factory1 = enchantment_factory("Sword")
    enchantment = enchantment_factory1("Flaming")
    enchantment_factory2 = enchantment_factory("shield")
    enchantment2 = enchantment_factory2("Frozen")
    print(f"{enchantment}")
    print(f"{enchantment2}")


main()
