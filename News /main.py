# Author: Murtadha Marzouq
# Class: Web Mining
# Assignment News Crawling

import json
import newspaper
from newspaper import Article

# placeholder to save articles
articles_array = []


# to write the json file to system
def write_json_to_file(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


# Function that takes a limit and url to start the application
def crawl_news(limit, url):
    site = newspaper.build(url, memoize_articles=False, language='en')
    try:
        for article in site.articles:
            # to limit to 200 pages
            if limit < len(articles_array):
                break
            article = Article(article.url, memoize_articles=False)
            article.download()
            article.parse()
            article_meta_data = article.meta_data
            if 'article' in str(article.meta_data.items()):
                article_published_date = str({value for (key, value) in article_meta_data.items() if 'date' in key}).strip('{').strip('}').strip('\'')
                art = {'title': article.title, 'data_published': article_published_date,
                       'content': str(article.text).replace('\n\n', '').replace('\'', ''), 'link': article.url}
                print(art)
                # article_author = article.authors
                # print(article.publish_date)
                # print(article_author)
                # print(article.text)
                # print(article.url)
                articles_array.append(art)
    except Exception as error:
        print(error)
        # call write to file function
    write_json_to_file(articles_array);


# calling the main function with 200 pages limit
crawl_news(200, 'https://cnn.com')
# For debugging:
print(articles_array)
