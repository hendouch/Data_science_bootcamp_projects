import tweepy
import pymongo
import logging
import time


BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMdMiwEAAAAAyuHXg31y0LhU2yEEM3K1wy7GqEo%3DBvOf540GgdcNTaJiGXUfkxIeAAvBRXkxv6rhZDn85gEyazGzZ5"

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)

response = client.get_user(
    username='hendouch1',
    user_fields=['created_at', 'description', 'location',
                 'public_metrics', 'profile_image_url']
)

user = response.data

print(dict(user))

search_query = "racism lang:en"

cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'text'],
).flatten(limit=200)

conn = pymongo.MongoClient(host = 'mongo_db')
db = conn.mongo_db
collections =db.tweets


logging.warning('---Collecting tweets---')
time.sleep(3)
logging.warning('---Inserting tweets to DB---')
time.sleep(3)
for dic in cursor:  
    tweet = {
        'auther_id': dic.author_id,
        'text': dic.text
    }
    collections.insert_one(tweet)
time.sleep(3)
logging.warning('---Tweets inserted to DB---')