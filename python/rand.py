#! /usr/bin/env python3
"""
    ``rand`` command.
"""

import click
import random
import sys

@click.command()
@click.option('--min', '-m', help='minimum value', default=0,)
@click.option('--max', '-M', help='maximum value', default=6,)
def rand(min, max):
    """Print a random number."""
    print(random.randint(min,max))

if __name__ == "__main__":
    rand()
