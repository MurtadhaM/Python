# Author: Murtadha Marzouq
# Date: 08/29/2021
# Program: Python HTTP Retrieval

# Import Library to parse HTML/SOAP


from bs4 import BeautifulSoup
# import Requests library
import requests

# get the response after you run a http get request
response = requests.get('https://www.uncc.edu')
soup = BeautifulSoup(response.content, 'html.parser')
# print
print(soup)
