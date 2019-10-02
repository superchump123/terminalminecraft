from bs4 import BeautifulSoup
import json
import requests

data = requests.get('https://www.digminecraft.com/lists/item_id_list_pc.php')
soup = BeautifulSoup(data.text, 'html.parser')

items = []
for div in soup.find_all('div', {'class': 'article'}):
    for table in div.find_all('table', {'class': 'std_table'}):
        for td in table.find_all('td'):
            for a in td.find_all('a'):
                string_a = str(a)
                startslice = string_a.index('>')
                endslice = string_a.rindex('<')
                items.append(string_a[(startslice + 1):endslice])

with open('items.json', mode='w') as file:
    json.dump(items, file)
