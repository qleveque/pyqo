#! /usr/bin/env python3
"""
    ``a`` command.
"""

import click
import sys, os
from _reader import *
from _srl import *
from _write_scripts import write_scripts

@click.command()
@click.argument('keys', required = False, nargs = -1)
@decorate_srl
def a(keys, remove, set, list):
    """Aliases"""

    filename = resolve_json_filename('a')

    if handle_srl(filename, keys, set, remove, list):
        if remove or set:
            write_scripts()

if __name__ == "__main__":
    a()
