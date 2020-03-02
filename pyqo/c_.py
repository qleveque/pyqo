#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``c``

Set the working directory of the command line to your favourite directories with ease.
For a script to alter the current environment, it requires `source`'ing in linux.
We suggest you to create an alias to avoid doing it manually : `alias c="source c"`.
The command `c` shares its data with the command `d`.
See `c --help` for more details.

### Example

```
$ cd ~/Documents/games
$ # associate permanently the key 'games' to '~/Documents/games'
$ d games -a .
$ # associate permanently the key 'films' to '~/Documents/films'
$ d films -a /home/pyqo/Documents/films
$ # equivalent to 'cd ~/Documents/films'
$ c films
$ # equivalent to 'cd ~/Documents/games'
$ c games
```
"""

import argparse
import sys

from pyqo.utils.json import get_json, resolve_json_filename
from pyqo.utils.os import is_wsl, wsl_linux_path 


def main():
    """Navigate through directories."""

    parser = argparse.ArgumentParser(prog='c', description=main.__doc__)
    parser.add_argument('key', type=str)
    args = parser.parse_args()

    filename = resolve_json_filename('d')
    values = get_json(filename, [args.key])

    if not values:
        exit()

    ret = values[0]

    if is_wsl():
        ret = wsl_linux_path(ret)

    exit(ret)


if __name__ == "__main__":
    main()
