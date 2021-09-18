#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``v``
Associative table to save small variables.
### Example
```
$ # save the value '+44 1234 123456' under the key 'john_number'
$ pyqo v add john_number '+44 1234 123456'
$ # print John's number
$ v john_number
$ # forget John's number
$ pyqo v remove john_number
```
"""

import argparse

from pyqo.utils.json import get_json


def main():
    """Store variables."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    for key in args.keys:
        value = get_json('v', key)
        print(value)


if __name__ == "__main__":
    main()
