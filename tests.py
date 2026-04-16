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