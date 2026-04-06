#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


def main():
    print("=== Garden Plant Registry ===")

    rose = Plant("rose", 15.5, 5)
    sunflower = Plant("sunflower", 80.0, 30)
    oak = Plant("oak", 120.5, 365)

    rose.show()
    sunflower.show()
    oak.show()


if __name__ == "__main__":
    main()
