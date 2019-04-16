#! /usr/bin/env python3
"""
    ``d`` command.
"""

import click
import sys, os
from ._json import *
from ._srl import *
import subprocess
from subprocess import DEVNULL

@click.command()
@click.argument('keys', required = False, nargs=-1)
@decorate_srl

def main(keys, remove, set, list):
    """Open directories."""
    filename = resolve_json_filename('c')

    if handle_srl(filename, keys, set, remove, list, type='file'):
        return

    cmd = 'xdg-open {}' if sys.platform in ['linux','linux2'] else 'open "{}"'

    if len(keys)<1:
        dirs = [os.getcwd()]
    else:
        dirs = get_json(filename, keys)

    for dir in dirs:
        subprocess.call(cmd.format(dir), shell=True, stderr=DEVNULL, stdout=DEVNULL)

if __name__ == "__main__":
    main()
