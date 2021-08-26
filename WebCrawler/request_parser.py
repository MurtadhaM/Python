

import requests
from bs4 import BeautifulSoup

# storing variables
word_list = []
base_url = 'https://uncc.edu'
url = base_url


# function to get words
response_text = requests.get(url)  # getting response from the server after requesting the url
soup = BeautifulSoup(response_text.text, 'html.parser')


print(soup)

