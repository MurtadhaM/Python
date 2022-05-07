#Author: Murtadha Marzouq
#Description: This script fetches the repositories from any user on Github without API connections.

import urllib.request
import json
import bs4 as BeautifulSoup


'''
    Parses the HTML for a user's repositories.
    :param html: The HTML for a user's repositories.
    :return: A list of the URLs for the user's repositories.
  '''


def parse_repositories(html):
    """Parse the HTML for a user's repositories."""
    soup = BeautifulSoup.BeautifulSoup(html, 'lxml')

    values = soup.find_all('a', attrs={"itemprop": "name codeRepository"})
    urls = [f'https://github.com/{value.get("href")}' for value in values]
    return urls


def get_repositories(user):
    '''
      Gets the repositories for a user. 
    '''
    url = f'https://github.com/{user}?tab=repositories'
    response = urllib.request.urlopen(url)
    return parse_repositories(response.read().decode('utf-8'))


def print_urls(urls):
    for url in urls:
        '''
          Prints the URL.
        '''
        print(url)

def __main__():
  """ Main function."""
  user = input("Enter a Github username: ")
  urls = get_repositories(user)
  print_urls(urls)
  
  
__main__()