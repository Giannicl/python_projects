from ex0.CreatureCard import CreatureCard

def main():
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")

    fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    fire_dragon_info = fire_dragon.get_card_info()
    print(f"{fire_dragon_info}")
    
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}") 
    
    play_results = fire_dragon.play({})
    print(f"Play result: {play_results}")

    attack_results = fire_dragon.attack_target('Goblin Warrior')
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"attack result: {attack_results}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")

main()
