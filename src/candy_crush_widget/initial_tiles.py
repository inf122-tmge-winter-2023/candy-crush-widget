import random
from tilematch_tools import TileBuilder

from candy_crush_widget.cc_colors import CCTileColor
from candy_crush_widget.cc_tile import CCTile

builder = TileBuilder()
def initial_tiles(num_rows, num_cols):
    tiles = []
    colors = list(CCTileColor)
    for x in range(1,num_rows + 1):
        for y in range(1,num_cols + 1):
            tiles.append(builder.add_position(x,y).add_color(random.choice(colors)).construct(CCTile))

    return tiles