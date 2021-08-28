# Author: Murtadha Marzouq
# Date: 08/29/2021
# Program: Python HTTP Retrieval

# Import Library to parse HTML/SOAP
from urllib.parse import urljoin

from bs4 import BeautifulSoup
# import Requests library
import requests


def link_parser(response_content, url):
    print(url)
    links_list = []
    # links
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links_all = soup.find_all('a')

    for link in links_all:
        full_link = link.get('href')
        # To avoid empty slashes
        if full_link and full_link.startswith('/'):
            full_link = urljoin(url, full_link)
            links_list.append(full_link)
            # add_url_to_visit(full_link)

    links_list = list(filter(None, links_list))
    return links_list

url = 'https://charlotte.edu'

for u in link_parser('1', url):
    print(u)
