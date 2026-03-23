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

    def grow(self):
        self.height += 2

    def age(self):
        self.age_plant += 1
    
    def get_info(self):
        print(self)

if __name__ == "__main__":
    Plant("rose", 12.0, 0)
    Plant("tomatoe", 14.0, 3)
    Plant("fern", 4.2, 2)

    for day in range(1, 8):
        print(f"\n=== Day {day} ===")
        for plant in Plant.Garden: 
            plant.grow()
            plant.age()
            plant.get_info()