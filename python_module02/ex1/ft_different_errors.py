def garden_operations(error):
    """This function triggers a ValueError, a ZeroDivisionError,
    a FileNotFoundError or KeyError"""

    if error == "ValueError":
        error = int("abc")
    elif error == "ZeroDivisionError":
        error = 10 / 0
    elif error == "FileNotFoundError":
        error = open("./text.txt", "r")
    elif error == "KeyError":
        dictionary = {"key1": 1, "key2": 2}
        dictionary[error]


def test_error_types():
    """This function tests the different error types by calling
    the garden_operations function with the different errortypes as input"""

    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError..")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        garden_operations("KeyError")
    except KeyError:
        print("\nCaught KeyError: 'missing\\_plant'")
    print("\nTesting multiple errors together...")
    try:
        garden_operations("KeyError")
        garden_operations("ValueError")
    except KeyError or ValueError:
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")
