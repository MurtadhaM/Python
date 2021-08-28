# Author: Murtadha Marzouq
# Date: 08/29/2021
# Program: Python Web Spider
from urllib import request

from urllib.parse import urljoin

import domain.utils
import requests
from bs4 import BeautifulSoup
from domain import *

# Variables We Need
base_url = 'https://charlotte.edu'  # original url
host_name = ''
queue = set()
crawled = set()

other_links = set()


def link_parser(response_content, url):
    links_list = []
    # links
    soup = BeautifulSoup(response_content.content, 'html.parser')
    links_all = soup.find_all('a')

    for link in links_all:
        full_link = link.get('href')
        # To avoid empty slashes
        if full_link and full_link.startswith('/'):
            full_link = urljoin(url, full_link)
            links_list.append(full_link)
        else:
            other_links.add(full_link)

            # add_url_to_visit(full_link)

    links_list = list(filter(None, links_list))
    # for u in links_list:
    #     queue.add(u)
    add_links_to_queue(links_list)
    return links_list


def crawl_page(thread_name, page_url):
    if page_url in queue:
        print(thread_name + ' now crawling ' + page_url)
        print('Queue ' + str(len(queue)) + ' | Crawled  ' + str(len(crawled)))
        response_text = requests.get(page_url)  # getting response from the server after requesting the url

        add_links_to_queue(link_parser(response_text, page_url))
        print(page_url)

        # response_content = requests.get(u)
        # add_links_to_queue(link_parser(response_content, u))
    # print(page_url)


def add_links_to_queue(links):
    for link in links:
        if (link not in queue) or (link not in crawled):
            queue.add(link)
        else:
            continue


# crawl_page('1', base_url)
queue.add(base_url)
response_content = requests.get(base_url)
m_temp = link_parser(response_content, base_url)
add_links_to_queue(m_temp)

for url in m_temp:
    response_content = requests.get(base_url)
    m_temp = link_parser(response_content, base_url)

    add_links_to_queue(m_temp)
    print(url)



print(other_links)