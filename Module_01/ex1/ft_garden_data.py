class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"

class GardenData:
     def __init__(self):
        self.plants_list: list[Plant] = []

     def add_plant(self, plant: Plant) -> None:
        self.plants_list.append(plant)

     def delete_plant(self, name: str) -> None:
        self.plants_list = [p for p in self.plants_list if p.name != name.lower() != name.lower()]
        
     def print_all(self) -> None:
             for plant in self.plants_list:
                  print(plant)

def main():
    my_manager = GardenData()

    rose = Plant("rose", 15.5, 5)
    sunflower = Plant("sunflower", 80.0, 30)
    oak = Plant("oak", 120.5, 365)

    print("--- Adding plants to the garden ---")
    my_manager.add_plant(rose)
    my_manager.add_plant(sunflower)
    my_manager.add_plant(oak)

    print("\n[Current Inventory]")
    my_manager.print_all()

    print("\n--- Deleting 'SUNFLOWER' ---")
    my_manager.delete_plant("SUNFLOWER")

    print("\n[Updated Inventory]")
    my_manager.print_all()

if __name__ == "__main__":
    main()