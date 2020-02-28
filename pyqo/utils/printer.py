#! /usr/bin/env python3
"""
The ``printer`` module
=======================
Contains all functions whose purpose is to display results of this library.
"""
from typing import List, Dict

WIDTH = 19
PER_LINE = 4


def print_list(lst: List[str]):
    r = ""
    for idx, elem in enumerate(sorted(lst)):
        r += "{d:<{width}}".format(d=elem, width=WIDTH)
        if (idx+1) % PER_LINE == 0:
            r += "\n"
    print(r)


def print_map(map_: Dict[str, str]):
    for key, value in map_.items():
        print('{key:<{width}}: {value}'.format(key=key, width=WIDTH, value=value))
