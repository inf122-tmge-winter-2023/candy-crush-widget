import logging
import random
from tilematch_tools import TileBuilder, MatchCondition, BoardFactory
from collections.abc import Iterable
from .cc_model import CCTileColor, CCTile, CCGameBoard, VerticalMatch, HorizontalMatch

LOGGER = logging.getLogger(__name__)


builder = TileBuilder()
def random_tiles(num_rows, num_cols):
    tiles = []
    colors = list(CCTileColor)
    for x in range(1,num_rows + 1):
        for y in range(1,num_cols + 1):
            tiles.append(builder.add_position(x,y).add_color(random.choice(colors)).construct(CCTile))
    return tiles


def contains_matches(board, match_rules: Iterable[MatchCondition]):
    for match_rule in match_rules:
        if match_rule.check_match(board, 1, 1) is not None:
            return True
    return False

def get_unique_tiles() -> Iterable[CCTile]:
    rows = CCGameBoard.BOARD_HEIGHT
    cols = CCGameBoard.BOARD_WIDTH

    tiles_to_try = random_tiles(rows,cols)
    board = BoardFactory.create_board_with_tiles(CCGameBoard, rows, cols, tiles_to_try)
    COUNT = 0
    while contains_matches(board, [VerticalMatch(1), HorizontalMatch(1)]):
        tiles_to_try = random_tiles(rows, cols)
        board = BoardFactory.create_board_with_tiles(CCGameBoard, rows, cols, tiles_to_try)
        COUNT += 1
    LOGGER.info(f"Generated {COUNT} sets of tiles")
    
    return tiles_to_try
        