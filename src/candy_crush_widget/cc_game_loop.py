from collections.abc import Iterable
import queue
import time
from tilematch_tools.core import GameLoop 
from tilematch_tools import MatchCondition, View
from tilematch_tools.core.game_loop import FPSDelay

from .cc_game_state import CCGameState

class CCGameLoop(GameLoop):
    def __init__(self, state: CCGameState, view: View, delay: FPSDelay = FPSDelay.FPS30):
        super().__init__(state, view, delay)

    def clear_matches(self, matches_found: Iterable[MatchCondition.MatchFound]) -> None:
        """ Omitting the sleep from super()
            :arg matches_found: list of discovered matches to clear
            :arg type: list
            :returns: nothing
            :rtype: None
        """
        for match in matches_found:
            self._state.clear_match(match)
            self._state.adjust_score(match)
        self.state.collapse_all()
    

        
        

    
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
        try:
            mouse_event = self.view.mouse_event
            self.state.select_tile(mouse_event[0], mouse_event[1])
        except queue.Empty:
            pass
            
    def update_view(self) -> None:
        return super().update_view()
    