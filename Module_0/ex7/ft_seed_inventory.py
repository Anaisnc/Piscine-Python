def uppercase(seed_type: str) -> str:
    table = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
        'z': 'Z'
    }
    if seed_type[0] in table:
        first = table[seed_type[0]]
    else:
        first = seed_type[0]
    return first + seed_type[1:]

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(uppercase(seed_type), "seeds:", quantity, unit, "available")
	if unit == "grams":
		print(uppercase(seed_type), "seeds:", quantity, unit, "total")
	if unit == "area":
		print(uppercase(seed_type), "seeds:", "covers", quantity, "square meters")
	options =  "packets", "grams", "area"
	if unit not in options: 
		print("Unknown unit type")

#ft_seed_inventory("tomato", 15, "packets")
#ft_seed_inventory("carrot", 8, "grams")
#ft_seed_inventory("lettuce", 12, "area")
#ft_seed_inventory("lettuce", 12, "blabla")