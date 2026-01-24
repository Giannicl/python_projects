from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main():
    print("=== DataDeck Deck Builder ===")

    deck = Deck()
    lightning_bolt = SpellCard("Lightning Bolt", 4, "common", "damage")
    deck.add_card(lightning_bolt)
    mana_crystal = ArtifactCard("Mana Crystal", 3, "ultra rare", -1, "+1 mana per turn")
    deck.add_card(mana_crystal)
    fire_dragon = CreatureCard("Fire Dragon", 5, "rare", 3, 10)
    deck.add_card(fire_dragon)

    print("\nBuilding deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    print(f"\nDrew: {deck.draw_card().name} (Spell)")
    print(f"Play result: {lightning_bolt.play({})}")

    print(f"\nDrew: {deck.draw_card().name} (Artifact)")
    print(f"Play result: {mana_crystal.play({})}")

    print(f"\nDrew: {deck.draw_card().name} (Creature)")
    print(f"Play result: {fire_dragon.play({})}")

    print("\nPolymorphism in action: Same interface, different card behaviors!")


main()
