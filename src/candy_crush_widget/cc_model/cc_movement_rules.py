import logging
import time
from tilematch_tools import MovementRule, GameBoard, Tile, NullTile
from tilematch_tools.model.exceptions import IllegalTileMovementException

LOGGER = logging.getLogger(__name__)

class AbsoluteDescent(MovementRule):
    """
        Class that specifies that a ColumnsTile descent until blocked
    """
    def apply(self, board: GameBoard, tile_to_move: Tile) -> None:
        """
            Logic for executing this tile movement. Should raise exception if cannot be completed
            :arg board: gameboard move will be executed on
            :arg tile_to_move: tile to be moved by this movement rule
            :arg type: GameBoard
            :arg type: Tile
            :raises: IllegalTileMovementException if the tile movement is illegal
            :raises: InvalidBoardPositionError if the tile's new position is invalid
        """
        descent_file = tile_to_move.position.x 
        new_y_lvl = tile_to_move.position.y
        while new_y_lvl > 1 and isinstance(board.tile_at(descent_file, new_y_lvl - 1), NullTile):
            new_y_lvl -= 1

        if tile_to_move.position.y != new_y_lvl:
            tile_to_move.position = (descent_file, new_y_lvl)
            board.place_tile(tile_to_move)
        else:
            LOGGER.debug(f"Tried collapsing tile at ({tile_to_move.position.x}, {tile_to_move.position.y}) Tile is already at the lowest possible position")
            raise IllegalTileMovementException("Tile is already as low as possible")