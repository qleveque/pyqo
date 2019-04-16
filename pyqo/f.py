#! /usr/bin/env python3
"""
##``f`` command

Open your favourite files with ease. See `f --help` for more details.

###Example

```
$ cd ~
$ # associate permanently the key 'bashrc' to the file '~/.bashrc'
$ f bashrc -a .bashrc
$ # call 'f' with the associated key as parameter to open the affiliated file
$ f bashrc
$ # if '~/.bashrc' is not one of your favourite files anymore
$ f bashrc -r
```
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
    """open directories"""

    filename = resolve_json_filename('f')

    if handle_srl(filename, keys, set, remove, list, type='file'):
        return

    files = get_json(filename, keys)

    cmd = 'xdg-open {}' if sys.platform in ['linux','linux2'] else 'open "{}"'
    for file in files:
        subprocess.call(cmd.format(file), shell=True, stderr=DEVNULL, stdout=DEVNULL)

if __name__ == "__main__":
    main()
