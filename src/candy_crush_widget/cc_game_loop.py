from collections.abc import Iterable
from tilematch_tools.core import GameLoop 
from tilematch_tools import MatchCondition
class CCGameLoop(GameLoop):
    def clear_matches(self, matches_found: Iterable[MatchCondition.MatchFound]) -> None:
        return super().clear_matches(matches_found)
    
    def find_matches(self, match_rules: Iterable[MatchCondition]) -> Iterable[MatchCondition.MatchFound]:
        matches_found = []
        for match_rule in match_rules:
            match_found = match_rule.check_match(self.state.board, 1, 1)
            if match_found is not None:
                matches_found.append(match_found)
        return matches_found
    
    def gameover(self) -> bool:
        return super().gameover()
    
    def handle_input(self) -> None:
        return super().handle_input()

    def update_view(self) -> None:
        return super().update_view()
    