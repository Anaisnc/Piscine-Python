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

    def get_info(self):
        print(self)

def plant_factory(plants_data: list):
    plant_list = []
    for plant in plants_data:
        for name, height, age in plant:
            plant_list.append(Plant(name, height, age))

if __name__ == "__main__":
    plants_data = [
        ("rose", 12.0, 0),
        ("tomatoe", 14.0, 3),
        ("fern", 4.2, 2),
        ("poppy", 6.0, 1),
        ("carrot", 11.0, 3),
        ("clover", 8.2, 2),
    ]

    plant_factory(plants_data)

    print("=== Plant factory output ===")
    for plant in Plant.Garden: 
        plant.get_info()