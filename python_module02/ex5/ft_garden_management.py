class GardenError(Exception):
    ''' This is a custom error class for garden errors'''
    pass

class PlantError(GardenError):
    ''' This is a custom error class specifically for plant errors'''
    pass

class WaterError(GardenError):
    ''' This is a custom error class specifically for water errors'''
    pass

class GardenManager:
    def add_plants(plant_list, plant):
        if plant is None:
            raise PlantError("Plant name cannot be empty!")
        plant_list += [plant]
        print(f"{plant} successfully")
        return plant_list

    def water_plants(plant_list):
        ''' This function activates the watering system'''
        print("Opening watering system")
        try:
            index = 0
            while True:
                try:
                    if plant_list[index] is None:
                        raise PlantError("Cannot water none - invalid plant!") 
                        return
                    print (f"Watering {plant_list[index]}")
                    index += 1
                except IndexError:
                    break 
        finally:
            print("Closing watering system (cleanup)")
        
        print("Watering completed successfully!")


    
    def check_plant_health(plant_name, water_level, sunlight_hours):
         ''' This function checks if the conditions to grow a healthy plant are met'''
        if plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        elif water_level < 1 or water_level > 10:
            raise ValueError("Water level 15 is too high (max 10)")
        elif sunlight_hours <= 2:
            raise ValueError("Sunlight hours 0 is too low (min 2)")
        return print(f"Plant {plant_name} is healthy!")


def main():
    plant_list = []
    print("Adding plants to garden")
    add_plants(plant_list, "tomato")
    add_plants(plant_list, "lettuce")




main()
