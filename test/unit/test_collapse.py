import logging
import click

from tilematch_tools import  BoardFactory, \
    GameState, NullTile, TileBuilder

from candy_crush_widget.cc_model import CCScore, CCGameBoard, CCTile, CCTileColor, CCGameState
from candy_crush_widget import LOGGER, LOG_HANDLER

init_tiles = [
                TileBuilder().add_position(3, 2).add_color(CCTileColor.PURPLE).construct(CCTile),
                TileBuilder().add_position(4, 2).add_color(CCTileColor.RED).construct(CCTile),
                TileBuilder().add_position(5, 2).add_color(CCTileColor.RED).construct(CCTile),
                TileBuilder().add_position(4, 4).add_color(CCTileColor.BLUE).construct(CCTile),
                TileBuilder().add_position(7, 7).add_color(CCTileColor.ORANGE).construct(CCTile)
                ]

LOGGER.setLevel(logging.INFO)
LOG_HANDLER.setLevel(logging.INFO)
def test_collapse_tiles():
    board = BoardFactory.create_board_with_tiles(CCGameBoard, 7, 7, init_tiles)
    score = CCScore()
    state = CCGameState(board, score)
    state.collapse_all()
    state.collapse_all()

    assert isinstance(state.board.tile_at(3,2), NullTile)
    assert isinstance(state.board.tile_at(3,1), CCTile)
