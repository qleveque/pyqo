#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The ``json`` module
======================
Contains all the functions related to the reading and modifications of the ``.json`` files
"""

import json
import os
import subprocess
import distutils.spawn

from typing import List, Dict

from pyqo.utils.printer import print_map

HOME_PATH = os.path.expanduser('~')
DATA_PATH = os.path.join(HOME_PATH, '.config', 'pyqo')


def resolve_json_filename(command: str):
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    # init default filename
    filename = os.path.join(DATA_PATH, '{}.json'.format(command))
    # test if config
    config = read_json(os.path.join(DATA_PATH, 'config.json'))
    key_name = '{}_json'.format(command)
    if key_name in config:
        filename = config[key_name]

    return filename


def set_config(command: str, datafile: str):
    config_file = os.path.join(DATA_PATH, 'config.json')
    key_name = '{}_json'.format(command)
    data = read_json(config_file)
    data[key_name] = datafile
    write_json(config_file, data)


def read_json(filename: str):
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as f:
            data = json.loads(f.read())
    else:
        data = {}
    return data


def list_json(filename: str):
    data = read_json(filename)
    print_map(data)


def get_json(filename: str, keys: List[str], verbose: bool = True):
    data = read_json(filename)
    lst = []
    for key in keys:
        if key in data:
            lst.append(data[key])
        else:
            if verbose:
                print('The key "{}" has no attributed value.'.format(key))
            del key
    return lst


def write_json(filename: str, data: Dict[str, str]):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def set_json(filename: str, map_: Dict[str, str]):
    data = read_json(filename)
    for key, value in map_.items():
        data[key] = value
    write_json(filename, data)


def remove_json(filename: str, keys: List[str]):
    data = read_json(filename)
    for key in keys:
        data.pop(key)
    write_json(filename, data)

