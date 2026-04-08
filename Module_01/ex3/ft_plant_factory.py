#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name.capitalize()}: "
              f"{self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 2.0


def plant_factory(name: str, height: float, age: int) -> Plant:
    return Plant(name, height, age)


def main():
    print("=== Plant Factory Output ===")

    data = [
        ("rose", 25.0, 30),
        ("fern", 200.0, 365),
        ("poppy", 5.0, 90),
        ("hoya", 80.0, 45),
        ("tulip", 15.0, 2)
    ]

    my_garden = [plant_factory(n, h, a) for n, h, a in data]

    for plant in my_garden:
        plant.show()

    print("\n=== After Growth ===")
    for plant in my_garden:
        plant.grow()
        plant.show()

    print("\n=== Accessing only one plant ===")
    print(f"{my_garden[2].name.capitalize()}: {my_garden[2].height}cm, "
          f"{my_garden[2].age} days old.")


if __name__ == "__main__":
    main()
