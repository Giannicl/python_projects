from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        result = reduce(add, spells)
    elif operation == "multiply":
        result = reduce(mul, spells)
    elif operation == "max":
        result = reduce(max, spells)
    elif operation == "min":
        result = reduce(min, spells)

    return result


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
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


def spell_dispatcher() -> callable:
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
    print("Testing spell reducer...")
    list = [10, 20, 30, 40]
    sum_spell = spell_reducer(list, "add")
    print(f"Sum: {sum_spell}")
    list = [24, 10, 10, 10, 10]
    multiply_spell = spell_reducer(list, "multiply")
    print(f"Product: {multiply_spell}")
    list = [12, 40, 23, 9]
    max_spell = spell_reducer(list, "max")
    print(f"Max: {max_spell}")

    print("\nTesting memoized fibonacci..")
    fibonacci10 = memoized_fibonacci(10)
    print(f"Fib(10): {fibonacci10}")
    fibonacci15 = memoized_fibonacci(15)
    print(f"Fib(15): {fibonacci15}")


if __name__ == "__main__":
    main()
