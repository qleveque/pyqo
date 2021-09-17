#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``s``

Perform a web search with ease.

### Example

```
$ # associate permanently the key 'so' to a search on stackoverflow
$ s so -a https://stackoverflow.com/search?q={}
$ # perform a search on stackoverflow
$ s so "what is __init__.py for ?"
```
"""

import argparse
from urllib.parse import quote

from pyqo.utils.json import get_json, resolve_json_filename
from pyqo.utils.srl import handle_srl, complete_srl_parser
from pyqo.utils.os import os_open


def main():
    """Perform web searches."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    complete_srl_parser(parser)
    parser.add_argument('key', type=str, nargs='?')
    parser.add_argument('query', type=str, nargs='?')
    args = parser.parse_args()

    command = 's'
    if handle_srl(command, args):
        return

    if args.query is None:
        print("This command requires a KEY and a QUERY.")

    filename = resolve_json_filename(command)
    urls = get_json(filename, [args.key])
    if not urls:
        return
    url = urls[0].format(quote(args.query))

    os_open(url)


if __name__ == "__main__":
    main()
