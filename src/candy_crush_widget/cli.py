"""
    :module_name: cli
    :module_summary: a CLI for candy_crush_widget
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import logging
import click

from tilematch_tools import View, GameEngine, BoardFactory, \
    GameState, LOGGER

from candy_crush_widget.initial_tiles import initial_tiles
from candy_crush_widget.cc_game_loop import CCGameLoop
from candy_crush_widget.cc_scoring import CCScore
from candy_crush_widget.cc_game_board import CCGameBoard

LOGGER.setLevel(logging.ERROR)


@click.command()
def candy_crush():
    """Entry point to candy-crush"""
    cc_init()


def cc_init():
    board = BoardFactory.create_board_with_tiles(CCGameBoard, 10, 10, initial_tiles(10,10))
    score = CCScore()
    state = GameState(board, score)
    view = View(state)

    loop = CCGameLoop(state, view)

    engine = GameEngine([loop])
    engine.run()