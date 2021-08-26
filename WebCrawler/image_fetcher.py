import requests
import re

# url = "https://uncc.edu"
url = "http://books.toscrape.com/"
request = requests.get(url)

# filter using regex to get links
result = re.findall('img.*?src="(.*?)".*?', request.text)
for image in result:
    print(image)


