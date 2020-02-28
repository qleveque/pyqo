#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``v``

Associative table to save small variables.

### Example

```
$ # save the value '+44 1234 123456' under the key 'john_number'
$ v john_number -a '+44 1234 123456'
$ # print John's number
$ v john_number
$ # forget John's number
$ v john_number -d
```
"""

import argparse

from pyqo.utils.json import get_json, resolve_json_filename
from pyqo.utils.srl import handle_srl, complete_srl_parser


def main():
    """Contains variables."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    complete_srl_parser(parser)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    command = 'v'
    if handle_srl(command, args):
        return
    
    filename = resolve_json_filename(command)
    values = get_json(filename, args.keys)
    for value in values:
        print(value)


if __name__ == "__main__":
    main()
