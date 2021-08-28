import logging
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests

# this function takes in a filename and a list to write it to a file
from pandas import unique


def write_file(filename, list_contents):
    outfile = open(filename, 'w')
    for line in list_contents:
        outfile.write(line)
        outfile.write('\n')
    outfile.close()


def make_request(url_request):
    html = requests.get(url_request)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


# Take a reponse and put the hrefs in a list and return in
def link_parser(response_content):
    links_list = []
    # links
    soup = BeautifulSoup(response_content, 'html.parser')

    links_all = soup.find_all('a')

    for link in links_all:
        full_link = link.get('href')
        # To avoid empty slashes
        if full_link and full_link.startswith('/'):
            full_link = urljoin(url, full_link)
            links_list.append(full_link)
            #add_url_to_visit(full_link)

    links_list = list(filter(None, links_list))
    return links_list


def word_parser(response_text):
    word_list = []
    # populate a wordlist based on page
    for word in response_text.getText().strip().replace("\n", " ").split(" "):
        word_list.append(word.replace("\n", ' '))
    word_list = list(filter(None, word_list))
    return word_list


def image_parser(response):
    list_images = []
    all_images = response.find_all('img')
    for image in all_images:
        image_path = image.get('src')
        list_images.append(image_path)
    list_images = list(filter(None, list_images))
    return list_images


# test the functions
url = 'https://uncc.edu'

response = make_request(url)

# word_list = word_parser(response)
#link_list = link_parser(response)
# image_list = image_parser(response)
#
# # Print List
# output = ''
#
# for i in range(len(link_list)):
#     output += (link_list[i]) + '\n'
# print(output)



# FOR CRAWLING
visited_urls = []
urls_to_visit = []
urls = []

def add_url_to_visit(url):
    if url not in visited_urls and url not in urls_to_visit:
        urls_to_visit.append(url)

def download_url(url):
    return requests.get(url).text

def crawl(url):
    if(url in urls_to_visit):
        unique(urls_to_visit)
    else:
        urls_to_visit.append(url)




url = 'https://uncc.edu'

output = ''
html = download_url(url)
urls_to_visit = link_parser(html)

for i in range(len(urls_to_visit)):
    crawl(url)
    print(urls_to_visit[i])






for i in range(len(urls_to_visit)):
    output += (urls_to_visit[i]) + '\n'
print(output)


# FOR CRAWLING
