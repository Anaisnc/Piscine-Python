#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords: list = []
        valid = True
        i = 0
        while i < len(parts):
            try:
                coords.append(float(parts[i].strip()))
            except ValueError as e:
                print(f"Error on parameter '{parts[i].strip()}': {e}")
                valid = False
            i += 1
        if valid:
            return (coords[0], coords[1], coords[2])


def distance(p1: tuple, p2: tuple) -> float:
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
