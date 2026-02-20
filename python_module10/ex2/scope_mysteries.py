from typing import Any, Callable, Dict


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count: int = count + 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def power_up(amount: int) -> int:
        nonlocal power
        power: int = power + amount
        return power

    return power_up


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return apply


def memory_vault() -> dict[str, Callable]:
    memory: Dict = {}

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


def main() -> None:
    try:
        print("Testing mage counter...")
        mage_counter1: Callable = mage_counter()

        print(f"Call 1: {mage_counter1()}")
        print(f"Call 2: {mage_counter1()}")
        print(f"Call 3: {mage_counter1()}")
        print("\nTesting enchantment factory...")
        enchantment_factory1 = enchantment_factory("Flaming")
        enchantment = enchantment_factory1("Sword")
        enchantment_factory2 = enchantment_factory("Frozen")
        enchantment2 = enchantment_factory2("Shield")
        print(f"{enchantment}")
        print(f"{enchantment2}")
    except Exception:
        print("Error")


if __name__ == "__main__":
    main()
