from typing import Dict
from ex0.Card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.deck = []
    def add_card(self, card: Card) -> None:
        self.deck = self.deck + [card]
        return self.deck
    def remove_card(self, card_name: str) -> bool:
        index = 0
        for card in self.deck:
            if card.name == card_name:
                del self.deck[index]
                return True
            index = index + 1
        return False
    def shuffle(self) -> None:
        shuffle(self.deck)
    def draw_card(self) -> Card: 
        card = self.deck[0]
        self.deck = self.deck[1:]
        return card
    def get_deck_stats(self) -> Dict: 
        creatures = 0 
        spells = 0 
        artifacts = 0 
        total_cost = 0
        total_cost = 0
        index = 0 
        for card in self.deck:
            if card.__class__.__name__ == "CreatureCard":
                creatures = creatures + 1
                average_cost = average_cost + card.cost
            elif card.__class__.__name__ == "ArtifactCard":
                artifacts = artifacts + 1
                average_cost = average_cost + card.cost
            elif card.__class__.__name__ == "SpellCard":
                spells = spells + 1
                average_cost = average_cost + card.cost
            index = index + 1
        total_cards = index 
        average_cost = total_cost / total_cards
        return {'total_cards': total_cards,
                'creatures': creatures,
                'spells': spells,
                'artifacts': artifacts,
                'average_cost': average_cost
        }
