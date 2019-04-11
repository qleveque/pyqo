#! /usr/bin/env python3
"""
    ``syn`` command.
"""

import click
from bs4 import BeautifulSoup
import requests
import re
from _printer import print_list
from urllib.parse import quote

@click.command()
@click.argument('word')
def ant(word):
    """Retrieve synonyms."""
    url_antonyme = 'http://www.antonyme.org/antonyme/{}'
    url = url_antonyme.format(quote(word))

    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('ul', attrs={"class": "synos"})
    syns = table.find_all('a', attrs={"href": re.compile(r'http://www.antonyme.org/antonyme/*')})
    syns_txt = [syn.text.replace(u'\xa0', u'') for syn in syns]

    print_list(syns_txt)

if __name__ == "__main__":
    ant()
