import requests
import re

url = "https://uncc.edu"
request = requests.get(url)

# filter using regex to get links
result = re.findall('img.*?src="(.*?)".*?', request.text)
for image in result:
    print(image)


# to write to file

filename = "images.txt"
outfile = open(filename, 'w')
for line in result:
    outfile.write(line)
    outfile.write('\n')
outfile.close()
