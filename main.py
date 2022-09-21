
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.orangepage.net/recipes/search/6')
soup = BeautifulSoup(res.text, 'html.parser')

recipes = soup.find('div', id='recipe_list', class_='recipesList')
p_tit_tags = recipes.find_all('h2', class_='tit')
p_tit_str = [x.string for x in p_tit_tags]
print(p_tit_str)