class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self.height += 8.0
        self.stats.grow_calls += 1

    def age_plant(self) -> None:
        self.age += 1
        self.stats.age_calls += 1

    def show(self) -> None:
        self.stats.show_calls += 1
        print(f"{self.name.capitalize()}: \
              {self.height:.1f}cm, {self.age} days old")


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
        status = "blooming beautifully!" if self.is_blooming else \
            "has not bloomed yet"
        print(f"{self.name.capitalize()} {status}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats = self.TreeStats()

    def produce_shade(self) -> None:
        self.stats.shade_calls += 1
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.height:.1f}cm long and \
                {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42  # Example seed production

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.stats.display()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sun = Seed("sunflower", 80.0, 45, "yellow")
    sun.show()
    print("[make sunflower grow, age and bloom]")
    sun.grow()
    for _ in range(20):
        sun.age_plant()
    sun.bloom()
    sun.show()
    display_plant_stats(sun)

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()


if __name__ == "__main__":
    main()
