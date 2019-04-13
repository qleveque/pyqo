#! /usr/bin/env python3
"""
    ``yget`` command.
"""

import click
import pytube
import sys
import os

@click.command()
@click.argument('url')
def main(url):
    """Download the youtube video in the current directory."""

    print("Downloading {}".format(val))
    try:
        yt = pytube.YouTube(val)
        stream = yt.streams.first()
        stream.download(os.getcwd())
    except Exception as e:
        print(e)
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
