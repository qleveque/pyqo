#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the `README.md`.
"""

from os import listdir
import sys
import re

if __name__ == "__main__":

    docstrings = {}
    files = [file[:-3] for file in listdir('pyqo') if re.match('^[^_].*.py$', file)]
    for file in files:
        lib = 'pyqo.{}'.format(file)
        __import__(lib)
        docstrings[file] = sys.modules[lib].__doc__

    with open('README.md', 'w', encoding = 'utf-8') as f:
        f.write(docstrings['pyqo'])
        for key, value in docstrings.items():
            if key == 'pyqo':
                continue
            f.write(value)
