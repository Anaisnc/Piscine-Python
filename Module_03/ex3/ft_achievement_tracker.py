#!/usr/bin/env python3
import random


ALL_ACHIEVEMENTS = [
    "First Steps", "Speed Runner", "Survivor", "Master Explorer",
    "Treasure Hunter", "Crafting Genius", "Boss Slayer", "World Savior",
    "Collector Supreme", "Untouchable", "Unstoppable", "Strategist",
    "Sharp Mind", "Hidden Path Finder", "Dragon Slayer", "Night Owl",
    "Pacifist", "Completionist", "Speedster", "Legend"
]

PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set:
    count = random.randint(4, 12)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    player_data: dict = {}
    for name in PLAYERS:
        player_data[name] = gen_player_achievements()
        print(f"Player {name}: {player_data[name]}")
    sets = list(player_data.values())
    all_achievements = sets[0].union(*sets[1:])
    print(f"\nAll distinct achievements: {all_achievements}")
    common = sets[0].intersection(*sets[1:])
    print(f"Common achievements: {common}")
    print()
    for name, achieved in player_data.items():
        others: set = set()
        for other_name, other_set in player_data.items():
            if other_name != name:
                others = others.union(other_set)
        exclusive = achieved.difference(others)
        missing = all_achievements.difference(achieved)
        print(f"Only {name} has: {exclusive}")
    print()
    for name, achieved in player_data.items():
        missing = all_achievements.difference(achieved)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()