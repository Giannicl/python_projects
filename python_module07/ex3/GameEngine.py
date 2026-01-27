from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict
from random import randint

class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turn_count = 0
        self.total_damage = 0
        self.cards_created = 0
        
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> Dict:
        self.factory = factory
        self.strategy = strategy
        return {
            'factory_configured': True,
            'strategy_configured': True,
            'strategy_name': self.strategy.get_strategy_name()
        }
    
    def simulate_turn(self) -> Dict:
        self.hand = []
        card_count = 0
        while card_count < 5:
            card_type_choice = randint(0,2)
            if card_type_choice == 0:
                card = self.factory.create_creature()
            elif card_type_choice == 1:
                card = self.factory.create_spell()
            else:
                card = self.factory.create_artifact()
            self.hand = self.hand + [card]
            card_count = card_count + 1
        self.cards_created = card_count
        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)
        for card in turn_result['cards_played']:
            self.battlefield = self.battlefield + [card]
        self.turn_count = self.turn_count + 1
        self.total_damage = self.total_damage + turn_result['damage_dealt']
        return turn_result
    
    def get_engine_stats(self) -> Dict:
        battlefield_size = 0
        for card in self.battlefield:
            battlefield_size = battlefield_size + 1
        
        return {
            'turns_simulated': self.turn_count, 
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
