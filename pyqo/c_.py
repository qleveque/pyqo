#! /usr/bin/env python3
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
$ c games -a
$ # associate permanently the key 'films' to '~/Documents/films'
$ c films -a /home/pyqo/Documents/films
$ # equivalent to 'cd ~/Documents/films'
$ c films
$ # equivalent to 'cd ~/Documents/games'
$ c games
```
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
        exit('')

    if len(keys)!=1:
        exit("When changing directory, you should provide exactly one key.")

    values = get_json(filename, keys)

    if len(values)<1:
        exit("Key not known, aborting.")

    print(values[0])

if __name__ == "__main__":
    main()
