import sys


def add_score(players_score: list) -> list:
    """This function creates, and returns,
    a list with the added players score"""
    if len(sys.argv) < 2:
        raise ValueError(
            "No scores provided. "
            f"Usage: python3 {sys.argv[0]} <score1> <score2> ..."
        )
    else:
        i = 1
        while i < len(sys.argv):
            players_score += [int(sys.argv[i])]
            i += 1
    return players_score


def count_players(players_score: list) -> int:
    """This function counts and returns the amount of players scores
    that were added"""
    return len(players_score)


def total_score(players_score: list) -> int:
    """This function returns the sum of all the scores"""
    return sum(players_score)


def average_score(players_score: list) -> float:
    """This function returns the average of all scores"""
    return sum(players_score) / len(players_score)


def max_score(players_score: list) -> int:
    """This function returns the highest score"""
    return max(players_score)


def min_score(players_score: list) -> int:
    """This function returns the lowest score"""
    return min(players_score)


def range_score(players_score: list) -> int:
    """This function returns the range between the maximum and minimum score"""
    return max(players_score) - min(players_score)


def show_stats() -> None:
    """This function displays the statistics of all the scores (all the scores,
    the amount of players added, the sum of all scores,
    the highscore, the lowest score and the range)"""
    print("=== Player Score Analytics ===")
    players_score = []
    if len(sys.argv) > 1:
        try:
            players_score = add_score(players_score)
            print(f"Scores processed: {players_score}")
            players = count_players(players_score)
            print(f"Total players: {players}")
            total = total_score(players_score)
            print(f"Total score: {total}")
            average = average_score(players_score)
            print(f"Average score: {average}")
            high_score = max_score(players_score)
            print(f"High score: {high_score}")
            lowest_score = min_score(players_score)
            print(f"Low score: {lowest_score}")
            range = range_score(players_score)
            print(f"Score range: {range}")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
    elif len(sys.argv) < 2:
        try:
            players_score = add_score(players_score)
            print(f"Scores processed: {players_score}")
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"{e}")


if __name__ == "__main__":
    show_stats()
