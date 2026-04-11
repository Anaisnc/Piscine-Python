#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def perform_garden_task(task_type: str) -> None:
    if task_type == "plant_issue":
        raise PlantError("The tomato plant is wilting!")
    elif task_type == "water_issue":
        raise WaterError("Not enough water in the tank!")
    elif task_type == "other":
        raise GardenError()


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        perform_garden_task("plant_issue")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        perform_garden_task("water_issue")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    tasks = ["plant_issue", "water_issue"]
    for task in tasks:
        try:
            perform_garden_task(task)
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
