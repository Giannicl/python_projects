from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card
from typing import Dict, List


class EliteCard(Combatable, Magical, Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana: int,
        combat_type: str,
    ):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.power = self.cost * 3
        self.health = health
        self.mana = mana
        self.combat_type = combat_type
        self.defence = self.health // 6
        self.spells = []

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "elite warrior summoned to the battlefield",
        }

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack,
            "combat_type": self.combat_type,
        }

    def defend(self, incoming_damage: int) -> Dict:
        remainder_damage = incoming_damage - self.defence
        self.health = self.health - remainder_damage
        alive = self.health > 0
        return {
            "defender": self.name,
            "damage_taken": remainder_damage,
            "damage_blocked": incoming_damage - remainder_damage,
            "still_alive": alive,
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        mana_cost = self.cost
        self.mana = self.mana - mana_cost
        self.spells = self.spells + [spell_name]
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "damage": self.power,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana = self.mana + amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_combat_stats(self):
        return {
            "attack_power": self.attack,
            "health": self.health,
            "combat_type": self.combat_type,
            "defence": self.defence,
        }

    def get_magic_stats(self):
        return {
            "current_mana": self.mana,
            "spell_power": self.power,
            "spells": self.spells,
        }
