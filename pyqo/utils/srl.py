#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The ``srl`` module
===================
Contains all the functions related to the SRL ("set", "delete" and "list") commands.
"""

import os
from argparse import ArgumentParser, Namespace

from pyqo.utils.json import resolve_json_filename, set_json, remove_json, list_json, set_config


def complete_srl_parser(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument('-a', '--assign',
                        metavar='Value',
                        help='Assign a value to the given key.',
                        type=str)
    parser.add_argument('-s', '--set-datafile',
                        metavar='Datafile',
                        help='Set the datafile for this command.', 
                        type=str)
    parser.add_argument('-d', '--delete',
                        help='Delete a key.',
                        action='store_true')
    parser.add_argument('--list',
                        '-l',
                        help='List all the existing keys.',
                        action='store_true')
    return parser


def handle_srl(command: str, args: Namespace, file_type: bool = False) -> bool:
    filename = resolve_json_filename(command)

    if hasattr(args, "key"):
        if args.key is not None:
            keys = [args.key]
        else:
            keys = []
    elif hasattr(args, "key"):
        if args.keys is not None:
            keys = args.keys
        else:
            keys = []
    else:
        keys = []

    if args.assign is not None:
        assign = args.assign
        if len(keys) != 1:
            print("When setting a new value, you should provide exactly one key.")
            exit()
        if file_type in ['dir', 'file']:
            assign = resolve_path(assign)
            if len(assign) >= 2 and assign[-2:] in ["\\.", "/."]:
                assign = assign[:-2]
        set_json(filename, {keys[0]: assign})
        return True

    if args.delete:
        remove_json(filename, keys)
        return True

    if args.list:
        list_json(filename)
        return True

    if args.set_datafile is not None:
        if keys:
            print('Should not provide any key when setting a new datafile')
            exit()
        set_config(command, resolve_path(args.set_datafile))
        return True

    return False


def resolve_path(path: str) -> str:
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    if not os.path.exists(path):
        open(path, 'a').close()
    return path