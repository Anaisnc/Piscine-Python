#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_attribute = age

    def grow(self) -> None:
        self.height += 2.0

    def age(self) -> None:
        self.age_attribute += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age_attribute} days old")

def main():
    print("=== Garden Plant Growth ===")

    rose = Plant("rose", 12.0, 0)
    initial_height = rose.height
    rose.show()

    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()

    total_growth = rose.height - initial_height
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
