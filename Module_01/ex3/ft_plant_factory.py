def uppercase(name: str) -> str:
    table = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
        'z': 'Z'
    }
    if not name:
        return ""
    first = table.get(name[0].lower(), name[0])
    return first + name[1:]


class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def __str__(self) -> str:
        return f"Created: {uppercase(self.name)} \
            ({self.height}cm, {self.age} days)"


def main():
    garden_inventory: list[Plant] = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 120)
    ]

    print("=== Plant Factory Output ===")
    for plant in garden_inventory:
        print(plant)

    print(f"Total plants created: {len(garden_inventory)}")


if __name__ == "__main__":
    main()
