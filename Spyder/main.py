# Author: Murtadha Marzouq
# Program: THIS IS THE MAIN CLASS WHERE THE USER INTERACTS WITH THE PROGRAM

import threading
from queue import Queue
from urllib.parse import urlparse



from spider import Spider
from domain import *
from file_writer import *
import argparse

# Set a parser
parser = argparse.ArgumentParser(description='Process Passed-in Parameters.')
# Add a url Parameter
parser.add_argument('--url', type=str, default="https://google.com",
                    help='a string for the url (default: https://google.com)')
# Add a depth parameter
parser.add_argument('--depth', type=int, default='1',
                    help='set the depth of of the crawler (default: 1)')
# Add Threads count
parser.add_argument('--threads', type=int, default=1,
                    help='Threads to consume (default: 2)')

# Parse The Arguments
args = parser.parse_args()
# Print the url
# print("The url is: " + str(args.url))
# Print the crawl depth
# print("The depth is: " + str(args.depth))
# Print the threads switch
# print("threads now is : " + str(args.threads))


PROJECT_NAME = urlparse(str(args.url)).netloc.split('.')[0].upper()
HOMEPAGE = str(args.url)
DOMAIN_NAME = Spider.get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
LINKS_FILE = PROJECT_NAME + '/all_links.txt'
# NUMBER_OF_THREADS = 8
NUMBER_OF_THREADS = int(args.threads)
CRAWL_LIMIT = int(args.depth)

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
