import os
import telegram
import tweepy 
from facepy import GraphAPI

class Telegram:
    def __init__(self):
        self.token = os.environ['TOKEN']
        self.chat_id = os.environ['CHANNEL']

    def post(self, msg):
        bot = telegram.Bot(token=self.token)
        bot.sendMessage(chat_id=self.chat_id, text=msg)

class Facebook:
    def __inti__(self):
        self.api = os.environ['FACEBOOK_KEY']
        self.group = os.environ['FACEBOOK_GROUP']
        self.graph = GraphAPI(self.api)

    def post(self, msg):
        if self.api == 'None' or self.group == 'None':
            return
        message = msg
        self.graph.post(path=str(self.group) + '/feed', message=message)