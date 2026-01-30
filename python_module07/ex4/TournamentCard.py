from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict
    

class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, 
                 attack: int, health: int, combat_type: str,
                 interaces: List):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.defence = self.health // 6
        self.wins = 0
        self.losses = 0
        self.score = 0
        self.combat_type = combat_type
        self.interaces = interaces

    def play(self, game_state: Dict) -> Dict:
        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Tournament card summoned to the battleield",
               }
    def attack(self, target) -> Dict:
        return {
                "attacker": self.name,
                "target": target,
                "damage": self.attack_power,
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
    def get_combat_stats(self):
        return {
            "attack_power": self.attack_power,
            "health": self.health,
            "combat_type": self.combat_type,
            "defence": self.defence,
        }
    def calculate_rating(self) -> int:
        return self.score - (self.losses * 50) + (self.wins * 50)
    def update_wins(self, wins: int)-> None:
        self.wins = wins
    def update_losses(self, losses: int)-> None:
        self.losses = losses
    def get_rank_info(self,)-> Dict:
        return { 
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
        }
    def get_tournament_stats(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "attack_power": self.attack_power,
            "health": self.health,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}"
            }


