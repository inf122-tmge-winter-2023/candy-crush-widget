"""
    :module_name: cli
    :module_summary: a CLI for candy_crush_widget
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import logging
import click

from tilematch_tools import  GameEngine, BoardFactory, Game
from .cc_model import CCGameState, CCGameLoop, CCScore, CCGameBoard,  HorizontalMatch, VerticalMatch
from .cc_view import CCView
from .initial_tiles import *

LOGGER = logging.getLogger(__name__)

@click.command()
def candy_crush():
    """Entry point to candy-crush"""
    cc_init()

def cc_init():
    rows = CCGameBoard.BOARD_HEIGHT
    cols = CCGameBoard.BOARD_WIDTH
    
    board = BoardFactory.create_board_with_tiles(CCGameBoard, rows, cols, initial_tiles(rows,cols))
    COUNT = 0
    while contains_matches(board, [VerticalMatch(1), HorizontalMatch(1)]):
        board = BoardFactory.create_board_with_tiles(CCGameBoard, rows, cols, initial_tiles(rows,cols))
        COUNT += 1
    LOGGER.critical(f"Generated {COUNT} sets of tiles")
    score = CCScore()
    state = CCGameState(board, score)
    state.add_match_condition(VerticalMatch(1))
    state.add_match_condition(HorizontalMatch(1))

    engine = GameEngine([Game(state, CCGameLoop, CCView, 750_000_000)])
    engine.run()