# Author: Murtadha Marzouq
# Program: THIS CLASS WILL EXTRACT ALL THE HREF TAGS FROM THE HOST AND ITS SUBDOMAINS

from html.parser import HTMLParser
from urllib import parse
import requests
from bs4 import BeautifulSoup

tags = set()


def html_parser(url, tag):
    response = requests.get(url)
    html_response = BeautifulSoup(response.text, 'html.parser')
    # xml_response = BeautifulSoup(response.text, 'xml')
    # print(xml_response)

    try:

        contents = html_response.find_all('description')

        for tag in contents:
            tags.add(tag)
            print(tag.text)
        # print(xml_response.find_all('url'))


    except Exception as e:
        print('Error is : {}'.format(e))

    return tags

#   TAGS :
# print(html_response.find_all(None , attrs={"class": "lsb"}))
