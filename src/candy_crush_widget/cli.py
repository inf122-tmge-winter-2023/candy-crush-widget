"""
    :module_name: cli
    :module_summary: a CLI for candy_crush_widget
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import logging
import click

from .cc_model import CCFactory
from tilematch_tools import  GameEngine


@click.command()
def candy_crush():
    """Entry point to candy-crush"""
    engine = GameEngine([CCFactory.create_game()])
    engine.run()
