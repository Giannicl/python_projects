import math
import sys





def calculate_distance(position) -> float:
    """ This function calculates the distance between 2 3D positions"""
    x1, y1, z1 = (0, 0, 0)
    x2, y2, z2= position
    return (math.sqrt(((int(x2) - int(x1))**2) + ((int(y2) - int(y1))**2) + ((int(z2) - int(z1))**2)))



def test_calculations() -> None:
    """ This function parses the user input/ positions andd tests the calculation function"""
    try:
        position1 = ()
        array1 = []
        array1 = sys.argv[1].split(',')
        x1, y1, z1 = array1
        position1 = (int(x1), int(y1), int(z1))
        print("=== Game Coordinate System ===")
        print(f"\nPosition created: {position1}")
        print(f"Distance between (0, 0, 0) and {position1}: {calculate_distance(position1):.2f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    try:
        position2 = ()
        array2 = []
        array2 = sys.argv[2].split(',')
        x2, y2, z2 = array2
        position2 = (int(x2), int(y2), int(z2))
        print(f"\nParsing coordinates: \"{sys.argv[2]}\"")
        print(f"Parsed position: {position2}")
        print(f"Distance between (0, 0, 0) and {position2}: {calculate_distance(position2):.1f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    try:
        position3 = ()
        array3 = []
        array3 = sys.argv[3].split(',')
        x3, y3, z3 = array3
        print(f"\nParsing invalid coordinates: \"{sys.argv[3]}\"")
        position3 = (int(x3), int(y3), int(z3))
        print(f"Parsed position: {position3}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: (\"{e}\".)")
    try:
        position2 = ()
        array2 = []
        array2 = sys.argv[2].split(',')
        x2, y2, z2 = array2
        position2 = (int(x2), int(y2), int(z2))
        print("\nUnpacking demonstration:")
        print(f"Player at x={x2}, y={y2}, z={z2}")
        print(f"Coordinates: x={x2}, y={y2}, z={z2}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")



test_calculations() 
