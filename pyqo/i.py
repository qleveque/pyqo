#! /usr/bin/env python3
"""
## Command ``i``

Open your favourite websites with ease. See `i --help` for more details.

### Example

```
$ # associate permanently the key 'github' to 'http://www.github.com'
$ i github -a http://www.github.com
$ # associate permanently the key 'so' to 'https://stackoverflow.com/'
$ i so -a https://stackoverflow.com/
$ # open the two websites on the existing webbrowser window
$ i github so
$ # open github and performs a google search for 'python' on a new webbrowser window
$ i -n github -g python
```
"""

import click
import sys, os
from ._json import *
from ._srl import *
from ._webbrowser import open_new, open_new_tab
from urllib.parse import quote

@click.command()
@click.argument('keys', required = False, nargs=-1)
@click.option('--new_window', '-n', help='Open results in a new window.', is_flag=True,)
@click.option('--google', '-g', help='Perform a google search.', multiple=True)
@decorate_srl
def main(keys, remove, set, list, new_window, google):
    """Open websites."""

    filename = resolve_json_filename('i')

    if handle_srl(filename, keys, set, remove, list):
        return

    value_keys = get_json(filename, keys)

    google_url = 'https://www.google.com/search?q={}'
    value_google = [google_url.format(quote(r)) for r in google]

    urls = value_keys + value_google
    if len(urls)==0:
        urls = ['']

    for i in range(len(urls)):
        if i == 0 and new_window:
            open_new(urls[i])
        else:
            open_new_tab(urls[i])

if __name__ == "__main__":
    main()
