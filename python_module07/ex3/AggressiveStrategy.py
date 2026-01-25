from typing import Dict, List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        pass

    def get_strategy_name(self) -> str:
        pass

    def prioritize_targets(self, available_targets: List) -> List:
        pass
