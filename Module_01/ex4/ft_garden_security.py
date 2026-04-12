#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.set_height(height, init=True)
        self.set_age(age, init=True)
        print(f"Plant created: {self}\n")

    def __str__(self) -> str:
        return (f"{self.name.capitalize()}: "
                f"{self.get_height():.1f}cm, {self.get_age()} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float, init: bool = False) -> None:
        if new_height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            if not init:
                print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int, init: bool = False) -> None:
        if new_age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(new_age)
            if not init:
                print(f"Age updated: {new_age} days\n")


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("rose", 15.0, 10)
    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-10)
    rose.set_age(-5)

    print(f"\nCurrent state: {rose}")


if __name__ == "__main__":
    main()
