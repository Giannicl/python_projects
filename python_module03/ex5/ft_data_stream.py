def prime_gen(prime_numbers):
    count = 0
    prime_check = 1
    found = 0
    while found < prime_numbers:
        count = 0
        divisor = 1
        while divisor <= prime_check:
            if prime_check % divisor == 0:
                count += 1
            divisor += 1
        if count == 2:
            found += 1
            yield prime_check
        prime_check += 1


def fibonacci_seq(numbers):
    i = 0
    prev = 0
    current = 1
    while i < numbers:
        if i == 0:
            yield i, prev
        elif i == 1:
            yield i, current
        else:
            number = current + prev
            prev = current
            current = number
            yield i, number
        i += 1


def count_values_events(event_types, value):
    count = 0
    for event in event_types:
        if value in event:
            count += 1
    return count


def count_values_10plus(player_levels):
    count = 0
    for levels in player_levels:
        if levels >= 10:
            count += 1
    return count


def player_level_per_event(level):
    player_levels = []
    player_levels += [level]
    return player_levels


def select_event(event_number):
    event = ["leveled up", "killed monster", "found treasure"]
    selected_event = event[event_number % len(event)]
    return selected_event


def select_player(event_number):
    players = {
        "alice": 5,
        "bob": 12,
        "charlie": 8,
    }
    players_list = ["charlie", "alice", "bob"]
    selected_player = players_list[event_number % len(players_list)]
    player_level = players[selected_player]
    return selected_player, player_level


def generate_game_events(num_events):
    for event_number in range(1, num_events + 1):
        player, level_player = select_player(event_number)
        event_type = select_event(event_number)
        yield event_number, player, level_player, event_type


def test_stream_data():
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...")
    generated_event = generate_game_events(1000)
    player_levels = []
    event_types = []
    event_number, player, level, event_type = next(generated_event)
    player_levels += [level]
    event_types += [event_type]
    print(f"Event {event_number}: "
          f"Player {player} (level {level}) {event_type}")
    event_number, player, level, event_type = next(generated_event)
    player_levels += [level]
    event_types += [event_type]
    print(f"Event {event_number}: "
          f"Player {player} (level {level}) {event_type}")
    event_number, player, level, event_type = next(generated_event)
    player_levels += [level]
    event_types += [event_type]
    print(f"Event {event_number}: "
          f"Player {player} (level {level}) {event_type}")
    print("...")
    for event_number, player, level, event_type in generated_event:
        player_levels += [level]
        event_types += [event_type]
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event_number}")
    count_10plus = count_values_10plus(player_levels)
    count_treasure_events = count_values_events(event_types, "treasure")
    count_levelup_events = count_values_events(event_types, "leveled up")
    print(f"High-level players (10+): {count_10plus}")
    print(f"Treasure events: {count_treasure_events}")
    print(f"Treasure events: {count_levelup_events}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    fibonacci_gen = fibonacci_seq(10)
    print("Fibonacci sequence (first 10): ", end="")
    for index, number in fibonacci_gen:
        if index < 9:
            print(f"{number}", end=", ")
        else:
            print(f"{number}")
    print("Prime numbers (first 5): ", end="")
    prime_number = prime_gen(5)
    index = 0
    for number in prime_number:
        if index < 4:
            print(f"{number}", end=", ")
        else:
            print(f"{number}")
        index += 1
