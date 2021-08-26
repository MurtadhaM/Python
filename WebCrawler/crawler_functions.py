import re
from bs4 import BeautifulSoup
import requests

# this function takes in a filename and a list to write it to a file
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
def link_parser(response):
    links_list = []
    # links
    links_all = response.find_all('a')

    for link in links_all:
        full_link = link.get('href')
        links_list.append(full_link)
    links_list = list(filter(None, links_list))
    return links_list


def word_parser(response):
    word_list = []
    # populate a wordlist based on page
    for word in response.getText().strip().replace("\n", " ").split(" "):
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
# link_list = link_parser(response)
image_list = image_parser(response)
#
# # Print List
output = ''

for i in range(len(image_list)):
    output += (image_list[i]) + '\n'
print(output)
