from typing import  Type
from tilematch_tools import GameFactory, Game, BoardFactory
from .cc_game_state import CCGameState
from .cc_game_board import CCGameBoard
from .cc_game_loop import CCGameLoop
from .cc_scoring import CCScore
from .cc_match_rules import HorizontalMatch, VerticalMatch
from ..initial_tiles import get_unique_tiles
from ..cc_view import CCView

import logging
LOGGER = logging.getLogger(__name__)

class CandyCrush(Game):
    def __init__(self, state: CCGameState, loop_class: Type[CCGameLoop], view_class: Type[CCView], tick_speed: int):
        super().__init__(state, loop_class, view_class, tick_speed)

    def setup(self):
        LOGGER.info("Setting up Candy Crush")
        self.state.add_match_condition(VerticalMatch(1))
        self.state.add_match_condition(HorizontalMatch(1))

class CCFactory(GameFactory):
    @staticmethod
    def create_game():
        board = BoardFactory.create_board_with_tiles(CCGameBoard, CCGameBoard.BOARD_HEIGHT, CCGameBoard.BOARD_WIDTH, get_unique_tiles())
        score = CCScore()
        state = CCGameState(board, score)
        game =  CandyCrush(state, CCGameLoop, CCView, 750_000_000)
        LOGGER.info("Created Candy Crush Game Object")
        game.setup()
        return game
