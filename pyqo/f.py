#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``f``

Open your favourite files with ease.

### Example

```
$ cd ~
$ # associate permanently the key 'bashrc' to the file '~/.bashrc'
$ pyqo f add bashrc .bashrc
$ cd ~/Documents/games
$ # open the '~/.bashrc' file
$ f bashrc
```
"""

import argparse

from pyqo.utils.json import get_json
from pyqo.utils.os import os_open


def main():
    """Open files."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    files = [get_json('f', key) for key in args.keys]

    for f in files:
        os_open(f)


if __name__ == "__main__":
    main()
