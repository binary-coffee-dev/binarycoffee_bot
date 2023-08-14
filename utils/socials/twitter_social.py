import os

import tweepy

from utils.socials.base_social import SocialAdapter

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


class TwitterAdapter(SocialAdapter):

    def __init__(self):
        self.client = tweepy.Client(consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET,
                                    access_token=TWITTER_ACCESS_TOKEN,
                                    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

    def post(self, msg):
        print("msg")
        try:
            self.client.create_tweet(text=msg)
        except:
            pass
