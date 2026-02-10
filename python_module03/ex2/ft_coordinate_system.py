import math
import sys


def calculate_distance(position: tuple) -> float:
    """This function calculates the distance from origin to a 3D positions"""
    x1, y1, z1 = (0, 0, 0)
    x2, y2, z2 = position
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))


def test_calculations() -> None:
    """This function parses the user input/
    positions andd tests the calculation function"""
    try:
        array = [sys.argv[1], sys.argv[2], sys.argv[3]]
        x1, y1, z1 = array
        position1 = (int(x1), int(y1), int(z1))
        array2 = sys.argv[4].split(",")
        x2, y2, z2 = array2
        position2 = (int(x2), int(y2), int(z2))
        print("=== Game Coordinate System ===")
        print(f"\nPosition created: {position1}")
        print(
            f"Distance between (0, 0, 0) and {position1}: "
            f"{calculate_distance(position1):.2f}"
        )
        print(f'\nParsing coordinates: "{sys.argv[4]}"')
        print(f"Parsed position: {position2}")
        print(
            f"Distance between (0, 0, 0) and {position2}: "
            f"{calculate_distance(position2)}"
        )
        print('Parsing invalid coordinates: "abc,def,ghi"')
        array_error = sys.argv[5].split(",")
        x3, y3, z3 = array_error
        position3 = (int(x3), int(y3), int(z3))
        print(f"{position3}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: {e.__class__.__name__}, Args: ("{e}",)')
    except IndexError:
        print(
            "Pass the arguments in this format to test: "
            '10 20 5 "3, 4, 0" "abc, def, ghi"'
        )
    try:
        print("\nUnpacking demonstration:")
        print(f"Player at x={x2}, y={y2}, z={z2}")
        print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    except IndexError:
        print(
            "Pass the arguments in this format to test: "
            '10 20 5 "3, 4, 0" "abc, def, ghi"'
        )


if __name__ == "__main__":
    test_calculations()
