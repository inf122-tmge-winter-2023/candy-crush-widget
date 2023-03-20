

import logging
from candy_crush_widget.cc_colors import CCTileColor
from candy_crush_widget.cc_match_rules import HorizontalMatch, VerticalMatch
from candy_crush_widget.cc_scoring import CCScore
from candy_crush_widget.cc_game_board import CCGameBoard
from tilematch_tools import BoardFactory, GameState, TileBuilder


from candy_crush_widget.cc_tile import CCTile



def test_horizontal_match():
    board = BoardFactory.create_board(CCGameBoard, 10, 10)
    score = CCScore()
    state = GameState(board, score)

    for x in range(1,11):
        if x != 5 and x != 6 and x != 7:
            board.place_tile(TileBuilder().add_position(x,3).add_color(CCTileColor.BLUE).construct(CCTile))

    for x in range(3, 6):
        board.place_tile(TileBuilder().add_position(x,6).add_color(CCTileColor.BLUE).construct(CCTile))

    match = state.find_match(1,1, HorizontalMatch(1))
    assert  match.value == 10

def test_vertical_match():
    board = BoardFactory.create_board(CCGameBoard, 10, 10)
    score = CCScore()
    state = GameState(board, score)

    for y in range(1,11):
        if y != 5 and y != 6 and y != 7:
            board.place_tile(TileBuilder().add_position(3, y).add_color(CCTileColor.BLUE).construct(CCTile))

    for y in range(3, 6):
        board.place_tile(TileBuilder().add_position(6, y).add_color(CCTileColor.BLUE).construct(CCTile))

    match = state.find_match(1,1, VerticalMatch(1))
    assert  match.value == 10
