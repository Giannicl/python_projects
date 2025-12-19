def check_plant_health(plant_name, water_level, sunlight_hours):
    """This function checks if the
    conditions to grow a healthy plant are met"""
    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1 or water_level > 10:
        raise ValueError("Water level 15 is too high (max 10)")
    elif sunlight_hours <= 2:
        raise ValueError("Sunlight hours 0 is too low (min 2)")
    return print(f"Plant {plant_name} is healthy!")


def test_plant_checks():
    """This function tests the custom error messages of
    the check_plant_health function"""
    print("=== Garden Plant Health Checker ===")
    try:
        print("\nTesting good values...")
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting empty plant name...")
        check_plant_health(None, 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")
