import logging
from tilematch_tools import GameView, MouseEvent

from ..cc_model.cc_game_state import CCGameState

LOGGER = logging.getLogger(__name__)

class CCView(GameView):
    """Class representing the candy-crush view"""
    def __init__(self, parent, game_state):
        super().__init__(parent, game_state, 'Candy Crush')
        self.bind_inputs()
        
    def create_widgets(self):
        super().create_widgets()
        self._game_widgets["move_counter"] = MoveCounter(self, self._game)
    
    def place_widgets(self):
        super().place_widgets()
        self._game_widgets['move_counter'].grid(column=6, row=3, columnspan=2, rowspan=4, padx=30, pady=30)

    
    def bind_inputs(self):
        self.bind_click('<Button-1>', CCMouseEvent(self._game, self.board_view))

    def update(self):
        if self._game.gameover():
            for w in self._game_widgets.values():
                w.update()
            self._block_board()
            return
        for w in self._game_widgets.values():
            w.update()



class CCMouseEvent(MouseEvent):
    def __init__(self, listener, board_clicked_on):
        super().__init__(listener, board_clicked_on)

    def __call__(self, event):
        if self.listener.gameover():
            LOGGER.warning(f"Attempting to click on the board while the game is over.")
            return
        tile_position = super().__call__(event)
        tile = self.listener.board.tile_at(*tile_position)
        LOGGER.info(f"Player clicked on {tile.position}")
        self.listener.select_tile(tile)

import tkinter as tk

from tilematch_tools import GameInfo
class MoveCounter(GameInfo):
    """
        GUI widget for displaying moves left
    """
    
    def __init__(self, parent, state: CCGameState, **options):
        super().__init__(parent, **options)
        self._watching = state

    @property
    def watching(self):
        return self._watching.moves_left 

    @property
    def showing(self):
        if not hasattr(self, '_showing'):
            self._showing = tk.StringVar()
            self._showing.set('25')
            
        return self._showing

    def update(self):
        self.showing.set(self.watching)

    def create_widgets(self):
        self._counter_label = tk.Label(self, text='Moves Left: ', font=self.font, width=10, anchor=tk.W)
        self._coutner_display = tk.Label(self, textvariable=self.showing, font=self.font, width=4, anchor=tk.E)

    def place_widgets(self):
        self._counter_label.grid(row=0, column=0)
        self._coutner_display.grid(row=0, column=1)
