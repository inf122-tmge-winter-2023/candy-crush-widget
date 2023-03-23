from tilematch_tools import GameBoard, NullTile


class CCGameBoard(GameBoard):
    BOARD_HEIGHT = 10
    BOARD_WIDTH = 10
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
