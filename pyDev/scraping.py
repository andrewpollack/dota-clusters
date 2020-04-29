from bs4 import BeautifulSoup
import requests

url = 'https://dota2.gamepedia.com/Table_of_hero_attributes'

response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
