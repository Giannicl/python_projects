import sys


def command_quest() -> None:
    """This function displays the name of the programme
    and the total of arguments given"""
    print("=== Command Quest ===")
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {len(sys.argv)}")


def command_quest1() -> None:
    """This function displays the name of the programme,
    the given arguments, and the total arguments given"""
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    print(f"Argument 1: {sys.argv[1]}")
    print(f"Argument 2: {sys.argv[2]}")
    print(f"Argument 3: {sys.argv[3]}")
    print(f"Total arguments: {len(sys.argv)}")


def command_quest2() -> None:
    """This function displays the programme name,
    the amount of arguments received,
    the first arguments, and the total arguments given"""
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    print(f"Argument 1: {sys.argv[1]}")
    print(f"Total arguments: {len(sys.argv)}")


def command_interpreter() -> None:
    """This function chooses which command_quest function to call
    based on the amount of arguments"""
    if len(sys.argv) == 1:
        command_quest()
    elif len(sys.argv) == 4:
        command_quest1()
    elif len(sys.argv) == 2:
        command_quest2()
    else:
        print("only pass 1 or 3 argument(s)")


if __name__ == "__main__":
    command_interpreter()
