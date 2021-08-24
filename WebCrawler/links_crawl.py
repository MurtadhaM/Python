import requests
import re

url = "https://uncc.edu"
request = requests.get(url)

# filter using regex to get links
result = re.findall('<a .*? href="(.*?)" .*?>', request.text)
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
