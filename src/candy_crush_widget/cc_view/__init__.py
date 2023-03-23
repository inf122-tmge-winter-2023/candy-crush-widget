import logging
from tilematch_tools import GameView, MouseEvent

LOGGER = logging.getLogger(__name__)

class CCView(GameView):
    """Class representing the candy-crush view"""
    def __init__(self, parent, game_state):
        super().__init__(parent, game_state, 'Candy Crush')

class CCMouseEvent(MouseEvent):
    def __init__(self, listener, board_clicked_on):
        super().__init__(listener, board_clicked_on)

    def __call__(self, event):
        tile_position = super().__call__(event)
        tile = self.listener.board.tile_at(*tile_position)
        LOGGER.info(f"Player clicked on {tile.position}")
        self.listener.select_tile(tile)