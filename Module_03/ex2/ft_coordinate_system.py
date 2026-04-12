#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        input_string = input("Enter new coordinates as floats in format 'x,y,z': ")
        coords = []
        current_val = ""
        valid_parse = True
        
        for char in (input_string + ","):
            if char == ",":
                cleaned = current_val.strip()
                if cleaned:
                    try:
                        coords.append(float(cleaned))
                    except ValueError as e:
                        print(f"Error on parameter '{cleaned}': {e}")
                        valid_parse = False
                        break
                current_val = ""
            else:
                current_val += char
        if valid_parse:
            if len(coords) == 3:
                return (coords[0], coords[1], coords[2])
            else:
                print("Invalid syntax")


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    center = (0.0, 0.0, 0.0)
    dist_center = round(distance(pos1, center), 4)
    print(f"Distance to center: {dist_center}")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist_points = round(distance(pos1, pos2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist_points}")


if __name__ == "__main__":
    main()
