#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""

# pyqo
A set of useful command line scripts to navigate through your files, directories and favourite websites with ease.

## Compatibility
Fully compatible with :

- **Windows** 7 and higher.
- **Linux** distributions running under the X Window System.

Requires `Python 3.0` or higher.

## Usage
Clone the repository:
```
$ git clone https://github.com/Whenti/pyqo
```
or [download and extract the zip](https://github.com/Whenti/pyqo/archive/master.zip), and then run the setup:
```
$ python setup.py install
```

Check the [commands documentation below](https://github.com/Whenti/pyqo#Commands) to see what is available.

## Authors

* **Quentin LÉVÊQUE** - [Whenti](https://github.com/Whenti)

## License
This project is proudly licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

# Commands
Below we briefly describe the different commands of `pyqo`. Make sure to use the `--help` option for more details.


## Command ``pyqo``

Generic command: see ``pyqo --help``.

"""
import argparse
import os

import pyperclip

import pyqo
from pyqo.utils.json import get_json, list_json, remove_json, set_json
from pyqo.utils.os import is_wsl, wsl_windows_path


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    files = [f for f in os.listdir(path) if f.endswith('.py')]
    files = [f for f in files if f not in {'__init__.py', 'pyqo.py'}]
    commands = [f[:-3] for f in files]

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version',
                        action='version',
                        version=pyqo.__version__)
    parser.add_argument('command', choices=commands, help='Command')
    sub_parsers = parser.add_subparsers(dest='action', help='Action')

    parser_add = sub_parsers.add_parser('add',
            help='Assign a value to the given key.')
    parser_add.add_argument('key')
    parser_add.add_argument('value')

    parser_remove = sub_parsers.add_parser('remove',
            help='Delete a key.')
    parser_remove.add_argument('key')

    parser_show = sub_parsers.add_parser('show',
            help='Display the value of the given key.')
    parser_show.add_argument('key')

    parser_copy = sub_parsers.add_parser('copy',
            help='Copy the value of the given key in the clipboard.')
    parser_copy.add_argument('key')

    sub_parsers.add_parser('list',
            help='List all the existing keys.')

    args = parser.parse_args()

    if args.action == 'add':
        value = args.value
        if args.command in ['f', 'd']:
            value = os.path.abspath(value)
            if is_wsl():
                value = wsl_windows_path(value)
        set_json(args.command, args.key, value)

    elif args.action == 'remove':
        remove_json(args.command, args.key)

    elif args.action == 'show':
        print(get_json(args.command, args.key))

    elif args.action == 'copy':
        value = get_json(args.command, args.key)
        pyperclip.copy(value)

    elif args.action == 'list':
        list_json(args.command)


if __name__ == "__main__":
    main()
