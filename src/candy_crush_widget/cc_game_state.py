from tilematch_tools import GameState, TileColor

from .cc_game_board import CCGameBoard
from .cc_scoring    import CCScore
from tilematch_tools.model.match import MatchCondition

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
        
        