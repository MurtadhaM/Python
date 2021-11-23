# Author: Murtadha Marzouq
# Assignment: Reddit
# Date: 11/9/2019
# Thank for an awesome assignment

# importing the requests library
import praw
import pandas as pd


# creating the Reddit object

reddit = praw.Reddit(client_id='SCCAe_MW2AQRpRyBnD9Vkw', #my client id
                     client_secret='YUCw18b32GVwqvMaWGljIG2EIZYuIw',  #your client secret
                     user_agent='Firebox', #user agent name
                     username = '',     # your reddit username
                     password = '')     # your reddit password
# creating the subreddit object

sub = ['Askreddit']  # make a list of subreddits you want to scrape the data from
print(reddit)

 # creating the subreddit object

for s in sub:
    subreddit = reddit.subreddit(s)   # Choosing the subreddit
    query = ['food']
    # creating the submission object
    for item in query:
        post_dict = {
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num": [],
            "created" : [],
            "body" : []
        }
        # getting the top 100 posts
        comments_dict = {
            "comment_id" : [],
            "comment_parent_id" : [],
            "comment_body" : [],
            "comment_link_id" : []
        }
        # getting the top 100 posts
        for submission in subreddit.search(query,sort = "top",limit = 6):
            post_dict["title"].append(submission.title)
            post_dict["score"].append(submission.score)
            post_dict["id"].append(submission.id)
            post_dict["url"].append(submission.url)
            post_dict["comms_num"].append(submission.num_comments)
            post_dict["created"].append(submission.created)
            post_dict["body"].append(submission.selftext)
            
            ##### Acessing comments on the post
            submission.comments.replace_more(limit = 6)
            for comment in submission.comments.list():
                comments_dict["comment_id"].append(comment.id)
                comments_dict["comment_parent_id"].append(comment.parent_id)
                comments_dict["comment_body"].append(comment.body)
                comments_dict["comment_link_id"].append(comment.link_id)
        # creating the dataframe
        post_comments = pd.DataFrame(comments_dict)
        # creating the dataframe again
        post_comments.to_csv(s+"_comments_"+ item +"output.csv")
        post_data = pd.DataFrame(post_dict)
        post_data.to_csv(s+"_"+ item +"output.csv")