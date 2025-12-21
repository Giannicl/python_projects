import sys

def add_score(players_score):
    """ This function accepts scores of players"""
    if len(sys.argv) < 2:
        raise ValueError(f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    if len(sys.argv) == 2:
        players_score += [int(sys.argv[1])]
    elif len(sys.argv) > 2:
        i = 1
        while i < len(sys.argv):
            players_score += [int(sys.argv[i])]
            i += 1
    return players_score

def count_players(players_score):
    return len(players_score)

def total_score(players_score):
    """ This function adds all the scores together"""
    return sum(players_score)

def average_score(players_score):
    return sum(players_score) / len(players_score)

def max_score(players_score):
    """ This function returns the highest score"""
    return max(players_score)

def min_score(players_score):
    """ This function returns the lowest score"""
    return min(players_score)

def range_score(players_score):
    return max(players_score) - min(players_score)


def show_stats():
    """ This function shows all the scores, the sum of the scores, the high score and the lowest score"""
    print("=== Player Score Analytics ===")    
    players_score = []
    if len(sys.argv) > 2:
        try:
            players_score = add_score(players_score)
            print(f"Scores processed: {players_score}")
        except ValueError as e:
            print(f"No scores provided. {e}")
        except NameError as e:
            print(f"Error: {e}")
        try:
            players = count_players(players_score)
            print(f"Total players: {players}")
        except TypeError as e:
            print(f"Error: {e}")
        try:
            total = total_score(players_score)
            print(f"Total score: {total}")
        except TypeError as e:
            print(f"Error: {e}")
        try:
            average = average_score(players_score)
            print(f"Average score: {average}")
        except TypeError as e:
            print(f"Error: {e}")
        try:
            high_score = max_score(players_score)
            print(f"Total score: {high_score}")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
        try:
            lowest_score = min_score(players_score)
            print(f"Low score: {lowest_score}")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError:
            print(f"Error: {e}")
        try:
            range = range_score(players_score)
            print(f"Score range: {range}")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
    elif len(sys.argv) < 2:
        try:
            players_score = add_score(players_score)
            print(f"Scores processed: {players_score}")
        except ValueError as e:
            print(f"No scores provided. {e}")

show_stats()
