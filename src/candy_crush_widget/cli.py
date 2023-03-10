"""
    :module_name: cli
    :module_summary: a CLI for candy_crush_widget
    :module_author: Nathan Mendoza (nathancm@uci.edu)
"""

import click
import tilematch_tools

@click.command()
def candy_crush():
    """Entry point to candy-crush"""
    click.echo('Hello World!')
