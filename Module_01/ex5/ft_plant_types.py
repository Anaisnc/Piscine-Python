#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
        else:
            self._height = float(new_height)

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
        else:
            self._age = int(new_age)

    def grow(self) -> None:
        self.set_height(self._height + 2.1)

    def age_plant(self) -> None:
        self.set_age(self._age + 1)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age_plant(self) -> None:
        super().age_plant()
        self.nutritional_value += 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("\n=== Flower")
    new_flower = Flower("rose", 15.0, 10, "red")
    new_flower.show()
    print(f"[asking the {new_flower.name} to bloom]")
    new_flower.bloom()
    new_flower.show()

    print("\n=== Tree")
    new_tree = Tree("oak", 200.0, 365, 5.0)
    new_tree.show()
    print(f"[asking the {new_tree.name} to produce shade]")
    new_tree.produce_shade()

    print("\n=== Vegetable")
    new_vegetable = Vegetable("tomato", 5.0, 10, "April")
    new_vegetable.show()
    print(f"[make {new_vegetable.name} grow and age for 20 days]")
    for _ in range(20):
        new_vegetable.grow()
        new_vegetable.age_plant()
    new_vegetable.show()


if __name__ == "__main__":
    main()
