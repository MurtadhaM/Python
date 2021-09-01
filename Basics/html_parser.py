# Author: Murtadha Marzouq
# Program: THIS PROGRAM WILL GET THE LINKS FROM AN INITIAL PAGE AND IF ENABLED WILL CRAWL ALL BUT FOR NOW
# I LIMITED THE FUNCTIONALITY TO JUST PRINT THE URLS AND SAVE THEM TO A FILE

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os


# THE FOLLOWING NUMBER OF FUNCTIONS ARE FOR WRITING A FILE
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)

def create_data_files(project_name, base_url):
    crawled_data = os.path.join('OUTPUT', 'data.csv')
    link_file = os.path.join('OUTPUT', 'links.csv')

    if not os.path.isfile(crawled_data):
        write_file(crawled_data, base_url)
    if not os.path.isfile(link_file):
        write_file(link_file, base_url)


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(str(data))


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        # print(links)
        for link in links:
            f.write(link + "\n")


# Get some variables to store the information
urls = list()
titles = list()
authors = list()
times = list()
contents = ['title , author, time, url']
create_project_dir('OUTPUT')
create_data_files('OUTPUT', urls)


# This will output the contents to a file
def update_files():
    links_file = 'OUTPUT' + '/links.csv'
    data_file = 'OUTPUT' + '/data.csv'

    # csv_data = urls.append(titles)
    # csv_data = urls
    set_to_file(urls, links_file)
    set_to_file(contents, data_file)


def cnn_parser(response_html, url):
    title = ' '
    author = ' '
    time = ' '

    try:
        html_response = response_html.text
        soup = BeautifulSoup(html_response, 'html.parser')
        # Getting the Title
        # print("Title: ", soup.find('h1').get_text())
        title = soup.find('h1').get_text()
        # Addding to List
        titles.append(soup.find('h1').get_text())
        # Getting the Autor
        temp_ls = soup.find_all('span', {"class": 'metadata__byline__author'})
        for temp in temp_ls:
            # print("Author: ", temp.find('a').get_text())
            author = temp.find('a').get_text()
            authors.append(temp.find('a').get_text())
        # Getting the Time
        temp_time = soup.find('p', {'class': 'update-time'})
        # print("Time: ", temp_time.get_text())
        time = temp_time.get_text().replace(',', ' ')

        # adding dates
        times.append(temp_time.get_text())
        contents.append('{} , {}, {}, {}'.format(title, author, time, url))
        # print(contents)
        update_files()
    except Exception as e:
        # print('Error is: {}'.format(e))
        print('')


# Spider for the Science Section only
def get_links(url):
    start_url = url
    links_list = []
    # links
    response = requests.get(start_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for l in soup.find_all('h3', class_='cd__headline'):
        a = l.find('a')
        # Titles a.get_text()
        full_link = a['href']
        # To avoid empty slashes
        if full_link and full_link.startswith('/'):
            full_link = urljoin(start_url, full_link)
            links_list.append(full_link)
            urls.append(full_link)
            # DEBUGGING
            # print(full_link)
            # add_url_to_visit(full_link)
    links_list = list(filter(None, links_list))
    # Write it to file for future use
    update_files()
    # Return the list
    return links_list


# Printing Links
def print_log():
    for u in urls:
        print(u)
    print('The total Number of links is {}'.format(len(urls)))


# To Get the Links
get_links('https://www.cnn.com/specials/space-science')
# This will print the urls to output Console
print_log()
