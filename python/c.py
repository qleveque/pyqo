#! /usr/bin/env python3
"""
    ``c`` command.
"""

import click
import sys, os
from _reader import *
from _srl import *

@click.command()
@click.argument('keys', required = False, nargs = -1)
@decorate_srl
def c(keys, remove, set, list):
    """Navigate through directories."""

    write_cd_file('')

    filename = resolve_json_filename('c')

    if handle_srl(filename, keys, set, remove, list, type='file'):
        return

    if len(keys)!=1:
        print("When changing directory, you should provide exactly one key.")
    values = get_json(filename, keys)

    if len(values)<1:
        exit()

    to_write = 'cd {}\n'.format(values[0])
    write_cd_file(to_write)

def write_cd_file(to_write):
    ext = '' if sys.platform in ['linux', 'linux2'] else '.bat'
    end_file = os.path.join(SCRIPTS_PATH,'_c'+ext)
    with open(end_file,'w', encoding = 'utf-8') as f:
        f.write(to_write)

if __name__ == "__main__":
    c()
