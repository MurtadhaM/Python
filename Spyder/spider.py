# Author: Murtadha Marzouq
# Program: This class will handle the fetching and iteration throughout the site and its subdomains
from urllib.parse import urlparse
from urllib.request import urlopen
from link_finder import LinkFinder
from file_writer import *


class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    links_file = ''
    queue = set()
    crawled = set()
    links_list = set()
    include_subdomains = False

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.links_file = Spider.project_name + '/all_links.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    # Get sub domain name (name.example.com)
    def get_sub_domain_name(url):
        try:
            return urlparse(url).netloc
        except:
            return ''

    @staticmethod
    def get_domain_name(url):
        try:
            results = Spider.get_sub_domain_name(url).split('.')
            # if subdomains are enabled
            if Spider.include_subdomains:
                return results[-2] + '.' + results[-1]
            else:
                return ' '

        except:
            return ''

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            # Using discard to avoid null exception
            Spider.queue.discard(page_url)
            Spider.crawled.add(page_url)
            Spider.links_list.add(page_url)
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != Spider.get_domain_name(url):
                # NO SubDomain
                # if urlparse(Spider.base_url).netloc != urlparse(url).netloc:
                continue

            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)

        # Combining Thee Two Links
        all_union = Spider.links_list.union(Spider.queue)

        set_to_file(all_union, Spider.links_file)
