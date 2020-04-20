#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``i``

Open your favourite websites with ease.

### Example

```
$ # associate permanently the key 'github' to 'http://www.github.com'
$ i github -a http://www.github.com
$ # associate permanently the key 'so' to 'https://stackoverflow.com/'
$ i so -a https://stackoverflow.com/
$ # open the two websites on the existing webbrowser window
$ i github so
```
"""

import argparse

from pyqo.utils.json import get_json, resolve_json_filename
from pyqo.utils.srl import handle_srl, complete_srl_parser
from pyqo.utils.os import os_open


def main():
    """Open websites."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    complete_srl_parser(parser)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    command = 'i'
    if handle_srl(command, args):
        return

    filename = resolve_json_filename(command)

    if not args.keys:
        urls = ['https://']
    else:
        urls = get_json(filename, args.keys)

    for url in urls:
        os_open(url)


if __name__ == "__main__":
    main()
