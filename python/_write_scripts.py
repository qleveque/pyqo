#! /usr/bin/env python3
"""
    The ``_write_scripts`` module
    =============================
    Contains all functions whose purpose is to write scripts that will be directly interpreted by the command line.
    The scripts are written in the ``scripts`` directory.
"""

import sys
import os
import re
import shutil
from _reader import *

particulars = {'c' :
                {'windows' : 'call  {}/_c.bat\n'.format(SCRIPTS_PATH),
                'linux' : 'source  {}/_c\n'.format(SCRIPTS_PATH)}
              }

if sys.platform in ['linux', 'linux2']:
    ext = ''

    def script_content(command) :
        r= """#!/bin/bash
python3 {}.py "$@"
""".format(os.path.join(PYTHON_PATH,command))
        if command in particulars:
            r+=particulars[command]['linux']
        return r

    def a_script_content(command):
        return "{} $*".format(command)

else:
    ext = '.bat'

    def script_content(command) :
        r = """@echo off
python {}.py %*
""".format(os.path.join(PYTHON_PATH,command))
        if command in particulars:
            r+=particulars[command]['windows']
        return r

    def a_script_content(command):
        return "@ {} %*".format(command)

def write_all_rights(filename, content):
    with open(filename, 'w+', encoding = 'utf-8') as f:
        f.write(content)
    os.chmod(filename, 0o777)

def write_scripts():
    if os.path.isdir(SCRIPTS_PATH):
        shutil.rmtree(SCRIPTS_PATH)
    os.mkdir(SCRIPTS_PATH)
    os.chmod(SCRIPTS_PATH, 0o777)

    files = os.listdir(PYTHON_PATH)
    pattern = re.compile("^[^_].*.py$")
    files = [file for file in files if pattern.match(file)]
    commands = [file[:-3] for file in files]

    for command in commands:
        file = os.path.join(SCRIPTS_PATH, command+ext)
        write_all_rights(file, script_content(command))

    a_data = read_json(os.path.join(DATA_PATH,'a.json'))
    for key, value in a_data.items():
        file = os.path.join(SCRIPTS_PATH, key+ext)
        write_all_rights(file, a_script_content(value))

    file_c = os.path.join(SCRIPTS_PATH, '_c'+ext)
    write_all_rights(file_c, '')

if __name__ == '__main__':
    write_scripts()
