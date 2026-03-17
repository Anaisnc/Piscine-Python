class Plant:
    Garden: list["Plant"] = []

    def __init__(self, name: str, starting_height: float, starting_age: int):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        Plant.Garden.append(self)

