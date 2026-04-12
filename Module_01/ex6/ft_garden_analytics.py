#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self.stats = self.Stats()

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
        else:
            self._height = float(new_height)

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
        else:
            self._age = int(new_age)

    def grow(self) -> None:
        self.set_height(self._height + 8.0)
        self.stats.grow_calls += 1

    def age_plant(self) -> None:
        self.set_age(self._age + 20)
        self.stats.age_calls += 1

    def show(self) -> None:
        self.stats.show_calls += 1
        print(f"{self.name.capitalize()}: "
              f"{self._height:.1f}cm, {self._age} days old")

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
        status = "blooming beautifully!" if self.is_blooming \
            else "has not bloomed yet"
        print(f"{self.name.capitalize()} {status}")


class Tree(Plant):
    stats: "TreeStats"

    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats = self.TreeStats()

    def produce_shade(self) -> None:
        self.stats.shade_calls += 1
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    new_flower = Flower("rose", 15.0, 10, "red")
    new_flower.show()
    display_plant_stats(new_flower)
    print(f"[asking the {new_flower.name} to bloom]")
    new_flower.grow()
    new_flower.bloom()
    new_flower.show()
    display_plant_stats(new_flower)

    print("\n=== Tree")
    new_tree = Tree("oak", 200.0, 365, 5.0)
    new_tree.show()
    display_plant_stats(new_tree)
    print(f"[asking the {new_tree.name} to produce shade]")
    new_tree.produce_shade()
    display_plant_stats(new_tree)

    print("\n=== Seed")
    new_seed = Seed("sunflower", 80.0, 45, "yellow")
    new_seed.show()
    print(f"[make the {new_seed.name} grow, age and bloom]")
    new_seed.grow()
    new_seed.age_plant()
    new_seed.bloom()
    new_seed.show()
    display_plant_stats(new_seed)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)


if __name__ == "__main__":
    main()
