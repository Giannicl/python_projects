from typing import Dict

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.power = self.cost*2
    def play(self, game_state: Dict)-> Dict:
        effect = ""
        if self.effect_type == "damage":
            effect = f"Deal {self.power} {self.effect_type} to target"
        elif self.effect_type == "heal":
            effect = f"Gain {power} HP"
        else:
            effect = f"{self.effect_type} spell cast"
        return {'card_played': self.name, 'mana_used': self.cost, 'effect': effect}
    def resolve_effect(self, targets: List)-> Dict:
        return {'spell': self.name,
               'effect_type': self.effect_type,
               'targets': targets,
               'power': self.power,
               'resolved': True
                }
        




