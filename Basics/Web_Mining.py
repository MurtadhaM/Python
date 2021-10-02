from http.client import responses

import requests
from bs4 import BeautifulSoup

URL = "https://Charlotte.edu"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')

print(len(links))

