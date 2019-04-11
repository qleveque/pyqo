#! /usr/bin/env python3
"""
    The ``_srl`` module
    ===================
    Contains all the functions related to the SRL ("set", "remove" and "list") commands.
"""

import click
from _reader import *

def decorate_srl(f):
    return click.option('--set', '-s', help='Assign a value to the given key.', default=None,)(
    click.option('--remove', '-r', help='Remove a key.', is_flag=True,)(
    click.option('--list', '-l', help='List all the keys if no given key. Otherwise print the associated value.', is_flag=True,)(
    f)))

def handle_srl(filename, keys, set, remove, list, type = None):
    if set is not None:
        if len(keys)!=1:
            print("When setting a new value, you should provide exactly one key.")
            exit()
        if type in ['dir','file']:
            set = resolve_path(set)
        set_json(filename, {keys[0]: set})
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
        print("Given file not found. Aborting.")
        exit()
    return set.replace('\\','/')
