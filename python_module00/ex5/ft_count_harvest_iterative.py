def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    current = 1

    while current <= days:
        print(f"Day {current}")
        current += 1
    print("Harvest time!")
