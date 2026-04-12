#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: "
              f"{self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 2.0


def plant_factory(plants: list[tuple[str, float, int]]) -> list[Plant]:
    Garden: list[Plant] = []

    for n, h, a in plants:
        Garden.append(Plant(n, h, a))
    return Garden


def plant_factory_show(garden: list[Plant]) -> None:
    for plant in garden:
        plant.show()


def main() -> None:
    print("=== Plant Factory Output ===")

    data = [
        ("rose", 25.0, 30),
        ("oak", 200.0, 365),
        ("cactus", 5.0, 90),
        ("sunflower", 80.0, 45),
        ("fern", 15.0, 120)
    ]

    my_garden = plant_factory(data)
    plant_factory_show(my_garden)

    print("\n=== Accessing only one plant ===")
    print(f"{my_garden[2].name}: {my_garden[2].height}cm, "
          f"{my_garden[2].age} days old.")

    print("\n=== Plant Grow ===")
    my_garden[2].grow()
    print(f"{my_garden[2].name}: {my_garden[2].height}cm, "
          f"{my_garden[2].age} days old.")


if __name__ == "__main__":
    main()
