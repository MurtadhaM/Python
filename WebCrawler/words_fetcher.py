import requests
from bs4 import BeautifulSoup

# storing variables
base_url = 'https://uncc.edu'
url = base_url


# function to get words
response_text = requests.get(url)  # getting response from the server after requesting the url
soup = BeautifulSoup(response_text.content, 'html.parser')

word_list = []
# populate a wordlist based on page
for word in soup.getText().strip().replace("\n", " ").split(" "):
    word_list.append(word.replace("\n", ' '))
word_list = list(filter(None, word_list))

# print all words
output = ''
for i in range(len(word_list)):
    output += (word_list[i]) + ' '
print(output)


