def check_plant_health(plant_name, water_level, sunlight_hours):

    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    #elif water_level < 1 || water_level > 10:



    


    return print(f"Plant {plant_name} is healthy!")






def test_plant_checks():
   

        print("=== Garden Plant Health Checker ===")
        print("\nTesting good values...")
    check_plant_health("tomato", 5, 5)
    print("\nTesting empty plant name...")
    check_plant_health(None, 5, 5)
    print("\nTesting bad water level...")
    print("\nTesting bad sunlight hours...")



test_plant_checks()
