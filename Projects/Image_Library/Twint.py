
# Author: Murtadha Marzouq
# Date: 2020-04-20
# Version: 1.0
# Application: Twitter API
from datetime import date, timedelta
import twint
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS





# this function will take the tweets and create a word cloud
def create_wordcloud(text):
    # processing words in all tweets stored in the list
    words = ''
    for value in text:
        value = str(value)   
        words += value
    # creating a wordcloud
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 1000, height = 1000,
                        background_color = 'grey',
                        stopwords = stopwords,
                        min_font_size = 2).generate(words)
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
# this function will return information stored 
def show_info(data):
    print('Columns are')
    print(data.keys())
    print('number of entries:' + str(len(data.values)))

# this function will take the output of the twint function populate lists with information

def process_data(data):
    tweets = data['tweet']
    dates_list = data['date'].to_list()
    data['date_only'] = pd.to_datetime(data['date'])
    hashtag_list = data['hashtags'].to_list()
    filtered_list = list(filter(None, hashtag_list))
    
    
    
# this is the main function that will start the application 
def start(config):
    try:
        twint.run.Search(config)
        df = twint.storage.panda.Tweets_df
        process_data(df)
        create_wordcloud(df['tweet'])
    except Exception as e:
        print(e)





# setting the config Data for the twint function
config = twint.Config()
config.Username = "Ps5Pickups"
config.Pandas = True
# Initial setup
config.Limit = 1






start(config)