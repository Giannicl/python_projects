from ex4.TournamentCard import TournamentCard
from typing import Dict, List

class TournamentPlatform:
    def __init__(self):
        self.id = {}
        self.id_number = 000
        self.matches_played = 0
        
    def register_card(self, card: TournamentCard) -> str: 
        card_type = ""
        if "dragon" in card.name or "dragon" in card.name:
            card_type = "dragon"
        elif "wizard" in card.name or "wizard" in card.name:
            card_type = "wizard"
        else:
            card_type = "unknown_type"
        self.id_number = self.id_number + 1
        self.id[card_type + f"_{self.id_number}"] = card
        return card_type + f"_{self.id_number}"
    
    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        combatant1 = self.id[card1_id]
        combatant2 = self.id[card2_id]
        winner = ""
        loser = ""
        self.matches_played = self.matches_played + 1
        while combatant1.health > 0 and combatant2.health > 0:
            combatant2.health = combatant2.health - combatant1.attack_power
            combatant1.health = combatant1.health - combatant2.attack_power

        if combatant1.health <= 0:
            winner = card2_id
            combatant2.wins = combatant2.wins + 1
            loser = card1_id
            combatant1.losses = combatant1.losses + 1
        else:
            winner = card1_id
            combatant1.wins = combatant1.wins + 1
            loser = card2_id
            combatant2.losses = combatant2.losses + 1
        return {
                "winner": winner,
                "loser": loser,
                "winner_rating": self.id[winner].calculate_rating(),
                "loser_rating": self.id[loser].calculate_rating(),
        }
    def get_leaderboard(self) -> List:
        card_info = []
        for card_id in self.id:
            card = self.id[card_id]
            card_info = card_info + [{
                    "id": card_id,
                    "name": card.name,
                    "rating": card.calculate_rating(),
                    "wins": card.wins,
                    "losses": card.losses,
            }]
        size = 0
        for card in card_info:
            size = size + 1

        index = 0
        while index < size: 
            index2 = 0
            while index2 < size - 1 - index: 
                info = card_info[index]
                info2 = card_info[index2 + 1] 
                if info["rating"] < info2["rating"]:
                    temp = card_info[index2] 
                    card_info[index2] = card_info[index2 + 1]
                    card_info[index2 + 1] = temp
            index2 = index2 + 1
            index = index + 1
        return card_info
    def generate_tournament_report(self) -> Dict:
        size = 0
        for card_info in self.id:
            size = size + 1
        total_rating = 0
        for card_info in self.id:
            card = self.id[card_info]
            total_rating = total_rating + card.calculate_rating() 
        average_rating = total_rating / size if size > 0 else 0 
        return {
            "total_cards": size,
            "matches_played": self.total_matches_played,
            "average_rating": average_rating,
            "platorm_status": 'active'
        }
