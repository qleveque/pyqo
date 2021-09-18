#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Command ``i``

Open your favourite websites with ease.

### Example

```
$ # associate permanently the key 'github' to 'http://www.github.com'
$ pyqo i add github http://www.github.com
$ # associate permanently the key 'so' to 'https://stackoverflow.com/'
$ pyqo i add so https://stackoverflow.com/
$ # open the two websites with your web browser
$ i github so
```
"""

import argparse

from pyqo.utils.json import get_json
from pyqo.utils.os import os_open


def main():
    """Open websites."""

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('keys', type=str, nargs='*')
    args = parser.parse_args()

    if not args.keys:
        os_open('https://')
    else:
        urls = [get_json('i', key) for key in args.keys]
        for url in urls:
            os_open(url)



if __name__ == "__main__":
    main()
