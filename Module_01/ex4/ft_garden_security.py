#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        if height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

        print(f"Plant created: {self}\n")

    def __str__(self) -> str:
        return (f"{self.name.capitalize()}: "
                f"{self._height:.1f}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self._age = int(new_age)
            print(f"Age updated: {new_age} days\n")

def main():
    print("=== Garden Security System ===")

    rose = Plant("rose", 15.0, 10)

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-10)
    rose.set_age(-5)

    print(f"Current state: {rose}")


if __name__ == "__main__":
    main()
