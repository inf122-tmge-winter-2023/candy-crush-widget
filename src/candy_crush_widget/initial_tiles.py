import random
from tilematch_tools import TileBuilder, MatchCondition
from collections.abc import Iterable
from .cc_model import CCTileColor, CCTile



builder = TileBuilder()
def initial_tiles(num_rows, num_cols):
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