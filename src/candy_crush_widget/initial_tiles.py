import logging
import random
from tilematch_tools import TileBuilder, MatchCondition
from collections.abc import Iterable
from candy_crush_widget.cc_colors import CCTileColor
from candy_crush_widget.cc_tile import CCTile

LOGGER = logging.getLogger(__name__)
COUNT = 0

builder = TileBuilder()
def initial_tiles(num_rows, num_cols):
    tiles = []
    colors = list(CCTileColor)
    for x in range(1,num_rows + 1):
        for y in range(1,num_cols + 1):
            tiles.append(builder.add_position(x,y).add_color(random.choice(colors)).construct(CCTile))
    global COUNT
    COUNT = COUNT + 1
    LOGGER.info(f"Generated {COUNT} sets of tiles")
    return tiles


def contains_matches(board, match_rules: Iterable[MatchCondition]):
    for match_rule in match_rules:
        if match_rule.check_match(board, 1, 1) is not None:
            return True
    return False