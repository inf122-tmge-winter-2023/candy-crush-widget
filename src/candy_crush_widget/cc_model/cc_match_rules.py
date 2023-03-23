from tilematch_tools import MatchCondition, GameBoard, NullTile, Tile
from tilematch_tools.model.match import ScanDelta
from tilematch_tools.model.exceptions import InvalidBoardPositionError

class HorizontalMatch(MatchCondition):
    def __init__(self, value: int, equality_rule: callable = Tile.__eq__):
        super().__init__(ScanDelta.RIGHT, value, equality_rule)

    def check_match(self, board: GameBoard, start_x: int, start_y: int) -> MatchCondition.MatchFound or None:
        """Returns all horizontally matching tiles in 3+ formation

        Args:
            board (GameBoard): game
            start_x (int): start x position
            start_y (int): start y position

        Returns:
            MatchCondition.MatchFound or None:  A matchfound with matching tiles > 0 or None
        """
        matching_tiles = set()
        try:
            for y in range(start_y, board.num_cols + 1):
                for x in range(start_x, board.num_rows - 1):
                    first_tile = board.tile_at(x, y)
                    second_tile = board.tile_at(x + self._scan_delta.value[0], y)
                    third_tile = board.tile_at(x + 2 * self._scan_delta.value[0], y)
                    if self._eq(first_tile, second_tile) and \
                        self._eq(first_tile, third_tile) and \
                            not isinstance(first_tile, NullTile):
                        matching_tiles.add(first_tile)
                        matching_tiles.add(second_tile)
                        matching_tiles.add(third_tile)

        except InvalidBoardPositionError:
            pass

        return  None if len(matching_tiles) == 0 else MatchCondition.MatchFound(len(matching_tiles), matching_tiles)
    

class VerticalMatch(MatchCondition):
    def __init__(self, value: int, equality_rule: callable = Tile.__eq__):
        super().__init__(ScanDelta.UP, value, equality_rule)

    def check_match(self, board: GameBoard, start_x: int, start_y: int) -> MatchCondition.MatchFound or None:
        """Returns all vertically matching tiles in 3+ formation

        Args:
            board (GameBoard): board
            start_x (int): start x position
            start_y (int): start y position

        Returns:
            MatchCondition.MatchFound or None: A matchfound with matching tiles > 0 or None
        """
        matching_tiles = set()
        try:
            for x in range(start_x, board.num_rows + 1):
                for y in range(start_y, board.num_cols - 1):
                    first_tile = board.tile_at(x, y)
                    second_tile = board.tile_at(x, y + self._scan_delta.value[1])
                    third_tile = board.tile_at(x, y + 2 * self._scan_delta.value[1])
                    if self._eq(first_tile, second_tile) and \
                        self._eq(first_tile, third_tile) and \
                            not isinstance(first_tile, NullTile):
                        matching_tiles.add(first_tile)
                        matching_tiles.add(second_tile)
                        matching_tiles.add(third_tile)

        except InvalidBoardPositionError:
            pass

        return  None if len(matching_tiles) == 0 else MatchCondition.MatchFound(len(matching_tiles), matching_tiles)
