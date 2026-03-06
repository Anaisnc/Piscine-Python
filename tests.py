Voici ton code corrigé et complet :

```python
class Plant:
    Garden: list["Plant"] = []

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        Plant.Garden.append(self)

    def __str__(self):
        return f"{self.name.upper()}: {self.height}cm, {self.age} days old"

    @classmethod
    def delete_plant(cls, name: str):
        Plant.Garden = [p for p in Plant.Garden if p.name != name]

    def grow(self, days: int) -> float:
        self.height = (self.height + (1/4) * self.height) * days
        return self.height

    def age_plant(self, days: int) -> int:
        self.age = self.age + days
        return self.age

    @staticmethod
    def get_info() -> None:
        print("\n === Garden Plant Registry ===")
        for plant in Plant.Garden:
            print(plant)


if __name__ == "__main__":
    days = 1

    while True:
        name = input("\nWrite:\n1.'plant name' to add a new plant\n2.'delete' to delete a plant\n3.'stop' to quit\n4.'garden complete' if your garden is full\nAction: ")

        if name == "stop":
            break

        elif name == "delete":
            name = input("\nEnter plant name to delete: ")
            Plant.delete_plant(name)

        elif name == "garden complete":
            while days <= 7:
                for plant in Plant.Garden:
                    plant.grow(days)
                    plant.age_plant(days)
                days += 1
            Plant.get_info()
            break

        else:
            height = float(input("Enter height (cm): "))
            age = int(input("Enter age (days): "))
            Plant(name, height, age)

