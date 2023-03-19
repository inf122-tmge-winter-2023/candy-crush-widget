"""
    :module_name: cli
    :module_summary: a CLI for candy_crush_widget
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import logging
import click

from tilematch_tools import View, GameEngine, BoardFactory, \
    GameState
from candy_crush_widget.cc_game_state import CCGameState
from candy_crush_widget.cc_match_rules import HorizontalMatch, VerticalMatch

from candy_crush_widget.initial_tiles import initial_tiles, contains_matches
from candy_crush_widget.cc_game_loop import CCGameLoop
from candy_crush_widget.cc_scoring import CCScore
from candy_crush_widget.cc_game_board import CCGameBoard


@click.command()
@click.argument('rows')
@click.argument('cols')
def candy_crush(rows, cols):
    """Entry point to candy-crush"""
    try:
        rows = int(rows)
        cols = int(cols)
        cc_init(rows, cols)
    except ValueError:
        print("Invalid paramters received. Pass in the numbers of rows and columns. Ex: candy-crush 10 10") 


def cc_init(rows, cols):

    board = BoardFactory.create_board_with_tiles(CCGameBoard, rows, cols, initial_tiles(rows,cols))
    while contains_matches(board, [VerticalMatch(1), HorizontalMatch(1)]):
        board = BoardFactory.create_board_with_tiles(CCGameBoard, rows, cols, initial_tiles(rows,cols))

    score = CCScore()
    state = CCGameState(board, score)
    view = View(state)

    state.add_match_condition(VerticalMatch(1))
    state.add_match_condition(HorizontalMatch(1))
    loop = CCGameLoop(state, view)
    
    engine = GameEngine([loop])
    view.add_event_listener("ButtonRelease")
    engine.run()