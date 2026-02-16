from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        durability = ""
        if self.durability == -1:
            durability = f"Permanent: {self.effect}"
        else:
            durability = f"Durability {self.durability} turns: {self.effect}"
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": durability}

    def activate_ability(self) -> Dict:
        if self.durability > 0:
            self.durability = self.durability - 1
            durability_remainder = self.durability
        else:
            durability_remainder = "Permanent"
        return {
            "artifact": self.name,
            "effect_activated": self.effect,
            "durability": durability_remainder,
            "activated": True,
        }
