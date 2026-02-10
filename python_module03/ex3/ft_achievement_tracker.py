def create_achievements(
    game_achievements: dict, player: str, achievements: set
) -> dict:
    """This function creates a dictionary with player/ achievement pairs"""
    game_achievements[player] = achievements
    return game_achievements


def filter_unique(tuple_players: tuple) -> set:
    """This function filters all the unique achievements
    from the totality of achievements"""
    if len(tuple_players) == 2:
        set_player1, set_player2 = tuple_players
        return set(set_player1).union(set(set_player2))
    elif len(tuple_players) == 3:
        set_player1, set_player2, set_player3 = tuple_players
        return set(set_player1).union(set(set_player2)).union(set(set_player3))
    else:
        print("Max 3 players supported")
        return set()


def filter_common(players: tuple) -> set:
    """This function filters all the shared achievements"""
    if len(players) == 2:
        player1, player2 = players
        return set(player1).intersection(set(player2))
    elif len(players) == 3:
        player1, player2, player3 = players
        return (set(player1).intersection(set(player2))
                .intersection(set(player3)))
    else:
        print("Max 3 players supported")
        return set()


def filter_rare(all_achievements: list) -> set:
    """This function filters all the functions that are unique to a player"""
    i = 0
    rare_achievements = []
    while i < len(all_achievements):
        c = 0
        j = 0
        while j < len(all_achievements):
            if all_achievements[i] == all_achievements[j]:
                c += 1
            j += 1
        if c == 1:
            rare_achievements += [all_achievements[i]]
        i += 1
    return set(rare_achievements)


def test_tracker_system():
    """This function tests the achievement tracker system.
    The function tracks unique achievments, finds shared achievements,
    spots the rare achievements, clusters players with shared achievements
    and checks what player is missing which achievement
    """
    game_achievements = {}
    alice = ["first_kill", "level_10", "treasure_hunter", "speed_demon"]
    bob = ["first_kill", "level_10", "boss_slayer", "collector"]
    charlie = [
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    ]
    game_achievements = (create_achievements(game_achievements,
                                             "alice", set(alice)))
    game_achievements = (create_achievements(game_achievements,
                                             "bob", set(bob)))
    game_achievements = (create_achievements(game_achievements,
                                             "charlie", set(charlie)))
    print("=== Achievement Tracker System ===")
    print(f"\nPlayer alice achievements: {game_achievements['alice']}")
    print(f"Player bob achievements: {game_achievements['bob']}")
    print(f"Player charlie achievements: {game_achievements['charlie']}")
    unique_achievements = filter_unique((alice, bob, charlie))
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    common_achievement = filter_common((alice, bob, charlie))
    all_achievements = alice + bob + charlie
    rare_achievements = filter_rare(all_achievements)
    print(f"\nCommon to all players: {common_achievement}")
    print(f"Rare achievements (1 player): {rare_achievements}")
    print(f"\nAlice vs Bob common: {filter_common((alice, bob))}")
    print(f"Alice unique: {set(alice).difference(set(bob))}")
    print(f"Bob unique: {set(bob).difference(set(alice))}")


if __name__ == "__main__":
    test_tracker_system()
