#!/usr/bin/env python3

def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    name: str = "Poppy"
    height: int = 15
    age: int = 5

    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days old")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
