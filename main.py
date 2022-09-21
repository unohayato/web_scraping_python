import imp
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.orangepage.net/recipes/search/6')
soup = BeautifulSoup(res.text, 'html.parser')
h2_tags = soup.find_all('h2')
print(h2_tags[2])