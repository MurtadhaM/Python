import requests
from bs4 import BeautifulSoup
from collections import Counter

# storing variables
word_list = []
base_url = 'https://uncc.edu'
url = base_url


# function to get words
response_text = requests.get(url)  # getting response from the server after requesting the url
soup = BeautifulSoup(response_text.content, 'html.parser')

for word in soup.getText().strip().replace("\n", " ").split(" "):
    word_list.append(word.replace("\n", ' '))
word_list = list(filter(None, word_list))

for word_to_print in word_list:
    print(word_to_print)



