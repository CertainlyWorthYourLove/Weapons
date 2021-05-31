import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import sqlite3

conn = sqlite3.connect('Weapons.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Weapons
 (id INTEGER PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(50),
 priceInHryvnia INTEGER)''')

for i in range(1,6):
    url = 'https://stvol.ua/catalog/pnevmatika/?PAGEN_{i}={i}'
    resp = requests.get(url)
    content = resp.text
    soup = BeautifulSoup(content,'html.parser')
    div = soup.find('div',class_ = 'main-wrapper')
    products = div.find('main', class_ = 'content')
    center_block = products.find('div',class_ = 'center-block')
    wrapper = center_block.find('div',class_ = 'wrapper')
    center = wrapper.find('div',class_ = 'center')
    catalog = center.find('div',class_ = 'catolog-block')
    weapons = catalog.find('div',class_ = 'panes')
    weapons1 = weapons.find('div',class_ = 'pane active')
    weapons2 = weapons1.find('div',class_ = 'catalog-tovs point_5763543687687684')
    for weapon in weapons2.find_all('div',class_ = 'cover-tov'):
        div0 = weapon.find('div',class_ = 'tov')
        name = div0.find('a',class_ = 'tov-name').text
        price = div0.find('div',class_ = 'tov-price-block')
        price2 = price.find('div',class_ = 'price')
        price3 = price2.find('div',class_ = 'current-price')
        weapon_price = price3.find('b').text
        cursor.execute('INSERT INTO Weapons (name,priceInHryvnia) VALUES (?,?)',(name,weapon_price))
        conn.commit()
    sleep(randint(8, 20))
conn.close()
