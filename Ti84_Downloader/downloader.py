from mimetypes import init
import os
import bs4 as BeautifulSoup
import requests
import json


def download_file(url):
    local_filename = 'data/'+url.split('/')[-1]
    # create folder if it doesn't exist
    if not os.path.exists('./data'):
        os.makedirs('./data')
    # NOTE the stream=True parameter
    print("Downloading: " + url)

    print(local_filename)
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):

            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())
    return local_filename

def get_urls(initial_url):
  html =requests.get('https://www.ticalc.org/pub/83plus/basic/math/statistics/').text      
  soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
  urls = [] 
  for link in soup.find_all('a'):
    if link.get('href').endswith('.zip'):
      urls.append('https://www.ticalc.org' +link.get('href'))
  print(urls)     
  return urls
          
  

initial_url = 'https://www.ticalc.org/pub/83plus/basic/math/statistics/'
urls = get_urls(initial_url)
for url in urls:
  download_file(url)
