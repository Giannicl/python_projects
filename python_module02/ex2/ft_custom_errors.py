class GardenError(Exception):
    ''' This is a custom error class for garden errors'''
    pass

class PlantError(GardenError):
    ''' This is a custom error class specifically for plant errors'''
    pass

class WaterError(GardenError):
    ''' This is a custom error class specifically for water errors'''
    pass

def raise_custom_errors():
    ''' This function raises the custom error classes'''
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise GardenError("Caught a garden error: The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


