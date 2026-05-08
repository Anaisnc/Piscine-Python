#!/usr/bin/env python3

from collections.abc import Callable


# --- Sample spells following the contract: spell(target: str, power: int) -> str ---

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


# --- Higher-order functions ---

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    # --- spell_combiner ---
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    # --- power_amplifier ---
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Dragon", 10)
    amplified = mega_fireball("Dragon", 10)
    print("Original: 10, Amplified: 30")
    print(f"  -> {original}")
    print(f"  -> {amplified}")

    # --- conditional_caster ---
    print("\nTesting conditional caster...")
    high_power_only = conditional_caster(
        lambda target, power: power >= 50,
        fireball
    )
    print(f"Power 80 (>= 50): {high_power_only('Goblin', 80)}")
    print(f"Power 20 (< 50):  {high_power_only('Goblin', 20)}")

    # Condition based on target name
    boss_only = conditional_caster(
        lambda target, power: callable(target) is False and target.startswith("Boss"),
        lightning
    )
    print(f"Target 'Boss Dragon': {boss_only('Boss Dragon', 60)}")
    print(f"Target 'Goblin':      {boss_only('Goblin', 60)}")

    # --- spell_sequence ---
    print("\nTesting spell sequence...")
    full_combo = spell_sequence([fireball, heal, shield])
    results = full_combo("Warrior", 25)
    for r in results:
        print(f"  {r}")

    # Demonstrate callable() usage
    print("\nDemonstrating callable()...")
    print(f"callable(fireball)  -> {callable(fireball)}")
    print(f"callable(42)        -> {callable(42)}")
    print(f"callable('string')  -> {callable('string')}")
