# Author: Murtadha Marzouq
# Date: 08/29/2021
# Program: Python HTTP Retrieval

# Import Library to parse HTML/SOAP
from urllib.request import urlopen

from bs4 import BeautifulSoup
# import Requests library
import requests

# get the response after you run a http get request
response = requests.get('https://www.uncc.edu')
soup = BeautifulSoup(response.content, 'html.parser')

url = "https://uncc.edu"
html = urlopen(url)
html_contents = BeautifulSoup(html,features="html5lib")


# links
links_all = html_contents.find_all("a")



# search word
html_page_pretty = html_contents.prettify()
print(html_page_pretty)


#print(response)
# print
#print(soup)
