import threading
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os
import concurrent.futures


class Spider:
    filename = 'output.txt'
    log = ''
    threads = 2

    def __init__(self, start_url, depth, enable_log):
        self.urls = list()
        self.external_urls = list()
        self.crawled = list()
        self.titles = list()
        self.authors = list()
        self.times = list()
        self.responses = list()
        self.depth = depth
        self.enable_log = enable_log
        self.start_url = start_url
        # TO GET INITIAL URLS
        self.get_links(self.start_url)
        self.main()
        # create a file to save output files
        if bool(self.enable_log):
            self.log_write()

    # setup a log file
    def log_write(self):
        self.log += 'WEBSITE URLS:\n'
        self.log += str(self.urls).replace(',', '\n').strip('\'').strip('[').strip(']').replace('\'', '')
        self.log += '\nEXTERNAL URLS:\n'
        self.log += str(self.external_urls).replace(',', '\n').strip('\'').strip('[').strip(']').replace('\'', '')
        self.write_file(self.log)

    # Get the text from a class name
    def make_request(self, url):
        try:
            if url not in self.crawled:
                # Prepare the request for Parsing
                response_html = requests.get(url)
                # Adding the responses to a list
                self.responses.append(BeautifulSoup(response_html.text, 'html.parser').prettify())
                if url.endswith('/'):
                    url = url[:-1]
                self.crawled.append(url)
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
                if full_link.endswith('/'):
                    full_link = full_link[:-1]
                self.external_urls.append(full_link)

        links_list = list(filter(None, links_list))

        # self.update_files()
        return links_list

    # Printing Log
    def print_log(self):
        for u in self.urls:
            print(u)

    # Create a file to append the output to
    def create_file(self, filename):
        if not os.path.exists('OUTPUT'):
            print('Creating directory ' + 'OUTPUT')
            os.makedirs('OUTPUT')
        if not os.path.isfile('OUTPUT/' + filename):
            with open('OUTPUT/' + filename, 'x') as f:
                f.close()

    # Add data onto an existing file
    def append_to_file(self, data):
        self.create_file(self.filename)
        with open('OUTPUT/' + self.filename, 'a') as file:
            file.write(str(data) + '\n')
            file.close()

    # override file contents
    # Create a new file
    def write_file(self, data):
        self.create_file(self.filename)
        with open('OUTPUT/' + self.filename, 'w') as f:
            f.write(str(data))

    # depth is to limit the requests in THREADING
    def main(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result = [executor.submit(self.make_request, self.urls[i]) for i in range(self.threads)]
        for index, f in enumerate(concurrent.futures.as_completed(result)):
            self.log += f'\n REQUEST: {index + 1} \nURL: {self.urls[index]}\n' + str(f.result().text) + '\n'


s = Spider(start_url='https://charlotte.edu', depth=3, enable_log='1')
s.print_log()
print(s.external_urls)
print(s.crawled)
