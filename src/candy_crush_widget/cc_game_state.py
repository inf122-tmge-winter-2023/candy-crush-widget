from tilematch_tools import GameState, TileColor, NullTile

from .cc_game_board import CCGameBoard
from .cc_scoring    import CCScore
from candy_crush_widget.cc_movement_rules import AbsoluteDescent

class CCGameState(GameState):
    def __init__(self, board: CCGameBoard, score: CCScore):
        super().__init__(board, score)
        self.selected_tile = None

    def select_tile(self, x: int, y: int):
        if not self.selected_tile:
            self.selected_tile = self.board.tile_at(x, y)
            self.selected_tile.border = TileColor.RED
            return
        
        if self.selected_tile.position != self.board.tile_at(x,y).position:
            self.swap_tiles(self.selected_tile, self.board.tile_at(x, y))
            self.selected_tile.border = TileColor.GRAY
            self.selected_tile = None
        
    def collapse_all(self):
        for x in range(1, self.board.num_cols + 1):
            for y in range(1, self.board.num_rows + 1):
                if(not isinstance(self.board.tile_at(x,y), NullTile)):
                    collapse = AbsoluteDescent()
                    collapse.move(self.board, self.board.tile_at(x,y))
                    