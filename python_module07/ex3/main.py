from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():

    print("=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")
    card_factory = FantasyCardFactory()
    print(f"Factory: {card_factory.__class__.__name__}")
    strategy = AggressiveStrategy()
    print(f"Strategy: {strategy.get_strategy_name()}")
    supported_types = card_factory.get_supported_types()
    print(f"Available types: {supported_types}")

    print("\nSimulating aggressive turn...")
    fire_dragon = card_factory.create_creature("Fire Dragon")
    goblin_warrior = card_factory.create_creature("Goblin Warrior")
    lightning_bolt = card_factory.create_spell("Lightning Bolt")

    hand = [goblin_warrior, fire_dragon, lightning_bolt]
    simulating_aggressive_strategy = strategy.execute_turn(hand, [])

    print(f"Hand: {simulating_aggressive_strategy['cards_played']}")
    print("\nTurn execution:")
    engine = GameEngine()
    engine.configure_engine(card_factory, strategy)
    turn = engine.simulate_turn()
    print(f"Strategy: {turn['strategy']}")
    print(f"Actions: {turn}")
    print("\nGame Report:")
    print(f"{engine.get_engine_stats()}")


if __name__ == "__main__":
    main()
