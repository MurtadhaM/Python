from urllib.parse import urljoin
from file_writer import *
import requests
from bs4 import BeautifulSoup

urls = list()
titles = list()
authors = list()
times = list()
contents = ['title , author, time']
create_project_dir('OUTPUT')
create_data_files('OUTPUT', urls)

# url = 'https://www.cnn.com/2020/07/28/politics/republican-reaction-gop-stimulus-plan/index.html'



def make_request(url):
    # Prepare the request for Parsing

    response_html = requests.get(url)
    # Adding the URL to List
    cnn_parser(response_html)


def update_files():
    links_file = 'OUTPUT' + '/links.csv'
    data_file = 'OUTPUT' + '/data.csv'

    # csv_data = urls.append(titles)
    # csv_data = urls
    set_to_file(urls, links_file)
    set_to_file(contents, data_file)


def cnn_parser(response_html):

    title = ' '
    author = ' '
    time = ' '

    try:
        html_response = response_html.text
        soup = BeautifulSoup(html_response, 'html.parser')
        # Getting the Title
        print("Title: ", soup.find('h1').get_text())
        title = soup.find('h1').get_text()
        # Addding to List
        titles.append(soup.find('h1').get_text())
        # Getting the Autor
        temp_ls = soup.find_all('span', {"class": 'metadata__byline__author'})
        for temp in temp_ls:
            print("Author: ", temp.find('a').get_text())
            author = temp.find('a').get_text()
            authors.append(temp.find('a').get_text())
        # Getting the Time
        temp_time = soup.find('p', {'class': 'update-time'})
        print("Time: ", temp_time.get_text())
        time = temp_time.get_text().replace(',',' ')

        # adding dates
        times.append(temp_time.get_text())
        contents.append('{} , {}, {}'.format(title, author, time))
        #print(contents)
        update_files()
    except Exception as e:
        print('Error is: {}'.format(e))


# Decorator Function to parse the content text
def get_full_text(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    for s in soup(['script', 'style']):
        s.extract()
    return (soup.text.strip()).encode('ascii', 'ignore').decode("utf-8")

    # Adding the Contents
    # contents.append(get_full_text(html_response))


# Spider for the Science Section only
def get_links():
    start_url = 'https://www.cnn.com/specials/space-science'
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

    update_files()

    return links_list


# Printing Log
def print_log():
    for u in urls:
        print(u)


def main():
    for u in urls:
        make_request(u)


# For Testing
get_links()
print_log()
main()
#make_request('https://www.cnn.com/2020/07/28/politics/republican-reaction-gop-stimulus-plan/index.html')

# print('Page URL: {}'.format(urls.pop()))
# print('Published Date: {}'.format(times.pop()))
# print('Article Title: {}'.format(titles.pop()))
# print('Author Name: {}'.format(authors.pop()))
