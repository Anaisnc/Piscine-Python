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
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.plants_list: list["Plant"] = []

    def __str__(self):
        return f"{uppercase(self.name)}: {self.height}cm, {self.age} days old"

    def add_plant(self, plant: "Plant"):
        self.plants_list.append(plant)

    def delete_plant(self, name: str):
        self.plants_list = [p for p in self.plants_list if p.name != name]

if __name__ == "__main__":
    first_plant = Plant("Poppy", 15, 3)

    while True:
        name = input("\nWrite:\n1.'plant name' to add a new plant\n2.'delete' to delete a plant\n3.'stop' to quit\nAction: ")
        if name == "stop":
            break
        if name == "delete":
            name = input("\nEnter plant name to delete: ")
            first_plant.delete_plant(name)
        else:
            height = float(input("Enter height (cm): "))
            age = int(input("Enter age (days): "))
            new_plant = Plant(name, height, age)
            first_plant.add_plant(new_plant)

        print("\n === Garden Plant Registry ===")
        for plant in first_plant.plants_list:
            print(plant)