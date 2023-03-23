from tilematch_tools import GameState, TileColor, NullTile

from .cc_game_board import CCGameBoard
from .cc_movement_rules import AbsoluteDescent
from .cc_scoring import CCScore
from .cc_tile import CCTile



class CCGameState(GameState):
    def __init__(self, board: CCGameBoard, score: CCScore):
        super().__init__(board, score)
        self.selected_tile = None

    def select_tile(self, clicked_tile: CCTile):
        if not self.selected_tile:
            self.selected_tile = clicked_tile
            self.selected_tile.border = TileColor.RED
            return
        
        if self.selected_tile.position != clicked_tile.position:
            self.swap_tiles(self.selected_tile, clicked_tile)
            self.selected_tile.border = TileColor.GRAY
            self.selected_tile = None
        
    def collapse_all(self):
        for x in range(1, self.board.num_cols + 1):
            for y in range(1, self.board.num_rows + 1):
                if(not isinstance(self.board.tile_at(x,y), NullTile)):
                    collapse = AbsoluteDescent()
                    collapse.move(self.board, self.board.tile_at(x,y))
        
    def gameover(self) -> bool:
        return self.score.score > 49