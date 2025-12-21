
def create_achievements(game_achievements, player, achievements):
    game_achievements[player] = achievements;
    return game_achievements

def filter_unique(tuple_players):
    if len(tuple_players) == 2:
        set_player1, set_player2 = tuple_players
        return set(set_player1).union(set(set_player2))
    elif len(tuple_players) == 3:
        set_player1, set_player2, set_player3 = tuple_players
        return set(set_player1).union(set(set_player2)).union(set(set_player3))

def filter_common(tuple_players):
    if len(tuple_players) == 2:
        set_player1, set_player2 = tuple_players
        return set(set_player1).intersection(set(set_player2))
    elif len(tuple_players) == 3:
        set_player1, set_player2, set_player3 = tuple_players
        return set(set_player1).intersection(set(set_player2)).intersection(set(set_player3))

def filter_rare(all_achievements):
    i = 0
    rare_achievements = []
    print(f"{all_achievements}")
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
    game_achievements = {}
    alice = ["first_kill", "level_10", "treasure_hunter", "speed_demon"]
    bob = ["first_kill", "level_10", "boss_slayer", "collector"]
    charlie = ["level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"]
    game_achievements = create_achievements(game_achievements, "alice", set(alice))
    game_achievements = create_achievements(game_achievements, "bob", set(bob))
    game_achievements = create_achievements(game_achievements, "charlie", set(charlie))

    print("=== Achievement Tracker System ===")
    print(f"\nPlayer alice achievements: {game_achievements["alice"]}")
    print(f"Player bob achievements: {game_achievements["bob"]}")
    print(f"Player charlie achievements: {game_achievements["charlie"]}")
    unique_achievements = filter_unique((alice, bob, charlie))
    print(f"\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    common_achievement = filter_common((alice, bob, charlie))
    all_achievements = alice + bob + charlie
    rare_achievements = filter_rare(all_achievements)
    print(f"Common to all players: {common_achievement}")
    print(f"Rare achievements (1 player): {rare_achievements}")
    print(f"\nAlice vs Bob common: {filter_common((alice, bob))}")


test_tracker_system()
