from tilematch_tools import GameState, TileColor, NullTile, TileBuilder

from .cc_colors import CCTileColor
from .cc_game_board import CCGameBoard
from .cc_movement_rules import AbsoluteDescent
from .cc_scoring import CCScore
from .cc_tile import CCTile

import random

class CCGameState(GameState):
    def __init__(self, board: CCGameBoard, score: CCScore):
        super().__init__(board, score)
        self.selected_tile = None
        self.moves_left = 25

    def select_tile(self, clicked_tile: CCTile):
        if not self.selected_tile:
            self.selected_tile = clicked_tile
            self.selected_tile.border = TileColor.RED
            return
        
        if self.selected_tile.position != clicked_tile.position:
            self.swap_tiles(self.selected_tile, clicked_tile)
            self.selected_tile.border = TileColor.GRAY
            self.selected_tile = None
            self.moves_left -= 1
        
    def collapse_all(self):
        for x in range(1, self.board.num_cols + 1):
            for y in range(1, self.board.num_rows + 1):
                if(not isinstance(self.board.tile_at(x,y), NullTile)):
                    collapse = AbsoluteDescent()
                    collapse.move(self.board, self.board.tile_at(x,y))
        
    def regen_tiles(self):
        tile_builder = TileBuilder()
        for x in range(1, self.board.num_cols + 1):
            for y in range(1, self.board.num_rows + 1):
                if(isinstance(self.board.tile_at(x,y), NullTile)):

                    random_tile = tile_builder \
                        .add_position(x,y) \
                        .add_color(random.choice(list(CCTileColor))) \
                        .construct(CCTile)
                    self.board.place_tile(random_tile)


    def gameover(self) -> bool:
        return self.moves_left <= 0