class Plant:
    Garden: list["Plant"] = []

    def __init__(self, name: str, starting_height: float, starting_age: int):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        Plant.Garden.append(self)

if __name__ == "__main__":
    while True:
        name = input("\nWrite:\n'plant name' to add a new plant")
        starting_height = float(input("Enter height (cm): "))
        starting_age = int(input("Enter age (days): "))
        new_plant = Plant(name, height, age_plant)

