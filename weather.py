import requests
from bs4 import BeautifulSoup

search = "weather in Delhi"
url = f"https://www.google.com/search?q={search}"

r = requests.get(url)

s = BeautifulSoup(r.text)