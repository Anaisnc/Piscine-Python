class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 2.0

    def get_older(self) -> None:
        self.age += 1

    def __str__(self) -> str:
        return f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"

def main():
    print("=== Garden Plant Growth ===")
    
    rose = Plant("rose", 12.0, 0)
    initial_height = rose.height
    print(rose)

    for day in range(1, 8):
       rose.grow()
       rose.get_older()
       print(f"=== Day {day} ===")
       print(rose)

    total_growth = rose.height - initial_height
    print(f"Growth this week: {total_growth:1f}cm")
    
if __name__ == "__main__":
   main()