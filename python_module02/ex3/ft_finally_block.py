def water_plants(plant_list):
    """This function activates the watering system"""
    print("Opening watering system")
    try:
        index = 0
        while True:
            try:
                if plant_list[index] is None:
                    print("Error: Cannot water None - invalid plant!")
                    return
                print(f"Watering {plant_list[index]}")
                index += 1
            except IndexError:
                break
    finally:
        print("Closing watering system (cleanup)")

    print("Watering completed successfully!")


def test_watering_system():
    """This function tests if the plant watering function works as suspected"""
    print("=== Garden Watering System ===")

    try:
        plant_list = ["tomato", "lettuce", "carrots"]
        print("\nTesting normal watering...")
        water_plants(plant_list)

        plant_list = ["Tomato", None]
        print("\nTesting with error...")
        water_plants(plant_list)
    except KeyError:
        print("error found")
    finally:
        print("\nCleanup always happens, even with errors!")
