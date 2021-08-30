# Author: Murtadha Marzouq
# Program: THIS CLASS WILL EXTRACT ALL THE HREF TAGS FROM THE HOST AND ITS SUBDOMAINS

from html.parser import HTMLParser
from urllib import parse
import requests
from bs4 import BeautifulSoup



tags = set()

def html_parser(url , tag):
    response = requests.get(url)
    html_response = BeautifulSoup(response.text, 'html.parser')
    try:

        contents = html_response.find_all()
        for tag in contents:

            tags.add(tag)
            #print(html_response.find_all(None , attrs={"class": "lsb"}))


    except Exception as e:
        print('Error is : {}'.format(e))
    print(html_response.select('a')[0].get('href'))

    for tag in html_response.select('a'):
        print (tag.get('href'))
    return tags


#   TAGS :
# print(html_response.find_all(None , attrs={"class": "lsb"}))




