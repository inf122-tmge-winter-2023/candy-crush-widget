from tilematch_tools import Tile

class CCTile(Tile):
    def __hash__(self):
        return hash(self.position.x + self.position.y * 89)