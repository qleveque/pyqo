#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re, os
from pyqo import __version__
from pyqo import __author__
from pyqo import __email__

with open('requirements.txt', 'r', encoding='utf-8') as f:
    REQUIREMENTS = f.readlines()

PYQ_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pyqo')
files = os.listdir(PYQ_PATH)
pattern = re.compile('^[^_].*.py$')
commands = [file[:-3] for file in files if pattern.match(file)]
CONSOLE_SCRIPTS = ['{c}=pyqo.{c}:main'.format(c=com) for com in commands]

with open('README.md', 'r', encoding='utf-8') as f:
    README = '\n'.join(f.readlines())

setup(
    name='pyqo',
    version=__version__,
    description='Useful collection of command line scripts.',
    long_description_content_type='text/markdown',
    long_description=README,
    author=__author__,
    author_email=__email__,
    url='https://github.com/Whenti/pyqo',
    packages=['pyqo', 'pyqo.utils'],
    package_dir={'pyqo': 'pyqo', 'pyqo.utils': 'pyqo/utils'},
    include_package_data=True,
    license='Apache License',
    zip_safe=False,
    keywords='command line scripts',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    }
)
