class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name.capitalize()}: {self.height}cm, {self.age} days old")
    
    def grow(self) -> None:
        self.height += 2.0
    
def plant_factory(name: str, height: float, age: int) -> Plant:
        return Plant(name, height, age)

def main():
    print("=== Plant Factory Output ===")
    
    data = [
        ("rose", 25.0, 30),
        ("fern", 200.0, 365),
        ("poppy", 5.0, 90),
        ("hoya", 80.0, 45),
        ("tulip", 15.0, 2)
    ]

    for name, height, age in data:
        new_plant = plant_factory(name, height, age)
        new_plant.show()

if __name__ == "__main__":
   main()