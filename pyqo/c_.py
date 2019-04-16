#! /usr/bin/env python3
"""
    ``c`` command.
"""

import click
import sys, os
from ._json import *
from ._srl import *

@click.command()
@click.argument('keys', required = False, nargs = -1)
@decorate_srl
def main(keys, remove, set, list):
    """Navigate through directories."""

    filename = resolve_json_filename('c')

    if handle_srl(filename, keys, set, remove, list, type='file'):
        exit('')

    if len(keys)!=1:
        exit("When changing directory, you should provide exactly one key.")

    values = get_json(filename, keys)

    if len(values)<1:
        exit("Key not known, aborting.")

    print(values[0])

if __name__ == "__main__":
    main()