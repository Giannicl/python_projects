def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if seed_type.capitalize() == "Tomato":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif seed_type.capitalize() == "Carrot":
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif seed_type.capitalize() == "Lettuce":
        print(f"{seed_type} seeds: cover {quantity} {unit} meters")
    else:
        print(f"{seed_type} seeds: cover {quantity} {unit} Unknown unit type")
