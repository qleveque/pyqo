#! /usr/bin/env python3
"""
    The ``_srl`` module
    ===================
    Contains all the functions related to the SRL ("set", "remove" and "list") commands.
"""

import click
from ._json import *

def decorate_srl(f):
    return click.option('--assign', '-a', help='Assign a value to the given key.', default=None,)(
    click.option('--remove', '-r', help='Remove a key.', is_flag=True,)(
    click.option('--list', '-l', help='List all the keys if no given key. Otherwise print the associated value.', is_flag=True,)(
    f)))

def handle_srl(filename, keys, assign, remove, list, type = None):
    if assign is not None:
        if len(keys)!=1:
            exit("When setting a new value, you should provide exactly one key.")
        if type in ['dir','file']:
            assign = resolve_path(assign)
        set_json(filename, {keys[0]: assign})
        return True

    if remove:
        remove_json(filename, keys)
        return True

    if list:
        list_json(filename, keys)
        return True

    return False

def resolve_path(set):
    if os.path.exists(set):
        if not os.path.isabs(set):
            set = os.path.join(os.getcwd(),set)
    else:
        exit("Given file not found. Aborting.")
    return set.replace('\\','/')
