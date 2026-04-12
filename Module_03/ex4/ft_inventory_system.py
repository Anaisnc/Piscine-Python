#!/usr/bin/env python3
import sys


def parse_inventory(args: list) -> dict:
    inventory: dict = {}
    i = 1
    while i < len(args):
        param = args[i]
        parts = param.split(":")
        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            print(f"Error - invalid parameter '{param}'")
            i += 1
            continue
        name, qty_str = parts[0], parts[1]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            i += 1
            continue
        try:
            inventory[name] = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
        i += 1
    return inventory


def display_inventory(inventory: dict) -> None:
    print(f"Got inventory: {inventory}")


def display_items(inventory: dict) -> None:
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for name, qty in inventory.items():
        pct = round(qty / total * 100, 1)
        print(f"Item {name} represents {pct}%")
    most = max(inventory.keys(), key=lambda k: inventory[k])
    least = min(inventory.keys(), key=lambda k: inventory[k])
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv)
    if len(inventory) == 0:
        print("No valid items provided.")
        return
    display_inventory(inventory)
    display_items(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
