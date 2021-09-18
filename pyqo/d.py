#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``d``

Open the file manager to your favourite directories with ease.

### Example

```
$ cd ~/Documents/games
$ # open the current working directory, here '~/Documents/games'
$ d
$ # associate permanently the key 'films' to '~/Documents/films'
$ pyqo d add films /home/pyqo/Documents/films
$ # open '~/Documents/films'
$ d films
```
"""

import os
import argparse

from pyqo.utils.json import get_json
from pyqo.utils.os import os_open, is_wsl, wsl_windows_path


def main():
    """Open directories."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    if not args.keys:
        d = os.getcwd()
        if is_wsl():
            d = wsl_windows_path(d)
        os_open(d)
    else:
        dirs = [get_json('d', key) for key in args.keys]
        for d in dirs:
            os_open(d)


if __name__ == "__main__":
    main()
