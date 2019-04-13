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
        return

    if len(keys)!=1:
        print("When changing directory, you should provide exactly one key.")

    values = get_json(filename, keys)

    if len(values)<1:
        exit()

    os.chdir(values[0])
    os.system("/bin/bash")

if __name__ == "__main__":
    main()
