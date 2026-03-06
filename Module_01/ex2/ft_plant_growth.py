def uppercase(seed_type: str) -> str:
    table = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
        'z': 'Z'
    }
    if seed_type[0] in table:
        first = table[seed_type[0]]
    else:
        first = seed_type[0]
    return first + seed_type[1:]

class Plant:
    Garden: list["Plant"] = []

    def __init__(self, name: str, height: float, age_plant: int):
        self.name = name
        self.height = height
        self.age_plant = age_plant
        Plant.Garden.append(self)

    def __str__(self):
        return f"{uppercase(self.name)}: {self.height}cm, {self.age_plant} days old"

    def delete_plant(self, name: str):
        Plant.Garden = [p for p in Plant.Garden if p.name != name]

    def grow(self) -> float:
        self.height = self.height + 2
        return self.height

    def age(self, days: int) -> int:
        self.age_plant = self.age_plant + 1
        return self.age_plant

    def get_info() -> None:
        print("\n === Day",days, "===")
        for plant in new_plant.Garden:
            print(plant)

if __name__ == "__main__":
    days = 1

    while True:
        name = input("\nWrite:\n1.'plant name' to add a new plant\n2.'delete' to delete a plant\n3.'stop' to quit\n4.'Week' to see your plant grow in a week\n 5.'Month' to see your plant grow in a month\nAction: ")
        if name == "stop":
            break
        elif name == "delete":
            name = input("\nEnter plant name to delete: ")
            Plant.delete_plant(name)
        elif name == "Week":
            print("A week of Growth in the garden: ")
            Plant.get_info()
            while days <= 7:
                for plant in Plant.Garden:
                    plant.grow()
                    plant.age(days)
                days += 1
                Plant.get_info()
            break
        elif name == "Month":
            while days <= 30:
                for plant in Plant.Garden:
                    plant.grow()
                    plant.age(days)
                for plant in Plant.Garden[:]:
                    if plant.age_plant > 16: 
                        print(plant.name, " died")
                        Plant.delete_plant(plant.name)
                days += 1
                Plant.get_info()
        else:
            height = float(input("Enter height (cm): "))
            age_plant = int(input("Enter age (days): "))
            new_plant = Plant(name, height, age_plant)

        