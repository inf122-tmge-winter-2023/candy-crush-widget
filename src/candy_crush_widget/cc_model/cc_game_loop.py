from collections.abc import Iterable
import time
from tilematch_tools import MatchCondition, GameView, GameLoop

from candy_crush_widget.cc_view import CCMouseEvent

from .cc_game_state import CCGameState

class CCGameLoop(GameLoop):
    def __init__(self, state: CCGameState, view: GameView, delay: int = 1000000000):
        super().__init__(state, view, delay)
        self.bind_inputs()

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

    def tick(self) -> None:
        return super().tick()
    
    def clean_up_state(self):
        time.sleep(.2)
        self.state.collapse_all()

    def find_matches(self, match_rules: Iterable[MatchCondition]) -> Iterable[MatchCondition.MatchFound]:
        matches_found = []
        for match_rule in match_rules:
            match_found = match_rule.check_match(self.state.board, 1, 1)
            if match_found is not None:
                matches_found.append(match_found)
        return matches_found

    def bind_inputs(self):
        self.view.bind_click('<Button-1>', CCMouseEvent(self.state, self.view.board_view))

