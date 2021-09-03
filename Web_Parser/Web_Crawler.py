from urllib.parse import urljoin
from file_writer import *
import requests
from bs4 import BeautifulSoup


class Spider:

    def __init__(self, start_url, depth):
        self.urls = list()
        self.external_urls = list()
        self.titles = list()
        self.authors = list()
        self.times = list()
        self.responses = list()
        self.depth = depth
        self.start_url = start_url
        # TO GET INITIAL URLS
        self.get_links(self.start_url)

    # Get the text from a class name
    @staticmethod
    def make_request(url):
        try:
            # Prepare the request for Parsing
            response_html = requests.get(url)
            # Adding the URL to List
            return response_html
        except Exception as e:
            print(e)

    # Get the text from a class name
    def get_class(self, class_name):
        try:
            response = self.make_request(self.start_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            class_text = soup.find_all(None, class_=class_name)
            return class_text
        except Exception as e:
            print('Error found: {}'.format(e))

    # Spider for the Science Section only
    def get_links(self, start_url):
        links_list = []
        # links
        response = self.make_request(start_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            full_link = link.get('href')
            # To avoid empty slashes
            if full_link and full_link.startswith('/'):
                full_link = urljoin(start_url, full_link)
                links_list.append(full_link)
                self.urls.append(full_link)
            elif full_link and full_link.startswith('https://'):
                self.external_urls.append(full_link)

        links_list = list(filter(None, links_list))

        # self.update_files()
        return links_list

    # Printing Log
    def print_log(self):
        for u in self.urls:
            print(u)

    # depth is to limit the requests
    def main(self, url, depth):
        for i in range(0, self.depth):
            self.make_request(self.urls[i])


s = Spider(start_url='https://charlotte.edu', depth=1)
s.print_log()
# print(s.external_urls)
