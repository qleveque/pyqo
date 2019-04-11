#! /usr/bin/env python3
"""
    ``def`` command.
"""

import click
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import quote

@click.command()
@click.argument('word')
def definition(word):
    """Retrieve french definition."""
    url_larousse = 'http://www.larousse.fr/dictionnaires/rechercher?q={}&l=francais&culture='
    url = url_larousse.format(quote(word))
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    defs = soup.find_all('li',attrs={"class":u"DivisionDefinition"})
    for def_ in defs:
        print('--'+def_.text)

if __name__ == "__main__":
    definition()
