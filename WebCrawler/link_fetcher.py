# Author: Murtadha Marzouq
# Date: 08/29/2021
# Program: Python HTTP Retrieval

# Import Library to parse HTML/SOAP

from bs4 import BeautifulSoup
# import Requests library
import requests

url = "https://uncc.edu"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
links_list = []

# links
links_all = soup.find_all('a')

# search word
for link in links_all:
    fullLink = link.get('href')
    links_list.append(fullLink)

# printing the links
for line in links_list:
    print(line)
