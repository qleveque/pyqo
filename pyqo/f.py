#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``f``

Open your favourite files with ease.
The command ``ef`` is also available on linux to open the file directly with your favourite editor (```$EDITOR```).

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

import argparse

from pyqo.utils.json import get_json, resolve_json_filename
from pyqo.utils.srl import handle_srl, complete_srl_parser
from pyqo.utils.os import os_open


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
    for file_ in files:
        os_open(file_)


if __name__ == "__main__":
    main()
