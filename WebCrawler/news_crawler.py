import os
import threading
from queue import Queue
from urllib.parse import urlparse
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from domain import *

project_name = ''
base_url = 'https://charlotte.edu'
domain_name = 'charlotte.com'
queue_file = 'queue.txt'
crawled_file = 'crawled.txt'
queue = set()
crawled = set()


def __init__(self, project_name, base_url, domain_name):
    project_name = project_name
    base_url = base_url
    domain_name = domain_name

    crawl_page('First spider', base_url)

# Author: Murtadha Marzouq
# Date: 08/29/2021
# Program: Python HTTP Retrieval

# Import Library to parse HTML/SOAP
from urllib.parse import urljoin

from bs4 import BeautifulSoup
# import Requests library
import requests


def link_parser(response_content, url):
    print(url)
    links_list = []
    # links
    response_content = requests.get(url)
    soup = BeautifulSoup(response_content, 'html.parser')
    links_all = soup.find_all('a')
    for link in links_all:
        full_link = link.get('href')
        # To avoid empty slashes
        if full_link and full_link.startswith('/'):
            full_link = urljoin(url, full_link)
            links_list.append(full_link)
            # add_url_to_visit(full_link)

    links_list = list(filter(None, links_list))
    return links_list






def crawl_page(thread_name, page_url):
    if page_url not in crawled:
        print(thread_name + ' now crawling ' + page_url)
        print('Queue ' + str(queue.qsize()) + ' | Crawled  ' + str(len(crawled)))
        add_links_to_queue(gather_links(page_url))
        queue.pop()
        crawled.add(page_url)
        update_files()

def update_files():
        set_to_file(queue, queue_file)
        set_to_file(crawled, crawled_file)

def gather_links(page_url):
    html_string = ''
    try:
        response = urlopen(page_url)
        html = requests.get(page_url)
        soup = BeautifulSoup(html.content, 'html.parser')
        finder = link_parser(soup, page_url)
        #finder.feed(html_string)
    except Exception as e:
        print(e)
        return set()
    return finder


def add_links_to_queue(links):
    for url in links:
        if (url in queue) or (url in crawled):
            continue
        if domain_name != get_domain_name(url):
            continue
        queue.add(url)


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")


PROJECT_NAME = 'charlotte'
HOMEPAGE = 'http://charlotte.edu/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = 'queue.txt'
CRAWLED_FILE = 'crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()


def work():
    while True:
        url = queue.get()
        crawl_page('1', url)
        queue.task_done()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        print(link)
    #queue.join()
    work()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()




crawl()