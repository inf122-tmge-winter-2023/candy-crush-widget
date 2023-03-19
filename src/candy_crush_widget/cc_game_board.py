from tilematch_tools import GameBoard, NullTile

from candy_crush_widget.cc_movement_rules import AbsoluteDescent

class CCGameBoard(GameBoard):
    def __init__(self, width, height):
        super().__init__(width, height)


    def collapse_all(self):
        for x in range(1, self.num_cols + 1):
            for y in range(1, self.num_rows + 1):
                if(not isinstance(self.tile_at(x,y), NullTile)):
                    collapse = AbsoluteDescent()
                    collapse.move(self, self.tile_at(x,y))
                    