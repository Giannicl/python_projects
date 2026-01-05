import sys


def command_quest():
    """This function displays the name of the programme
    and the total of arguments given"""
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {len(sys.argv)}")


def command_quest1():
    """This function displays the name of the programme,
    the given arguments, and the total arguments given"""
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    print(f"Argument 1: {sys.argv[1]}")
    print(f"Argument 2: {sys.argv[2]}")
    print(f"Argument 3: {sys.argv[3]}")
    print(f"Total Arguments: {len(sys.argv)}")


def command_quest2():
    """This function displays the programme name,
    the amount of arguments received,
    the first arguments, and the total arguments given"""
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    print(f"Argument 1: {sys.argv[1]}")
    print(f"Total arguments: {len(sys.argv)}")


def command_interpreter():
    """This function chooses which command_quest function to call
    based on the amount of arguments"""
    if len(sys.argv) == 1:
        command_quest()
    elif len(sys.argv) == 4:
        command_quest1()
    elif len(sys.argv) == 2:
        command_quest2()
