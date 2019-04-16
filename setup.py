#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re, os, ast
from pyq import __version__
from pyq import __author__
from pyq import __email__

README_BASE = """#pyq

A set of useful command line scripts to navigate through your files and directories with ease and to get informed quickly.

##Compatibility
Fully compatible with :

- **Windows** 7 and higher.
- **Linux** distributions running under the X Window System.

##Usage
Install the [PyPI package](https://pypi.python.org/pypi/pyq/):

    pip install pyq

or clone the repository:

    git clone https://github.com/Whenti/pyq

or [download and extract the zip](https://github.com/Whenti/pyq/archive/master.zip) into your project folder.

Then check the [commands doc below](https://github.com/Whenti/pyq#Commands) to see what commands are available.

##Dependencies
See the

##Authors
* **Quentin LÉVÊQUE** - [Whenti](https://github.com/Whenti)

## License
This project is proudly licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
"""


PYQ_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'pyq')

#commands
def commands():
    files = os.listdir(PYQ_PATH)
    pattern = re.compile("^[^_].*.py$")
    commands = [file[:-3] for file in files if pattern.match(file)]
    commands.sort(key=len, reverse=False)
    return commands

COMMANDS = commands()

#scripts
CONSOLE_SCRIPTS = ['{c}=pyq.{c}:main'.format(c=command) for command in COMMANDS]
SCRIPTS = ['bin/c','bin/c.bat']

#README
README_COMMAND = ["""
#Commands
Below we briefly describe the different commands of `pyq`. Make sure to use the `--help` option for more details.
"""]
for command in COMMANDS:
    command_file = os.path.join('pyq',command+'.py')
    with open(command_file, 'r') as f:
        tree = ast.parse(f.read())
        docstring = ast.get_docstring(tree)
        README_COMMAND.append(docstring)
README = README_BASE + '\n\n'.join(README_COMMAND)
with open('README.md','w',encoding='utf-8') as f:
    f.write(README)


#requirements
os.system('pipreqs {}'.format(PYQ_PATH))
def requirements():
    with open('requirements.txt','r',encoding = 'utf-8') as f:
        lines = f.readlines()
        return [line.replace('==','>=').strip() for line in lines]
REQUIREMENTS = requirements()

#setup
setup(
    name='pyq',
    version=__version__,
    description='Useful collection of command line scripts.',
    long_description=README,
    author=__author__,
    author_email=__email__,
    url='https://github.com/Whenti/pyq',
    packages = ['pyq'],
    package_data={'pyq': ['data/*.json']},
    package_dir={'pyq':'pyq'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license='Apache License',
    zip_safe=False,
    keywords='pip requirements imports',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    scripts = SCRIPTS,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    },
)
