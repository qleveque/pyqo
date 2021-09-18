#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

from typing import Dict


def resolve_json_filename(command: str) -> str:
    config_path = os.path.join(os.path.expanduser('~'), '.config', 'pyqo')
    if not os.path.isdir(config_path):
        os.makedirs(config_path)
    filename = os.path.join(config_path, '{}.json'.format(command))
    return filename

def read_json(command: str) -> Dict[str, str]:
    filename = resolve_json_filename(command)
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as f:
            data = json.loads(f.read())
    else:
        data = {}
    return data

def write_json(command: str, data: Dict[str, str]):
    filename = resolve_json_filename(command)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def list_json(command: str):
    data = read_json(command)
    for key, value in data.items():
        print('{key:<{width}}: {value}'.format(key=key, width=19, value=value))

def get_json(command: str, key: str) -> str:
    data = read_json(command)
    r = data.get(key)
    if r is None:
        print(f'Unknown key: {key}')
        exit(1)
    return r

def set_json(command: str, key: str, value: str):
    data = read_json(command)
    data[key] = value
    write_json(command, data)

def remove_json(command: str, key: str):
    data = read_json(command)
    data.pop(key)
    write_json(command, data)
