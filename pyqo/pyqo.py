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

Generic command to get help. Lists all the commands available.

"""
import argparse
import pyqo
import os

WELCOME_MESSAGE = r"""
Welcome to the wonderful world of
  _ __  _   _  __ _  ___
 | '_ \| | | |/ _` |/ _ \
 | |_) | |_| | (_| | (_) |
 | .__/ \__, |\__, |\___/.
 | |     __/ |   | |
 |_|    |___/    |_|

`pyqo` is a set of command line tools to improve your productivity.
It is easy to get use to, and besides it's devilishly effective.
`pyqo` includes the following commands:
{}
Be sure to use --help in case you need some.
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version',
                        action='version',
                        version=pyqo.__version__)
    parser.parse_args()

    path = os.path.dirname(os.path.realpath(__file__))
    files = [f for f in os.listdir(path) if f.endswith('.py')]
    files = [f for f in files if f not in {'__init__.py', 'pyqo.py'}]
    commands = [f[:-3] for f in files]
    to_print = []
    for command in commands:
        func = __import__('pyqo.{}'.format(command), fromlist=[command])
        func = func.__getattribute__('main')
        to_print.append('> {} : {}'.format(command, func.__doc__))

    print(WELCOME_MESSAGE.format('\n'.join(to_print)))


if __name__ == "__main__":
    main()
