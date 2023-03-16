from tilematch_tools.core import GameLoop 
from tilematch_tools import MatchCondition
class CCGameLoop(GameLoop):
    def clear_matches(self, matches_found: [MatchCondition.MatchFound]) -> None:
        return super().clear_matches(matches_found)
    
    def find_matches(self, match_rules: [MatchCondition]) -> [MatchCondition.MatchFound]:
        return super().find_matches(match_rules)
    
    def gameover(self) -> bool:
        return super().gameover()
    
    def handle_input(self) -> None:
        return super().handle_input()

    def update_view(self) -> None:
        return super().update_view()
    