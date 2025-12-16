def check_temperature(temp_str):
   ''' This function checks if the user had passed the correct temperature for plants'''
    try:
        user_input = int(temp_str)
    except:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    
    if user_input > 40:
        print(f"Error: {user_input}°C is too hot for plants (max 40°C)")
        return None
    
    if user_input < 0:
        print(f"Error: {user_input}°C is too cold for plants (min 0°C)")
        return None
    
    return user_input


def test_temperature_input():
    ''' This function test the error messages for different input and the result for a correct input'''

    print("=== Garden Temperature Checker ===")
    
    print("\nTesting temperature: 25")
    output = check_temperature("25")
    if output != None:
        print(f"Temperature {output}°C is perfect for plants!")
    
    print("\nTesting temperature: abc")
    output = check_temperature("abc")
    if output != None:
        print(f"Temperature {output}°C is perfect for plants!")
    
    print("\nTesting temperature: 100")
    output = check_temperature("100")
    if output != None:
        print(f"Temperature {output}°C is perfect for plants!")
    
    print("\nTesting temperature: -50")
    output = check_temperature("-50")
    if output != None:
        print(f"Temperature {output}°C is perfect for plants!")
    
    print("\nAll tests completed - program didn't crash!")

