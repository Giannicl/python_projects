from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            if "dragon" in name_lower:
                return CreatureCard(name_or_power, 8, "Legendary", 10, 8)
            elif "goblin" in name_lower:
                return CreatureCard(name_or_power, 2, "Common", 2, 2)
            elif "knight" in name_lower:
                return CreatureCard(name_or_power, 5, "Rare", 6, 6)
            else:
                attack = random.randint(3, 10)
                rarity_category = ["Legendary", "Common", "Rare"]
                rarity = random.choice(rarity_category)
                health = random.randint(3, 10)
                cost = random.randint(1, 6)
                return CreatureCard(name_or_power, cost,
                                    rarity, attack, health)
        elif isinstance(name_or_power, int):
            attack = random.randint(3, 10)
            rarity_category = ["Legendary", "Common", "Rare"]
            rarity = random.choice(rarity_category)
            health = random.randint(3, 10)
            cost = random.randint(1, 6)
            return CreatureCard("Unknown Creature", cost, rarity,
                                attack, health)
        else:
            return CreatureCard("Slime", 5, "Common", 0, 0)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            if "lightning" in name_lower:
                return SpellCard(name_or_power, 6, "Legendary", "damage")
            elif "air" in name_lower:
                return SpellCard(name_or_power, 2, "Common", "damage")
            elif "fire" in name_lower:
                return SpellCard(name_or_power, 5, "Rare", "damage")
            else:
                rarity_category = ["Legendary", "Common", "Rare"]
                rarity = random.choice(rarity_category)
                cost = random.randint(1, 6)
                return SpellCard(name_or_power, cost, rarity, "damage")
        elif isinstance(name_or_power, int):
            rarity_category = ["Legendary", "Common", "Rare"]
            rarity = random.choice(rarity_category)
            cost = random.randint(1, 6)
            return SpellCard("Unknown Spell", cost, rarity, "damage")
        else:
            return SpellCard("Cast Failure", 5, "Common", "Fail")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            if "mana" in name_lower:
                return ArtifactCard(
                    name_or_power, 6, "Legendary", -1, "+1 mana per turn"
                )
            elif "armor" in name_lower:
                return ArtifactCard(name_or_power, 2, "Common", 5, "+2 health")
            elif "elixir" in name_lower:
                return ArtifactCard(
                    name_or_power, 5, "Rare", 1, "full health recovery "
                )
            else:
                rarity_category = ["Legendary", "Common", "Rare"]
                rarity = random.choice(rarity_category)
                cost = random.randint(1, 6)
                durability = random.randint(-1, 20)
                effect_category = ["+1 mana per turn", "+1 health per turn"]
                effect = random.choice(effect_category)
                return ArtifactCard(name_or_power, cost, rarity,
                                    durability, effect)
        elif isinstance(name_or_power, int):
            rarity_category = ["Legendary", "Common", "Rare"]
            rarity = random.choice(rarity_category)
            durability = random.randint(-1, 20)
            effect_category = ["+1 mana per turn", "+1 health per turn"]
            effect = random.choice(effect_category)
            cost = random.randint(1, 6)
            return ArtifactCard("Unknown Spell", cost, rarity,
                                durability, effect)
        else:
            return SpellCard("Stone", 5, "Common", 0)

    def create_themed_deck(self, size: int) -> Dict:
        deck = []
        get_supported_types = self.get_supported_types()

        item_count = size
        while size > 0:
            card_type = random.choice(["creatures", "spells", "artifacts"])
            if card_type == "creatures":
                card_name = random.choice(get_supported_types[card_type])
                card = self.create_creature(card_name)
            elif card_type == "spells":
                card_name = random.choice(get_supported_types[card_type])
                card = self.create_spell(get_supported_types[card_name])
            else:
                card_name = random.choice(get_supported_types[card_type])
                card = self.create_artifact(get_supported_types[card_name])
            deck = deck + [card]
            size = size - 1
        return {"deck": deck, "size": item_count, "theme": "Fantasy"}

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin", "knight"],
            "spells": ["lightning", "air", "fire"],
            "artifacts": ["mana", "armor", "elixir"],
        }
