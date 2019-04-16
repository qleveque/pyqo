#! /usr/bin/env python3
"""
    ``v`` command.
"""

import click
import sys, os
from ._json import *
from ._srl import *

@click.command()
@click.argument('keys', required = False, nargs=-1)
@decorate_srl
def main(keys, remove, set, list):
    """Contains variables."""

    filename = resolve_json_filename('v')

    if handle_srl(filename, keys, set, remove, list):
        return

    values = get_json(filename, keys)
    for value in values:
        print(value)

if __name__ == "__main__":
    main()
