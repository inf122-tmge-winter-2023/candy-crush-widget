from tilematch_tools import Tile

class CCTile(Tile):
    def __init__(self, **properties):
        super().__init__(**properties)
        self._movable = True

    def __hash__(self):
        return hash(self.position.x + self.position.y * 89)