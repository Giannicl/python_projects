from abc import ABC, abstractmethod
from typing import Dict, List, Any, Protocol
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to the battlefield",
        }

    def attack_target(self, target: Any) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = "Creature"
        info['attack'] = self.attack
        info['health'] = self.health
        return info



