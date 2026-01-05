def test_analytics_dashboard():
    players_data = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "speed_run",
                "perfect_score",
            ],
            "region": "north",
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "region": "east",
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "speed_run",
                "perfect_score",
                "triple_kill",
                "headshot",
            ],
            "region": "central",
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "achievements": ["first_kill", "level_10"],
            "region": "west",
        },
    ]
    print("=== Game Analytics Dashboard ===")
    high_scorers = [player["name"] for player in players_data if player["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers} ")
    scores_doubled = [player["score"] * 2 for player in players_data]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [player["name"] for player in players_data if player["active"]]
    print(f"Active players: {active_players}")
    print("\n=== Dict Comprehension Examples ===")
    players_scores = {
        player["name"]: player["score"] for player in players_data if player["active"]
    }
    print(f"Player scores: {players_scores}")
    score_categories = {
        "high": sum(1 for player in players_data if player["score"] > 2000),
        "medium": sum(1 for player in players_data if 1500 < player["score"] <= 2000),
        "low": sum(1 for player in players_data if player["score"] <= 1500),
    }
    print(f"Score categories: {score_categories}")
    achievement_count = {
        player["name"]: len(player["achievements"])
        for player in players_data
        if len(player["achievements"]) > 2
    }
    print(f"Achievement counts: {achievement_count}")
    print("\n=== Set Comprehension Examples ===")
    unique_players = {player["name"] for player in players_data}
    print(f"Unique players: {unique_players}")
    list_achievements = [
        item for player in players_data for item in player["achievements"]
    ]
    unique_achievements = {item for item in list_achievements}
    print(f"Unique achievements: {unique_achievements}")


test_analytics_dashboard()
