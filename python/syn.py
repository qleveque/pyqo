from bs4 import BeautifulSoup
import requests
import sys
import re

command = ' '.join(sys.argv[1:])

url = 'http://www.crisco.unicaen.fr/des/synonymes/'+command
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table')
syns = table.find_all('a', attrs={"href": re.compile(r'des/synonymes/*')})
syns_txt = [syn.text for syn in syns]
print(syns_txt)