#! /usr/bin/env python3
"""
    ``say`` command.
"""

import click
import sys, os
import pyttsx3

@click.command()
@click.argument('speech', nargs=-1)
def say(speech):
    """Simulate the reading of the given speech."""
    engine = pyttsx3.init()
    for word in speech:
        engine.say(speech)
    engine.runAndWait()

if __name__ == "__main__":
    say()
