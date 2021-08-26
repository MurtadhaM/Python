import requests
from bs4 import BeautifulSoup
import request_parser as  m


class request_parser():
    url = "http://books.toscrape.com/"

    def main(self):
        self.parse_requests()

    def parse_requests(self):
        args = requests.get(self.url)

        for line_print in args:
            # filter using regex to get links
            print(line_print)
        return None

    # url = "https://uncc.edu"

    # to write to file
    def file_save(self, file):
        filename = "links.txt"
        outfile = open(filename, 'w')
        for line in file:
            outfile.write(line)
            outfile.write('\n')
        outfile.close()


# BACKUP

# Second Method
# soup = BeautifulSoup(requests.get(url).content, "html.parser")


# Second Method
# soup.prettify()
# Get the link
# url_list = soup.find_all('a')
#
# # print to terminal
# for url in url_list:
#     print(url.get('href'))


# Running the file
s = m.request_parser()
s.parse_requests()
