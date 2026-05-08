#!/usr/bin/env python3

import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable] = {
        'add':      operator.add,
        'multiply': operator.mul,
        'max':      max,
        'min':      min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'. "
                         f"Supported: {list(operations.keys())}")

    if operation in ('max', 'min'):
        return operations[operation](spells)

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire':  functools.partial(base_enchantment, power=50, element='fire'),
        'ice':   functools.partial(base_enchantment, power=50, element='ice'),
        'storm': functools.partial(base_enchantment, power=50, element='storm'),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    # --- spell_reducer ---
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")
    print(f"Empty list: {spell_reducer([], 'add')}")
    try:
        spell_reducer(powers, 'unknown')
    except ValueError as e:
        print(f"Unknown operation caught: {e}")

    # --- partial_enchanter ---
    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} enchantment on {target} with power {power}"

    variants = partial_enchanter(base_enchantment)
    print(variants['fire'](target='Sword'))
    print(variants['ice'](target='Shield'))
    print(variants['storm'](target='Staff'))

    # --- memoized_fibonacci ---
    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    # --- spell_dispatcher ---
    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["bolt", "heal", "shield"]))
    print(dispatch(3.14))
