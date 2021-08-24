import requests
import re

from bs4 import BeautifulSoup


url = "https://uncc.edu"
request = requests.get(url)

# filter using regex to get links
result = re.findall('.*? href="(.*?)" .*?>', request.text)
# Second Method
soup = BeautifulSoup(requests.get(url).content, "html.parser")


# Second Method
soup.prettify()
# Get the link
url_list = soup.find_all('a')
#
# # print to terminal
# for url in url_list:
#     print(url.get('href'))

# print to terminal
for line_print in result:
    print(line_print)

# to write to file

filename = "links.txt"
outfile = open(filename, 'w')
for line in result:
    outfile.write(line)
    outfile.write('\n')
outfile.close()



