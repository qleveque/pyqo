#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``f``

Open your favourite files with ease. See `f --help` for more details.

### Example

```
$ cd ~
$ # associate permanently the key 'bashrc' to the file '~/.bashrc'
$ f bashrc -a .bashrc
$ cd ~/Documents/games
$ # open the '~/.bashrc' file
$ f bashrc
```
"""

import subprocess
import sys
import argparse
from subprocess import DEVNULL

from pyqo.utils.json import get_json, resolve_json_filename
from pyqo.utils.srl import handle_srl, complete_srl_parser


def main():
    """Open files."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    complete_srl_parser(parser)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    command = 'f'
    if handle_srl(command, args, file_type=True):
        return

    filename = resolve_json_filename(command)
    files = get_json(filename, args.keys)
    cmd = 'xdg-open {}' if sys.platform in ['linux', 'linux2'] else 'start "" "{}"'
    for file in files:
        subprocess.call(cmd.format(file), shell=True, stderr=DEVNULL, stdout=DEVNULL)


if __name__ == "__main__":
    main()
