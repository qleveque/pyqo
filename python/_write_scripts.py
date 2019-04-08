import sys
import os
import re
import shutil
from _reader import *

PYTHON = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(PYTHON,'..','scripts')

particulars = {'c' :
                {'windows' : 'call  %~dp0/_c.bat\n',
                'linux' : ''}
              }

if sys.platform in ['linux', 'linux2']:
    ext = ''

    def script_content(command) :
        r= """#!/bin/bash
python3 {}.py $*
""".format(os.path.join(PYTHON,command))
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
""".format(os.path.join(PYTHON,command))
        if command in particulars:
            r+=particulars[command]['windows']
        return r

    def a_script_content(command):
        return "@{} %*".format(command)

def write_scripts():
    if os.path.isdir(SCRIPTS):
        shutil.rmtree(SCRIPTS)
    os.mkdir(SCRIPTS)

    files = os.listdir(PYTHON)
    pattern = re.compile("^[^_].*.py$")
    files = [file for file in files if pattern.match(file)]
    commands = [file[:-3] for file in files]

    for command in commands:
        file = os.path.join(SCRIPTS, command+ext)
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(script_content(command))

    a_data = read_json('../data/a.json')
    for key, value in a_data.items():
        file = os.path.join(SCRIPTS, key+ext)
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(a_script_content(value))

if __name__ == '__main__':
    write_scripts()
