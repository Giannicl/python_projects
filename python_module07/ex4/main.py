from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...")

    fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 10, 8, "melee")
    ice_wizard = TournamentCard("Ice Wizard", 4, "Rare", 6, 7, "magic")

    platform = TournamentPlatform()

    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    print(f"\nFire Dragon (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {fire_dragon.calculate_rating()}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")

    print(f"\nIce Wizard (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {ice_wizard.calculate_rating()}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    position = 1
    for entry in leaderboard:
        print(
            f"{position}. {entry['name']} - Rating: {entry['rating']} "
            f"({entry['wins']}-{entry['losses']})"
        )
        position = position + 1

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(f"{report}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
