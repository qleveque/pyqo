#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``d``

Open the file manager to your favourite directories with ease.
The command `d` shares its data with the command `c`.

### Example

```
$ cd ~/Documents/games
$ # open the current working directory, here '~/Documents/games'
$ d
$ # associate permanently the key 'films' to '~/Documents/films'
$ d films -a /home/pyqo/Documents/films
$ # open '~/Documents/films'
$ d films
```
"""

import os
import subprocess
import sys
import argparse
from subprocess import DEVNULL

from pyqo.utils.json import get_json, resolve_json_filename
from pyqo.utils.srl import handle_srl, complete_srl_parser
from pyqo.utils.os import os_open


def main():
    """Open directories."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    complete_srl_parser(parser)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    command = 'd'
    if handle_srl(command, args, file_type=True):
        return

    if not args.keys:
        dirs = [os.getcwd()]
    else:
        filename = resolve_json_filename(command)
        dirs = get_json(filename, args.keys)
        if not dirs:
            return

    for dir_ in dirs:
        os_open(dir_)


if __name__ == "__main__":
    main()

