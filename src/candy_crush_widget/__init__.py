"""
    :module_name: candy_crush_widget
    :module_summary: A widget representint an instance of the candy crush tile matching game
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

from .cc_colors import CCTileColor
from .cc_game_board import CCGameBoard
from .cc_game_loop import CCGameLoop
from .cc_match_rules import *
from .cc_scoring import Scoring
from .cc_tile import CCTile
from .cc_movement_rules import AbsoluteDescent

from tilematch_tools import LOGGER as TMT_LOGGER
import logging

TMT_LOGGER.setLevel(logging.CRITICAL)

CC_LOGGER = logging.getLogger(__name__)
LOG_HANDLER = logging.StreamHandler()
LOG_FORMAT = logging.Formatter('[%(asctime)s|%(name)s|%(levelname)s] - %(message)s')

CC_LOGGER.setLevel(logging.CRITICAL)
LOG_HANDLER.setLevel(logging.CRITICAL)

LOG_HANDLER.setFormatter(LOG_FORMAT)
CC_LOGGER.addHandler(LOG_HANDLER)