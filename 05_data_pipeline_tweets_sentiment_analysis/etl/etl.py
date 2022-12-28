import pymongo
import time
from sqlalchemy import create_engine
import logging
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import re

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongo_db", port=27017)

# Select the database you want to use withing the MongoDB server
#db = client.tweets
db = client.mongo_db


time.sleep(10)  # seconds
# docs = db.tweets.find(limit=3)
# for doc in docs:
#     print(doc)



pg = create_engine('postgresql://postgres:henda@postgresdb:5432/twitter', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')
mentions_regex= '@[A-Za-z0-9_]+' #pattern to remove all @ mentions in the tweet
url_regex='https?:\/\/\S+' #Pattern to remove all URL's
hashtag_regex= '#' # pattern to remove  hashtag
rt_regex= 'RT\s' # pattern to remove all retweets ie. RT

def clean_tweets(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  #removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) #removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) #removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet) #removes most URLs
    
    return tweet

analyzer = SentimentIntensityAnalyzer()
webhook_url = "https://hooks.slack.com/services/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"
docs = db.tweets.find()
for doc in docs:
    #print(doc)
    text = doc['text']
    clean_tweets1 = clean_tweets(text)
    score = analyzer.polarity_scores(clean_tweets1)['compound']  # placeholder value
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (clean_tweets1, score))
    logging.warning('---Score inserted to Postgres---')
a = "SELECT text FROM tweets ORDER BY sentiment DESC LIMIT (1) "
b = "SELECT sentiment FROM tweets ORDER BY sentiment DESC LIMIT (1) "
result = pg.execute(a).fetchall()
result1 = pg.execute(b).fetchall()

message = f""" The most racist tweet is | {result} | with VADER sentiments analysis score | {result1} """
data = {'text': message}
requests.post(url=webhook_url, json = data)
