#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The ``srl`` module
===================
Contains all the functions related to the SRL ("set", "delete" and "list") commands.
"""

import os
from argparse import ArgumentParser, Namespace

import pyperclip

from pyqo.utils.json import (resolve_json_filename, set_json, remove_json, list_json, set_config,
                             get_json)
from pyqo.utils.os import is_wsl, wsl_windows_path, wsl_linux_path


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
    parser.add_argument('-l',
                        '--list',
                        help='List all the existing keys.',
                        action='store_true')
    parser.add_argument('-e',
                        '--echo',
                        help='Display the value of the given key.',
                        action='count',
                        default=0)
    parser.add_argument('-c',
                        '--copy',
                        help='Copy the value of the given key in the clipboard.',
                        action='count',
                        default=0)
    return parser


def handle_srl(command: str, args: Namespace, file_type: bool = False) -> bool:
    filename = resolve_json_filename(command)

    if hasattr(args, "key"):
        if args.key is not None:
            keys = [args.key]
        else:
            keys = []
    elif hasattr(args, "keys"):
        if args.keys is not None:
            keys = args.keys
        else:
            keys = []
    else:
        keys = []

    if args.assign is not None:
        assign = args.assign
        if len(keys) != 1:
            exit("When setting a new value, you should provide exactly one key.")
        if file_type:
            assign = resolve_path(assign)
            if len(assign) >= 2 and assign[-2:] in ["\\.", "/."]:
                assign = assign[:-2]
            if is_wsl():
                assign = wsl_windows_path(assign)

        set_json(filename, {keys[0]: assign})
        return True

    if args.echo + args.copy:
        if not len(keys) and command == 'd':
            value = os.getcwd()
            if is_wsl():
                value = wsl_windows_path(value)
        elif len(keys) != 1:
            exit("When printing or copying a value, you should provide exactly one key.")
        else:
            values = get_json(filename, keys, False)
            if len(values) != 1:
                exit("Unknown key")
            value = values[0]

        if file_type and is_wsl() and args.echo + args.copy == 1:
            value = wsl_linux_path(value)

        if args.echo:
            print(value)
        elif args.copy:
            pyperclip.copy(value)
        return True

    if args.delete:
        remove_json(filename, keys)
        return True

    if args.list:
        list_json(filename)
        return True

    if args.set_datafile is not None:
        if keys:
            exit('Should not provide any key when setting a new datafile')
        set_config(command, resolve_path(args.set_datafile))
        return True

    return False


def resolve_path(path: str) -> str:
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write('{}')
    return path
