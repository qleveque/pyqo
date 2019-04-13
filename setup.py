#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re, os
from pyq import __version__
from pyq import __author__
from pyq import __email__

PYQ_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'pyq')

with open('README.rst') as readme_file:
    readme = readme_file.read()

def console_scripts():
    files = os.listdir(PYQ_PATH)
    pattern = re.compile("^[^_].*.py$")
    files = [file for file in files if pattern.match(file)]
    commands = [file[:-3] for file in files]
    return ['{c}=pyq.{c}:main'.format(c=command) for command in commands]


requirements = [
]

setup(
    name='pyq',
    version=__version__,
    description='Useful collection of command line scripts.',
    long_description=readme,
    author=__author__,
    author_email=__email__,
    url='https://github.com/Whenti/pyq',
    packages = ['pyq'],
    package_data={'pyq': ['data/*.json']},
    package_dir={'pyq':'pyq'},
    include_package_data=True,
    install_requires=requirements,
    license='Apache License',
    zip_safe=False,
    keywords='pip requirements imports',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': console_scripts(),
    },
)
