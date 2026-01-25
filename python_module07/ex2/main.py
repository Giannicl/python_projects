from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    card_methods = ["play", "get_card_info", "is_playable"]
    combatable_methods = ["attack", "defend", "get_combat_stats"]
    magical_methods = ["cast_spell", "channel_mana", "get_magic_stats"]
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    arcane_warrior = EliteCard("Arcane Warrior", 8, "Ultra rare", 5, 15, 20, "melee")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}")
    print("\nMagic phase:")
    print(f"Spell cast: {arcane_warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


main()
