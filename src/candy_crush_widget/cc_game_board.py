from tilematch_tools import GameBoard, NullTile


class CCGameBoard(GameBoard):
    def __init__(self, width, height):
        super().__init__(width, height)
