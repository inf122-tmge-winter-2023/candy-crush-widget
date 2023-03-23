"""
    :module_name: candy_crush_widget
    :module_summary: A widget representint an instance of the candy crush tile matching game
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

from .cc_model import *
from .cc_view import *

from tilematch_tools import LOGGER 
import logging


LOGGER = logging.getLogger(__name__)
LOG_HANDLER = logging.StreamHandler()
LOG_FORMAT = logging.Formatter('[%(asctime)s|%(name)s|%(levelname)s] - %(message)s')

LOGGER.setLevel(logging.INFO)
LOG_HANDLER.setLevel(logging.INFO)

LOG_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(LOG_HANDLER)