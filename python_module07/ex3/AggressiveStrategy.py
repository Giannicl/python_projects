from typing import Dict, List
from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        creatures = []
        remainder = []
        mana_used = 0
        damage_dealt = 0
        size_creatures = 0
        size_remainder = 0
        for item in hand:
            card = item.__class__.__name__
            if card == "CreatureCard":
                creatures = creatures + [item]
            else:
                remainder = remainder + [item]
            
        for item in creatures:
            size_creatures = size_creatures + 1
        for item in remainder:
            size_remainder = size_remainder + 1
        if size_creatures > 1:
            index = 0
            while index < size_creatures:
                index2 = 0
                while index2 < size_creatures - index - 1:
                    if creatures[index2].attack < creatures[index2 + 1].attack:
                        temp = creatures[index2]
                        creatures[index2] = creatures[index2 + 1]
                        creatures[index2 + 1] = temp
                    index2 = index2 + 1
                index = index + 1
        cards_played = creatures + remainder
        name_cards_played = []
        for card in cards_played:
           name_cards_played = name_cards_played + [card.name + f" ({card.cost})"] 


        for card in battlefield:
            if card.__class__.__name__ == "CreatureCard":
                damage_dealt = damage_dealt + card.attack
        for card in cards_played:
            mana_used = mana_used + card.cost
        return {'strategy': 'AggressiveStrategy',
                'cards_played': name_cards_played,
                'mana_used': mana_used,
                'damage_dealt': damage_dealt
                }
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        prioritize = []
        for targets in available_targets:
            if "goblin" in targets:
                prioritize = prioritize + [targets]
        return prioritize
