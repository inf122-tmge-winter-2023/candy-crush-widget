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
@click.argument('rows')
@click.argument('cols')
def candy_crush(rows, cols):
    """Entry point to candy-crush"""
    try:
        rows = int(rows)
        cols = int(cols)
        cc_init(rows, cols)
    except ValueError as e:
        print("Invalid paramters received. Pass in the numbers of rows and columns. Ex: candy-crush 10 10") 


def cc_init(rows, cols):
    board = BoardFactory.create_board_with_tiles(CCGameBoard, rows, cols, initial_tiles(rows,cols))
    score = CCScore()
    state = GameState(board, score)
    view = View(state)

    loop = CCGameLoop(state, view)

    engine = GameEngine([loop])
    engine.run()