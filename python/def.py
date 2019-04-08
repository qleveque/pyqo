from bs4 import BeautifulSoup
import requests
import sys

command = ' '.join(sys.argv[1:])

url = 'http://www.larousse.fr/dictionnaires/rechercher?q='+command+'&l=francais&culture='
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
defs = soup.find_all('li',attrs={"class":u"DivisionDefinition"})
for def_ in defs:
    print('--'+def_.text)