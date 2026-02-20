from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any, Callable, List


def spell_reducer(spells: list[int], operation: str) -> int:
    result = 0
    if operation == "add":
        result: int = reduce(add, spells)
    elif operation == "multiply":
        result: int = reduce(mul, spells)
    elif operation == "max":
        result: int = reduce(max, spells)
    elif operation == "min":
        result: int = reduce(min, spells)

    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:

    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(power: Any) -> str:
        return f"Unknown power {power}"

    @cast_spell.register(int)
    def _(power):
        return f"Damage spell with power {power}"

    @cast_spell.register(str)
    def _(power):
        return f"Enchantment {power}"

    @cast_spell.register(list)
    def _(power):
        return f"Multi-cast {power}"

    return cast_spell


def main() -> None:
    try:
        print("Testing spell reducer...")
        list_n: List = [10, 20, 30, 40]
        sum_spell: int = spell_reducer(list_n, "add")
        print(f"Sum: {sum_spell}")
        list_n: List = [24, 10, 10, 10, 10]
        multiply_spell: int = spell_reducer(list_n, "multiply")
        print(f"Product: {multiply_spell}")
        list_n: List = [12, 40, 23, 9]
        max_spell: int = spell_reducer(list_n, "max")
        print(f"Max: {max_spell}")

        print("\nTesting memoized fibonacci..")
        fibonacci10: int = memoized_fibonacci(10)
        print(f"Fib(10): {fibonacci10}")
        fibonacci15: int = memoized_fibonacci(15)
        print(f"Fib(15): {fibonacci15}")
    except Exception:
        print("Error")


if __name__ == "__main__":
    main()
