class GardenError(Exception):
    ''' This is a custom error class for garden errors'''
    pass

class PlantError(GardenError):
    ''' This is a custom error class specifically for plant errors'''
    pass

class WaterError(GardenError):
    ''' This is a custom error class specifically for water errors'''
    pass

class SunError(GardenError):
    ''' This is a custom error class specifically for sun errors'''
    pass


class GardenManager:
    ''' This is a GardenManager class that has methods to add plants, water plants, and check health'''
    water_in_tank = 4

    @classmethod
    def check_water_level(cls):
        try:
            if cls.water_in_tank < 2:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...")


    def add_plants(plant_list, plant):
        if plant is None:
            raise PlantError("Plant name cannot be empty!")
        plant_list += [plant]
        print(f"Added {plant} successfully")
        return plant_list
    @classmethod
    def water_plants(cls, plant_list):
        ''' This function activates the watering system'''
        print("Opening watering system")
        try:
            index = 0
            while True:
                try:
                    if plant_list[index] is None:
                        raise PlantError("Cannot water none - invalid plant!") 
                    print (f"Watering {plant_list[index]} - succes")
                    index += 1
                    cls.water_in_tank -= 2
                except IndexError:
                    break   
        finally:
            print("Closing watering system (cleanup)")

    
    def check_plant_health(plant_name, water_level, sunlight_hours):
        ''' This function checks if the conditions to grow a healthy plant are met'''
        if plant_name is None:
            raise PlantError("Plant name cannot be empty!")
        elif water_level < 1 or water_level > 10:
            raise WaterError("Water level 15 is too high (max 10)")
        elif sunlight_hours <= 2:
            raise SunError("Sunlight hours 0 is too low (min 2)")
        return print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")


def garden_management_system_test():
    plant_list = []
    print("Adding plants to garden...")
    try:
        plant_list = GardenManager.add_plants(plant_list, "tomato")
        plant_list = GardenManager.add_plants(plant_list, "lettuce")
        plant_list = GardenManager.add_plants(plant_list, None)
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    try:
        GardenManager.water_plants(plant_list)
    except PlantError as e:
        print("Error: {e}")
    print("\nChecking plant health...")
    try:
        GardenManager.check_plant_health(plant_list[0], 5, 8)
        GardenManager.check_plant_health(plant_list[1], 15, 8)
    except (PlantError, SunError, WaterError) as e :
        print(f"Error checking {plant_list[1]}: {e}")
    print("\nTesting error recovery...")
    try:
        GardenManager.check_water_level()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

garden_management_system_test()
